import customtkinter as ctk
from PIL import Image

class TownBaseScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Fixed grid: 2 columns, 2 rows, fixed pixel sizes
        self.grid_rowconfigure(0, weight=0, minsize=400)
        self.grid_rowconfigure(1, weight=0, minsize=200)
        self.grid_columnconfigure(0, weight=0, minsize=600)
        self.grid_columnconfigure(1, weight=0, minsize=200)

    def welcome_message(self):
        self.controller.message_box.add_message("Hello World")

class TownScreen(TownBaseScreen):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Image frame (row 0, spans both columns)
        self.town_image_frame = ctk.CTkFrame(self, width=800, height=400)
        self.town_image_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.town_image_frame.grid_propagate(False)
        self.town_image_frame.grid_rowconfigure(0, weight=1)
        self.town_image_frame.grid_columnconfigure(0, weight=1)
        town_image = ctk.CTkImage(Image.open("assets/scenery/town.png"), size=(800, 400))
        self.town_image_label = ctk.CTkLabel(self.town_image_frame, image=town_image, text="")
        self.town_image_label.grid(row=0, column=0, sticky="nsew")

    def welcome_message(self):
        self.controller.message_box.add_message("This is the town. Here you can find a Town Keep, an Inn, a Blacksmith, a General Shop, and a Temple.")

class TownKeepScreen(TownBaseScreen):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.town_keep_image_frame = ctk.CTkFrame(self, width=800, height=400)
        self.town_keep_image_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.town_keep_image_frame.grid_propagate(False)
        self.town_keep_image_frame.grid_rowconfigure(0, weight=1)
        self.town_keep_image_frame.grid_columnconfigure(0, weight=1)
        town_keep_image = ctk.CTkImage(Image.open("assets/scenery/town_keep.jpg"), size=(800, 400))
        self.town_keep_image_label = ctk.CTkLabel(self.town_keep_image_frame, image=town_keep_image, text="")
        self.town_keep_image_label.grid(row=0, column=0, sticky="nsew")

    def welcome_message(self):
        self.controller.message_box.add_message("This is the Town Keep where you can find nobles to give you quests.")

class InnScreen(TownBaseScreen):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.inn_image_frame = ctk.CTkFrame(self, width=800, height=400)
        self.inn_image_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.inn_image_frame.grid_propagate(False)
        self.inn_image_frame.grid_rowconfigure(0, weight=1)
        self.inn_image_frame.grid_columnconfigure(0, weight=1)
        inn_image = ctk.CTkImage(Image.open("assets/scenery/inn.jpg"), size=(800, 400))
        self.inn_image_label = ctk.CTkLabel(self.inn_image_frame, image=inn_image, text="")
        self.inn_image_label.grid(row=0, column=0, sticky="nsew")

    def welcome_message(self):
        self.controller.message_box.add_message("Welcome to the Town Inn where you can rest up and heal")

class BlackSmithScreen(TownBaseScreen):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.blacksmith_image_frame = ctk.CTkFrame(self, width=800, height=400)
        self.blacksmith_image_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.blacksmith_image_frame.grid_propagate(False)
        self.blacksmith_image_frame.grid_rowconfigure(0, weight=1)
        self.blacksmith_image_frame.grid_columnconfigure(0, weight=1)
        blacksmith_image = ctk.CTkImage(Image.open("assets/scenery/blacksmith.jpg"), size=(800, 400))
        self.blacksmith_image_label = ctk.CTkLabel(self.blacksmith_image_frame, image=blacksmith_image, text="")
        self.blacksmith_image_label.grid(row=0, column=0, sticky="nsew")

    def welcome_message(self):
        self.controller.message_box.add_message("The Blacksmith has various armor and weapons for sale. He will also buy any weapons or armor you have to sell")

class GeneralShopScreen(TownBaseScreen):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.generalshop_image_frame = ctk.CTkFrame(self, width=800, height=400)
        self.generalshop_image_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.generalshop_image_frame.grid_propagate(False)
        self.generalshop_image_frame.grid_rowconfigure(0, weight=1)
        self.generalshop_image_frame.grid_columnconfigure(0, weight=1)
        generalshop_image = ctk.CTkImage(Image.open("assets/scenery/generalshop.jpg"), size=(800, 400))
        self.generalshop_image_label = ctk.CTkLabel(self.generalshop_image_frame, image=generalshop_image, text="")
        self.generalshop_image_label.grid(row=0, column=0, sticky="nsew")

    def welcome_message(self):
        self.controller.message_box.add_message("The general shop is full of all kinds of various items you may need and will buy anything off of you that you want to sell")

class TempleScreen(TownBaseScreen):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.temple_image_frame = ctk.CTkFrame(self, width=800, height=400)
        self.temple_image_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.temple_image_frame.grid_propagate(False)
        self.temple_image_frame.grid_rowconfigure(0, weight=1)
        self.temple_image_frame.grid_columnconfigure(0, weight=1)
        temple_image = ctk.CTkImage(Image.open("assets/scenery/temple.jpg"), size=(800, 400))
        self.temple_image_label = ctk.CTkLabel(self.temple_image_frame, image=temple_image, text="")
        self.temple_image_label.grid(row=0, column=0, sticky="nsew")

    def welcome_message(self):
        self.controller.message_box.add_message("Medidate and focus your experience to learn new abilities")