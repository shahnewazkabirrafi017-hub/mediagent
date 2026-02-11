import flet as ft

def main(page: ft.Page):
    page.title = "MediAgent AI"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 800
    page.padding = 0

    # The most direct URL to bypass wrappers
    HF_URL = "https://rafi11223-medi-agent.hf.space/?__theme=light"

    status_text = ft.Text("🏥 Connecting to Medical Agent...", size=16, color=ft.Colors.BLUE_800)
    error_text = ft.Text("", size=14, color=ft.Colors.RED_ACCENT, visible=False)
    
    # Fallback button in case WebView is totally blocked by the phone
    fallback_btn = ft.ElevatedButton(
        "Open in Browser", 
        icon=ft.Icons.OPEN_IN_BROWSER,
        on_click=lambda _: page.launch_url(HF_URL),
        visible=False
    )

    def on_page_ended(e):
        status_text.visible = False
        loading_ring.visible = False
        page.update()

    def on_error(e):
        error_text.value = f"Connection Issue: {e.data}"
        error_text.visible = True
        fallback_btn.visible = True
        page.update()

    loading_ring = ft.ProgressRing(width=30, height=30, stroke_width=3)

    webview = ft.WebView(
        HF_URL,
        expand=True,
        javascript_enabled=True,
        on_page_ended=on_page_ended,
        on_web_resource_error=on_error,
    )

    page.add(
        ft.Column(
            [
                ft.Container(
                    content=ft.Column([
                        ft.Row([loading_ring, status_text], alignment=ft.MainAxisAlignment.CENTER),
                        error_text,
                        fallback_btn
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=20,
                    alignment=ft.alignment.center
                ),
                webview
            ],
            expand=True,
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
