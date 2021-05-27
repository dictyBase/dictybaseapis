generate:
	buf generate --path dictybase

lint:
	buf build
	buf lint
	# buf breaking --against 'https://github.com/dictyBase/dictybaseapis.git#branch=master'

BUF_VERSION:=0.41.2
PROTOC_GEN_GO_VERSION:=1.5.2
PROTOC_GEN_GO_GRPC_VERSION:=1.1.0
PROTOC_GEN_GOVALIDATORS_VERSION:=0.3.2
PROTOC_GEN_GRPC_GATEWAY_VERSION:=2.4.0

install:
	go install \
		google.golang.org/protobuf/cmd/protoc-gen-go@v${PROTOC_GEN_GO_VERSION} \
		google.golang.org/grpc/cmd/protoc-gen-go-grpc@v${PROTOC_GEN_GO_GRPC_VERSION} \
		github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway@v${PROTOC_GEN_GRPC_GATEWAY_VERSION} \
		github.com/mwitkow/go-proto-validators/protoc-gen-govalidators@v${PROTOC_GEN_GOVALIDATORS_VERSION}
	curl -L \
    	"https://github.com/bufbuild/buf/releases/download/v${BUF_VERSION}/buf-Linux-x86_64" \
    	-o "$(shell go env GOPATH)/bin/buf" && \
  		chmod +x "$(shell go env GOPATH)/bin/buf"