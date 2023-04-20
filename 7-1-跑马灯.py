'''
跑马灯时钟
'''
import os
import time

def paomadeng():


    while True:
        
        content = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ' '
        content_len = len(content) + 1
        os.system('clear')
        for i in range(2):
            print(content)
            time.sleep(0.5)
            os.system('clear')
            time.sleep(0.5)
        for i in range(content_len):
            os.system('clear')
            print(content)
            content = content[1:] + content[0]
            time.sleep(0.3)

paomadeng()