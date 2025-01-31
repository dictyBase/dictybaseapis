# dictyBase APIs

[![License](https://img.shields.io/badge/License-BSD%202--Clause-blue.svg)](LICENSE)
![Buf](https://github.com/dictyBase/dictybaseapis/workflows/Buf/badge.svg)
[![Funding](https://badgen.net/badge/Funding/NIH%2C%20Rex%20L%20Chisholm%20Lab/yellow)](https://reporter.nih.gov/project-details/10024726)

Protocol Buffer definitions for dictyBase's gRPC APIs. Used to generate client libraries, 
server stubs, and documentation.

## Overview

This repository contains:

- .proto definitions for dictyBase's public APIs
- Shared message types and service definitions in the `dictybase` namespace
- Generated code via [Buf](https://buf.build/) (managed through GitHub Actions)

## Repository structure

/dictybase
  /api          # Common API patterns and utilities
  /content      # Content management API definitions
  /user         # User service definitions
  /stock        # Stock management interfaces
  ...           # Other domain-specific APIs

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
