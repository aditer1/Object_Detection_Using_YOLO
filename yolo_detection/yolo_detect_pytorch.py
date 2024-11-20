import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

img = input("Enter the path to the image file: ")

results = model(img)

results.show()

