# 说明

author_server.py 为鉴权模块服务端，在服务器上后台启动，一直运行即可。
author_client.py 为测试用的鉴权模块客户端，模拟向鉴权模块服务端发送请求

author_module_c++ 为鉴权模块客户端的C++样例，如果主体程序为C++框架，可以将该样例加入到主体代码中。

## 服务端部署

1. 启动鉴权模块服务器，linux下后台启动方法：
nohup python author_server.py > log 2>&1

2. 鉴权服务器默认为8080端口，新申请的阿里服务器需要设置开放端口，参考
https://www.jianshu.com/p/fc9012820f08

3. 添加crontab 定时任务，定时杀死并重启python author_server.py，用于解决时间长后客户端连接不上服务端的问题。