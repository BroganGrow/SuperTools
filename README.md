# Flet 项目

这是一个使用 Flet 框架创建的跨平台应用项目。


# 快速使用

-  启动
python main.py

- 更新版本号
python update_version.py 1.0.2

- 打包
python build_exe.py





## 功能特性

- 简单的用户界面
- 文本输入和按钮交互
- 响应式布局
- 内置计算器功能

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行应用

### 桌面应用模式

```bash
python main.py
```

### Web 浏览器模式

修改 `main.py` 文件的最后一行，将：
```python
ft.app(target=main)
```
改为：
```python
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
```

然后运行：
```bash
python main.py
```

## 打包成exe文件

要将项目打包成exe可执行文件，请参考 [BUILD.md](BUILD.md) 文档。

快速打包步骤：
```bash
# 1. 安装依赖（包括打包工具）
pip install -r requirements.txt

# 2. 运行打包脚本
python build_exe.py
```

打包完成后，exe文件将生成在 `dist/SuperTools-版本号.exe`（例如：`dist/SuperTools-1.0.1.exe`），可以直接分发给其他Windows用户使用。

**注意**：exe文件名会自动包含版本号，版本号从 `version.txt` 文件中读取。

### 版本信息

打包的exe文件会自动包含版本信息。查看版本信息：
- 右键exe文件 → 属性 → 详细信息
- 或参考 [VERSION.md](VERSION.md) 了解如何更新版本号

## 项目结构

```
.
├── main.py              # 主应用文件
├── requirements.txt     # Python 依赖
├── build_exe.py         # 打包脚本
├── update_version.py     # 版本号更新脚本
├── version.rc            # 版本信息文件
├── SuperTools.spec       # PyInstaller配置文件
├── BUILD.md              # 打包详细说明
├── VERSION.md            # 版本信息说明
├── README.md             # 项目说明
└── assets/              # 资源文件目录
    ├── logo.ico         # 应用图标
    ├── logo.png         # Logo图片
    └── logo.svg         # Logo矢量图
```

## 关于 Flet

Flet 是一个基于 Flutter 的 Python 框架，允许您使用 Python 构建跨平台的桌面、Web 和移动应用。

更多信息请访问：[Flet 官网](https://flet.dev/)

