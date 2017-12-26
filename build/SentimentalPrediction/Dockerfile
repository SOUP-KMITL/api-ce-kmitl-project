# Use an official Python runtime as a parent image
FROM python:3.6.2-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN sudo apt-get update
RUN sudo apt-get install build-essential libicu-dev software-properties-common -y
RUN sudo add-apt-repository "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" -y
RUN sudo apt-get update
RUN sudo echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
RUN sudo echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 seen true" | debconf-set-selections
RUN sudo apt-get install oracle-java8-installer -y
RUN sudo ./install-packages.sh

# Set timezone 
ENV TZ=Asia/Bangkok 
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Make port 80 available to the world outside this container
EXPOSE 5006

# Run app.py when the container launches
CMD ["python", "cron.py"]
