import matplotlib . pyplot as plt

import psutil as p

app_name_dict = []
count = 0

for process in p.process_iter():
    
    count = count + 1
    
    if count <= 6:
        
       name = process.name()
       cpu_usage = p.cpu_percent()
       print('name : ' , name , '-- cpu_usage : ' , cpu_usage)
       app_name_dict.append(name)
       






