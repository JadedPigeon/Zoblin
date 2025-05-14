import customtkinter as ctk

class BattleScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Title
        self.title_label = ctk.CTkLabel(self, text="Battle Screen", font=("Arial", 28))
        self.title_label.pack(pady=20)

        # Action Buttons
        self.attack_button = ctk.CTkButton(self, text="Attack", command=self.attack)
        self.attack_button.pack(pady=10)

        self.defend_button = ctk.CTkButton(self, text="Defend", command=self.defend)
        self.defend_button.pack(pady=10)

        self.run_button = ctk.CTkButton(self, text="Run Away", command=self.run_away)
        self.run_button.pack(pady=10)

    def attack(self):
        print("Player attacks!")

    def defend(self):
        print("Player defends!")

    def run_away(self):
        print("Player runs away!")
        # Switch back to the main menu
        self.controller.show_frame("MainMenu")
