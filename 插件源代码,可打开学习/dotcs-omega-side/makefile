.PHONY:build/dotcs_pro run
TARGETS:= build/ complete input_prompt pro pro-input_prompt exp exp-input_prompt
# tag

### *-----------------------------------* ###
### | These processes are designed for  | ###
### | GitHub Actions. You should ignore | ###
### | this part if not performing cross | ###
### | -compilations.                    | ###
### *-----------------------------------* ###
# mkdir -p ${BUILD_DIR}
# chmod u+x -R ${BUILD_DIR}
# mkdir -p $@
# mkdir -p $@/depends/python
# chmod u+x -R ./dotcs/depend/python/Python-${PYTHON_VERSION}/
# echo $@
# 临时变量
build-linux:
	go build -buildmode=plugin -o libdotcs-omega-side-linux-amd64.so main.go
# build-windows:
# 	GODEBUG=madvdontneed=1 CGO_CFLAGS=${CGO_DEF} CC=/usr/bin/x86_64-w64-mingw32-gcc GOOS=windows GOARCH=amd64 CGO_ENABLED=1 go build -buildmode=plugin -o libdotcs-omega-side-windows-amd64.dll main.go
build-linux-arrch64:
	GODEBUG=madvdontneed=1 CGO_CFLAGS=${CGO_DEF} CC=/usr/bin/aarch64-linux-gnu-gcc CGO_ENABLED=1 GOARCH=arm64 go build -buildmode=plugin -o libdotcs-omega-side-linux-arm64.dll main.go
