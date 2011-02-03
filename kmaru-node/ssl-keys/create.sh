#!/bin/bash

echo "Creating new key"
openssl genrsa -des3 -out server.key 1024

echo "Creating a new CSR"
openssl req -new -key server.key -out server.csr

echo "Stripping the password from the key"
cp server.key server.key.org
openssl rsa -in server.key.org -out server.key 

echo "Generating the self-signed cert"
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

