# Databricks notebook source
# DBTITLE 1,Install MQ Distributable Client - Header Files are required for PIP install
# MAGIC %sh
# MAGIC cd /databricks/driver
# MAGIC rm -rf mq
# MAGIC mkdir mq
# MAGIC cd mq
# MAGIC wget https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/messaging/mqdev/redist/9.3.3.0-IBM-MQC-Redist-LinuxX64.tar.gz
# MAGIC tar zxvf 9.3.3.0-IBM-MQC-Redist-LinuxX64.tar.gz
# MAGIC cp -r inc/* /usr/include/

# COMMAND ----------

# DBTITLE 1,apt install the MQ Client Libraries - the PIP install does some internal check (copying redist libraries to system library location doesn't work)
# MAGIC %sh
# MAGIC cd /databricks/driver
# MAGIC rm -rf mqadv
# MAGIC mkdir mqadv
# MAGIC cd mqadv
# MAGIC wget https://public.dhe.ibm.com/ibmdl/export/pub/software/websphere/messaging/mqadv/mqadv_dev930_ubuntu_x86-64.tar.gz
# MAGIC tar zxvf mqadv_dev930_ubuntu_x86-64.tar.gz 
# MAGIC
# MAGIC # Accept the license
# MAGIC cd MQServer
# MAGIC ./mqlicense.sh -accept
# MAGIC returnCode=$?
# MAGIC if [ $returnCode -eq 0 ]
# MAGIC then
# MAGIC     echo "license accepted"
# MAGIC     echo
# MAGIC else
# MAGIC     echo "license not accepted"
# MAGIC     exit $returnCode
# MAGIC fi
# MAGIC
# MAGIC # Create a .list file to let the system add the new packages to the apt cache
# MAGIC cd /etc/apt/sources.list.d
# MAGIC echo "deb [trusted=yes] file:/databricks/driver/mqadv/MQServer ./" > mq-install.list
# MAGIC apt-get update
# MAGIC returnCode=$?
# MAGIC if [ $returnCode -eq 0 ]
# MAGIC then
# MAGIC     echo "apt cache update succeeded."
# MAGIC     echo
# MAGIC else
# MAGIC     echo "apt cache update failed! See return code: " $returnCode
# MAGIC     exit $returnCode
# MAGIC fi
# MAGIC
# MAGIC echo "Beginning MQ install"
# MAGIC apt-get install -y "ibmmq-client*"
# MAGIC returnCode=$?
# MAGIC if [ $returnCode -eq 0 ]
# MAGIC then
# MAGIC     echo "Install succeeded."
# MAGIC else
# MAGIC     echo "Install failed. See return code: " $returnCode
# MAGIC     exit $returnCode
# MAGIC fi
# MAGIC
# MAGIC echo "
# MAGIC /usr/local/lib
# MAGIC /opt/mqm/lib64
# MAGIC /opt/mqm/lib" >> /etc/ld.so.conf.d/libc.conf
# MAGIC ldconfig

# COMMAND ----------

# MAGIC %pip install pymqi

# COMMAND ----------

# MAGIC %sh
# MAGIC sudo su
