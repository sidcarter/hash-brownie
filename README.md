Message hasher (aka Hash Brownie)
=================================

A simple docker image which servers the SHA256 hash of any message and returns the original message when requested for.

# Build specs and defaults

* This docker image uses Python 3.6 (Alpine) and Redis 3.2.8 (Alpine), also tested with Python 2.7
* The container is set to restart in case of any crashes etc.,
* By default, we have a max log file size of 100k and ensure we only keep 5 log files

## Docker versions tested on
```
$ docker --version
Docker version 17.03.1-ce, build c6d412e
$ docker-compose --version
docker-compose version 1.11.2, build dfed245
```

# HOWTO

## POST a message
```
$ curl -X POST -H "Content-Type: application/json" -d '{"message": "number"}'  --cacert localhost.crt https://localhost/messages
{
  "digest": "12886f9d00055adf24c40579e22d31b2b45f2023f892954ffd5567beb60825f8"
}
```
## GET a message
```
$ curl --cacert localhost.crt https://localhost/messages/12886f9d00055adf24c40579e22d31b2b45f2023f892954ffd5567beb60825f8
{
  "message": "number"
}
```

# SSL Certificate

For testing purposes, you might want to create a self-signed cert or use the included cert.

## Creating a self-signed certificate
You can follow the instructions from 
[here](https://www.linux.com/learn/creating-self-signed-ssl-certificates-apache-linux
"Self-Signed Certificates") or use the following set of instructions:

* openssl req -new > localhost.ssl.csr
* openssl rsa -in privkey.pem -out localhost.key
* openssl x509 -in new.cert.csr -out new.cert.cert -req -signkey new.cert.key -days NNN

# For Scaling
This is a simple app and the key software is Redis. There are many ways to scale Redis, depending on the use case.

In the simplest case, the app can be memory bound, and the easiest way to scale would be to scale up (vertically) using an instance with higher memory. Adding more CPUs may not help, since Redis is single threaded. 

For the use-case where the app is read heavy, you can scale out horizontally by adding read-replicas of the same data.
In cases where the app is write heavy, adding master replicas can help. Of course, in this cause, read consistency is not guaranteed.
In cases where the data is complex, sharding or partitioning can help scale too.

