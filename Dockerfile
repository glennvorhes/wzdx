FROM python:3.6-stretch
#FROM ubuntu
#RUN apt install python-dev build-essential

COPY ./ /wzdx/
WORKDIR "/wzdx"

RUN apt update
RUN apt install alien

RUN alien -i oracle-instantclient12.2-odbc-12.2.0.1.0-2.x86_64.rpm
RUN apt install -y libaio1
#
#printf "\n\n# Oracle Client environment\n \
#export LD_LIBRARY_PATH=/usr/lib/oracle/19.3/client64/lib/${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
#export ORACLE_HOME=/usr/lib/oracle/19.3/client64\n" | sudo tee /etc/profile.d/oracle-env.sh > /dev/null
#
#RUN export LD_LIBRARY_PATH=/usr/lib/oracle/19.3/client64/lib/${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}
#RUN export ORACLE_HOME=/usr/lib/oracle/19.3/client64\n" > /etc/profile.d/oracle-env.sh

RUN ldconfig
#
#
#RUN apt install unzip
#
#RUN mkdir /opt/oracle
#RUN unzip instantclient-basic-linux.x64-11.2.0.4.0.zip -d /opt/oracle/
#
#RUN echo "export ORACLE_HOME=/opt/oracle/instantclient_11_2" > /etc/profile.d/oracle.sh
#RUN echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ORACLE_HOME" >> /etc/profile.d/oracle.sh
#
#RUN echo "/opt/ora/instantclient_11_2" > /etc/ld.so.conf.d/oracle.conf
#
##RUN sh -c "echo /opt/oracle/instantclient_11_2 > /etc/ld.so.conf.d/oracle-instantclient.conf"
#RUN ldconfig
#
#RUN ln -s /opt/oracle/instantclient_11_2/libclntsh.so.11.1 /opt/oracle/instantclient_11_2/libclntsh.so

RUN pip install --upgrade pip
RUN pip install -r requirements.txt




#RUN apt update
#RUN apt install gdal-bin python3-gdal -y

EXPOSE 8085


CMD python app.py
#CMD gunicorn -w 4 -b 0.0.0.0:80 sc200.wsgi:application

