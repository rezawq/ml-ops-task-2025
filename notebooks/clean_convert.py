import findspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, LongType, TimestampType, IntegerType, DoubleType

findspark.init()

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Read txt, clean, convert and save as Parquet") \
    .getOrCreate()

# Define the schema
schema = StructType([
    StructField("transaction_id", LongType(), False),
    StructField("tx_datetime", TimestampType(), False),
    StructField("customer_id", IntegerType(), False),
    StructField("terminal_id", IntegerType(), False),
    StructField("tx_amount", DoubleType(), False),
    StructField("tx_time_seconds", LongType(), False),
    StructField("tx_time_days", IntegerType(), False),
    StructField("tx_fraud", IntegerType(), False),
    StructField("tx_fraud_scenario", IntegerType(), False)
])

# File path
data_path = "data"
output_path = "data_convert/data.parquet"

# Read the TXT file as a CSV file
df_txt = spark.read.csv(
    data_path,
    header=False,
    comment="#",  # comment character
    schema=schema,
    sep=",",       # separator (comma in this case)
    mode="PERMISSIVE" # Handles lines with more or fewer columns.
)
print('Converting and saving to ',output_path)

df = ( df_txt.repartition(10)
        .write
        .mode("overwrite")
        .parquet(output_path))

# Clean the DataFrame by:
# 1. Dropping rows where all columns have null values.
# 2. Removing duplicate rows.
# 3. Filtering rows to include only those with a positive `tx_amount`.
df_cleaned = df.na.drop(how="all").distinct().filter(df.tx_amount>0)

# Save the cleaned DataFrame as a Parquet file
df_cleaned.write.parquet(output_path, mode="overwrite")

print('Records count after clean:',df_cleaned.count())

# Stop the Spark session
spark.stop()