import paramiko
import sys
import datetime
import base64
import time 

nbytes = 4096
port = 22
user = "sshuser"
secret = "sshpassword"
#secret = base64.b64decode(b'passhash'.decode("utf-8"))


reload(sys)
sys.setdefaultencoding('utf8')

now = datetime.datetime.now()
datex = now.strftime("%Y%m%d-%H%MBST")

h = str(sys.argv[1])
c = str(sys.argv[2])

######################################## 
#### connect ############################
#########################################
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Set policy to use when connecting to servers without a known host key
ssh.connect(hostname=h, username=user, password=secret, port=port)

##########################################
#### command  ############################
##########################################
chan = ssh.invoke_shell()

# turn off paging
chan.send('tmsh \n')
time.sleep(1)
chan.send('cd / \n')
time.sleep(1)
chan.send(c + ' \n')
time.sleep(1)
chan.send('y \n')
time.sleep(3)
resp = chan.recv(999999)

#print(resp)
output = resp
command = c.replace(" ", "-")
file = open('' + h +'-'+ command.replace("|", "") +'-'+ datex +'.txt', 'w')
file.write(''.join(output))
file.close() 
ssh.close()
