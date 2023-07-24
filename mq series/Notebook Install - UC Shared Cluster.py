# Databricks notebook source
# MAGIC %md
# MAGIC ### Background  
# MAGIC
# MAGIC The MQ Series client requires both a set of C compiled libraries plus a python package (pymqi).   
# MAGIC The pip install of pymqi will compile the python client, but requires the C compiled libraries to exist.   
# MAGIC Hence, the MQ libraries needs to be copied onto the driver file system, and corresponding environment variables are set for the compile to succeed.
# MAGIC
# MAGIC UC Shared clusters do not support init scripts (as of 2023-07-23).  There is a private preview feature which may be deprecated altogether.   
# MAGIC This mechanism requires you set cluster-wide environment variables AND you execute the shell cell below.
# MAGIC   
# MAGIC Concerns - We are modifying the LD_LIBRARY_PATH to include the MQ libraries we'll unpack in the shell cell. This can be seen as potentially breaking the cluster environment.
# MAGIC
# MAGIC ### Setup Instructions
# MAGIC
# MAGIC 1 - Configure a UC Shared cluster with the following Advance Configuration   
# MAGIC <br/>
# MAGIC <img src="https://github.com/ronguerrero/Third-Party-Clients-Install/blob/main/mq%20series/png/Cluster_Config_UC_Shared.png?raw=true">

# COMMAND ----------

# MAGIC %sh
# MAGIC # this code is not "thread-safe" i.e. concurrent users running this may have issues, but this is unlikely
# MAGIC # we need to install in /tmp as that's the only place we have write access in a UC Shared Cluster
# MAGIC # we have to run it as part of the notebook code because init scripts are not officially allowed to run in UC Shared Clusters as of (2023-07-24)
# MAGIC
# MAGIC MQ_FILE_PATH=/tmp/mqm
# MAGIC if [ ! -d "$FILE" ]; then
# MAGIC
# MAGIC    #first time we got here, means no one installed the mq libraries yet
# MAGIC
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


