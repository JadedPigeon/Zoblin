import customtkinter as ctk
from ui.main_menu import MainMenu
from ui.battle_screen import BattleScreen

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Fantasy Game")
        self.geometry("800x600")

        # Frame container (acts as a stack of frames)
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        # Dictionary to store frames
        self.frames = {}

        # Frame classes mapped by name
        self.frame_classes = {
            "MainMenu": MainMenu,
            "BattleScreen": BattleScreen
        }

        # Initialize frames
        for name, FrameClass in self.frame_classes.items():
            frame = FrameClass(self.container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the main menu first
        self.show_frame("MainMenu")

    def show_frame(self, frame_name):
        """Switch to the specified frame by name."""
        frame = self.frames[frame_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()
