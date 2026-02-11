import flet as ft

def main(page: ft.Page):
    page.title = "Medi-Agent Mobile"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 800
    page.padding = 0

    # Using the direct app URL instead of the Space wrapper for better performance in WebView
    HF_URL = "https://rafi11223-medi-agent.hf.space/?__theme=light"

    # The WebView component
    webview = ft.WebView(
        HF_URL,
        expand=True,
        javascript_enabled=True,
        # Setting a common user agent can help bypass some security blocks in WebViews
        user_agent="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
        on_page_started=lambda _: print("Loading Medi-Agent..."),
        on_page_ended=lambda _: print("Medi-Agent Ready!"),
        on_web_resource_error=lambda e: print(f"Page error: {e.description}"),
    )

    page.add(webview)

if __name__ == "__main__":
    ft.app(target=main)
