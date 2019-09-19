# Setup and build the client

FROM node:9.4.0-alpine as client

WORKDIR /usr/app/website/
COPY website/package*.json ./
RUN npm install -qy
COPY website/ ./
RUN npm run build
CMD ["npm", "start"]


# Setup the server

FROM python:3-onbuild
ADD . /content/app
WORKDIR /content/app
EXPOSE 4000
RUN pip install -r requirements.txt
ENTRYPOINT ["python","index.py"]

