NAME=mzdgnk/pgdemo
VERSION=latest

build:
	docker build -t ${NAME}:${VERSION} .

push: build
	docker push ${NAME}:${VERSION}
