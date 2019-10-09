# dictyBase APIs
[![License](https://img.shields.io/badge/License-BSD%202--Clause-blue.svg)](LICENSE)   
![GitHub repo size](https://img.shields.io/github/repo-size/dictyBase/dictybaseapis?style=plastic)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/dictyBase/dictybaseapis?style=plastic)
![Commits](https://badgen.net/github/commits/dictyBase/dictybaseapis/master)
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
payload messages. The same interface definition is used for both REST and RPC
versions of the API, which can be accessed two different wire protocols. 

1. JSON over HTTP: Access API using JSON over HTTP, using any standard HTTP library 
   of any language.
2. Protocol Buffers over gRPC: Access API through [gRPC](https://grpc.io).

## Repository structure
In general, every API has its own directory with matching proto packages. The
`api` folder contain reusable definitions.

