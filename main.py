import flet as ft
import os


def main(page: ft.Page):
    # 设置窗口图标（在其他设置之前）
    # 尝试多个可能的路径
    icon_paths = [
        "assets/logo.ico",  # assets目录中的图标（推荐）
        "logo.ico",  # 根目录中的图标
    ]
    
    icon_set = False
    for icon_path in icon_paths:
        if os.path.exists(icon_path):
            try:
                page.window.icon = icon_path
                print(f"✓ 已设置窗口图标: {icon_path}")
                icon_set = True
                break
            except Exception as e:
                print(f"✗ 设置图标 {icon_path} 失败: {e}")
                continue
    
    if not icon_set:
        print("⚠ 未找到可用的图标文件")
        print("请确保 logo.ico 文件存在于项目根目录或 assets 目录中")
    
    page.title = "超级工具箱"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # 更新页面以应用图标设置
    page.update()
    
    # 清空界面内容
    # 页面保持空白，不添加任何控件


if __name__ == "__main__":
    # 运行桌面应用，指定assets目录
    ft.app(target=main, assets_dir="assets")
    
    # 如果想在浏览器中运行，取消下面的注释并注释掉上面的行
    # ft.app(target=main, view=ft.AppView.WEB_BROWSER)

