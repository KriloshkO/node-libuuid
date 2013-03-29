GYP = /usr/bin/env node-gyp

.PHONY: all
all: build

clean:
	$(GYP) clean

configure: clean
	$(GYP) configure

build: configure
	$(GYP) build
