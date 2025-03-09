import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import re
import json

class RequestPanel(ctk.CTkFrame):
    def __init__(self, parent, on_send_request):
        super().__init__(parent)
        
        self.on_send_request = on_send_request
        
        #URL Input
        self.url_entry = ctk.CTkEntry(self, placeholder_text="Enter URL")
        self.url_entry.pack(pady=10,padx=30, fill='x')

        #Request Method Selector 
        self.method_var= ctk.StringVar(value="GET")
        self.method_menu = ctk.CTkOptionMenu(self, variable=self.method_var, 
                                             values=["GET", "POST", "PUT", "DELETE", "PATCH"])
        self.method_menu.pack(pady=10,padx=100, fill='x')

        #Headers Input
        self.headers_entry = ctk.CTkEntry(self, placeholder_text="Enter Headers")
        self.headers_entry.pack(pady=10, fill='x')

        #Body Input
        self.body_entry = ctk.CTkTextbox(self, height=100)
        self.body_entry.insert('0.0', 'Requst Body for POST, PUT, DELETE, PATCH')
        self.body_entry.pack(pady=10, fill='both', expand=True)

        #Send Request Button
        self.send_button = ctk.CTkButton(self, text='Send Request', command=self.send_request)
        self.send_button.pack(pady=20)

    def send_request(self):
        url = self.url_entry.get().strip()
        method = self.method_var.get()
        headers = self.headers_entry.get().strip()
        body = self.body_entry.get('0.0', 'end').strip()


        #validate URL
        if not self.is_valid_url(url):
            CTkMessagebox(title="Invalid URL", message="Please enter a valid URL",icon="cancel", option_1="OK")
            return
        
        #validate Headers
        parsed_headers = None
        if headers:
            try:
                parsed_headers = json.loads(headers)
                if not isinstance(parsed_headers, dict):
                    raise ValueError("Headers must be a JSON object")
            except json.JSONDecodeError:
                CTkMessagebox(title="Invalid Headers", message="Headers must be a valid JSON object",icon="cancel", option_1="OK")
                return
            
        #validate Body 
        if method in ["POST", "PUT", "PATCH"] and not body:
            CTkMessagebox(title="Invalid Body", message="Request body is empty for a write method",icon="warning", option_1="OK")
        
        
        self.on_send_request(url, method, headers, body)

    def is_valid_url(self, url):
        url_pattern=re.compile(
            r'^(https?://)?'
            r'((([a-zA-Z0-9\-_]+\.)+[a-zA-Z]{2,})'
            r'|localhost'
            r'|\d{1,3}(\.\d{1,3}){3})'
            r'(:\d+)?'
            r'(/.*)?$'
        )
        return re.match(url_pattern, url)