# #coding: utf-8
# from ultralytics import YOLO
# import matplotlib
# matplotlib.use("Agg")
#
# if __name__ == '__main__':
#     #加载训练好的模型
#     model = YOLO('runs/detect/train54_BiFormer/weights/best.pt')
#     # 对验证集进行评估
#     metrics = model.val_57(data='ultralytics/cfg/datasets/DIOR.yaml')


############################################################################################################
from ultralytics import YOLO


def main():
    model = YOLO('train55_SlideLoss/weights/best.pt')
    model.val(data='Data_yaml/DIOR.yaml', imgsz=640, batch=4, workers=3)


if __name__ == '__main__':
    main()
