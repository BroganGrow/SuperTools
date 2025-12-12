import flet as ft
import os


def _minimize_window(page: ft.Page):
    """最小化窗口"""
    page.window.minimized = True
    page.update()


def _maximize_window(page: ft.Page):
    """最大化/还原窗口"""
    page.window.maximized = not page.window.maximized
    page.update()


def main(page: ft.Page):
    # 设置窗口图标（在其他设置之前）
    # 尝试多个可能的路径，使用绝对路径确保能找到文件
    icon_paths = [
        os.path.abspath("assets/logo.ico"),  # assets目录中的图标（绝对路径）
        os.path.abspath("logo.ico"),  # 根目录中的图标（绝对路径）
        "assets/logo.ico",  # 相对路径
        "logo.ico",  # 相对路径
    ]
    
    icon_set = False
    for icon_path in icon_paths:
        if os.path.exists(icon_path):
            try:
                # 使用绝对路径
                abs_path = os.path.abspath(icon_path)
                page.window.icon = abs_path
                print(f"✓ 已设置窗口图标: {abs_path}")
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
    
    # 设置窗口居中
    page.window.center()
    
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
                        shadow_color="transparent",
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
                            on_click=lambda e: _minimize_window(page),
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
                            on_click=lambda e: _maximize_window(page),
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
    
    # 计算器功能
    display_text = ft.TextField(
        value="0",
        text_align=ft.TextAlign.RIGHT,
        read_only=True,
        border=ft.InputBorder.NONE,
        bgcolor="#1E1E1E",
        color="#FFFFFF",
        text_size=32,
        height=80,
        content_padding=ft.padding.only(right=20, top=20, bottom=20),
    )
    
    current_value = "0"
    previous_value = None
    operation = None
    should_reset = False
    
    def button_click(e):
        nonlocal current_value, previous_value, operation, should_reset
        button_text = e.control.text
        
        if should_reset:
            current_value = "0"
            should_reset = False
        
        if button_text in "0123456789":
            if current_value == "0":
                current_value = button_text
            else:
                current_value += button_text
        elif button_text == ".":
            if "." not in current_value:
                current_value += "."
        elif button_text == "C":
            current_value = "0"
            previous_value = None
            operation = None
        elif button_text == "⌫":
            if len(current_value) > 1:
                current_value = current_value[:-1]
            else:
                current_value = "0"
        elif button_text in "+-×÷":
            if previous_value is not None and operation:
                calculate_result()
            previous_value = float(current_value)
            operation = button_text
            should_reset = True
        elif button_text == "=":
            calculate_result()
        
        display_text.value = current_value
        page.update()
    
    def calculate_result():
        nonlocal current_value, previous_value, operation, should_reset
        if previous_value is not None and operation:
            try:
                if operation == "+":
                    result = previous_value + float(current_value)
                elif operation == "-":
                    result = previous_value - float(current_value)
                elif operation == "×":
                    result = previous_value * float(current_value)
                elif operation == "÷":
                    if float(current_value) == 0:
                        current_value = "错误"
                        previous_value = None
                        operation = None
                        should_reset = True
                        return
                    result = previous_value / float(current_value)
                
                # 格式化结果，去除不必要的.0
                if result == int(result):
                    current_value = str(int(result))
                else:
                    current_value = str(result)
                
                previous_value = None
                operation = None
                should_reset = True
            except:
                current_value = "错误"
                previous_value = None
                operation = None
                should_reset = True
    
    # 创建按钮的辅助函数
    def create_button(text, bg_color, text_color="#FFFFFF", expand=1):
        return ft.ElevatedButton(
            text=text,
            on_click=button_click,
            bgcolor=bg_color,
            color=text_color,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
            expand=expand,
            height=60,
        )
    
    # 计算器按钮布局（标准布局）
    button_grid = [
        # 第一行：C, ⌫, ÷, ×
        ft.Row(
            controls=[
                create_button("C", "#505050"),
                create_button("⌫", "#505050"),
                create_button("÷", "#FF9500"),
                create_button("×", "#FF9500"),
            ],
            spacing=10,
        ),
        # 第二行：7, 8, 9, -
        ft.Row(
            controls=[
                create_button("7", "#3C3C3C"),
                create_button("8", "#3C3C3C"),
                create_button("9", "#3C3C3C"),
                create_button("-", "#FF9500"),
            ],
            spacing=10,
        ),
        # 第三行：4, 5, 6, +
        ft.Row(
            controls=[
                create_button("4", "#3C3C3C"),
                create_button("5", "#3C3C3C"),
                create_button("6", "#3C3C3C"),
                create_button("+", "#FF9500"),
            ],
            spacing=10,
        ),
        # 第四行：1, 2, 3, =
        ft.Row(
            controls=[
                create_button("1", "#3C3C3C"),
                create_button("2", "#3C3C3C"),
                create_button("3", "#3C3C3C"),
                create_button("=", "#FF9500", expand=1),
            ],
            spacing=10,
        ),
        # 第五行：0 (占两列), ., = (占一列)
        ft.Row(
            controls=[
                create_button("0", "#3C3C3C", expand=2),
                create_button(".", "#3C3C3C"),
                create_button("=", "#FF9500"),
            ],
            spacing=10,
        ),
    ]
    
    # 计算器容器
    calculator_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("计算器", size=24, color="#FFFFFF", weight=ft.FontWeight.BOLD),
                ft.Container(height=20),
                display_text,
                ft.Container(height=20),
                ft.Column(controls=button_grid, spacing=10),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        ),
        padding=20,
        bgcolor="#2B2B2B",
        border_radius=10,
        width=400,
    )
    
    # 主内容区域
    content_area = ft.Container(
        content=ft.Row(
            controls=[calculator_container],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
        ),
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

