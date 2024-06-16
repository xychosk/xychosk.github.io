CLI
YOLOv8 may be used directly in the Command Line Interface (CLI) with a command:yolo

yolo predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
yolo can be used for a variety of tasks and modes and accepts additional arguments, i.e. . See the YOLOv8 CLI Docs for examples.imgsz=640

Python
YOLOv8 may also be used directly in a Python environment, and accepts the same arguments as in the CLI example above:

from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="coco8.yaml", epochs=3)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
path = model.export(format="onnx")  # export the model to ONNX format


数据集
（1）COCO数据集：这是一个用于目标检测、分割和描述的大型数据集。包含80个类别和超过20万张图像，其中有11.8万张用于训练，5,000张用于验证，40,500张用于测试。这个数据集非常具有挑战性，因为涵盖了各种不同大小、形状和类别的对象。
（2）PASCAL VOC数据集：这是一个经典的用于目标检测和分类的数据集。包含20个类别和超过11,000张图像，其中5,000张用于训练和验证，6,000张用于测试。这个数据集相对简单和平衡，因为涵盖了常见的对象类别，并且具有适度的难度。
（3）WIDER FACE数据集：这是一个用于人脸检测的大型数据集。包含超过32,000张图像和393,000张人脸，其中12,800张用于训练，3,200张用于验证，16,000张用于测试。这个数据集具有挑战性和复杂性，因为涵盖了各种不同尺度、姿势、表情、遮挡和光照的人脸。
（4）DIOR数据集：是一个大规模、公开的遥感图像目标检测数据集。该数据集包含23463张图像和192472个实例，涵盖20个不同的目标类别。

在yolov8的基础上加入Bi-former机制