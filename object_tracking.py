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
    cam = cv2.VideoCapture(0)
    kwargs = init_model()
    while(True):

        ret, frame = cam.read()
        boxes = get_bounding_boxs(frame, **kwargs)
        for (x, y, w, h) in boxes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow('Face Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()