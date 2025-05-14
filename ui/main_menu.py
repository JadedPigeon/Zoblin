import customtkinter as ctk

class MainMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Title
        self.title_label = ctk.CTkLabel(self, text="Fantasy Game", font=("Arial", 32))
        self.title_label.pack(pady=20)

        # New Game Button
        self.start_button = ctk.CTkButton(self, text="New Game", command=self.start_game)
        self.start_button.pack(pady=10)

        # Exit Button
        self.exit_button = ctk.CTkButton(self, text="Exit", command=self.controller.quit)
        self.exit_button.pack(pady=10)

    def start_game(self):
        """Switch to the battle screen."""
        print("Transitioning to the battle screen...")
        # Use the string name of the frame class to avoid import issues
        self.controller.show_frame("BattleScreen")
