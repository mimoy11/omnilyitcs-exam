# ReactJS, Flask, NGINX, MongoDB
This repository contains example code showing how to to set up and containerize a full stack web application with a React frontend, a Flask RESTful API and a MongoDB database using Docker. It includes one docker-compose file to set up a development environment and a docker-compose-prod file to set up a production environment.

## System Requirements
- Ubuntu  18.04 ~ 20 operating system 
- [Docker engine](https://docs.docker.com/engine/install/ubuntu/)
- [Docker compose](https://docs.docker.com/compose/install/)

## Installation

**Clone the repo:**

```
$ git clone git@github.com:mimoy11/omnilyitcs-exam.git
$ cd master
```

**Build the images and start docker:**
```bash
$ docker-compose up -d --build
```

## Usage

**Running the application in development w/ watch mode**
```bash
$ docker-compose up -d --build
```

**Running the application in production**
```bash
$ docker-compose -f docker-compose-prod.yml up -d --build
```

## Mongo Free Monitoring
https://cloud.mongodb.com/freemonitoring/cluster/OU363NQFVGFQN4TOOWT2S3TW2TTMFVRI

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIMOY](https://github.com/mimoy11/)

