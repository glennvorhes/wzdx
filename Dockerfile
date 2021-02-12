
FROM python:3.8

COPY ./ /wzdx/
WORKDIR "/wzdx"

RUN apt update
RUN apt install -y libaio1 libaio-dev

RUN mkdir /opt/oracle
RUN unzip instantclient-basic-linux.x64-11.2.0.4.0.zip -d /opt/oracle/
RUN ln -s /opt/oracle/instantclient_11_2/libclntsh.so.11.1 /opt/oracle/instantclient_11_2/libclntsh.so

RUN echo "/opt/oracle/instantclient_11_2" > /etc/ld.so.conf.d/oracle-instant-client.conf
RUN ldconfig

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8085

CMD python app.py
#CMD gunicorn -w 4 -b 0.0.0.0:80 sc200.wsgi:application
