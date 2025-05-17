import customtkinter as ctk
from PIL import Image
from ui.message_box import MessageBox
from ui.action_box import ActionBox

class TownScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure rows and columns to expand

        self.grid_propagate(False)

        # Image frame
        self.town_image_frame = ctk.CTkFrame(self, width=800, height=400)
        self.town_image_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.town_image_frame.grid_propagate(False)
        # Load and display the town.png image
        town_image = ctk.CTkImage(Image.open("assets/scenery/town.png"), size=(800, 400))
        self.town_image_label = ctk.CTkLabel(self.town_image_frame, image=town_image, text="")
        self.town_image_label.grid(row=0, column=0, sticky="nsew")

        # Message frrame
        self.message_box = MessageBox(self, controller)
        self.message_box.grid(row=1, column=0, sticky="nsew")

        # Action frame
        self.town_action_frame = ActionBox(self, controller, "town")
        self.town_action_frame.grid(row=1, column=1, sticky="nsew")

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

class InnScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid_propagate(False)
        
        # Image frame
        self.inn_image_frame = ctk.CTkFrame(self, width=800, height=400)
        self.inn_image_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.inn_image_frame.grid_propagate(False)
        # Load and display the town.png image
        inn_image = ctk.CTkImage(Image.open("assets/scenery/inn.jpg"), size=(800, 400))
        self.inn_image_label = ctk.CTkLabel(self.inn_image_frame, image=inn_image, text="")
        self.inn_image_label.grid(row=0, column=0, sticky="nsew")

        # Message frrame
        self.message_box = MessageBox(self, controller)
        self.message_box.grid(row=1, column=0, sticky="nsew")
        self.message_box.add_message("Welcome to the inn! Here you can relax and rest")

        # Action frame
        self.town_action_frame = ActionBox(self, controller, "town")
        self.town_action_frame.grid(row=1, column=1, sticky="nsew")

class BlackSmithScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid_propagate(False)
        
        # Image frame
        self.blacksmith_image_frame = ctk.CTkFrame(self, width=800, height=400)
        self.blacksmith_image_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.blacksmith_image_frame.grid_propagate(False)
        # Load and display the town.png image
        blacksmith_image = ctk.CTkImage(Image.open("assets/scenery/blacksmith.jpg"), size=(800, 400))
        self.blacksmith_image_label = ctk.CTkLabel(self.blacksmith_image_frame, image=blacksmith_image, text="")
        self.blacksmith_image_label.grid(row=0, column=0, sticky="nsew")

        # Message frrame
        self.message_box = MessageBox(self, controller)
        self.message_box.grid(row=1, column=0, sticky="nsew")
        self.message_box.add_message("Welcome to the blacksmith! Here you can buy and sell weapons and armor")

        # Action frame
        self.town_action_frame = ActionBox(self, controller, "town")
        self.town_action_frame.grid(row=1, column=1, sticky="nsew")

class GeneralShopScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid_propagate(False)
        
        # Image frame
        self.generalshop_image_frame = ctk.CTkFrame(self, width=800, height=400)
        self.generalshop_image_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.generalshop_image_frame.grid_propagate(False)
        # Load and display the town.png image
        generalshop_image = ctk.CTkImage(Image.open("assets/scenery/generalshop.jpg"), size=(800, 400))
        self.generalshop_image_label = ctk.CTkLabel(self.generalshop_image_frame, image=generalshop_image, text="")
        self.generalshop_image_label.grid(row=0, column=0, sticky="nsew")

        # Message frrame
        self.message_box = MessageBox(self, controller)
        self.message_box.grid(row=1, column=0, sticky="nsew")
        self.message_box.add_message("Welcome to the generalshop! Here you can buy and sell items")

        # Action frame
        self.town_action_frame = ActionBox(self, controller, "town")
        self.town_action_frame.grid(row=1, column=1, sticky="nsew")

class TempleScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.grid_propagate(False)
        
        # Image frame
        self.temple_image_frame = ctk.CTkFrame(self, width=800, height=400)
        self.temple_image_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.temple_image_frame.grid_propagate(False)
        # Load and display the town.png image
        temple_image = ctk.CTkImage(Image.open("assets/scenery/temple.jpg"), size=(800, 400))
        self.temple_image_label = ctk.CTkLabel(self.temple_image_frame, image=temple_image, text="")
        self.temple_image_label.grid(row=0, column=0, sticky="nsew")

        # Message frrame
        self.message_box = MessageBox(self, controller)
        self.message_box.grid(row=1, column=0, sticky="nsew")
        self.message_box.add_message("Welcome to the temple! Here you can upgrade your character!")

        # Action frame
        self.town_action_frame = ActionBox(self, controller, "town")
        self.town_action_frame.grid(row=1, column=1, sticky="nsew")