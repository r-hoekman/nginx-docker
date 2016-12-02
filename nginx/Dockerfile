FROM nginx

MAINTAINER "Rob Hoekman robbiehoekman@hotmail.com"

ENV TERM xterm

RUN apt-get update && apt-get install -y \
git \
curl \
nano \
zip \
unzip \
wget


RUN echo "deb http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list
RUN echo "deb-src http://packages.dotdeb.org jessie all" >> /etc/apt/sources.list

RUN wget https://www.dotdeb.org/dotdeb.gpg && \
apt-key add dotdeb.gpg

RUN apt-get update && apt-get install -y \
php7.0 \
php7.0-gd \
php7.0-intl \
php7.0-curl \
php7.0-mbstring \
php7.0-dom \
php7.0-cli \
php7.0-pgsql \
nodejs \
nodejs-legacy \

build-essential \
npm


RUN curl -sS http://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer



#RUN composer create-project -s alpha sylius/sylius-standard panelprint
#RUN cd panelprint
#RUN php app/console sylius:install
#RUN npm install
#RUN npm run gulp
#RUN gulp


EXPOSE 80
