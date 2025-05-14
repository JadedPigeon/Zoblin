import customtkinter as ctk
from PIL import Image
from ui.message_box import MessageBox
from ui.action_box import ActionBox

class TownScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure rows and columns to expand
        self.grid_rowconfigure(0, weight=2)  # Town image gets more space
        self.grid_rowconfigure(1, weight=1)  # Message and actions share space
        self.grid_columnconfigure(0, weight=3)  # Message history gets more space
        self.grid_columnconfigure(1, weight=1)  # Action frame gets less space

        # Image frame
        self.town_image_frame = ctk.CTkFrame(self, width=800, height=400)
        self.town_image_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        # Load and display the town.png image
        town_image = ctk.CTkImage(Image.open("assets/scenery/town.png"), size=(800, 400))
        self.town_image_label = ctk.CTkLabel(self.town_image_frame, image=town_image, text="")
        self.town_image_label.grid(row=0, column=0, sticky="nsew")

        # Message frrame
        self.message_box = MessageBox(self, controller)
        self.message_box.grid_rowconfigure(0, weight=1)
        self.message_box.grid_columnconfigure(0, weight=1)
        self.message_box.grid(row=1, column=0, sticky="nsew")

        # Action frame
        self.town_action_frame = ActionBox(self, controller)
        self.town_action_frame.grid(row=1, column=1, sticky="nsew")

    def open_shop(self):
        print("Opening shop...")

    def open_inn(self):
        print("Opening inn...")

    def exit_town(self):
        print("Exiting town...")