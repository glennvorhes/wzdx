FROM python:3.6-stretch

COPY ./ /wzdx/
WORKDIR "/wzdx"

RUN mkdir /opt/oracle
RUN unzip instantclient-basic-linux.x64-11.2.0.4.0.zip -d /opt/oracle/

RUN sh -c "echo /opt/oracle/instantclient_11_2 > /etc/ld.so.conf.d/oracle-instantclient.conf"
RUN ldconfig

RUN pip install --upgrade pip
RUN pip install -r requirements.txt




#RUN apt update
#RUN apt install gdal-bin python3-gdal -y

EXPOSE 8085


CMD python app.py
#CMD gunicorn -w 4 -b 0.0.0.0:80 sc200.wsgi:application