"""
版本信息更新脚本
用于更新version.txt文件中的版本号
使用方法: python update_version.py [版本号]
例如: python update_version.py 1.2.3
"""

import sys
import re
import os

VERSION_FILE = "version.txt"
DEFAULT_VERSION = "1.0.0"

def update_version(version_str):
    """更新version.txt文件中的版本号"""
    if not os.path.exists(VERSION_FILE):
        print(f"错误: 找不到文件 {VERSION_FILE}")
        return False
    
    # 解析版本号
    try:
        version_parts = [int(x) for x in version_str.split('.')]
        if len(version_parts) < 4:
            # 如果版本号少于4部分，补齐为4部分
            version_parts.extend([0] * (4 - len(version_parts)))
        version_tuple = tuple(version_parts[:4])
        version_str_full = '.'.join(str(x) for x in version_tuple)
    except ValueError:
        print(f"错误: 无效的版本号格式: {version_str}")
        print("版本号格式应为: X.Y.Z.W 或 X.Y.Z")
        return False
    
    # 读取文件
    try:
        with open(VERSION_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"错误: 读取文件失败: {e}")
        return False
    
    # 替换版本号 - PyInstaller Python格式
    # 替换 filevers 和 prodvers 元组
    version_tuple_str = f"({version_tuple[0]}, {version_tuple[1]}, {version_tuple[2]}, {version_tuple[3]})"
    content = re.sub(
        r'filevers=\(\d+,\s*\d+,\s*\d+,\s*\d+\)',
        f'filevers={version_tuple_str}',
        content
    )
    content = re.sub(
        r'prodvers=\(\d+,\s*\d+,\s*\d+,\s*\d+\)',
        f'prodvers={version_tuple_str}',
        content
    )
    
    # 替换 FileVersion 和 ProductVersion 字符串
    content = re.sub(
        r"StringStruct\(u'FileVersion',\s*u'[^']*'\)",
        f"StringStruct(u'FileVersion', u'{version_str_full}')",
        content
    )
    content = re.sub(
        r"StringStruct\(u'ProductVersion',\s*u'[^']*'\)",
        f"StringStruct(u'ProductVersion', u'{version_str_full}')",
        content
    )
    
    # 写回文件
    try:
        with open(VERSION_FILE, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ 版本号已更新为: {version_str_full}")
        return True
    except Exception as e:
        print(f"错误: 写入文件失败: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        version = sys.argv[1]
    else:
        # 从build_exe.py读取默认版本号
        try:
            with open("build_exe.py", 'r', encoding='utf-8') as f:
                content = f.read()
                match = re.search(r'VERSION\s*=\s*"([^"]+)"', content)
                if match:
                    version = match.group(1)
                else:
                    version = DEFAULT_VERSION
        except:
            version = DEFAULT_VERSION
        print(f"使用默认版本号: {version}")
    
    update_version(version)

