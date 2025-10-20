import os

project_name = "smart_construction_backend"

structure = {
    "app": [
        "main.py", "database.py", "models.py", "schemas.py",
        "crud.py", "auth.py"
    ],
    "app/routers": ["user_router.py"],
    "app/utils": ["hash.py"],
}

def create_project_structure(base_path, structure_dict):
    for folder, files in structure_dict.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            open(os.path.join(folder_path, file), "a").close()
    print(f"✅ 项目结构创建完成：{base_path}")

if __name__ == "__main__":
    base_path = os.path.join(os.getcwd(), project_name)
    os.makedirs(base_path, exist_ok=True)
    create_project_structure(base_path, structure)

    with open(os.path.join(base_path, "requirements.txt"), "w") as f:
        f.write("fastapi\nuvicorn\nsqlalchemy\npydantic\npasslib[bcrypt]\njwt\nmysql-connector-python\n")

    with open(os.path.join(base_path, "README.md"), "w") as f:
        f.write("# 智慧工地后端系统\n\n基于 FastAPI + MySQL + JWT 的后端服务。\n")

    print("📦 完整结构创建完成！")
