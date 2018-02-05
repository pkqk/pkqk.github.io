.PHONY: build deploy

build:
	docker-compose run site jekyll build

deploy: build
	tar -zcf - _site/ | ssh dreamhost tar -zxf - --strip-components=1 -C www/pkqk.net
