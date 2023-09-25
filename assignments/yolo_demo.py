from ultralytics import YOLO
import cv2
import numpy as np

def plot_result(img, result):
    result = result.cpu().numpy()
    coords = result.boxes.xyxy
    names = result.names
    for i in range(len(coords)):
        id = names[result.boxes.cls[i]]
        random_color = (255*np.random.randint(0, 2), 255*np.random.randint(0, 2), 255*np.random.randint(0, 2))
        cv2.rectangle(img, (int(coords[i,0]), int(coords[i,1])), (int(coords[i,2]), int(coords[i,3])), color=random_color, thickness=3)
        cv2.rectangle(img, (int(coords[i,0]), int(coords[i,1])), (int(coords[i,0]+200), int(coords[i,1])-40), (255, 255, 255), -1)
        cv2.putText(img, id, (int(coords[i,0]), int(coords[i,1]-10)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    return img


model = YOLO('yolov8n.pt')
video_path = r"C:\Users\edvar\programming\robotics_hw\ch1_intro_ML\monkey.mp4"

cap = cv2.VideoCapture(video_path)
while cap.isOpened():
    success, frame = cap.read()
    if success:
        results = model(frame)
        annotated_frame = plot_result(frame, results[0])
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()