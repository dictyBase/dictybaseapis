generate:
	buf generate --path dictybase

lint:
	buf build
	buf lint
	# buf breaking --against 'https://github.com/dictyBase/dictybaseapis.git#branch=master'

BUF_VERSION:=0.41.2
PROTOC_GEN_GO_VERSION:=1.26.0
PROTOC_GEN_GO_GRPC_VERSION:=1.1.0
PROTOC_GEN_GRPC_GATEWAY_VERSION:=1.16.0
PROTOC_GEN_GOVALIDATORS_VERSION:=0.3.2

install:
	go install google.golang.org/protobuf/cmd/protoc-gen-go@v${PROTOC_GEN_GO_VERSION}
	go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@v${PROTOC_GEN_GO_GRPC_VERSION}
	go install github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway@v${PROTOC_GEN_GRPC_GATEWAY_VERSION}
	go install github.com/mwitkow/go-proto-validators/protoc-gen-govalidators@v${PROTOC_GEN_GOVALIDATORS_VERSION}
	mkdir -p buf/bin
	curl -L -o buf/bin/buf \
		https://github.com/bufbuild/buf/releases/download/v${BUF_VERSION}/buf-Linux-x86_64
	chmod +x buf/bin/buf