# Author: unknown
Description: unknown



# PLUGIN TYPE: def
def handle_client(client_socket):
    #http的api相关代码.
    global needToGet, target, sended, client_address, server_socket, api, api2, client_address
    try:
        request_data = client_socket.recv(1024).decode() #获取浏览器请求
        if not("/favicon.ico" in request_data): #过滤浏览器网页图片请求.
            try:
                api = request_data.split("\r\n")[0].split(" HTTP/")[0].split("GET ")[1] #解析访问的api.
                api = urllib.parse.unquote(api)
                api2 = api
                try:
                    api = api.split("&encoding=")[0]
                except:
                    pass
            except:
                api = "/error"
            try:
                clientIP, clientPort = client_address
                if clientIP == "127.0.0.1":
                    log(clientIP+":"+str(clientPort)+" 访问了http的api: "+api2)
                    if api == "/api?getPlayers": #返回在线玩家列表.
                        response_body = str(getTarget("@a"))
                    elif "/api?getTarget=" in api: #返回选择器.
                        if "&format=true" in api:
                            revTarg = getTarget(api[15:].split("&format=true")[0])
                            response_body = "共 %d 个实体:" % len(revTarg)
                            for i in revTarg:
                                response_body += "\n"+i
                        elif "&format=false" in api:
                            response_body = str(getTarget(api[15:].split("&format=false")[0]))
                        else:
                            response_body = str(getTarget(api[15:]))
                    elif "/api?sendcmd=/" in api: #执行命令.
                        sendto = "/"+api[14:]
                        log(sendto)
                        sendcmd(sendto)
                        response_body = "成功执行: "+sendto
                    else: #api不在列表.
                        response_body = "api未找到"
                else:
                    response_body = "拒绝访问"
            except Exception as err:
                errmsg = "handle_client()中处理api报错, 信息:\n"+str(err)
                response_body = errmsg
                log(errmsg, sendtogamewithERROR = True)
        else:
            response_body = "api未找到"
        #构造响应数据
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: My server\r\n"
        response = response_start_line + response_headers + "\r\n" + response_body
        if "&encoding=gbk" in api2 or "&encoding=GBK" in api2:
            encoding = "gbk"
        else:
            encoding = "utf-8"
        client_socket.send(bytes(response, encoding)) #向客户端返回响应数据
        client_socket.close() #关闭客户端连接
    except Exception as err:
        errmsg = "handle_client()方法报错, 信息:\n"+str(err)
        log(errmsg)
def httpApi():
    global client_address
    #接收http的api请求.
    print("Starting httpApi thread.")
    global needToGet, target, sended, client_socket, client_address, server_socket
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(("", 5556))
        server_socket.listen(128)
        print("httpApi service started.")
        while True:
            client_socket, client_address = server_socket.accept()
            handle_client(client_socket)
            client_socket.close()
    except Exception as err:
        errmsg = "httpApi()方法报错, 信息:\n"+str(err)
        log(errmsg, sendtogamewithERROR = True)



# PLUGIN TYPE: init
thread.start_new_thread(httpApi, ())



