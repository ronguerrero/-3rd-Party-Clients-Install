cd /tmp/
rm -rf mq
mkdir mq
cd mq

#note replace the /Workspace path with the actual location of the GZ file
cp /Workspace/Repos/ron.guerrero@databricks.com/-3rd-Party-Clients-Install.git/9.3.3.0-IBM-MQC-Redist-LinuxX64.tar.gz .
tar zxvf 9.3.3.0-IBM-MQC-Redist-LinuxX64.tar.gz
cp -r inc/* /usr/include/
mkdir -p /opt/mqm/lib64
mkdir -p /opt/mqm/lib
cp -r /tmp/mq/lib64/* /opt/mqm/lib64
cp -r /tmp/mq/lib/* /opt/mqm/lib

# the next set of commands registers the Library Path system wide so that Python will find the mqm libraries
echo "
/opt/mqm/lib64
/opt/mqm/lib" >> /etc/ld.so.conf.d/libc.conf
ldconfig
