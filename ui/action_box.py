import customtkinter as ctk

class ActionBox(ctk.CTkFrame):
    def __init__(self, parent, controller, zone):
        super().__init__(parent)
        self.controller = controller

        self.configure(width=200, height=200)
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_propagate(False)

        # Make the single row and column expandable
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Action Frame
        self.action_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.action_frame.grid(row=0, column=0, sticky="nsew")
        self.action_frame.grid_propagate(False)
        self.action_frame.grid_columnconfigure(0, weight=1)
        self.action_buttons = [
            ctk.CTkButton(self.action_frame, text="Locations", command=self.show_locations),
            ctk.CTkButton(self.action_frame, text="Inventory", command=self.placeholder_command),
            ctk.CTkButton(self.action_frame, text="Info", command=self.placeholder_command),
            ctk.CTkButton(self.action_frame, text="Save", command=self.placeholder_command),
            ctk.CTkButton(self.action_frame, text="Exit", command=self.controller.quit),
        ]
        for i, btn in enumerate(self.action_buttons):
            btn.grid(row=i, column=0, padx=10, pady=5, sticky="nsew")

        # Location Frame
        self.location_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.location_buttons = [
            ctk.CTkButton(self.location_frame, text="Town Keep", command=lambda: self.go_to_location("TownKeepScreen")),
            ctk.CTkButton(self.location_frame, text="Inn", command=lambda: self.go_to_location("InnScreen")),
            ctk.CTkButton(self.location_frame, text="Blacksmith", command=lambda: self.go_to_location("BlackSmithScreen")),
            ctk.CTkButton(self.location_frame, text="General Shop", command=lambda: self.go_to_location("GeneralShopScreen")),
            ctk.CTkButton(self.location_frame, text="Temple", command=lambda: self.go_to_location("TempleScreen")),
            ctk.CTkButton(self.location_frame, text="<-", command=self.show_actions),
            ctk.CTkButton(self.location_frame, text="Town", command=lambda: self.go_to_location("TownScreen")),
            ctk.CTkButton(self.location_frame, text="Adventure", command=self.placeholder_command),
        ]
        for i, btn in enumerate(self.location_buttons):
            if i < 5:
                btn.grid(row=i, column=0, padx=10, pady=5, sticky="nsew")
            else:
                btn.grid(row=i-5, column=1, padx=10, pady=5, sticky="nsew")

        # Make location_frame's grid expandable too
        self.location_frame.grid_rowconfigure(tuple(range(5)), weight=1)
        self.location_frame.grid_columnconfigure((0, 1), weight=1)

        # Show only the action frame at start
        self.show_actions()

    def show_actions(self):
        self.location_frame.grid_remove()
        self.action_frame.grid(row=0, column=0, sticky="nsew")

    def show_locations(self):
        self.action_frame.grid_remove()
        self.location_frame.grid(row=0, column=0, sticky="nsew")

    def placeholder_command(self):
        print("This feature is not implemented yet.")

    def go_to_location(self, location):
        self.controller.show_frame(location)
        self.show_actions()
        