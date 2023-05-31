# This mockup code shows how to implement exactly-once processing
# using Spark Structured Streaming and PostgreSQL.
# It is not meant to be run as-is, but rather to be used as a reference.
# Example presumes that the PostgreSQL table has primary key "id"
# and that the metadata table has column "last_processed_id".

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder.appName("ExactlyOnceProcessing").getOrCreate()

# JDBC properties
properties = {
    "user": "<username>",
    "password": "<password>",
    "driver": "org.postgresql.Driver",
}

# Load last processed ID from the metadata table
metadata_df = spark.read.jdbc(
    url="<database_url>",
    table="<metadata_table>",
    properties=properties,
)
last_processed_id = metadata_df.select("last_processed_id").collect()[0][0]

# Read new data from the PostgreSQL table
query = f"(SELECT * FROM daily_events WHERE id > {last_processed_id}) AS tmp"
events_df = spark.read.jdbc(
    url="<database_url>",
    table=query,
    properties=properties,
)

# Perform the aggregation
aggregated_df = events_df.groupBy("event_type").count()

# Here you can write the aggregated_df DataFrame to another database.
# For simplicity, we'll just show it.
aggregated_df.show()

# Update the last processed ID in the metadata table
new_last_processed_id = events_df.select("id").rdd.max()[0]
update_query = f"UPDATE <metadata_table> SET last_processed_id = {new_last_processed_id}"
spark.write.jdbc(
    url="<database_url>",
    table="<metadata_table>",
    mode="overwrite",
    properties=properties,
)
