# Use an official Python runtime as a parent image
FROM python:3.6.2-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update
RUN apt-get install build-essential libicu-dev software-properties-common -y
RUN add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" -y
RUN apt-get update
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 seen true" | debconf-set-selections
RUN apt-get install oracle-java8-installer -y
RUN ./install-packages.sh

# Set timezone 
ENV TZ=Asia/Bangkok 
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Set localhost
RUN echo '127.0.0.1   localhost localhost.localdomain' >> /etc/hosts

# Make port 80 available to the world outside this container
EXPOSE 5006

# Run app.py when the container launches
CMD ["python", "cron.py"]
