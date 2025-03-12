import customtkinter as ctk
from utils.collections_handler import load_collections, get_collection_by_id, delete_collection

class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, request_panel):
        super().__init__(parent, width=200)
        self.pack_propagate(False)
        self.request_panel = request_panel

        self.label = ctk.CTkLabel(self, text="Collections", font=("Arial", 15, "bold"))
        self.label.pack(pady=10)

        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.pack(fill="both", expand=True,padx=10,pady=5)

        self.load_collections()

    def load_collections(self):
        """Loads collections from the database and displays them."""
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        for entry in load_collections():
            collection_id = entry["id"]  # Unique identifier
            collection_name = entry["name"]

            frame = ctk.CTkFrame(self.scrollable_frame)
            frame.pack(fill="x", pady=2)

            frame.columnconfigure(0, weight=1)
            frame.columnconfigure(1, weight=0)

            button = ctk.CTkButton(frame, text=collection_name, anchor="w",
                                   width=120, height=30,
                                   command=lambda id=collection_id: self.load_selected_request(id))
            button.grid(row=0, column=0, sticky="ew", padx=(5, 2))

            delete_btn = ctk.CTkButton(frame, text="❌", width=30, height=30,
                                       fg_color="red", hover_color="darkred",
                                       command=lambda id=collection_id: self.delete_selected(id))
            delete_btn.grid(row=0, column=1, padx=(2, 5))

    def load_selected_request(self, collection_id):
        """Loads requests from the selected collection."""
        request_data = get_collection_by_id(collection_id)

        if request_data:
            self.request_panel.load_requests(
                request_data["url"],
                request_data["method"],
                request_data["headers"],
                request_data["body"]
            )

    def delete_selected(self, collection_id):
        """Deletes the selected collection."""
        delete_collection(collection_id)
        self.load_collections()