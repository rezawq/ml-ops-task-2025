"""
Script: pyspark_script.py
Description: PySpark script for testing.
"""

from argparse import ArgumentParser
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, LongType, TimestampType, IntegerType, DoubleType


def clean_convert(source_path: str, output_path: str, bucket_name:str) -> None:

    spark = (SparkSession
        .builder
        .appName("Read txt, clean, convert and save as Parquet")
        .enableHiveSupport()
        .getOrCreate()
    )

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


    print("Try to read CSV files from source bucket...")

    #Read the TXT file as a CSV file
    df_txt = spark.read.csv(
        source_path,
        header=False,
        comment="#",  # comment character
        schema=schema,
        sep=",",  # separator (comma in this case)
        mode="PERMISSIVE"  # Handles lines with more or fewer columns.
    )
    # df = (df_txt.repartition(10)
    #       .write
    #       .mode("overwrite")
    #       .parquet("tmp.parquet"))

    # File path
    output_path_tmp = f"s3a://{bucket_name}/output_data/tmp.parquet"
    #
    # print('Converting and saving to ', output_path_tmp)
    #
    df = (df_txt
          .repartition(10)
          .write
          .mode("overwrite")
          .parquet(output_path_tmp))


    # Clean the DataFrame by:
    # 1. Dropping rows where all columns have null values.
    # 2. Removing duplicate rows.
    # 3. Filtering rows to include only those with a positive `tx_amount`.
    df_cleaned = df.na.drop(how="all").distinct().filter(df.tx_amount > 0)

    # Save the cleaned DataFrame as a Parquet file
    df_cleaned.repartition(10).write.mode("overwrite").parquet(output_path)

    # print('Records count after clean:', df_cleaned.count())
    #
    # # Stop the Spark session
    # spark.stop()
    print("Successfully saved the result to the output bucket!")


def main():
    """Main function to execute the PySpark job"""
    parser = ArgumentParser()
    parser.add_argument("--bucket", required=True, help="S3 bucket name")
    args = parser.parse_args()
    bucket_name = args.bucket

    if not bucket_name:
        raise ValueError("Environment variable S3_BUCKET_NAME is not set")

    input_path = f"s3a://{bucket_name}/input_data/*.txt"
    output_path = f"s3a://{bucket_name}/output_data/clean_data.parquet"
    clean_convert(input_path, output_path, bucket_name)

if __name__ == "__main__":
    main()