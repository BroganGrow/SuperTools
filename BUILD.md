# 打包说明文档

本文档说明如何将SuperTools项目打包成exe可执行文件。

## 方法一：使用打包脚本（推荐）

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行打包脚本

```bash
python build_exe.py
```

打包完成后，exe文件将生成在 `dist/SuperTools-版本号.exe`（例如：`dist/SuperTools-1.0.1.exe`）

**注意**：exe文件名会自动包含版本号，版本号从 `version.txt` 文件中自动读取。

## 方法二：使用PyInstaller命令

### 1. 安装PyInstaller

```bash
pip install pyinstaller
```

### 2. 执行打包命令

```bash
pyinstaller --name SuperTools --onefile --windowed --icon assets/logo.ico --add-data "assets;assets" main.py
```

### 参数说明：
- `--name SuperTools`: 生成的exe文件名
- `--onefile`: 打包成单个exe文件（推荐）
- `--windowed`: 无控制台窗口（GUI应用）
- `--icon assets/logo.ico`: 设置exe图标
- `--add-data "assets;assets"`: 包含资源文件目录
- `main.py`: 主程序文件

## 方法三：使用Flet打包命令

Flet也提供了打包功能：

```bash
flet build windows
```

但需要先安装Flet CLI：

```bash
pip install flet-cli
```

## 打包后的文件

打包完成后，会在项目目录下生成：
- `dist/`: 包含最终的exe文件
- `build/`: 临时构建文件（可删除）
- `SuperTools.spec`: PyInstaller配置文件（可保留用于后续打包）

## 分发exe文件

1. **单个exe文件**：如果使用 `--onefile` 参数，只需要分发 `dist/SuperTools.exe` 这一个文件即可
2. **文件大小**：单个exe文件通常较大（50-100MB），这是正常的，因为包含了Python解释器和所有依赖
3. **运行要求**：
   - 目标机器必须是Windows系统
   - 不需要安装Python
   - 首次运行可能需要几秒钟加载时间

## 常见问题

### 1. 打包失败：找不到模块
- 确保所有依赖都已安装：`pip install -r requirements.txt`
- 检查是否有未导入但使用的模块

### 2. exe文件无法运行
- 检查是否有杀毒软件拦截
- 尝试在命令行运行查看错误信息（去掉 `--windowed` 参数）

### 3. 资源文件找不到
- 确保 `--add-data` 参数正确
- 检查代码中资源文件路径是否正确

### 4. 文件太大
- 这是正常的，因为包含了Python运行时
- 可以使用 `--onedir` 代替 `--onefile` 来减小单个文件大小（但需要分发整个文件夹）

## 优化建议

1. **减小文件大小**：
   - 使用虚拟环境，只安装必要的包
   - 使用 `--exclude-module` 排除不需要的模块

2. **提高启动速度**：
   - 使用 `--onedir` 模式（但需要分发文件夹）
   - 优化代码，减少导入时间

3. **添加版本信息**：
   - 创建 `version.txt` 文件
   - 使用 `--version-file` 参数

## 测试打包结果

打包完成后，建议：
1. 在打包机器上测试exe文件
2. 在没有Python环境的机器上测试
3. 测试所有功能是否正常

