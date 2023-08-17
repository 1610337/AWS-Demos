FROM public.ecr.aws/docker/library/node:alpine3.16

# Create app directory
WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

# Bundle app source
COPY . .

EXPOSE 3000

ENTRYPOINT ["node","index.js"]
