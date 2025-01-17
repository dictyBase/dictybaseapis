# dictyBase APIs

[![License](https://img.shields.io/badge/License-BSD%202--Clause-blue.svg)](LICENSE)  
![Buf](https://github.com/dictyBase/dictybaseapis/workflows/Buf/badge.svg)
![Last commit](https://badgen.net/github/last-commit/dictyBase/dictybaseapis/master)  
[![Funding](https://badgen.net/badge/Funding/Rex%20L%20Chisholm,dictyBase,DCR/yellow?list=|)](https://reporter.nih.gov/project-details/10024726)

## Misc Badges

![Open Issues](https://badgen.net/github/open-issues/dictyBase/dictybaseapis)
![Open PRS](https://badgen.net/github/open-prs/dictyBase/dictybaseapis)
![Commits](https://badgen.net/github/commits/dictyBase/dictybaseapis/master)
![Branches](https://badgen.net/github/branches/dictyBase/dictybaseapis)
![Tags](https://badgen.net/github/tags/dictyBase/dictybaseapis)  
![GitHub repo size](https://img.shields.io/github/repo-size/dictyBase/dictybaseapis?style=plastic)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/dictyBase/dictybaseapis?style=plastic)

This repository contains interface definitions of public
[dictyBase](http://dictybase.org) API that supports gRPC protocols. These definitions
can be used with open source tools generate client libraries, documentation and
other artifacts.

## Overview

dictyBase APIs are typically deployed as API services that are hosted under different DNS names.
It uses Protocol Buffers version 3 (proto3) as their Interface
Definition Language (IDL) to define the API interface and the structure of the
payload messages. It can be accessed through [gRPC](https://grpc.io).

## Repository structure

In general, every API has its own directory with matching proto packages. The
`dictybase` folder contains reusable definitions.

## Development

This project has been designed to be automated by GitHub Actions. To make
changes, create a new branch and push your changes. This will automatically
create a pull request then run `buf lint` to verify your changes. If everything
is fine, merge it to the master branch and it will generate updated Go code and
open a PR in the [go-genproto](https://github.com/dictyBase/go-genproto)
repository where it will need to be manually reviewed.

Additionally, when changes are merged to master, API documentation will be
automatically generated using the protobuf documentation generator plugin.

**Note: if making any updates to the `buf.gen.yaml` file, you need to run `buf beta mod update`
to update the lock file.**
