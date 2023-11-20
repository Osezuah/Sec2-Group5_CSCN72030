import tkinter as tk
from tkinter import simpledialog, messagebox

# Enumeration for HVAC modes
class HVACMode:
    Ventilation = "Ventilation"
    FanOnly = "FanOnly"
    Auto = "Auto"

# PreferencesObject definition 
class PreferencesObject:
    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity

# Sensor data structure 
class SensorData:
    def __init__(self, occupancy_status, co2_concentration):
        self.occupancy_status = occupancy_status
        self.co2_concentration = co2_concentration

# ventilation class
class Ventilation:
    def __init__(self, user_id):
        self.user_id = user_id
        self.current_hvac_mode = HVACMode.Ventilation

    def set_hvac_mode(self, new_mode):
        # to check if the new HVAC Mode is valid (it would be case sensitive)
        if new_mode in [HVACMode.Ventilation, HVACMode.FanOnly, HVACMode.Auto]:
            self.current_hvac_mode = new_mode
        else:
            raise ValueError("Invalid HVAC mode")

    def is_user_authorized(self, requesting_user_id):
        # Always return True, effectively removing the authorization check
        return True

    def get_hvac_mode_as_string(self):
        return self.current_hvac_mode

def main():
    # Example usage with user ID "1A" 
    ventilation_module = Ventilation("1A")

    # Create Tkinter root window and GUI instance
    root = tk.Tk()
    gui = VentilationGUI(root, ventilation_module)

    # Run the Tkinter event loop
    root.mainloop()

class VentilationGUI:
    def __init__(self, master, ventilation_module):
        self.master = master
        self.ventilation_module = ventilation_module

        self.master.title("Ventilation Control")
        self.master.geometry("400x200")

        # Display user preferences 
        self.preferences_label = tk.Label(master, text=f"User {self.ventilation_module.user_id} preferences set: Temperature - 22.5, Humidity - 60")
        self.preferences_label.pack()

        # Display current HVAC mode
        self.current_mode_label = tk.Label(master, text=f"Current HVAC Mode: {self.ventilation_module.get_hvac_mode_as_string()}")
        self.current_mode_label.pack()

        # Button to change HVAC mode
        self.change_mode_button = tk.Button(master, text="Change HVAC Mode", command=self.change_mode)
        self.change_mode_button.pack()

    def change_mode(self):
        # Get user input for new HVAC mode
        new_mode = simpledialog.askstring("Change HVAC Mode", "Enter new HVAC mode (Ventilation, FanOnly, Auto):")

        # Validate and set the new HVAC mode
        try:
            self.ventilation_module.set_hvac_mode(new_mode)
            messagebox.showinfo("Success", f"HVAC mode set to {new_mode}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    main()
