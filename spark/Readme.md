# Spark���л�������

* Java������Spark����Scalaд�ģ�Scala���ջᱻ����ΪJava�ֽ��룬������ҪJVM����
* Sparkֻ��Ҫ����gz�ļ�����ѹ���ɣ�����Ҫ��װ


# �Spark���л�����Linux CentOS��

* ��װjre�������غͰ�װ�ο�[����](https://docs.oracle.com/javase/8/docs/technotes/guides/install/linux_jdk.html#BJFJJEFG)��
* ��װPython
* �ص�����ǽ��`service iptables stop`��`chkconfig iptables off`


# �Spark��Ⱥ����

��Ⱥ�����ǻ���Master-Slave�ṹ��

* ������Master-Slave�ڵ��ϣ�����Spark��gz�ļ�����ѹ
* ��Master�ڵ��ϣ�ִ��`./sbin/start-master.sh`
* ��Web���������Master��UI����URL��spark://host:7077��
* ������Slave�ڵ��ϣ�ִ��`./sbin/start-slave.sh spark://host:7077`
* Slave���ӵ�Master����Ⱥ�����ʹ�����


# ����PythonдSpark�������������

* [PythonдSpark������Spark����������](https://github.com/ybdesire/machinelearning/blob/master/16_spark/spark_local_run_basic)
* [PythonдSpark������Spark��Ⱥ������](https://github.com/ybdesire/machinelearning/blob/master/16_spark/spark_cluster_run_basic)


# Spark�ֲ�ʽ����

* [6 Slave �ֲ�ʽ������ȡ����](https://github.com/ybdesire/machinelearning/blob/master/16_spark/file_process_distributed)