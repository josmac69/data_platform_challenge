# This script is a mockup of a Spark script that reads data from Kafka, performs an aggregation, and writes the result to a PostgreSQL database.
# It is not meant to be run as-is, but rather to be used as a reference.
# Example presumes that the PostgreSQL table has primary key "id" and that the metadata table has column "last_processed_id".
# The checkpointLocation is used by Spark to maintain the state of the stream (including the Kafka offsets),
# which allows it to provide exactly-once semantics.

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StructField, StringType, TimestampType, IntegerType

# Define the schema of the Kafka data
schema = StructType([
    StructField("id", IntegerType()),
    StructField("created_at", TimestampType()),
    StructField("event_type", StringType()),
])

# Create a SparkSession
spark = SparkSession.builder.appName("ExactlyOnceProcessing").getOrCreate()

# Read the Kafka stream
kafka_df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "<kafka_bootstrap_servers>") \
    .option("subscribe", "<kafka_topic>") \
    .option("startingOffsets", "earliest") \
    .load()

# Deserialize the Kafka data from JSON
events_df = kafka_df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

# Perform the aggregation
aggregated_df = events_df.groupBy("event_type").count()

# JDBC properties
properties = {
    "user": "<username>",
    "password": "<password>",
    "driver": "org.postgresql.Driver",
}

# Write the aggregated data to the PostgreSQL database
query = aggregated_df.writeStream \
    .outputMode("complete") \
    .foreachBatch(lambda df, epoch_id: df.write.jdbc(
        url="<database_url>",
        table="<target_table>",
        mode="append",
        properties=properties,
    )) \
    .option("checkpointLocation", "<checkpoint_location>") \
    .start()

query.awaitTermination()
