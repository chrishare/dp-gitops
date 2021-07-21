# Commands

### Docker

Start a docker container with the latest DataPower image from dockerhub, exposing port 9090 and 5550 for webmgmt.
```
docker run -e DATAPOWER_ACCEPT_LICENSE=true ibmcom/datapower -p 9090:9090 -p 5550:5550
docker run -it \
  -e DATAPOWER_ACCEPT_LICENSE=true \
  -e DATAPOWER_INTERACTIVE=true \
  -e DATAPOWER_WORKER_THREADS=4 \
  -p 9090:9090 \
  -p 5550:5550

docker run -it \
  -v $PWD/test-data/docker/empty-domain/config:/drouter/config \
  -v $PWD/test-data/docker/empty-domain/local:/drouter/local \
  -e DATAPOWER_ACCEPT_LICENSE=true \
  -e DATAPOWER_INTERACTIVE=true \
  -e DATAPOWER_WORKER_THREADS=4 \
  -p 9090:9090 \
  -p 5550:5550 \
  ibmcom/datapower
```