FROM centos:latest
MAINTAINER warren@ourzoo.us

RUN yum -y update
RUN yum -y install wget
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN /usr/bin/python get-pip.py

RUN /usr/bin/pip install --upgrade pip
RUN /usr/bin/pip install flask-restful
COPY server.py .

EXPOSE 5000
CMD ["python", "server.py"]
