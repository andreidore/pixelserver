
import requests
import time


def main():
    print("Start")

    
    
    color=0
    while True:
        
        data=[]
        for i in range(10):
            
            data.append({"i":i,"r":color,"g":color,"b":color})
            
        r = requests.post('http://192.168.1.124:9000/api', json = data)

        time.sleep(0.2)

        color=color+10
        if color>255:
            color=0










if __name__=="__main__":
    main()