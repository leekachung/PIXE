# PIXE [PreInstall eXecution Environment]
预安装环境脚本

# 用处
可通过此脚本在新的服务器
快速构建所需环境

# 推荐使用方式[集群搭建]
可在运维后台添加表单<br>
通过表单方式提交服务器连接信息以及脚本运行id<br>
RPC调用此脚本运行<br>
脚本中提供回调API根据脚本运行id修改服务器环境搭建状态<br>

# 脚本所需环境
- python3
	- sys,argparse,logging,paramiko模块



