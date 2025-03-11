import customtkinter as ctk
from ui.request_panel import RequestPanel
from ui.response_panel import ResponsePanel
from utils.request_handler import handle_request  # Import from utils

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PeekAPI")
        self.geometry("800x800")

        # Request Panel
        self.request_panel = RequestPanel(self, self.process_request)
        self.request_panel.pack(pady=20, padx=10, fill="both", expand=True)

        # Response Panel
        self.response_panel = ResponsePanel(self)
        self.response_panel.pack(pady=20, padx=10, fill="both", expand=True)

    def process_request(self, url, method, headers, body):
        """Calls request handler and updates response panel."""
        response_data = handle_request(url, method, headers, body)
        self.response_panel.update_response(
            status_code=response_data["status_code"],
            headers=response_data["headers"],
            body=response_data["body"]
        )

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
