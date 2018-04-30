import cv2
def show():
    frame = cv2.VideoCapture(0)
    print(frame)
    while True:
        flag, used = frame.read()
       # print(flag)
        jik = cv2.cvtColor(used, cv2.COLOR_BGR2YCR_CB)
        cv2.imshow('frame', used)
    # cv2.imshow('frame1', jik)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    frame.release()
    cv2.destroyAllWindows()
