import customtkinter as ctk

class ActionBox(ctk.CTkFrame):
    def __init__(self, parent, controller, zone):
        super().__init__(parent)
        self.controller = controller

        self.configure(width=200, height=200)
        self.grid(row=0, column=0, sticky="nsew")

        self.grid_propagate(False)

        # Configure rows and columns to expand
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        

        # Action buttons
        if zone == "town":
            self.button_0 = ctk.CTkButton(self, text="Locations", command=self.locations_button)
        else:
            print("Not implemented yet")
        self.button_0.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        self.button_1 = ctk.CTkButton(self, text="Inventory", command=self.placeholder_command)
        self.button_1.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.button_2 = ctk.CTkButton(self, text="Info", command=self.placeholder_command)
        self.button_2.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
        self.button_3 = ctk.CTkButton(self, text="Save", command=self.placeholder_command)
        self.button_3.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")
        self.button_4 = ctk.CTkButton(self, text="Exit", command=self.controller.quit)
        self.button_4.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")


    def placeholder_command(self):
        """Placeholder function for button commands."""
        print("This feature is not implemented yet.")

    def locations_button(self):
        self.button_0.configure(text="Town Keep", command=lambda: self.go_to_location("TownKeepScreen"))
        self.button_1.configure(text="Inn", command=lambda: self.go_to_location("InnScreen"))
        self.button_2.configure(text="Blacksmith", command=lambda: self.go_to_location("BlackSmithScreen"))
        self.button_3.configure(text="General Shop", command=lambda: self.go_to_location("GeneralShopScreen"))
        self.button_4.configure(text="Temple", command=lambda: self.go_to_location("TempleScreen"))
        self.button_5 = ctk.CTkButton(self, text="<-", command=self.reset_buttons)
        self.button_5.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        self.button_6 = ctk.CTkButton(self, text="Town", command=lambda: self.go_to_location("TownScreen"))
        self.button_6.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
        self.button_7 = ctk.CTkButton(self, text="Adventure", command=self.placeholder_command)
        self.button_7.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")
 
    def reset_buttons(self):
        """Reset buttons to the original state."""
        self.button_0.configure(text="Locations", command=self.locations_button)
        self.button_1.configure(text="Inventory", command=self.placeholder_command)
        self.button_2.configure(text="Info", command=self.placeholder_command)
        self.button_3.configure(text="Save", command=self.placeholder_command)
        self.button_4.configure(text="Exit", command=self.controller.quit)

        # Remove the back button
        self.button_5.destroy()
        self.button_6.destroy()
        self.button_7.destroy()

    def go_to_location(self, location):
        self.controller.show_frame(location)
        print(f"Going to {location}")
