FROM ubuntu:16.04

MAINTAINER Sushant Athaley <sathaley@iu.edu>

RUN apt-get update

RUN apt-get update -q && apt-get install -qy \
    build-essential \
    python-dev \
    python-pip \
    wget \
    curl \
    emacs \
    git-core \
    default-jre \
software-properties-common

# Set the working directory to /app
WORKDIR /aws

# Copy the current directory contents into the container at /app
ADD . /aws

#RUN echo $PWD

#EXPOSE 8080

RUN make service

#CMD ["make", "start"]

