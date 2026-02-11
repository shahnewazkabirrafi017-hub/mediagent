import flet as ft
import os

def main(page: ft.Page):
    page.title = "MediAgent AI"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 800
    page.padding = 0

    # The production URL of your AI Agent (Embed version is more stable for mobile)
    HF_URL = "https://huggingface.co/spaces/rafi11223/Medi-Agent?embed=true"

    # Minimal UI for the WebView
    webview = ft.WebView(
        HF_URL,
        expand=True,
        javascript_enabled=True,
    )

    page.add(webview)

if __name__ == "__main__":
    ft.app(target=main)
