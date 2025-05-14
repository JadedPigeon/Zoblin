import customtkinter as ctk

class MainMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configure this frame to fill the parent container
        self.grid(row=0, column=0, sticky="nsew")

        # Configure rows and columns to expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Titale Frame
        self.title_frame = ctk.CTkFrame(self)
        self.title_frame.grid(row=0, column=0, padx=10, pady=20, sticky="n")

        # Title
        self.title_label = ctk.CTkLabel(self.title_frame, text="Zoblin", font=("Arial", 32))
        self.title_label.grid(row=0, column=0, padx=10, pady=20, sticky="n")

        # Subtitle
        self.subtitle_label = ctk.CTkLabel(self.title_frame, text="A Fantasy themed turn-based RPG", font=("Arial", 16))
        self.subtitle_label.grid(row=1, column=0, padx=10, pady=10, sticky="n")

        # Button Frame
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=1, column=0, pady=20, sticky="n")

        # Load Game Button
        self.load_button = ctk.CTkButton(self.button_frame, text="Load Game", command=lambda: print("Load Game clicked"), fg_color="darkblue")
        self.load_button.grid(row=0, column=0, padx=10, pady=20, sticky="n")

        # New Game Button
        self.start_button = ctk.CTkButton(self.button_frame, text="New Game", command=self.start_game)
        self.start_button.grid(row=2, column=0, padx=10, pady=20, sticky="n")

        # Options Button
        self.options_button = ctk.CTkButton(self.button_frame, text="Options", command=lambda: print("Options clicked"))
        self.options_button.grid(row=3, column=0, padx=10, pady=20, sticky="n")

        # Exit Button
        self.exit_button = ctk.CTkButton(self.button_frame, text="Exit", command=self.controller.quit)
        self.exit_button.grid(row=4, column=0, padx=10, pady=20, sticky="n")

    def start_game(self):
        """Switch to the battle screen."""
        print("Transitioning to the battle screen...")
        self.controller.show_frame("TownScreen")