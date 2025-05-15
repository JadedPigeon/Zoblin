import customtkinter as ctk
from PIL import Image
from ui.message_box import MessageBox
from ui.action_box import ActionBox

class TownKeepScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid_propagate(False)
        
        # Image frame
        self.town_keep_image_frame = ctk.CTkFrame(self, width=800, height=400)
        self.town_keep_image_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.town_keep_image_frame.grid_propagate(False)
        # Load and display the town.png image
        town_keep_image = ctk.CTkImage(Image.open("assets/scenery/town_keep.jpg"), size=(800, 400))
        self.town_keep_image_label = ctk.CTkLabel(self.town_keep_image_frame, image=town_keep_image, text="")
        self.town_keep_image_label.grid(row=0, column=0, sticky="nsew")

        # Message frrame
        self.message_box = MessageBox(self, controller)
        self.message_box.grid(row=1, column=0, sticky="nsew")
        self.message_box.add_message("Welcome to the keep! Here you can find quests")

        # Action frame
        self.town_action_frame = ActionBox(self, controller, "town")
        self.town_action_frame.grid(row=1, column=1, sticky="nsew")