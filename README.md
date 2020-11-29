# Web Crawler
Implementing a Web Crawler for pastebin website.

### Deployment

1. Extract the tar file
2. cd into the extracted directory
3. run:
        ```
        docker-compose up
        ```

### MongoDB

You can view the data saved in the mongo instance using the following steps:

1. Run the following command:

```sh
docker exec -it crawler-mongo /bin/bash
```

2. Once your inside the container, run the following steps:

```sh
mongo
use crawler
db.pastes.find().pretty()
```
