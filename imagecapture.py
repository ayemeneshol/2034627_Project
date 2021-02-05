import cv2

url = 'http://192.168.1.24:8080/video'
camera = cv2.VideoCapture(url)

counter = 0
while True:
    ret_val, img = camera.read()
    
    cv2.imshow('image', img)
    k = cv2.waitKey(1)
    if k%256 == 32: #space
        cv2.imwrite('test_img_{}.png'.format(counter),img)
        counter += 1
    if k%256 == 27: #ESC
        break
