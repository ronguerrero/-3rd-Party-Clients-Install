# Databricks notebook source
# MAGIC %md
# MAGIC <img src="./png/Cluster_Config_UC_Shared.png">

# COMMAND ----------

# MAGIC %sh
# MAGIC rm -rf /tmp/mqm
# MAGIC MQ_FILE_PATH=/tmp/mqm
# MAGIC if [ ! -d "$FILE" ]; then
# MAGIC    mkdir $MQ_FILE_PATH
# MAGIC    cd $MQ_FILE_PATH
# MAGIC    wget https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/messaging/mqdev/redist/9.3.3.0-IBM-MQC-Redist-LinuxX64.tar.gz
# MAGIC    tar zxvf 9.3.3.0-IBM-MQC-Redist-LinuxX64.tar.gz
# MAGIC fi
# MAGIC

# COMMAND ----------

pip install pymqi

# COMMAND ----------

import pymqi

# COMMAND ----------


