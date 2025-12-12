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
    
    # 隐藏窗口标题栏
    page.window.title_bar_hidden = True
    
    page.title = "超级工具箱"
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#2B2B2B"
    
    # 菜单项点击处理函数
    def on_menu_click(e):
        print(f"菜单项被点击: {e.control.text}")
    
    # 加载logo图片
    logo_path = None
    logo_paths = ["assets/logo.png", "assets/logo.svg", "logo.png", "logo.svg"]
    for path in logo_paths:
        if os.path.exists(path):
            logo_path = path
            break
    
    # 创建顶部栏（标题栏 + 菜单栏在同一行）
    top_bar_controls = []
    
    # 添加Logo图标（如果存在）
    if logo_path:
        top_bar_controls.append(
            ft.Image(
                src=logo_path,
                width=20,
                height=20,
                fit=ft.ImageFit.CONTAIN,
            )
        )
        # Logo和菜单之间的间距
        top_bar_controls.append(ft.Container(width=8))
    
    # 创建顶部栏（标题栏 + 菜单栏在同一行）
    top_bar = ft.Container(
        content=ft.Row(
            controls=top_bar_controls + [
                # 菜单栏
                ft.MenuBar(
                    style=ft.MenuStyle(
                        alignment=ft.alignment.top_left,
                        bgcolor="transparent",
                        mouse_cursor=ft.MouseCursor.CLICK,
                    ),
                    controls=[
                        ft.SubmenuButton(
                            content=ft.Text("文件", size=13, color="#CCCCCC"),
                            controls=[
                                ft.MenuItemButton(
                                    content=ft.Text("新建"),
                                    leading=ft.Icon("add", size=16),
                                    on_click=on_menu_click,
                                ),
                                ft.MenuItemButton(
                                    content=ft.Text("打开"),
                                    leading=ft.Icon("folder_open", size=16),
                                    on_click=on_menu_click,
                                ),
                                ft.MenuItemButton(
                                    content=ft.Text("保存"),
                                    leading=ft.Icon("save", size=16),
                                    on_click=on_menu_click,
                                ),
                                ft.Divider(),
                                ft.MenuItemButton(
                                    content=ft.Text("退出"),
                                    leading=ft.Icon("exit_to_app", size=16),
                                    on_click=lambda e: page.window.close(),
                                ),
                            ],
                        ),
                        ft.SubmenuButton(
                            content=ft.Text("编辑", size=13, color="#CCCCCC"),
                            controls=[
                                ft.MenuItemButton(
                                    content=ft.Text("撤销"),
                                    leading=ft.Icon("undo", size=16),
                                    on_click=on_menu_click,
                                ),
                                ft.MenuItemButton(
                                    content=ft.Text("重做"),
                                    leading=ft.Icon("redo", size=16),
                                    on_click=on_menu_click,
                                ),
                                ft.Divider(),
                                ft.MenuItemButton(
                                    content=ft.Text("剪切"),
                                    leading=ft.Icon("content_cut", size=16),
                                    on_click=on_menu_click,
                                ),
                                ft.MenuItemButton(
                                    content=ft.Text("复制"),
                                    leading=ft.Icon("content_copy", size=16),
                                    on_click=on_menu_click,
                                ),
                                ft.MenuItemButton(
                                    content=ft.Text("粘贴"),
                                    leading=ft.Icon("content_paste", size=16),
                                    on_click=on_menu_click,
                                ),
                            ],
                        ),
                        ft.SubmenuButton(
                            content=ft.Text("工具", size=13, color="#CCCCCC"),
                            controls=[
                                ft.MenuItemButton(
                                    content=ft.Text("设置"),
                                    leading=ft.Icon("settings", size=16),
                                    on_click=on_menu_click,
                                ),
                                ft.MenuItemButton(
                                    content=ft.Text("首选项"),
                                    leading=ft.Icon("tune", size=16),
                                    on_click=on_menu_click,
                                ),
                            ],
                        ),
                        ft.SubmenuButton(
                            content=ft.Text("关于", size=13, color="#CCCCCC"),
                            controls=[
                                ft.MenuItemButton(
                                    content=ft.Text("关于应用"),
                                    leading=ft.Icon("info", size=16),
                                    on_click=on_menu_click,
                                ),
                                ft.MenuItemButton(
                                    content=ft.Text("帮助"),
                                    leading=ft.Icon("help", size=16),
                                    on_click=on_menu_click,
                                ),
                            ],
                        ),
                    ],
                ),
                # 占位符，将窗口控制按钮推到右侧
                ft.Container(expand=True),
                # 窗口控制按钮
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon="remove",
                            icon_size=14,
                            icon_color="#CCCCCC",
                            tooltip="最小化",
                            on_click=lambda e: setattr(page.window, "minimized", True),
                            style=ft.ButtonStyle(
                                bgcolor="transparent",
                                overlay_color="#3C3C3C",
                            ),
                        ),
                        ft.IconButton(
                            icon="crop_square",
                            icon_size=12,
                            icon_color="#CCCCCC",
                            tooltip="最大化",
                            on_click=lambda e: setattr(page.window, "maximized", not page.window.maximized),
                            style=ft.ButtonStyle(
                                bgcolor="transparent",
                                overlay_color="#3C3C3C",
                            ),
                        ),
                        ft.IconButton(
                            icon="close",
                            icon_size=14,
                            icon_color="#CCCCCC",
                            tooltip="关闭",
                            on_click=lambda e: page.window.close(),
                            style=ft.ButtonStyle(
                                bgcolor="transparent",
                                overlay_color="#E81123",
                            ),
                        ),
                    ],
                    spacing=0,
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            height=32,
        ),
        padding=8,
        bgcolor="#2B2B2B",
    )
    
    # 主内容区域
    content_area = ft.Container(
        expand=True,
        padding=16,
        bgcolor="#2B2B2B",
    )
    
    # 分隔线
    divider = ft.Container(
        height=1,
        bgcolor="#3C3C3C",
    )
    
    # 使用 Column 布局
    page.add(
        ft.Column(
            controls=[
                ft.WindowDragArea(content=top_bar),
                divider,
                content_area,
            ],
            spacing=0,
            expand=True,
        )
    )
    
    # 更新页面
    page.update()


if __name__ == "__main__":
    # 运行桌面应用，指定assets目录
    ft.app(target=main, assets_dir="assets")
    
    # 如果想在浏览器中运行，取消下面的注释并注释掉上面的行
    # ft.app(target=main, view=ft.AppView.WEB_BROWSER)

