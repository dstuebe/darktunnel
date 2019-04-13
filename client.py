import cv2
import numpy as np
import socket
import sys
import pickle

cap=cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('localhost',8089))
while True:
    ret,frame=cap.read()
    #clientsocket.sendall(struct.pack("H", len(data))+data) ### new code
    ### Fixed size 2764800
    clientsocket.sendall(frame.tobytes())
    print("Sent frame!!!")
