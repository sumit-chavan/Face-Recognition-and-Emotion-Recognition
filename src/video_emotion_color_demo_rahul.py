from statistics import mode
from keras.models import load_model
from utils.datasets import get_labels
from utils.inference import detect_faces
from utils.inference import draw_text
from utils.inference import draw_bounding_box
from utils.inference import apply_offsets
from utils.inference import load_detection_model
from utils.preprocessor import preprocess_input
import sys
import cv2,csv,time
import numpy as np
import subprocess

def func(video_path):
    # file to store metadata
    metaData = open('C:/Users/ASUS/Desktop/Face Recognition/trial1/Face Detection and Emotion Analysis/src/final1.csv','a')
    writer = csv.writer(metaData)

    # parameters for loading data and images
    detection_model_path = '../trained_models/detection_models/haarcascade_frontalface_default.xml'
    emotion_model_path = '../trained_models/emotion_models/fer2013_mini_XCEPTION.102-0.66.hdf5'
    emotion_labels = get_labels('fer2013')

    # hyper-parameters for bounding boxes shape
    frame_window = 10
    emotion_offsets = (20, 40)

    # loading models
    face_detection = load_detection_model(detection_model_path)
    emotion_classifier = load_model(emotion_model_path, compile=False)

    # getting input model shapes for inference
    emotion_target_size = emotion_classifier.input_shape[1:3]

    # starting lists for calculating modes
    emotion_window = []

    toc = time.time()
    # starting video streaming
    cv2.namedWindow('window_frame')
    #video_capture = cv2.VideoCapture(sys.argv[1])
    video_capture = cv2.VideoCapture(video_path)
    #video_capture = cv2.VideoCapture('videoplayback.mp4')

    while True:
        bgr_image = video_capture.read()[1]
        gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
        rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        faces = detect_faces(face_detection, gray_image)
        
        frame_count = int(video_capture.get(cv2.CAP_PROP_POS_FRAMES))
        
        tic = time.time()
        
        for face_coordinates in faces:

            x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
            gray_face = gray_image[y1:y2, x1:x2]
            try:
                gray_face = cv2.resize(gray_face, (emotion_target_size))
            except:
                continue

            actor_face = cv2.resize(gray_face,(128,128))    
            cv2.imwrite("E:/tensorflow-master/tensorflow/examples/image_retraining/face.jpg",actor_face)
        
            video_capture.set(1,int(frame_count))
            ret, frame = video_capture.read()
            cv2.imwrite("E:/Object Detection/models-master/tutorials/image/imagenet/object.jpg", gray_image)
        


            gray_face = preprocess_input(gray_face, True)
            gray_face = np.expand_dims(gray_face, 0)
            gray_face = np.expand_dims(gray_face, -1)
            emotion_prediction = emotion_classifier.predict(gray_face)
            emotion_probability = np.max(emotion_prediction)
            emotion_label_arg = np.argmax(emotion_prediction)
            emotion_text = emotion_labels[emotion_label_arg]
            emotion_window.append(emotion_text)
            
            
            s2_out = subprocess.check_output([sys.executable, "E:/tensorflow-master/tensorflow/examples/label_image/label_image.py", "--graph=E:/tmp/output_graph.pb", "--labels=E:/tmp/output_labels.txt", "--input_layer=Mul", "--output_layer=final_result", "--input_mean=128", "--input_std=128", "--image=E:/tensorflow-master/tensorflow/examples/image_retraining/face.jpg"])
            actor_confidence = s2_out.split()[1]
            if(float(actor_confidence)>0.5):
                actor = s2_out.split()[0]
            else:
                actor = ""

            print(s2_out)    

            s3_out = subprocess.check_output([sys.executable, "E:/Object Detection/models-master/tutorials/image/imagenet/classify_image.py", "--image_file=E:/Object Detection/models-master/tutorials/image/imagenet/object.jpg"])
            object1 = s3_out.split()[0]
            print(s3_out)
            
            
            writer.writerows([[(tic-toc),frame_count,emotion_text,emotion_probability,actor,actor_confidence,face_coordinates,object1]])
            
            if len(emotion_window) > frame_window:
                emotion_window.pop(0)
            try:
                emotion_mode = mode(emotion_window)
            except:
                continue

            if emotion_text == 'angry':
                color = emotion_probability * np.asarray((255, 0, 0))
            elif emotion_text == 'sad':
                color = emotion_probability * np.asarray((0, 0, 255))
            elif emotion_text == 'happy':
                color = emotion_probability * np.asarray((255, 255, 0))
            elif emotion_text == 'surprise':
                color = emotion_probability * np.asarray((0, 255, 255))
            else:
                color = emotion_probability * np.asarray((0, 255, 0))

            color = color.astype(int)
            color = color.tolist()

            draw_bounding_box(face_coordinates, rgb_image, color)
            draw_text(face_coordinates, rgb_image, emotion_mode, color, 0, -20, 1, 1)
            draw_text(face_coordinates, rgb_image, actor, color, 0, -45, 1, 1)


        bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
        cv2.imshow('window_frame', bgr_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
