import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from utils.collections_handler import save_collection
import re
import json

class RequestPanel(ctk.CTkFrame):
    def __init__(self, parent, on_send_request,sidebar):
        super().__init__(parent)
        self.sidebar = sidebar
        
        self.on_send_request = on_send_request
        
        # Container Frame for URL and Method
        self.url_method_frame = ctk.CTkFrame(self)
        self.url_method_frame.pack(pady=10, padx=30, fill='x')

        # URL Input
        self.url_entry = ctk.CTkEntry(self.url_method_frame, placeholder_text="Enter URL")
        self.url_entry.pack(side='right', fill='x', expand=True)

        # Request Method Selector
        self.method_var = ctk.StringVar(value="GET")
        self.method_menu = ctk.CTkOptionMenu(self.url_method_frame, variable=self.method_var, 
                             values=["GET", "POST", "PUT", "DELETE", "PATCH"])
        self.method_menu.pack(side='left', padx=(0,5))

        #Headers Input
        self.headers_entry = ctk.CTkEntry(self, placeholder_text="Enter Headers")
        self.headers_entry.pack(pady=10,padx=30, fill='x')

        #Label for the Body Input
        body_label = ctk.CTkLabel(self, text="Request Body:")
        body_label.pack(pady=(10, 0), padx=20, anchor="w")

        #Body Input
        self.body_entry = ctk.CTkTextbox(self, height=100)
        self.body_entry.pack(pady=10,padx=20, fill='both', expand=True)

        # Container frame for buttons
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=20, padx=20)

        # Send Request Button
        self.send_button = ctk.CTkButton(self.button_frame, text='Send Request', command=self.send_request)
        self.send_button.pack(side='left', expand=True, padx=5)

        # Save Request Button
        self.save_button = ctk.CTkButton(self.button_frame, text='Save Request', command=self.save_request)
        self.save_button.pack(side='right', expand=True, padx=5)


    def save_request(self):
        name = self.url_entry.get() or "New Request"
        url = self.url_entry.get().strip()
        method = self.method_var.get()
        headers = self.headers_entry.get().strip()
        body = self.body_entry.get('0.0', 'end').strip()

        save_collection(name, url, method, headers, body)

        if self.sidebar:
            self.sidebar.load_collections()

    def load_requests(self, url, method, headers, body):
        self.url_entry.delete(0, 'end')
        self.url_entry.insert(0, url)

        self.method_var.set(method)

        self.headers_entry.delete(0, 'end')
        self.headers_entry.insert(0, headers)

        self.body_entry.delete('0.0', 'end')
        self.body_entry.insert('0.0', body)



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
        
        
        self.on_send_request(url, method, parsed_headers, body)

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