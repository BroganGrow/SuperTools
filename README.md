# Flet 项目

这是一个使用 Flet 框架创建的跨平台应用项目。

## 功能特性

- 简单的用户界面
- 文本输入和按钮交互
- 响应式布局

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

## 项目结构

```
.
├── main.py              # 主应用文件
├── requirements.txt     # Python 依赖
└── README.md           # 项目说明
```

## 关于 Flet

Flet 是一个基于 Flutter 的 Python 框架，允许您使用 Python 构建跨平台的桌面、Web 和移动应用。

更多信息请访问：[Flet 官网](https://flet.dev/)

