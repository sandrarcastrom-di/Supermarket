# Databricks notebook source
import getpass

# COMMAND ----------

jdbcHostname = "serversupermarket.database.windows.net"
jdbcDatabase = "dbssupermarket"
jdbcPort = 1433
jdbcUsername = "supermarketuser"
jdbcPassword = getpass.getpass("Introduce la contraseña de la base de datos: ")

# COMMAND ----------

# URL JDBC
jdbcUrl = f"jdbc:sqlserver://{jdbcHostname}:{jdbcPort};database={jdbcDatabase};encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.database.windows.net;loginTimeout=30;"

# COMMAND ----------

df_dim_product = spark.table('catalog_dev.golden.dim_product')

# COMMAND ----------

df_dim_product.write \
    .format("jdbc") \
    .option("url", jdbcUrl) \
    .option("dbtable", "dim_product") \
    .option("user", jdbcUsername) \
    .option("password", jdbcPassword) \
    .mode("overwrite") \
    .save()

# COMMAND ----------

df_dim_customer = spark.table('catalog_dev.golden.dim_customer')

# COMMAND ----------

df_dim_customer.write \
    .format("jdbc") \
    .option("url", jdbcUrl) \
    .option("dbtable", "dim_customer") \
    .option("user", jdbcUsername) \
    .option("password", jdbcPassword) \
    .mode("overwrite") \
    .save()

# COMMAND ----------

df_dim_date = spark.table('catalog_dev.golden.dim_date')

# COMMAND ----------

df_dim_date.write \
    .format("jdbc") \
    .option("url", jdbcUrl) \
    .option("dbtable", "dim_date") \
    .option("user", jdbcUsername) \
    .option("password", jdbcPassword) \
    .mode("overwrite") \
    .save()

# COMMAND ----------

df_dim_time = spark.table('catalog_dev.golden.dim_time')

# COMMAND ----------

df_dim_time.write \
    .format("jdbc") \
    .option("url", jdbcUrl) \
    .option("dbtable", "dim_time") \
    .option("user", jdbcUsername) \
    .option("password", jdbcPassword) \
    .mode("overwrite") \
    .save()

# COMMAND ----------

df_dim_order = spark.table('catalog_dev.golden.dim_order')

# COMMAND ----------

df_dim_order.write \
    .format("jdbc") \
    .option("url", jdbcUrl) \
    .option("dbtable", "dim_order") \
    .option("user", jdbcUsername) \
    .option("password", jdbcPassword) \
    .mode("overwrite") \
    .save()

# COMMAND ----------

df_fact_order_item = spark.table('catalog_dev.golden.fact_order_item')

# COMMAND ----------

df_fact_order_item.write \
    .format("jdbc") \
    .option("url", jdbcUrl) \
    .option("dbtable", "fact_order_item") \
    .option("user", jdbcUsername) \
    .option("password", jdbcPassword) \
    .mode("overwrite") \
    .save()
