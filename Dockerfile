FROM centos:latest
MAINTAINER warren@ourzoo.us

RUN yum -y update

# Install pip

RUN /usr/bin/pip install --upgrade pip
RUN /usr/bin/pip install flask-restful
COPY server.py .

EXPOSE 5000
CMD ["python", "server.py"]
