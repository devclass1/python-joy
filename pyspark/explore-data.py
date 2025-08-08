# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, mean, desc

# Initialize SparkSession
spark = SparkSession.builder.appName("TitanicDataExploration").getOrCreate()

# URL of the Titanic dataset on GitHub
titanic_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Read CSV into a DataFrame
titanic_df = spark.read.csv(titanic_url, header=True, inferSchema=True)

# Display the first few rows
display(titanic_df.limit(5))
