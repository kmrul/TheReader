# Setup and build the client

FROM node:9.4.0
WORKDIR /usr/app
COPY package*.json ./
RUN npm install -qy
COPY . .
EXPOSE 3000
CMD ["npm", "start"]


# Setup the server
FROM python:3-onbuild
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

