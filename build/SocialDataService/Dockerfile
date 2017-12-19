FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# RUN apt-get update
# RUN apt-get install nano net-tools
RUN pip install python-dateutil pymongo flask

# Set timezone
ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Set localhost 
RUN echo '127.0.0.1   localhost localhost.localdomain' >> /etc/hosts

EXPOSE 5005

CMD [ "python" ,"index.py" ]

