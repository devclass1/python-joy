# Import required libraries
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pandas as pd

# Initialize Spark session
spark = SparkSession.builder \
    .appName("CSV Data Loader") \
    .getOrCreate()

# Define the path to your CSV file
# For Databricks file system (DBFS), use paths like:
# '/FileStore/tables/your_file.csv' or 'dbfs:/FileStore/tables/your_file.csv'
csv_path = "/FileStore/tables/sample_data.csv"  # Update with your file path

def load_and_display_csv(file_path):
    """
    Loads a CSV file into a Spark DataFrame and displays its contents.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pyspark.sql.DataFrame: The loaded DataFrame
    """
    try:
        # Load the CSV file into a Spark DataFrame
        # You can customize these options based on your CSV file format
        df = spark.read \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .csv(file_path)
        
        print("\nSuccessfully loaded CSV file!")
        print(f"Number of rows: {df.count()}")
        print(f"Number of columns: {len(df.columns)}")
        
        # Display the DataFrame schema
        print("\nDataFrame Schema:")
        df.printSchema()
        
        # Show the first 20 rows of the DataFrame
        print("\nData Preview (first 20 rows):")
        display(df.limit(20))
        
        # Alternative display option (shows vertical output)
        # df.show(20, vertical=True)
        
        return df
        
    except Exception as e:
        print(f"\nError loading CSV file: {e}")
        return None

# Main execution
if __name__ == "__main__":
    print("Databricks CSV Data Loader")
    print("=========================")
    
    # Load and display the CSV data
    dataframe = load_and_display_csv(csv_path)
    
    # If you want to also display as a Pandas DataFrame (for smaller datasets)
    if dataframe:
        print("\nPandas DataFrame Conversion (first 10 rows):")
        pandas_df = dataframe.limit(10).toPandas()
        display(pandas_df)
