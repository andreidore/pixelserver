
import requests
import time


def main():
    print("Start")

    
    
    color=0
    while True:
        
        data=[]
        for i in range(558):
            
            data.append({"i":i,"r":color,"g":color+10,"b":color+10})
            
        r = requests.post('http://192.168.1.124:9000/api', json = data)

        time.sleep(0.2)

        color=color+10
        if color>255:
            color=0




def main2():
     print("start")
     idx=0
     while True:
            
            
            
            data=[]
            for i in range(558):
                
                if idx==i:
                   data.append({"i":i,"r":255,"g":255,"b":0})
                else:
                   data.append({"i":i,"r":0,"g":0,"b":0}) 

                
            
            #print(data)
            r = requests.post('http://192.168.1.124:9000/api', json = data)
            time.sleep(0.005)
                
            idx+=1

            if idx==558:
                idx=0

                






if __name__=="__main__":
    main2()