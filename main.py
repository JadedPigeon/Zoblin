import customtkinter as ctk
from ui.main_menu import MainMenu
from ui.battle_screen import BattleScreen
from ui.town_screen import TownScreen 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Zoblin - A Fantasy themed turn-based RPG")
        self.geometry("800x600")
        ctk.set_default_color_theme("assets/themes/earth_tones.json")

        # Frame container (acts as a stack of frames)
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        # Configure rows and columns to expand
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Dictionary to store frames
        self.frames = {}

        # Frame classes mapped by name
        self.frame_classes = {
            "MainMenu": MainMenu,
            "BattleScreen": BattleScreen,
            "TownScreen": TownScreen
        }

        # Initialize frames
        for name, FrameClass in self.frame_classes.items():
            frame = FrameClass(self.container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the main menu first
        self.show_frame("TownScreen")

    def show_frame(self, frame_name):
        """Switch to the specified frame by name."""
        frame = self.frames[frame_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()