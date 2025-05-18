import customtkinter as ctk

class CharacterCreationScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Name 
        self.name_label = ctk.CTkLabel(self, text="Please enter your character's name:")
        self.name_label.grid(row=0, column=0)

        self.name_textbox = ctk.CTkTextbox(self)
        self.name_textbox.grid(row=1, column=0)