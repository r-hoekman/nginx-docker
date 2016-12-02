FROM debian



RUN apt-get update && apt-get install -y \
git \
curl \
wget \
nodejs \
build-essential \
npm


RUN npm install npm@latest


#install dependencies
RUN mkdir -p /usr/src/app
RUN cd /usr/src/app


COPY package.json /usr/src/app
COPY . /usr/src/app

#create app directory for node

WORKDIR /usr/src/app
ADD . /usr/src/app

EXPOSE 90
RUN



