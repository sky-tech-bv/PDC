APP=$(shell basename $(shell git remote get-url origin))
REGESTRY=sky-tech-bv
VERSION=$(shell git describe --tags --always --abbrev=0)-$(shell git rev-parse --short HEAD)
TARGETOS=linux
TARGETARCH=arm64

format: 
	gofmt -s -w ./

lint:
	golint

get:
	go get

test:
	go test -v

build: format
	CGO_ENABLED=0 GOOS=${TARGETOS} GOARCH=${TARGETARCH} go build -v -o kbot -ldflags "-X="github.com/sky-tech-bv/PDC/Week-3/kbot/cmd.appVersion=${VERSION}
	
image:
	docker build . -t ${REGESTRY}/${APP}:${VERSION}-${TARGETARCH}

push:
	docker push ${REGESTRY}/${APP}:${VERSION}-${TARGETARCH}

clean:
	rm -rf kbot