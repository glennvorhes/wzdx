FROM python:3.6-stretch

COPY ./ /wzdx/
WORKDIR "/wzdx"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#
#RUN apt update
#RUN apt install gdal-bin python3-gdal -y

EXPOSE 5000


CMD python app.py
#CMD gunicorn -w 4 -b 0.0.0.0:80 sc200.wsgi:application