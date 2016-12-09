FROM nginx

MAINTAINER "Rob Hoekman robbiehoekman@hotmail.com"

ENV TERM xterm

RUN apt-get update && apt-get install -y \
git \
curl \
nano \
zip \
unzip \
net-tools \
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
php7.0-fpm \
nodejs \
nodejs-legacy \

build-essential \
npm



RUN curl -sS http://getcomposer.org/installer | php
RUN mv composer.phar /usr/local/bin/composer


#RUN cd /usr/share/nginx/html
#RUN composer create-project -s alpha sylius/sylius-standard panelprint
#RUN cd panelprint

#RUN npm install
#RUN npm run gulp
COPY conf.d/default.conf /etc/nginx/conf.d/
COPY nginx-config/nginx.conf /etc/nginx/
COPY php-config/php.ini /etc/php/7.0/cli/
COPY ../Sylius/app/config/parameters.yaml /usr/share/nginx/html/Sylius/app/config/
RUN php bin/console sylius:install

RUN service nginx reload
RUN service php7.0-fpm restart

EXPOSE 80
