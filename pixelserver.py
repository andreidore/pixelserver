#!/usr/bin/env python

import threading
import time
from queue import Queue,Empty

import opc
from bottle import request, route, run, static_file

ADDRESS = "localhost"
queue = Queue()


@route('/')
def index():
    return static_file("help.html",root="./")

@route('/api', method='POST')
def api():
    """ API JSON function.    
    """
    data = request.json
    print(data)
    queue.put(data)


def main():
    """ Main function.

        Return True on success or False on failure.

    """

    print("Start pixel server.")


    # Create a client object
    client = opc.Client('localhost:7890')

    # Test if it can connect (optional)
    if client.can_connect():
        print('connected to %s' % ADDRESS)
    else:
        # We could exit here, but instead let's just print a warning
        # and then keep trying to send pixels in case the server
        # appears later
        print('WARNING: could not connect to %s' % ADDRESS)


    threading.Thread(target=run, kwargs=dict(host='0.0.0.0', port=9000,quiet=True)).start()
    

    pixels=[(0,0,0)]*60

    pixels[0]=[255,0,0]
    while True:
        
        try:
            pixel = queue.get(True,0.1)
            if pixel is not None:
                if isinstance(pixel,list):
                    for p in pixel:
                        #print(p)
                        pixels[p["i"]]=(p["r"],p["g"],p["b"])

        

            queue.task_done()
        except Empty:
            pass

        #print(pixels)
        client.put_pixels(pixels, channel=0)
        

        
        time.sleep(1/30.0)




if __name__ == "__main__":
    main()
