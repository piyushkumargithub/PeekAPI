import customtkinter as ctk
from ui.request_panel import RequestPanel
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("peekAPI")
        self.geometry("800x600")

        # Request Panel
        self.request_panel = RequestPanel(self, self.handle_request)
        self.request_panel.pack(pady=20, fill="both", expand=True)

    def handle_request(self, url, method, headers, body):
        print(f"URL: {url}")
        print(f"Method: {method}")
        print(f"Headers: {headers}")
        print(f"Body: {body}")