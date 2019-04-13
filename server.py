import socket
import sys
import cv2
import numpy as np
import ipdb
import io

HOST=''
PORT=8089

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()

MSGLEN = 2764800

with io.BytesIO(bytearray(MSGLEN)) as mybuffer:

    while True:
        mybuffer.seek(0)

        while mybuffer.tell() < MSGLEN:
            chunk = conn.recv(4096)  # 2764800 / 4096 == 675
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            mybuffer.write(chunk)
    
        frame = np.frombuffer(mybuffer.getvalue(), dtype=np.uint8).reshape(720, 1280, 3)
        print("Got frame!!! {}".format(frame))
        cv2.imshow('frame',frame)
        cv2.waitKey(1)

# ### new
# data = b""
# payload_size = struct.calcsize("H") 
# while True:
#     while len(data) < payload_size:
#         data += conn.recv(4096)
#     packed_msg_size = data[:payload_size]
#     data = data[payload_size:]
#     msg_size = struct.unpack("H", packed_msg_size)[0]
#     while len(data) < msg_size:
#         data += conn.recv(4096)
#     frame_data = data[:msg_size]
#     data = data[msg_size:]
#     ###

#     frame=pickle.loads(frame_data)
#     print(frame)
#     cv2.imshow('frame',frame)