NAME=mzdgnk/pgdemo
VERSION=stable

build:
	docker build -t ${NAME}:${VERSION} .

push: build
	docker push ${NAME}:${VERSION}
