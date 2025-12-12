"""
打包脚本 - 将Flet应用打包成exe文件
使用方法: python build_exe.py
"""

import PyInstaller.__main__
import os
import re

# 项目配置
BASE_APP_NAME = "SuperTools"
MAIN_SCRIPT = "main.py"
ICON_PATH = "assets/logo.ico" if os.path.exists("assets/logo.ico") else None
VERSION_FILE = "version.txt"  # 版本信息文件（PyInstaller Python格式）

def get_version_from_file():
    """从version.txt文件中读取版本号"""
    if not os.path.exists(VERSION_FILE):
        return None
    
    try:
        with open(VERSION_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            # 查找 FileVersion 字符串
            match = re.search(r"StringStruct\(u'FileVersion',\s*u'([^']+)'\)", content)
            if match:
                return match.group(1)
            # 如果没有找到，尝试从filevers元组读取
            match = re.search(r'filevers=\((\d+),\s*(\d+),\s*(\d+),\s*(\d+)\)', content)
            if match:
                version_parts = [match.group(i) for i in range(1, 5)]
                # 去掉末尾的.0（如果存在）
                while len(version_parts) > 2 and version_parts[-1] == '0':
                    version_parts.pop()
                return '.'.join(version_parts)
    except Exception as e:
        print(f"⚠ 读取版本号失败: {e}")
    
    return None

def format_version_for_filename(version_str):
    """将版本号格式化为文件名格式（去掉末尾的.0）"""
    if not version_str:
        return ""
    
    parts = version_str.split('.')
    # 去掉末尾的0
    while len(parts) > 2 and parts[-1] == '0':
        parts.pop()
    
    # 保持点号分隔，例如 1.0.1 而不是 1-0-1
    return '.'.join(parts)

# 读取版本号
VERSION = get_version_from_file()
if VERSION:
    version_suffix = format_version_for_filename(VERSION)
    APP_NAME = f"{BASE_APP_NAME}-{version_suffix}" if version_suffix else BASE_APP_NAME
    print(f"✓ 检测到版本号: {VERSION}")
    print(f"✓ exe文件名: {APP_NAME}.exe")
else:
    APP_NAME = BASE_APP_NAME
    print("⚠ 未检测到版本号，使用默认文件名")

# PyInstaller参数
args = [
    MAIN_SCRIPT,
    "--name", APP_NAME,
    "--onefile",  # 打包成单个exe文件
    "--windowed",  # 无控制台窗口（GUI应用）
    "--clean",  # 清理临时文件
    "--noconfirm",  # 覆盖输出目录而不询问
]

# 添加图标
if ICON_PATH and os.path.exists(ICON_PATH):
    args.extend(["--icon", ICON_PATH])
    print(f"✓ 使用图标: {ICON_PATH}")
else:
    print("⚠ 未找到图标文件，将使用默认图标")

# 添加版本信息文件
if os.path.exists(VERSION_FILE):
    args.extend(["--version-file", VERSION_FILE])
    print(f"✓ 使用版本文件: {VERSION_FILE}")
    if VERSION:
        print(f"  版本号: {VERSION}")
else:
    print("⚠ 未找到版本文件，将不设置版本信息")
    print(f"  提示: 创建 {VERSION_FILE} 文件以添加版本信息")

# 添加assets目录（包含资源文件）
if os.path.exists("assets"):
    args.extend(["--add-data", f"assets;assets"])
    print("✓ 包含assets目录")

# 添加必要的隐藏导入
hidden_imports = [
    "flet",
]

for imp in hidden_imports:
    args.extend(["--hidden-import", imp])

print("开始打包...")
print("=" * 50)

try:
    PyInstaller.__main__.run(args)
    print("=" * 50)
    print("✓ 打包完成！")
    print(f"exe文件位置: dist/{APP_NAME}.exe")
    print("\n提示：")
    print("1. 可以将dist目录中的exe文件单独分发给其他用户")
    print("2. 确保目标机器是Windows系统")
    print("3. 首次运行可能需要几秒钟加载时间")
except Exception as e:
    print(f"✗ 打包失败: {e}")
    import traceback
    traceback.print_exc()
