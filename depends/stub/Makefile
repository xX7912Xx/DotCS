.PHONY: all clean
CC:=gcc
all: libreadline.so libz.so
ZLIB_SOVERSION := 1
libreadline.so: readline.c
	$(CC) $(CFLAGS) readline.c -Wl,-soname,libreadline.so.8 -shared -o libreadline.so
libz.so: zlib.c
	$(CC) $(CFLAGS) zlib.c -Wl,-soname,libz.so.$(ZLIB_SOVERSION),--version-script,zlib.map -shared -o libz.so
clean:
	rm -f libreadline.so libz.so
