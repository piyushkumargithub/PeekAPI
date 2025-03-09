import customtkinter as ctk
import json
class ResponsePanel(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        #Status code display
        self.status_label = ctk.CTkLabel(self, text="Status Code:",font=("Arial",14,"bold"))
        self.status_label.pack(pady=5,anchor='w')

        #Headers Display
        self.headers_textbox = ctk.CTkTextbox(self, height=100)
        self.headers_textbox.insert('0.0', 'Response Headers')
        self.headers_textbox.pack(pady=5, fill='both', expand=True)

        #Response Body Display
        self.body_textbox = ctk.CTkTextbox(self, height=200)
        self.body_textbox.insert('0.0', 'Response Body')
        self.body_textbox.pack(pady=5, fill='both', expand=True)

    def update_response(self, status_code: int, headers: dict, body: str):
        #Update Status Code
        self.status_label.configure(text=f"Status Code: {status_code}")

        #Pretty print headers
        self.headers_textbox.delete('0.0', 'end')
        self.headers_textbox.insert('0.0', json.dumps(headers, indent=4))

        #Pretty print body
        self
        try:
            parsed_body = json.loads(body)
            formatted_body = json.dumps(parsed_body, indent=4)
        except json.JSONDecodeError:
            formatted_body = body

        self.body_textbox.insert('0.0', formatted_body)