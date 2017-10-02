# dictyBase APIs
This repository contains interface definitions of public
[dictyBase](http://dictybase.org) API that supports both gRPC and REST
protocols. These definitions can be used with open source tools generate client
libraries, documentation and other artifacts.

## Overview 
dictyBase APIs are typically deployed as API services that are hosted under different DNS names. 
It uses Protocol Buffers version 3 (proto3) as their Interface
Definition Language (IDL) to define the API interface and the structure of the
payload messages. The same interface definition is used for both REST and RPC
versions of the API, which can be accessed two different wire protocols. 

1. JSON over HTTP: Access API using JSON over HTTP, using any standard HTTP library 
   of any language.
2. Protocol Buffers over gRPC: Access API through [gRPC](https://grpc.io).

## Repository structure
In general, every API has its own directory with matching proto packages. The
`api` folder contain reusable definitions.

