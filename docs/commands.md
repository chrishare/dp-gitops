# Commands

### Docker

Start a docker container with the latest Datapower image from dockerhub, with pure default configuration. Default password is admin/admin. That is, password has will be:
```
openssl passwd -1 -salt 12345678 "admin"  
> $1$12345678$kbapHduhihjieYIUP66Xt/
```
```
docker run -it \
  -e DATAPOWER_ACCEPT_LICENSE=true \
  -e DATAPOWER_INTERACTIVE=true \
  -e DATAPOWER_WORKER_THREADS=4 \
  -p 9090:9090 \
  -p 5550:5550 \
  ibmcom/datapower
```
Start a docker container with the latest DataPower image from dockerhub, exposing port 9090 and 5550 for webmgmt.
```
docker run -it \
  -v $PWD/test-data/docker/empty-domain/config:/opt/ibm/datapower/drouter/config \
  -v $PWD/test-data/docker/empty-domain/local:/opt/ibm/datapower//drouter/local \
  -e DATAPOWER_ACCEPT_LICENSE=true \
  -e DATAPOWER_INTERACTIVE=true \
  -e DATAPOWER_WORKER_THREADS=4 \
  -p 9090:9090 \
  -p 5550:5550 \
  ibmcom/datapower
```
Start a docker container using a specific config file:
```
docker run -it \
  -v $PWD/dp-gitops/tmp-data/config:/opt/ibm/datapower/drouter/config \
  -e DATAPOWER_ACCEPT_LICENSE=true \
  -e DATAPOWER_INTERACTIVE=true \
  -e DATAPOWER_WORKER_THREADS=4 \
  -p 9090:9090 \
  -p 5550:5550 \
  ibmcom/datapower
```

### OpenSSL

Generate a self-signed key that is suitable only for LOCAL development (not production!)

```
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"
```

### REST API

Get all object types
```
curl -v -k https://172.17.0.2:5554/mgmt/status/ -u "admin:admin"
```

Get a specific object
```
curl -v -k https://172.17.0.2:5554/mgmt/config/default/HTTPSourceProtocolHandler/test_http_handler -u "admin:admin"
```

