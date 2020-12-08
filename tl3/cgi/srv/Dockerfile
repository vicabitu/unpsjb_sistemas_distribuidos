FROM nginx

SHELL ["/bin/bash", "-c"]
RUN apt-get -qq update
RUN apt-get -qq install -y apt-utils
RUN apt-get -qq install -y python3
RUN apt-get -qq install -y python3-pip
RUN apt-get -qq install -y libpq-dev
RUN apt-get -qq install -y nginx 
RUN apt-get -qq install -y fcgiwrap


RUN pip3 install SQLAlchemy
RUN pip3 install psycopg2

RUN mkdir /usr/lib/cgi-bin -p
RUN chmod -R 755 /usr/lib/cgi-bin

COPY ./nginx.conf /etc/nginx/conf.d/nginx.conf