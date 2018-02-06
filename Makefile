.PHONY: build deploy

deploy: build
	tar -zcf - _site/ | ssh dreamhost tar -zxf - --strip-components=1 -C www/pkqk.net

build:
	docker-compose run site jekyll build
