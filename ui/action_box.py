import customtkinter as ctk

class ActionBox(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure this frame to fill the parent container
        self.grid(row=0, column=0, sticky="nsew")

        # Configure rows and columns to expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.configure(width=200, height=200)

        # Place holder buttons
        self.shop_button = ctk.CTkButton(self, text="Shop", command=self.place_holder)
        self.shop_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.inn_button = ctk.CTkButton(self, text="Inn", command=self.place_holder)
        self.inn_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.exit_button = ctk.CTkButton(self, text="Exit", command=self.place_holder)
        self.exit_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    def place_holder(self):
        """Placeholder for future actions."""
        print("Placeholder action executed.")