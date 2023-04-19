.PHONY: all clean
CC:=gcc
CXX:=g++
TARGET:=$(shell uname -m)-$(shell uname -i)-$(shell uname -s|tr '[:upper:]' '[:lower:]')
all: build/ \
	build/libncurses.a \
	build/libhistory.a \
	build/libreadline.a
build/:
	mkdir -p build
build/libncurses.a: build/
	env
	cd build
	../ncurses-6.3-20220319/