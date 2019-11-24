# PIXE [PreInstall eXecution Environment]
预安装环境脚本 [Beta V1.1]

# 用处
可通过此脚本在新的服务器
快速构建所需环境

# 目录结构
```
.
├── Install							安装配置目录
│   ├── Docker.py					Docker安装文件
│   └── __pycache__					生成的python缓存
├── Pixe.py							脚本文件
├── README.md						README	
└── logger.log						生成的日志文件
```

# cmd使用
```
python Pixe.py [--host HOSTNAME] [--pw PASSWORD] [--user USERNAME [DEFAULT root]] [--port PORT[DEFAULT 22]]
```

# 推荐使用方式[集群搭建]
可在运维后台添加表单<br>
通过表单方式提交服务器连接信息以及脚本运行id<br>
RPC调用此脚本运行<br>
脚本中提供回调API根据脚本运行id修改服务器环境搭建状态<br>

# 脚本所需环境
- python3
	- sys,argparse,logging,paramiko模块

# Todo
- 传递脚本参数选择需要安装的软件 [目前实现了docker环境的安装]

