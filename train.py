from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO("D:\\Study\\PyWorkSpace\\yolov8-main\\ultralytics\\cfg\\models\\v8\\yolo8_ContextGuideFusionModule.yaml")
    # model = YOLO("D:\\Study\\PyWorkSpace\\yolov8-main\\yolov8s.pt")

    model.train(data="D:/Study/PyWorkSpace/Yolo8_for_lab/ultralytics/cfg/datasets/SODA-D.yaml",
                imgsz=640,
                epochs=100,
                batch=-1,
                close_mosaic=0,
                workers=2,
                )

    # if __name__ == '__main__':
    #     # Use the model
    #     results = model.train(model="D:\\Study\\PyWorkSpace\\yolov8-main\\yolov8s.pt",
    #                           data="D:\\Study\\PyWorkSpace\\yolov8-main\\ultralytics\\cfg\\datasets\\FishData.yaml",
    #                           epochs=100, imgsz=640, batch=1, workers=2, close_mosaic=0)  # 训练模型
    #     results = model.val()
    #     success = YOLO("yolov8s.pt").export(format="onnx")


