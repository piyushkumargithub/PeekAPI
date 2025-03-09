import customtkinter as ctk

class RequestPanel(ctk.CTkFrame):
    def __init__(self, parent, on_send_request):
        super().__init__(parent)
        
        self.on_send_request = on_send_request
        
        #URL Input
        self.url_entry = ctk.CTkEntry(self, placeholder_text="Enter URL")
        self.url_entry.pack(pady=10, fill='x')

        #Request Method Selector 
        self.method_var= ctk.StringVar(value="GET")
        self.method_menu = ctk.CTkOptionMenu(self, variable=self.method_var, 
                                             values=["GET", "POST", "PUT", "DELETE", "PATCH"])
        self.method_menu.pack(pady=10, fill='x')

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
        url = self.url_entry.get()
        method = self.method_var.get()
        headers = self.headers_entry.get()
        body = self.body_entry.get('0.0', 'end').strip()

        self.on_send_request(url, method, headers, body)