from databricks.connect import DatabricksSession

spark = (
    DatabricksSession.builder
    .profile("vitalie")
    .serverless()
    .getOrCreate()
)

spark.sql("SELECT current_date() AS today").show()