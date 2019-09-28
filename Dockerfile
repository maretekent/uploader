FROM python:3.6
ARG ENVIRONMENT=development
ENV ENVIRONMENT=$ENVIRONMENT
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

#BEGIN TEMPORARY STATICS STOP GAP
RUN apt-get update
RUN apt-get -y install gnupg \
    apt-utils \
    apt-transport-https \
    curl \
    zip

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -

RUN apt-get -y install nodejs yarn
RUN yarn
RUN pip3 install -r ./requirements/${ENVIRONMENT}.txt
RUN node node_modules/webpack/bin/webpack.js

RUN python3 manage.py collectstatic --noinput
#END

# Install Python deps
RUN pip install --no-cache-dir -r ./requirements/${ENVIRONMENT}.txt

# Run environment build script
RUN ./devops/docker/build_${ENVIRONMENT}.sh

CMD ["/bin/bash", "./devops/scripts/run.sh"]
