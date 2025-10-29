from ultralytics import YOLO

if __name__ == "__main__":
    # 加载官方权重
    model = YOLO(r"D:\PycharmProjects\Test_yolov11_pro\yolo11n.pt")

    # 开始训练
    model.train(
        data=r"D:\PycharmProjects\Test_yolov11_pro\data\data.yaml",
        epochs=50,
        imgsz=640,
        batch=8,
        device=0
    )
