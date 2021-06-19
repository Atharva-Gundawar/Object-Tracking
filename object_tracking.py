import cv2


def init_model():
    """[summary]

    Returns:
        [type]: [description]
    """
    face_cascade = cv2.CascadeClassifier(
        'haarcascades\haarcascade_frontalface_default.xml')
    return {"face_cascade": face_cascade}


def get_bounding_boxs(frame, **kwargs):
    """[summary]

    Args:
        frame ([type]): [description]

    Returns:
        [type]: [description]
    """
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return kwargs.get('face_cascade').detectMultiScale(frame_gray)

def main():
    """[summary]
    """

    kwargs = init_model()
    cap = cv2.VideoCapture('Videos\WIN_20210619_10_22_40_Pro.mp4')
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            break
        boxes = get_bounding_boxs(frame, **kwargs)
        for (x, y, w, h) in boxes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()