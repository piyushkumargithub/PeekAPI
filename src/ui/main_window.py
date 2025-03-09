import customtkinter as ctk
from ui.request_panel import RequestPanel
from ui.response_panel import ResponsePanel
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
import httpx


class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("peekAPI")
        self.geometry("800x600")

        # Request Panel
        self.request_panel = RequestPanel(self, self.handle_request)
        self.request_panel.pack(pady=20, fill="both", expand=True)

        self.response_panel = ResponsePanel(self)
        self.response_panel.pack(pady=20, fill="both", expand=True)

    def handle_request(self, url, method, headers, body):
        try:
            with httpx.Client() as client:
                response = client.request(method=method,
                                            url=url,
                                            headers=headers,
                                            json=body if isinstance(body, dict) else None,
                                            data=body if isinstance(body, str) else None,
                                            )
                
                #Pass response data to response panel
                self.response_panel.update_response(
                    status_code=response.status_code,
                    headers=dict(response.headers),
                    body=response.text
                )
        except httpx.RequestError as e:
            self.response_panel.update_response(
                status_code=0,
                headers={},
                body=str(e)
            )