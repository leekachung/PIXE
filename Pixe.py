'''
pixe PreInstall eXecution Environment
@author LiKachung leekachung17@gmail.com
'''
#!/usr/bin/python
import sys,argparse,logging,time,paramiko
# Install What We Need
from Install.Docker import docker

class Pixe:
    # status tuple init
    __status_map = (0,1,2,3,4)
    # param init
    __client = __host = __user = __pw = __port = ''
    # callback status init
    callback_status = 0

    def __init__(self):
        # init log config
        self.__logger_config()
        # get args
        self.__get_args()
        # ssh target server
        self.connect()
        # run cmd
        self.excute_command()

    def __logger_config(self):
        logging.basicConfig(filename='logger.log', level=logging.WARNING)
        # only record paramiko important log
        logging.getLogger("paramiko").setLevel(logging.WARNING)

    def __get_args(self):
        # Recive args e.g:host/name/pw/todo and so on
        cmd = argparse.ArgumentParser(description="PIXE")
        cmd.add_argument('--host', default="127.0.0.1", help="the host which we will connect", dest="hostname")
        cmd.add_argument('--pw', default="password", help="ssh password", dest="password")
        cmd.add_argument('--user', default="root", help="ssh user", dest="username")
        cmd.add_argument('--port', default="22", help="the port which we will connect [default 22]",dest="port")
        args = cmd.parse_args()
        self.__host, self.__user, self.__pw, self.__port = args.hostname, args.username, args.password, args.port

    def connect(self):
        self.__client = paramiko.SSHClient()
        self.__client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            # Connect Host
            self.__client.connect(hostname=self.__host,port=self.__port,username=self.__user,password=self.__pw)
            logging.info(self.cur_time() + self.__host + ' running')
        except Exception as e:
            # callback notice server connect error
            self.callback_server_api(str(e))
            # record error log
            logging.error(self.cur_time() + 'Connect Error: host=>{}, reason=>{}'.format(self.__host, e))
            print(self.cur_time() + 'Connect Error: host=>{}, reason=>{}'.format(self.__host, e))
            sys.exit()

    def excute_command(self):
        # Excute Command
        for cmd in docker():
            stdin,stdout,stderr = self.__client.exec_command(cmd)
            if(stdout.channel.recv_exit_status()):
                logging.error(self.cur_time() + 'Install Error: ' + stdout.read().decode('UTF8'))
                self.callback_server_api(str("error"))
                sys.exit()
            print(stdout.read().decode('UTF8'))
        self.callback_server_api(str("success"))

    def callback_server_api(self, msg=None):
        if (msg):
            print("Callback: " + msg)
        # Todo: Callback Server Api to update status

    def cur_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " "

    def __del__(self):
        # close ssh
        if(self.__client):
            self.__client.close()

# enter pointer
if __name__ == '__main__':
    Pixe()
else:
    print('Error: this is from the other mod')

'''
End
'''
