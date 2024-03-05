from ultralytics import YOLO
model = YOLO("yolov8n.yaml")  #Loading model
results = model.train(data="config.yaml", epochs=1) # set epochs range from 20-100 for standard training