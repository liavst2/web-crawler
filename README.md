# Web Crawler
Implementing a Web Crawler

### Deployment

The crawler is crawling Pastebin website.

Every 10 seconds the crawler engine collects the new pastes done in the website, and saves their details in mongoDB.

The deployment of the system is done using docker-compose:

```sh
docker-compose up --build
```

### MongoDB

You can examine the data saved in the mongo instance using the following steps:

1. Run the following command:

```sh
docker exec -it crawler-mongo /bin/bash
```

2. Once your inside the container, run the following:

```sh
mongo # To connect to the running mongo instance CLI
use crawler
db.pastes.find().pretty()
```
