import customtkinter as ctk
from ui.main_menu import MainMenu
from ui.battle_screen import BattleScreen
from ui.town import TownScreen, TownKeepScreen, InnScreen, BlackSmithScreen, GeneralShopScreen, TempleScreen, TownBaseScreen
from ui.character_creation import CharacterCreationScreen
from ui.action_box import ActionBox
from ui.message_box import MessageBox

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Zoblin - A Fantasy themed turn-based RPG")
        self.geometry("800x600")
        self.resizable(False, False)
        ctk.set_default_color_theme("assets/themes/earth_tones.json")

        # In App.__init__ (main.py)
        self.geometry("800x600")
        self.resizable(False, False)

        self.container = ctk.CTkFrame(self, width=800, height=600)
        self.container.pack_propagate(False)
        self.container.pack(fill="both", expand=False)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dictionary to store frames
        self.frames = {}

        # Frame classes mapped by name
        self.frame_classes = {
            "MainMenu": MainMenu,
            "BattleScreen": BattleScreen,
            "TownScreen": TownScreen,
            "TownKeepScreen": TownKeepScreen,
            "InnScreen": InnScreen,
            "BlackSmithScreen": BlackSmithScreen,
            "GeneralShopScreen": GeneralShopScreen,
            "TempleScreen": TempleScreen,
            "CharacterCreationScreen": CharacterCreationScreen
        }

        # Initialize frames
        for name, FrameClass in self.frame_classes.items():
            frame = FrameClass(self.container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.grid_remove()

        # Message and action boxes
        self.message_box = MessageBox(self.container, self)
        self.message_box.configure(width=550, height=200)
        self.action_box = ActionBox(self.container, self, "town")       
        self.action_box.configure(width=250, height=200)

        # Show the main menu first
        self.show_frame("MainMenu")

    def place_message_box(self):
        self.message_box.grid(row=1, column=0)
        self.message_box.grid_propagate(False)

    def place_action_box(self, state):
        self.action_box.grid(row=1, column=1)
        self.action_box.grid_propagate(False)
        if state == "actions":
            self.action_box.show_actions()
        elif state == "locations":
            self.action_box.show_locations()

    def show_frame(self, frame_name):
        for name, frame in self.frames.items():
            if name == frame_name:
                if isinstance(frame, TownBaseScreen):
                    frame.grid(row=0, column=0, columnspan=2)
                else:
                    frame.grid()
                frame.tkraise()
                # Only place ActionBox and MessageBox on town screens
                if isinstance(frame, TownBaseScreen):
                    if frame_name == "TownScreen":
                        self.place_action_box("actions")
                    else:
                        self.place_action_box("locations")
                    self.place_message_box()
                    self.message_box.clear_history()
                    frame.welcome_message()
                else:
                    self.action_box.grid_remove()
                    self.message_box.grid_remove()
            else:
                frame.grid_remove()

if __name__ == "__main__":
    app = App()
    app.mainloop()