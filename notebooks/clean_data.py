from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, LongType, TimestampType, IntegerType, DoubleType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Read TXT as CSV and Save as Parquet") \
    .getOrCreate()

# Define the schema
schema = StructType([
    StructField("transaction_id", LongType(), True),
    StructField("tx_datetime", TimestampType(), True),
    StructField("customer_id", IntegerType(), True),
    StructField("terminal_id", IntegerType(), True),
    StructField("tx_amount", DoubleType(), True),
    StructField("tx_time_seconds", LongType(), True),
    StructField("tx_time_days", IntegerType(), True),
    StructField("tx_fraud", IntegerType(), True),
    StructField("tx_fraud_scenario", IntegerType(), True)
])

# File path
file_path = "data/2022-09-05.txt"

# Read the TXT file as a CSV file
df = spark.read.csv(
    file_path,
    header=False,
    comment="#",  # comment character
    schema=schema,
    sep=",",       # separator (comma in this case)
    mode="PERMISSIVE" # Handles lines with more or fewer columns.
)

# Drop all columns with null values
df_cleaned = df.na.drop(how="all")

# Save the cleaned DataFrame as a Parquet file
output_path = "data/output_2022-09-05.parquet"
df_cleaned.write.parquet(output_path, mode="overwrite")

# Stop the Spark session
spark.stop()