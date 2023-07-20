cd /databricks/driver
rm -rf mq
mkdir mq
cd mq
cp /Workspace/Repos/ron.guerrero@databricks.com/-3rd-Party-Clients-Install.git/9.3.3.0-IBM-MQC-Redist-LinuxX64.tar.gz .
tar zxvf 9.3.3.0-IBM-MQC-Redist-LinuxX64.tar.gz
cp -r inc/* /usr/include/
mkdir -p /opt/mqm/lib64
mkdir -p /opt/mqm/lib
cp -r /databricks/driver/mq/lib64/* /opt/mqm/lib64
cp -r /databricks/driver/mq/lib/* /opt/mqm/lib
echo "
/opt/mqm/lib64
/opt/mqm/lib" >> /etc/ld.so.conf.d/libc.conf
ldconfig
