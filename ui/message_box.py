import customtkinter as ctk

class MessageBox(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure this frame to fill the parent container
        self.grid_columnconfigure(0, weight=1)

        # Configure rows and columns to expand
        self.configure(width=400, height=200)
        self.grid_propagate(False)

        # Message Label
        self.message_history = ctk.CTkTextbox(self, corner_radius=0, wrap="word")
        self.message_history.grid(row=0, column=0, sticky="nesw")
        self.message_history.configure(state="disabled")

    def add_message(self, message):
        """Add a message to the message history."""
        self.message_history.configure(state="normal")
        self.message_history.insert("end", message + "\n")
        self.message_history.configure(state="disabled")

    def clear_history(self):
        self.message_history.configure(state="normal")
        self.message_history.delete("1.0", "end")
        self.message_history.configure(state="disabled")
