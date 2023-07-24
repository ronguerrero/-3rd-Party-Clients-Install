# Databricks notebook source
# MAGIC %md
# MAGIC ### Setup Steps
# MAGIC
# MAGIC 1 - save mqinit.sh script to dbfs  
# MAGIC 2 - configure init script for the cluster  
# MAGIC 3 - add the pymqi library to the cluster config  
# MAGIC 4 - start/restart the cluster  
# MAGIC

# COMMAND ----------

import pymqi
