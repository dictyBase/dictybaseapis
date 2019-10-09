# dictyBase APIs
[![License](https://img.shields.io/badge/License-BSD%202--Clause-blue.svg)](LICENSE)   
![GitHub repo size](https://img.shields.io/github/repo-size/dictyBase/dictybaseapis?style=plastic)
![Last commit](https://badgen.net/github/last-commit/dictyBase/dictybaseapis/master)   
[![Funding](https://badgen.net/badge/NIGMS/Rex%20L%20Chisholm,dictyBase/yellow?list=|)](https://projectreporter.nih.gov/project_info_description.cfm?aid=9476993)
[![Funding](https://badgen.net/badge/NIGMS/Rex%20L%20Chisholm,DSC/yellow?list=|)](https://projectreporter.nih.gov/project_info_description.cfm?aid=9438930)


This repository contains interface definitions of public
[dictyBase](http://dictybase.org) API that supports both gRPC and REST
protocols. These definitions can be used with open source tools generate client
libraries, documentation and other artifacts.

## Overview 
dictyBase APIs are typically deployed as API services that are hosted under different DNS names. 
It uses Protocol Buffers version 3 (proto3) as their Interface
Definition Language (IDL) to define the API interface and the structure of the
payload messages. It can be accessed through [gRPC](https://grpc.io).

## Repository structure
In general, every API has its own directory with matching proto packages. The
`api` folder contain reusable definitions.

## Requirements
* [Protobuf](https://github.com/protocolbuffers/protobuf) - v3.9.2
* [grpc-gateway](https://github.com/grpc-ecosystem/grpc-gateway) - v1.11.3
### Compiling to golang
* [Golang protobuf](https://github.com/golang/protobuf) - v1.3.2
* [go-proto-validators](https://github.com/mwitkow/go-proto-validators) - v0.2.0
### Optional
* [protoc-gen-doc](https://github.com/pseudomuto/protoc-gen-doc/) - v1.3.0


## Developers
<a href="https://sourcerer.io/cybersiddhu"><img src="https://sourcerer.io/assets/avatar/cybersiddhu" height="80px" alt="Sourcerer"></a>
<a href="https://sourcerer.io/wildlifehexagon"><img src="https://sourcerer.io/assets/avatar/wildlifehexagon" height="80px" alt="Sourcerer"></a>
