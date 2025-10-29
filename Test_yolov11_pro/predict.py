from ultralytics import YOLO

# 加载训练好的模型
model = YOLO("runs/train/exp/weights/best.pt")  # 训练输出的权重路径

# 预测
results = model.predict(
    source="D:\PycharmProjects\Test_yolov11_pro\Test\\testphoto",  # 可以是文件夹、图片或视频
    imgsz=640,
    conf=0.25,             # 置信度阈值
    device=0,              # GPU: 0, CPU: "cpu"
    save=True,             # 是否保存预测结果
    save_txt=True          # 是否保存txt标注
)

# 查看结果
print(results)
