Message hasher
==============

A simple docker image which servers the SHA256 hash of any message and returns the original message when requested for.

# Build/Run Requirements

* This docker image uses Python 3.6 (Alpine) and Redis 3.2.8 (Alpine), also tested with Python 2.7
* The container restarts on-failure

# Docker versions tested on
```
$ docker --version
Docker version 17.03.1-ce, build c6d412e
$ docker-compose --version
docker-compose version 1.11.2, build dfed245
```

# SSL Certificate

For testing purposes, you might want to create a self-signed cert or use the included cert.

## Creating a self-signed certificate
You can get the instructions
[here](https://www.linux.com/learn/creating-self-signed-ssl-certificates-apache-linux
"Self-Signed Certificates")

Short set of instructions:

* openssl req -new > localhost.ssl.csr
* openssl rsa -in privkey.pem -out localhost.key
* openssl x509 -in new.cert.csr -out new.cert.cert -req -signkey new.cert.key -days NNN

# For Scaling




