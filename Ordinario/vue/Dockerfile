# base image
FROM node:12.2.0-alpine

COPY . /usr/src/vue

# set working directory
WORKDIR /usr/src/vue

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json /app/package.json
RUN npm install
RUN npm install @vue/cli@3.7.0 -g


# start app
CMD ["npm", "run", "serve"]

