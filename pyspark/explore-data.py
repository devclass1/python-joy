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

# Print schema
titanic_df.printSchema()

# Show summary statistics for numerical columns
display(titanic_df.describe())

from pyspark.sql.functions import isnan, when, count

# Count missing values per column
missing_values = titanic_df.select([
    count(when(isnan(c) | col(c).isNull(), c)).alias(c) 
    for c in titanic_df.columns
])
display(missing_values)

# Group by 'Sex' and calculate survival rate
survival_by_gender = titanic_df.groupBy("Sex").agg(
    mean("Survived").alias("SurvivalRate"),
    count("Survived").alias("TotalPassengers")
).orderBy(desc("SurvivalRate"))

display(survival_by_gender)


#Survival Rate by Passenger Class (Pclass)
survival_by_class = titanic_df.groupBy("Pclass").agg(
    mean("Survived").alias("SurvivalRate"),
    count("Survived").alias("TotalPassengers")
).orderBy("Pclass")

display(survival_by_class)

#Average Age of Survivors vs. Non-Survivors
avg_age_survival = titanic_df.groupBy("Survived").agg(
    mean("Age").alias("AverageAge")
)
display(avg_age_survival)

#Survival Rate by Age Group

from pyspark.sql.functions import when

# Create age groups
titanic_df = titanic_df.withColumn(
    "AgeGroup",
    when(col("Age") < 18, "Child")
    .when((col("Age") >= 18) & (col("Age") < 60), "Adult")
    .otherwise("Senior")
)

# Calculate survival rate by age group
survival_by_agegroup = titanic_df.groupBy("AgeGroup").agg(
    mean("Survived").alias("SurvivalRate"),
    count("Survived").alias("TotalPassengers")
).orderBy(desc("SurvivalRate"))

display(survival_by_agegroup)

# Plot survival rate by gender
display(survival_by_gender)


