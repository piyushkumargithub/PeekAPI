import customtkinter as ctk
from ui.request_panel import RequestPanel
from ui.response_panel import ResponsePanel
from ui.sidebar import Sidebar
from utils.request_handler import handle_request  # Import from utils

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PeekAPI")
        self.geometry("1000x800")

        # self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = Sidebar(self, request_panel=None)
        self.sidebar.grid(row=0,column=0, sticky="nsw",padx=10, pady=20,rowspan=2)

        # Request Panel
        self.request_panel = RequestPanel(self, self.process_request, self.sidebar)
        self.request_panel.grid(row=0, column=1, sticky="nsew",pady=20, padx=10)

        # Response Panel
        self.response_panel = ResponsePanel(self)
        self.response_panel.grid(row=1, column=1, sticky="nsew",pady=20, padx=10)

        self.sidebar.request_panel = self.request_panel

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
