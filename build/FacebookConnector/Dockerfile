FROM node:7.10.1-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# RUN npm install forever babel-cli

# Set timezone 
ENV TZ=Asia/Bangkok 
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE 6001

#CMD [ "npm" ,"start" ]
