# locust-loadtesting-docker
## setup using docker compose 
``` create docker-comose.yml ``` file

```
version: '3'
services:
  locust:
    image: locustio/locust
    ports:
      - "8089:8089"
    volumes:
      - ./locust:/mnt/locust
    command: -f /mnt/locust/locustfile.py --host=https://mohsinrubel.com
    networks:
      - stress-network

networks:
  stress-network:

```

* crete folder name `` locust ``
* add configure file name ``` locustfile.py ``` this `` locust `` folder
* up docker compose using ``` docker compose up -d ```
  
