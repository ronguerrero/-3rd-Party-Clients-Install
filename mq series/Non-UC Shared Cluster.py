# Databricks notebook source
# MAGIC %md
# MAGIC %md
# MAGIC ### Background  
# MAGIC
# MAGIC The MQ Series client requires both a set of C compiled libraries plus a python package (pymqi).   
# MAGIC The pip install of pymqi will compile the python client, but requires the C compiled libraries to exist.   
# MAGIC Hence, the MQ libraries needs to be copied onto the driver file system, and corresponding environment variables are set for the compile to succeed.
# MAGIC We can have an init script perform this for us
# MAGIC  
# MAGIC Concerns - Init scripts are going away in general. This example uses DBFS, but you can convert to using Workspace.  We want customers to use UC Clusters!
# MAGIC
# MAGIC ### Setup Instructions
# MAGIC
# MAGIC 1 - save mqinit.sh script to dbfs    
# MAGIC example only:   
# MAGIC
# MAGIC <img src="https://github.com/ronguerrero/Third-Party-Clients-Install/blob/main/mq%20series/png/Init_script.png?raw=true">
# MAGIC
# MAGIC
# MAGIC 2 - configure init script for the cluster  
# MAGIC 3 - add the pymqi library to the cluster config  
# MAGIC   
# MAGIC example only:  
# MAGIC <img src="https://github.com/ronguerrero/Third-Party-Clients-Install/blob/main/mq%20series/png/install_package.png?raw=true">
# MAGIC
# MAGIC
# MAGIC
# MAGIC 4 - start/restart the cluster  
# MAGIC

# COMMAND ----------

import pymqi
