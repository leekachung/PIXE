'''
Quickly Install Docker/Docker-Compose
@author LiKachung leekachung17@gmail.com
'''
#!/usr/bin/python
def docker(version=None):
    return """
    sudo yum remove docker \
        docker-client \
        docker-client-latest \
        docker-common \
        docker-latest \
        docker-latest-logrotate \
        docker-logrotate \
        docker-engine && \
    sudo yum install -y yum-utils \
        device-mapper-persistent-data \
        lvm2 && \
    sudo yum-config-manager \
        https://download.docker.com/linux/centos/docker-ce.repo && \
    sudo yum update && \
    sudo yum install docker-ce docker-ce-cli containerd.io && \
    sudo systemctl start docker && \
    sudo systemctl enable docker
    """
def docker_compose():
    return '''
    '''
