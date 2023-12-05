## GROUP 5 BUILDING AUTOMATION SYSTEM PROJECT
##                 BY
## EHINOMHEN OSEZUAH
## TAYLOR ILMONEN
## DRASTI PATEL
## RAJVI PARMAR

import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random
import functools
from datetime import datetime
import os
import time
import threading
import logging

#Global variable used in server module
logging.basicConfig(filename='server_logs.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class EmergencyModule:
    def __init__(self):
        self.is_emergency = False

    def trigger_emergency(self):
        self.is_emergency = True
        # Logic to handle the emergency - alert authorities, perform safety protocols, etc.
        print("Emergency triggered!")

    def resolve_emergency(self):
        self.is_emergency = False
        # Logic to resolve the emergency situation
        print("Emergency resolved.")

class SecurityPersonnel:
    def __init__(self):
        self.name = ""
        self.role = ""

class SecurityModule:
    def __init__(self):
        self.personnel_list = []
        self.virtual_camera_list = []
        self.user_profiles = {} #User profiles 

    def add_security_personnel(self, personnel):
        self.personnel_list.append(personnel)
        self.save_security_personnel_to_file()

    def remove_security_personnel(self, name):
        self.personnel_list = [personnel for personnel in self.personnel_list if personnel.name != name]
        self.save_security_personnel_to_file()

    def save_security_personnel_to_file(self):
        with open("security_personnel.txt", "w") as file:
            for personnel in self.personnel_list:
                file.write(f"{personnel.name},{personnel.role}\n")

    def save_user_profiles(self):
     with open("user_profiles.txt", "w") as file:
        for username, password in self.user_profiles.items():
            file.write(f"{username},{password}\n")

    def load_user_profiles(self):
     try:
        with open("user_profiles.txt") as file:
            for line in file:
                username, password = line.strip().split(',')
                self.user_profiles[username.strip()] = password.strip()
     except FileNotFoundError:
        pass

    

    def load_user_profiles(self):
        try:
            with open("user_profiles.txt") as file:
                for line in file:
                    username, password = line.strip().split(',')
                    self.user_profiles[username] = password
        except FileNotFoundError:
            pass


    def create_user_profile(self, username, password):
        self.user_profiles[username] = password 
        self.save_user_profiles()

    def remove_user_profile(self, username):
        if username in self.user_profiles:
            del self.user_profiles[username]
            self.save_user_profiles()
            return True
        return False

    def login_user(self, username, password):
        return username in self.user_profiles and self.user_profiles[username] == password
        
    
    def add_virtual_camera(self, location):
        self.virtual_camera_list.append(location)
        self.save_camera_locations_to_file()  # Save locations immediately after addition

    def save_camera_locations_to_file(self):
        with open("camera_locations.txt", "w") as file:
            for location in self.virtual_camera_list:
                file.write(f"{location}\n")

    def load_camera_locations_from_file(self):
        try:
            with open("camera_locations.txt", "r") as file:
                for line in file:
                    location = line.strip()
                    self.virtual_camera_list.append(location)
        except FileNotFoundError:
            pass

    def generate_camera_feed(self, location):
        return f"Camera Feed from {location}: {random.randint(0, 99)} people detected"
    
    def load_security_personnel_from_file(self):
        try:
            with open("security_personnel.txt", "r") as file:
                for line in file:
                    name, role = line.strip().split(',')
                    personnel = SecurityPersonnel()
                    personnel.name = name
                    personnel.role = role
                    self.personnel_list.append(personnel)
        except FileNotFoundError:
            pass

class HVACMode:
    Ventilation = "Ventilation"
    FanOnly = "FanOnly"
    Auto = "Auto"
    AC = "A/C"

class Ventilation:
    def __init__(self, floor, room_number):
        self.floor = floor
        self.room_number = room_number
        self.ventilation_status = False
        self.current_hvac_mode = HVACMode.Ventilation

    def toggle_ventilation(self):
        self.ventilation_status = not self.ventilation_status
        return self.ventilation_status

    def set_hvac_mode(self, new_mode):
        if self.ventilation_status:
            if new_mode in [HVACMode.Ventilation, HVACMode.FanOnly, HVACMode.Auto, HVACMode.AC]:
                self.current_hvac_mode = new_mode
            else:
                raise ValueError("Invalid HVAC mode")
        else:
            raise ValueError("Cannot change HVAC mode when ventilation is off")

    def get_ventilation_status(self):
        return self.ventilation_status

    def get_hvac_mode_as_string(self):
        return self.current_hvac_mode

class LightingModule:
    def __init__(self):
        self.light_intensities = [0, 25, 50, 75, 100]
        self.current_intensity_index = 0
        self.is_light_on = False

    def set_light_intensity(self, intensity_index):
        if 0 <= intensity_index < len(self.light_intensities):
            self.current_intensity_index = intensity_index
            print(f"Light intensity set to {self.light_intensities[self.current_intensity_index]}%")
        else:
            print("Invalid intensity index")

    def toggle_light(self):
        self.is_light_on = not self.is_light_on
        status_text = "On" if self.is_light_on else "Off"
        print(f"Lights turned {status_text} in the room.")

class Process:
    def __init__(self, name, estimated_time):
        self.name = name
        self.estimated_time = estimated_time
        self.progress = 0  # Track progress of the process

class Hardware:
    def __init__(self, name, required_processing_speed):
        self.name = name
        self.required_processing_speed = required_processing_speed

class Rack:
    def __init__(self):
        self.hardware_list = []
        self.required_performance_speed = 0

    def add_hardware(self, hardware):
        self.hardware_list.append(hardware)
        self.calculate_required_performance_speed()

    def remove_hardware(self):
        if self.hardware_list:
            self.hardware_list.pop()  # Remove the last hardware item from the list
            self.calculate_required_performance_speed()
            print("Hardware removed from the rack.")
        else:
            print("No hardware to remove from the rack.")

    def remove_rack(self):
        if self.rack_list:
            self.rack_list.pop()  # Remove the last rack from the list
            print("Rack removed from the server.")
            self.check_required_performance_speed()
        else:
            print("No rack to remove from the server.")

    def calculate_required_performance_speed(self):
        self.required_performance_speed = sum(hardware.required_processing_speed for hardware in self.hardware_list)

    def display_hardware(self):
        print("Hardware in the rack:")
        for hardware in self.hardware_list:
            print(f"{hardware.name} (Required Speed: {hardware.required_processing_speed})")

    def is_empty(self):
        return not self.hardware_list

    def get_required_performance_speed(self):
        return self.required_performance_speed

    def get_hardware_list(self):
        return self.hardware_list

class Server:
    def __init__(self, initial_speed, initial_temp):
        self.processing_speed = initial_speed
        self.temperature = initial_temp
        self.processes = []  # List to hold ongoing processes
        self.process_speed = initial_speed  # Server processing speed
        self.rack_list = [Rack() for _ in range(4)]  # Assuming each server starts with 4 racks

    def adjust_performance(self, new_speed):
        old_speed = self.processing_speed
        total_rack_speed = sum(rack.get_required_performance_speed() for rack in self.rack_list)

        if new_speed != old_speed:
            if new_speed < total_rack_speed:
                logging.warning(f"Server speed adjusted to {new_speed}. It should be adjusted to {total_rack_speed}.")
            elif new_speed < 0:
                logging.error("Processing speed cannot be below zero.")
            elif new_speed > 150:
                logging.error("Processing speed cannot exceed 150.")
            else:
                self.processing_speed = new_speed
                self.temperature = self.calculate_new_temperature()
                logging.info(f"Server performance adjusted from {old_speed} to {new_speed}.")

    def display_status(self):
        print(f"Server Performance: {self.processing_speed}")
        print(f"Server Temperature: {self.temperature}")
        self.display_racks()

    def get_rack_list(self):
        return self.rack_list

    def get_temperature(self):
        return self.temperature

    def get_processing_speed(self):
        return self.processing_speed

    def get_hardware_list(self, rack_index):
        if 0 <= rack_index < len(self.rack_list):
            return self.rack_list[rack_index].get_hardware_list()
        else:
            print("Invalid rack index.")
            return []

    def add_rack(self):
        if len(self.rack_list) < 8:
            self.rack_list.append(Rack())
            self.check_required_performance_speed()
        else:
            print("Cannot add more racks. Maximum rack limit reached.")

    def remove_rack(self):
        if len(self.rack_list) > 1:
            self.rack_list.pop()
        else:
            print("Cannot remove. Server must have at least one rack.")

    def add_hardware_to_rack(self, rack_index, hardware):
        if 0 <= rack_index < len(self.rack_list):
            self.rack_list[rack_index].add_hardware(hardware)
            self.check_required_performance_speed()
        else:
            print("Invalid rack index.")
        logging.info(f"Added {hardware.name} to Rack {rack_index + 1}.")  # Assuming rack_index is 0-based


    def remove_hardware_from_rack(self, rack_index):
        if 0 <= rack_index < len(self.rack_list):
            self.rack_list[rack_index].remove_hardware()
        else:
            print("Invalid rack index.")
        self.check_required_performance_speed()
        logging.info(f"Removed hardware from Rack {rack_index + 1}.")  # Assuming rack_index is 0-based

    def display_racks(self):
        print("Racks in the server:")
        for i, rack in enumerate(self.rack_list, start=1):
            print(f"Rack {i} (Required Speed: {rack.get_required_performance_speed()}):")
            rack.display_hardware()

    def add_process(self, process):
        self.processes.append(process)
        # Start a new thread to update process progress
        threading.Thread(target=self.update_process_progress, args=(process, len(self.processes) - 1)).start()

    def update_process_progress(self, process, server_index):
        start_time = time.time()
        while process.progress < 100:
            elapsed_time = time.time() - start_time

            # Calculate progress based on the server's individual processing speed
            progress_increment = (100 / process.estimated_time) * (1 / self.processing_speed) * elapsed_time
            process.progress = min(100, process.progress + progress_increment)

            # Update every 0.1 seconds for better accuracy
            time.sleep(0.1)

        # When the process completes, reset the progress bar and allow adding another process
        self.reset_progress_bar(server_index)
        self.server_manager_app.toggle_timer_visibility(server_index)  # Hide the timer label
        self.complete_process(process)  # Call the method to signify process completion

    def reset_progress_bar(self, server_index):
        # Check if the progress bar reaches 100% and mark the associated process as completed
        if self.processes[server_index].progress >= 100:
            self.processes[server_index].progress = 100  # Ensure the progress is at 100%
            completed_process = self.processes[server_index]
            # Perform actions to handle the completion of the process
            self.complete_process(completed_process)  # Implement a method to handle completed processes

        # Reset the progress bar associated with the completed process
        self.processes[server_index].progress = 0

    def allow_adding_process(self):
        return not self.processes or all(process.progress >= 100 for process in self.processes)
    
    def complete_process(self, process):
        # Perform actions or updates upon completion of the process
        logging.info(f"Process '{process.name}' completed successfully.")

        # Remove the completed process from the list of ongoing processes
        if process in self.processes:
            self.processes.remove(process)


    def calculate_new_temperature(self):
        return self.processing_speed * 2
    
    def update_temperature(self, new_temperature):
        old_temp = self.temperature
        self.temperature = new_temperature

        logging.info(f"Temperature updated from {old_temp} to {new_temperature}.")

    def check_required_performance_speed(self):
        total_required_speed = sum(rack.get_required_performance_speed() for rack in self.rack_list)
        if self.processing_speed != total_required_speed:
            print("Warning: Current server performance speed does not match the required speed based on added hardware.")


class SensorType:
    MOTION = "Motion Sensor"
    OCCUPANCY = "Occupancy Sensor"

class Room:
    def __init__(self, room_number):
        self.room_number = room_number
        self.motion_detected = False
        self.occupancy = 0

class Floor:
    def __init__(self, floor_number, num_rooms):
        self.floor_number = floor_number
        self.rooms = [Room(f"{floor_number}{'abcdefghijklmnopqrstuvwxyz'[i]}") for i in range(num_rooms)]
        self.motion_in_corridor = False

class SensorClass:
    def __init__(self, floor_objects):
        self.floor_objects = floor_objects
        self.timestamp = None

    def read_sensor_data(self, selected_floor):
        # Simulating the sensor data retrieval process for the selected floor
        floor = next((floor for floor in self.floor_objects if floor.floor_number == selected_floor), None)
        if floor:
            for room in floor.rooms:
                room.motion_detected = random.choice([True, False])  # Simulate random motion detection
                room.occupancy = random.randint(1, 10) if room.motion_detected else 0
            floor.motion_in_corridor = random.choice([True, False])  # Simulate random motion detection in corridor
        self.timestamp = datetime.now()

    def get_sensor_reading(self):
        return [(floor.floor_number, room.room_number, room.motion_detected, room.occupancy) for floor in self.floor_objects for room in floor.rooms]

class Heating_Cooling_Unit:
    def __init__(self):
        self.state = False
    
    def setState(self, status):
        self.state = status
    
    def getState(self):
        return self.state

class Temperature(Heating_Cooling_Unit):
    def __init__(self):
        super().__init__()
        self.tempDegree = 0

    def setTemp(self, celsius_degree):
        self.tempDegree = celsius_degree
        if self.tempDegree > 100:
            raise Exception("Temperature should not go above 100°C")
        elif self.tempDegree < 20:
            raise Exception("Temperature should not go below 20°C")

    def getTemp(self):
        return self.tempDegree

    def increase_temp(self):
        self.tempDegree += 1
        if self.tempDegree <= 100:
            return self.tempDegree
        else:
            raise ValueError("Temperature should not go above 100°C")

    def decrease_temp(self):
        self.tempDegree -= 1
        if self.tempDegree >= 20:
             return self.tempDegree
        else:
            raise ValueError("Temperature should not go below 20°C")

class TemperatureGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Heating/Cooling Control")

        self.temperature = Temperature()
        self.unitState = Heating_Cooling_Unit()
        self.emergency_module = EmergencyModule()
        # Set font size
        font_size = 12

        self.emergency_status_label = tk.Label(master, text="Emergency Status: OFF", fg="black")
        self.emergency_status_label.pack()

        self.emergency_button = tk.Button(master, text="Trigger Emergency", command=self.toggle_emergency)
        self.emergency_button.pack()

        #creating a button for energy graph
        self.energy_button = tk.Button(master, text='Energy Graph', command=self.open_energy_consumed_graph, font=("Helvetica", font_size))
        # Pack the button to the top-left corner
        self.energy_button.pack(side=tk.LEFT, anchor=tk.NW)

        #ON HEATING/COOLING UNITS
        # A button to power on the Heating/Cooling Units
        self.heatcool_button = tk.Button(master, text="Press to Power-On/Off Heaters/Coolers", command=self.open_heatcool_gui, font=("Helvetica", font_size))
        self.heatcool_button.pack(pady=10)

        # Create and place widgets
        self.label = tk.Label(master, text="Current Temperature: 0°C", font=("Helvetica", font_size))
        self.label.pack(pady=10)

        self.increase_button = tk.Button(master, text="Increase Temperature", command=self.increase_temp, font=("Helvetica", font_size))
        self.increase_button.pack(pady=10)

        self.decrease_button = tk.Button(master, text="Decrease Temperature", command=self.decrease_temp, font=("Helvetica", font_size))
        self.decrease_button.pack(pady=10)

        self.label_prompt = tk.Label(master, text="Enter Temperature (°C):", font=("Helvetica", font_size))
        self.label_prompt.pack(pady=10)

        self.entry = tk.Entry(master, font=("Helvetica", font_size))
        self.entry.pack(pady=10)

        self.set_button = tk.Button(master, text="Set Temperature", command=self.set_temperature, font=("Helvetica", font_size))
        self.set_button.pack(pady=10)
        #error message label
        self.error_label = tk.Label(master, text="", fg="red", font=("Helvetica", font_size))
        self.error_label.pack(pady=10)

        #info label
        self.info_label = tk.Label(master, text="", fg="blue", font=("Helvetica", font_size))
        self.info_label.pack(pady=10)        

        # Centralize widgets
        for widget in [self.label, self.error_label, self.increase_button, self.decrease_button, self.label_prompt, self.entry, self.set_button]:
            widget.pack(side="top", fill="both", expand=True)
            

    def clear_info_label(self):
        self.info_label.config(text="")

    def update_info_label(self, message):
        self.info_label.config(text=message)
        # Schedule the info label to be cleared after 5 seconds
        self.master.after(5000, self.clear_info_label)       
        
    def update_label(self, final_temperature):
        self.label.config(text=f"Current Temperature: {final_temperature:.1f}°C")

    def update_temperature_label(self, new_temperature):
        self.label.config(text=f"Current Temperature: {new_temperature:.1f}°C")

    def clear_error_label(self):
        self.error_label.config(text="")

    def update_error_label(self, message):
        self.error_label.config(text=message)
        # Schedule the error label to be cleared after 5 seconds
        self.master.after(5000, self.clear_error_label)

    def increase_temp(self):
        try:
            tempp = self.temperature.increase_temp()
            if (tempp != float(self.entry.get())):
                target_temperature = tempp
                current_temperature = float(self.entry.get())

                # Calculate the number of steps and the step size
                num_steps = 50
                step_size = (target_temperature - current_temperature) / num_steps
                self.temperature.setTemp(target_temperature)
                
                # Schedule updates
                for step in range(1, num_steps + 1):
                    new_temperature = current_temperature + step * step_size
                    self.master.after(step * 100, functools.partial(self.update_temperature_label, new_temperature))
                
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(tempp))
                # Update the temperature label after the final step
                self.master.after((num_steps + 1) * 100, functools.partial(self.update_label, target_temperature))
                self.update_error_label("")  # Clear any previous error message
                
        except ValueError as temperature_error:
            self.update_error_label(str(temperature_error))

    def decrease_temp(self):   
        try:
            tempp = self.temperature.decrease_temp()
            if (tempp != float(self.entry.get())):
                target_temperature = tempp
                current_temperature = float(self.entry.get())

                # Calculate the number of steps and the step size
                num_steps = 50
                step_size = (target_temperature - current_temperature) / num_steps
                self.temperature.setTemp(target_temperature)
                
                # Schedule updates
                for step in range(1, num_steps + 1):
                    new_temperature = current_temperature + step * step_size
                    self.master.after(step * 100, functools.partial(self.update_temperature_label, new_temperature))
                
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(tempp))
                # Update the temperature label after the final step
                self.master.after((num_steps + 1) * 100, functools.partial(self.update_label, target_temperature))
                self.update_error_label("")  # Clear any previous error message
            
        except ValueError as temperature_error:
            self.update_error_label(str(temperature_error))

    def set_temperature(self):
        try:
            unit_State = self.unitState.state
            if unit_State == True:
                target_temperature = float(self.entry.get())
                current_temperature = self.temperature.getTemp()

                # Calculate the number of steps and the step size
                num_steps = 50
                step_size = (target_temperature - current_temperature) / num_steps

                self.temperature.setTemp(target_temperature)
                # Schedule updates
                for step in range(1, num_steps + 1):
                    new_temperature = current_temperature + step * step_size
                    self.master.after(step * 100, functools.partial(self.update_temperature_label, new_temperature))

                # Update the temperature label after the final step
                self.master.after((num_steps + 1) * 100, functools.partial(self.update_label, target_temperature))
                
                self.update_error_label("")  # Clear any previous error message
                self.update_info_label("")
                self.update_info_label("Temperature set successfully")
            else:
                self.update_error_label("")
                self.update_error_label("Heating and cooling units are not ON")
        except ValueError:
                self.update_error_label("Invalid input. Please enter a numeric value.")
        except Exception as BigInputError:
                self.update_error_label(str(BigInputError))           
             
    def open_heatcool_gui(self): 
        # Create a new window for the SchedulingGUI
        unit_state = self.unitState.getState()
        self.unitState.setState(not unit_state)
        heatcool_gui_window = tk.Toplevel(self.master)
        heatcool_gui = HeatCoolGUI(heatcool_gui_window)
        
    def open_energy_consumed_graph(self):
        energy_gui_window = tk.Toplevel(self.master)
        energy_gui_window = EnergyConsumedGUI(energy_gui_window)

    def toggle_emergency(self):
        if self.emergency_module.is_emergency:
            self.emergency_module.resolve_emergency()
        else:
            self.emergency_module.trigger_emergency()

        self.update_emergency_status()

        if self.emergency_module.is_emergency:
            messagebox.showwarning("Emergency Triggered", "Emergency alert sent!")
        else:
            messagebox.showinfo("Emergency Resolved", "Emergency resolved.")

    def update_emergency_status(self):
        status_text = "ON" if self.emergency_module.is_emergency else "OFF"
        self.emergency_status_label.config(text=f"Emergency Status: {status_text}", fg="red" if status_text == "ON" else "black")

        if status_text == "ON":
            self.master.configure(bg="red")  # Change window color to red when emergency is ON
        else:
            self.master.configure(bg="white")  # Change window color back to white when emergency is OFF

class HeatCoolGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("POWER HEATING/COOLING")
        self.heatcool = Heating_Cooling_Unit()
        # Set font size
        font_size = 14
        #create a heating/cooling button
        self.toggle_button = tk.Button(master, text="Power Heating/Cooling Units", command=self.toggle_visibility, font=("Helvetica", font_size))
        self.toggle_button.pack(pady=10)
        
        # Initialize boolean variable
        self.heatcool.setState(False)
        self.is_visible = self.heatcool.getState()

        self.info_label = tk.Label(master, text="", fg="blue", font=("Helvetica", font_size))
        self.info_label.pack(pady=10)

    def clear_info_label(self):
        self.info_label.config(text="")

    def update_info_label(self, message):
        self.info_label.config(text=message)
        # Schedule the info label to be cleared after 10 seconds
        self.master.after(5000, self.clear_info_label)
        
    def toggle_visibility(self):
        # Toggle the boolean value
        self.is_visible = not self.is_visible
        # Update the visibility of the hidden button
        self.update_visibility()

    def update_visibility(self):
        # Check the boolean value and update visibility accordingly
        if self.is_visible:
            self.update_info_label("")
            self.update_info_label("Heating/Cooling Units are ON")
        else:
            self.is_visible = False
            self.update_info_label("")
            self.update_info_label("Heating/Cooling Units are OFF")

class EnergyConsumedGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Energy Consumption Graph")
        self.time_interval_var = tk.StringVar()
        self.time_interval_combobox = ttk.Combobox(self.master, textvariable=self.time_interval_var,
                                                  values=["Weekly", "Monthly", "Yearly"])
        # Set a default value 
        self.time_interval_combobox.set('Select a timeline')

        # Bind the event handler to the <<ComboboxSelected>> event
        self.time_interval_combobox.bind("<<ComboboxSelected>>", self.plot_graph)

        # Create a frame for the Matplotlib plot
        self.graph_frame = tk.Frame(self.master)
                                                   
        self.time_interval_combobox.pack(pady=10)
        self.graph_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    def generate_random_data(self, time_interval):
        if time_interval == "Weekly":
            interval_list = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        elif time_interval == "Monthly":
            interval_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        elif time_interval == "Yearly":
            interval_list = [str(year) for year in range(2013, 2023)]
        else:
            return []

        data = []

        for interval in interval_list:
            energy_consumed = random.uniform(100, 1000)  # Random energy consumption between 100 and 1500 Watts
            data.append((interval, energy_consumed))

        return data

    def append_data_to_txt(self, data, filename):
        with open(filename, 'w') as txtfile:
            txtfile.write('Date,Energy Consumed (Watts)\n')  # Header
            for interval, energy in data:
                txtfile.write(f'{interval},{energy}\n')

    def plot_graph(self, event):
        time_interval = self.time_interval_var.get()

        if time_interval == "Weekly":
            filename = 'weekly_data.txt'
        elif time_interval == "Monthly":
            filename = 'monthly_data.txt'
        elif time_interval == "Yearly":
            filename = 'yearly_data.txt'
        else:
            return

        # Clear previous plot
        plt.clf()

        # Generate random data
        random_data = self.generate_random_data(time_interval)

        # Overwrite data in TXT file
        self.append_data_to_txt(random_data, filename)

        # Read data from TXT file for plotting
        intervals = []
        energy_consumed = []

        with open(filename, 'r') as txtfile:
            # Skip the first line (header)
            next(txtfile)
            for line in txtfile:
                interval, energy = line.strip().split(',')
                intervals.append(interval)
                energy_consumed.append(float(energy))

        # Plot the bar graph and clear previous plots
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
            
        # Create a figure and axis
        fig, ax = plt.subplots()
        ax.bar(intervals, energy_consumed, color='blue')
        ax.set_xlabel(f'{time_interval}')
        ax.set_ylabel('Energy Consumed (Watts)')
        ax.set_title(f'Energy Consumed {time_interval}')

        # Display the graph directly in the main window
        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

class SensorClassGUI:
    def __init__(self, root, floor_objects):
        self.root = root
        self.root.title("Building Automation System")

        # Add user authentication
        self.authenticate_user()        

        self.floor_objects = floor_objects
        self.floor_var = tk.StringVar()
        self.floor_var.set(str(self.floor_objects[0].floor_number))

        # Label for Floor Number
        self.floor_label = ttk.Label(root, text="Floor Number:")
        self.floor_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        # Dropdown for selecting floor
        self.floor_menu = ttk.Combobox(root, values=[str(floor.floor_number) for floor in self.floor_objects])
        self.floor_menu.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        self.floor_menu.current(0)
        self.floor_menu.bind("<<ComboboxSelected>>", self.read_motion_data)

        self.check_occupancy_button = ttk.Button(root, text="Check Occupancy", command=self.check_occupancy)
        self.check_occupancy_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.sensor = SensorClass(floor_objects)  # Create an instance of SensorClass

        # Sensor Reading Widgets
        self.sensor_reading_label = ttk.Label(root, text="Sensor Reading:")
        self.sensor_reading_value = ttk.Label(root, text="")
        self.time_date_label = ttk.Label(root, text="Current Time and Date:")
        self.time_date_value = ttk.Label(root, text="")

        # Real-time Monitoring Widgets
        self.real_time_label = ttk.Label(root, text="Real-Time Sensor Reading:")
        self.real_time_value = ttk.Label(root, text="")

        # Layout
        self.sensor_reading_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.sensor_reading_value.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.time_date_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.time_date_value.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        self.real_time_label.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.real_time_value.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Canvas for floor plan visualization
        self.canvas = tk.Canvas(root, width=500, height=300, bg="white")
        self.canvas.grid(row=6, column=0, columnspan=2, padx=10, pady=10, rowspan=3, sticky="w")

        # Automatically generate random data on initialization
        self.read_motion_data(None)

        # Schedule the update_sensor_reading function every 7000 milliseconds (7 seconds)
        self.root.after(7000, self.update_sensor_reading)

    def authenticate_user(self):
        # Hardcoded username and password (for demonstration purposes)
        correct_username = "admin"
        correct_password = "password"

        # Create a login window
        login_window = tk.Toplevel(self.root)
        login_window.title("Login")

        # Entry widgets for username and password
        username_label = ttk.Label(login_window, text="Username:")
        username_entry = ttk.Entry(login_window)
        password_label = ttk.Label(login_window, text="Password:")
        password_entry = ttk.Entry(login_window, show="*")

        username_label.grid(row=0, column=0, padx=10, pady=5)
        username_entry.grid(row=0, column=1, padx=10, pady=5)
        password_label.grid(row=1, column=0, padx=10, pady=5)
        password_entry.grid(row=1, column=1, padx=10, pady=5)

        # Function to check credentials
        def check_credentials():
            entered_username = username_entry.get()
            entered_password = password_entry.get()

            if entered_username == correct_username and entered_password == correct_password:
                login_window.destroy()
            else:
                messagebox.showerror("Authentication Failed", "Incorrect username or password")

        # Button to submit credentials
        submit_button = ttk.Button(login_window, text="Login", command=check_credentials)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Run the login window in a loop until it is destroyed
        login_window.wait_window()

    def draw_floor_plan(self, rooms):
        room_size = 50
        grid_spacing = 60
        floor_offset = 50

        for i, room in enumerate(rooms):
            row = i // 5
            col = i % 5
            x = col * grid_spacing + floor_offset
            y = row * grid_spacing + floor_offset

            # Draw room rectangle
            fill_color = "lightgray" if not room.motion_detected else "lightgreen"
            room_id = f"room_{row}_{col}"
            self.canvas.create_rectangle(x, y, x + room_size, y + room_size, fill=fill_color, outline="black", tags=room_id)

            # Display room number
            self.canvas.create_text(x + room_size // 2, y + room_size // 2, text=room.room_number)

    def update_floor_plan(self, selected_floor):
        self.canvas.delete("all")  # Clear the canvas
        floor = next((floor for floor in self.floor_objects if floor.floor_number == selected_floor), None)
        if floor:
            self.draw_floor_plan(floor.rooms)

    def update_real_time_floor_plan(self, selected_floor):
        floor = next((floor for floor in self.floor_objects if floor.floor_number == selected_floor), None)
        if floor:
            for i, room in enumerate(floor.rooms):
                row = i // 5
                col = i % 5
                fill_color = "lightgreen" if room.motion_detected else "lightgray"
                room_id = f"room_{row}_{col}"
                self.canvas.itemconfig(room_id, fill=fill_color)

    def read_motion_data(self, event):
        selected_floor = int(self.floor_menu.get())
        self.sensor.read_sensor_data(selected_floor)
        readings = self.sensor.get_sensor_reading()

        message = ""
        for floor_number, room_number, motion_detected, occupancy in readings:
            if floor_number == selected_floor:
                if motion_detected:
                    if isinstance(room_number, str):
                        message += f"Motion Detected in Floor {floor_number}, Room {room_number}\n"
                    else:
                        message += f"Motion Detected in Floor {floor_number}, Corridor\n"
                else:
                    message += f"No Motion in Floor {floor_number}, Room {room_number}\n"

        self.sensor_reading_value.config(text=message)

        # Update time and date label
        current_time_date = self.sensor.timestamp.strftime("%Y-%m-%d %H:%M")
        self.time_date_value.config(text=current_time_date)

        # Update the floor plan visualization
        self.update_floor_plan(selected_floor)
        # Update the real-time floor plan visualization
        self.update_real_time_floor_plan(selected_floor)

    def check_occupancy(self):
        selected_floor = int(self.floor_menu.get())
        readings = self.sensor.get_sensor_reading()

        motion_detected_rooms = [(room_number, occupancy) for floor_number, room_number, motion_detected, occupancy in readings if
                                 floor_number == selected_floor and motion_detected and isinstance(room_number, str)]

        if motion_detected_rooms:
            message = "Occupancy Information:\n"
            for room_number, occupancy in motion_detected_rooms:
                message += f"Room {room_number}: {occupancy} people\n"

            messagebox.showinfo("Occupancy Information", message)
        else:
            messagebox.showinfo("Occupancy Information", "No motion detected in any room.")

    def update_sensor_reading(self):
        selected_floor = int(self.floor_menu.get())
        self.sensor.read_sensor_data(selected_floor)
        readings = self.sensor.get_sensor_reading()

        message = "Sensor Reading:\n"
        for floor_number, room_number, motion_detected, occupancy in readings:
            if floor_number == selected_floor:
                if motion_detected:
                    if isinstance(room_number, str):
                        message += f"Motion Detected in Floor {floor_number}, Room {room_number}\n"
                    else:
                        message += f"Motion Detected in Floor {floor_number}, Corridor\n"
                else:
                    message += f"No Motion in Floor {floor_number}, Room {room_number}\n"

        self.sensor_reading_value.config(text=message)

        # Update time and date label
        current_time_date = self.sensor.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        self.time_date_value.config(text=current_time_date)

        # Update the real-time floor plan visualization
        self.update_real_time_floor_plan(selected_floor)

        # Schedule the next update after 7000 milliseconds (7 seconds)
        self.root.after(7000, self.update_sensor_reading)

class ServerManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Server Manager")
        self.master.geometry("800x700")  # Set a fixed size for the window (width x height)
        self.master.minsize(800, 700)   # Set minimum size
        self.master.maxsize(800, 700)   # Set maximum size
        self.btn_frame = tk.Frame(self.master)  # Define btn_frame as an instance variable
        self.btn_frame.pack(pady=10)
        self.servers = [Server(20, 50) for _ in range(4)]
        self.selected_server_index = tk.IntVar(value=0)
        self.server_progress_bars = []  # Initialize server_progress_bars as an empty list
        self.server_timer_labels = []   # Initialize server_timer_labels as an empty list
        self.timer_update_delay = 1000  # Timer update delay in milliseconds
        # Set the default room temperature to 20
        self.room_temperature = 20

        self.emergency_module = EmergencyModule()

        self.emergency_status_label = tk.Label(master, text="Emergency Status: OFF", fg="black")
        self.emergency_status_label.pack()

        self.emergency_button = tk.Button(master, text="Trigger Emergency", command=self.toggle_emergency)
        self.emergency_button.pack()

        #self.room_temp_label = tk.Label(self.master, text=f"Room Temperature: {self.room_temperature}")
        #self.room_temp_label.pack()

        self.process_generator = self.generate_processes()        
        
        # Flag to indicate if automatic process is running
        self.auto_process_running = False

         
        self.create_widgets()  # Create GUI elements
        self.display_server_status()  # Display initial server status
        self.check_room_temperature()  # Start checking room temperature   

    def create_widgets(self):
     # Server selection frame
     
     server_select_frame = tk.LabelFrame(self.btn_frame, text="Select Server")
     server_select_frame.pack(side=tk.RIGHT, padx=10, pady=10)  # Positioned at the bottom
      # Automatic process buttons
     auto_process_frame = tk.Frame(server_select_frame)
     auto_process_frame.pack(side=tk.TOP, padx=10, pady=10)
     
     
     # Progress bars and labels for servers
     server_frame = tk.Frame(self.master)
     server_frame.pack(side=tk.RIGHT, anchor=tk.N, padx=10, pady=10)

     add_process_button = tk.Button(self.btn_frame, text="Add Process", command=self.add_process_to_server)
     add_process_button.pack(side=tk.TOP, padx=5)

     # Add buttons for automatic process assignment and stopping
     self.start_auto_process_button = tk.Button(self.btn_frame, text="Start Automatic Process", command=self.start_auto_process)
     self.start_auto_process_button.pack(side=tk.TOP, padx=5)

     self.stop_auto_process_button = tk.Button(self.btn_frame, text="Stop Automatic Process", command=self.stop_auto_process)
     self.stop_auto_process_button.pack(side=tk.TOP, padx=5)
     self.stop_auto_process_button.config(state=tk.DISABLED)  # Initially disabled


     for i in range(4):
            tk.Radiobutton(server_select_frame, text=f"Server {i+1}", variable=self.selected_server_index,
                           value=i, command=self.display_server_status).pack(anchor=tk.W)     
    
     for i in range(4):  # Ensure to iterate over the correct number of servers
            # Create frame for each server
            server_info_frame = tk.Frame(server_frame)
            server_info_frame.grid(row=i, column=1, padx=10, pady=10)

            # Progress bar for the server
            progress_bar = tk.ttk.Progressbar(server_info_frame, orient=tk.HORIZONTAL, length=200, mode='determinate')
            progress_bar.pack()
            self.server_progress_bars.append(progress_bar)  # Append progress bars to the list

            # Countdown timer label
            timer_label = tk.Label(server_info_frame, text="")
            timer_label.pack()
            self.server_timer_labels.append(timer_label)

     self.update_progress_bars()  # Start updating progress bars
     

     #self.server_status_label = tk.Label(status_frame, text="")
     #self.server_status_label.pack()

     # Buttons for server operations
     btn_frame = tk.Frame(self.btn_frame)
     btn_frame.pack(side=tk.TOP, padx=30, pady=10)  # Positioned at the bottom

     # Action buttons
     adjust_button = tk.Button(btn_frame, text="Adjust Performance", command=self.adjust_performance)
     adjust_button.grid(row=0, column=1, padx=5, pady=5)

     add_rack_button = tk.Button(btn_frame, text="Add Rack", command=self.add_rack)
     add_rack_button.grid(row=1, column=1, padx=5, pady=5)

     remove_rack_button = tk.Button(btn_frame, text="Remove Rack", command=self.remove_rack)
     remove_rack_button.grid(row=1, column=2, padx=5, pady=5)

     add_hardware_button = tk.Button(btn_frame, text="Add Hardware to Rack", command=self.add_hardware_to_rack)
     add_hardware_button.grid(row=0, column=3, padx=5, pady=5)

     remove_hardware_button = tk.Button(btn_frame, text="Remove Hardware from Rack", command=self.remove_hardware_from_rack)
     remove_hardware_button.grid(row=0, column=2, padx=5, pady=5)

     view_logs_button = tk.Button(btn_frame, text="View Logs", command=self.view_logs)
     view_logs_button.grid(row=1, column=3, padx=5, pady=5)

     #add_process_button = tk.Button(auto_process_frame, text="Add Process", command=self.add_process_to_server)
     #add_process_button.pack(side=tk.LEFT, padx=5)

     #self.start_auto_process_button = tk.Button(auto_process_frame, text="Start Automatic Process", command=self.start_auto_process)
     #self.start_auto_process_button.pack(side=tk.LEFT, padx=5)

     #self.stop_auto_process_button = tk.Button(auto_process_frame, text="Stop Automatic Process", command=self.stop_auto_process)
     #self.stop_auto_process_button.pack(side=tk.LEFT, padx=5)
     self.stop_auto_process_button.config(state=tk.DISABLED)

     self.room_temp_label = tk.Label(server_select_frame, text=f"Room Temperature: {self.room_temperature}")
     self.room_temp_label.pack(side=tk.RIGHT)

     

     self.display_server_status()  # Display initial server status

    def generate_processes(self):
        process_index = 0
        while True:
            yield [
                Process("Process 1", 10),
                Process("Process 2", 15),
                Process("Process 3", 20),
                Process("Process 4", 25),
                Process("Process 5", 30)
            ][process_index]
            process_index = (process_index + 1) % 5  # Cycle through the list of processes


    def toggle_timer_visibility(self, server_index):
        if server_index < len(self.server_timer_labels):
            self.server_timer_labels[server_index].pack_forget()  # Hide the timer label


    def add_process_to_server(self):
        selected_index = self.selected_server_index.get()
        server = self.servers[selected_index]

        if server.allow_adding_process():
            process = next(self.process_generator)  # Get the next process from the generator

            adjusted_time = process.estimated_time / server.processing_speed

            server.add_process(process)
            self.start_timer(selected_index, adjusted_time)
            self.display_server_status()
            self.server_timer_labels[selected_index].pack()
        else:
            messagebox.showerror("Error", "Cannot add a new process. Server already has an ongoing process.")

    def update_progress_bars(self):
        for i, server in enumerate(self.servers):
            if server.processes:
                # Get the progress of the first process (assuming only one process at a time)
                progress = server.processes[0].progress
                self.server_progress_bars[i]['value'] = progress

                # Calculate the time remaining for process completion
                time_remaining = (100 - progress) * (server.processes[0].estimated_time / 100)
                time_remaining = round(time_remaining, 1)

                # Update the timer label with the time remaining
                self.server_timer_labels[i]['text'] = f"Time Left: {time_remaining} sec"

            else:
                self.server_progress_bars[i]['value'] = 0
                self.server_timer_labels[i]['text'] = ""

        self.master.after(1000, self.update_progress_bars)  # Schedule the next update after 1 second
    

    def start_timer(self, server_index, total_time):
     if server_index < len(self.server_timer_labels):
        remaining_time = total_time

        def update_timer():
         nonlocal remaining_time
         if remaining_time > 0:
            remaining_time -= 1
            # Convert seconds to 'GB' or any other unit of choice
            time_gb = remaining_time // 1024  # For example, converting seconds to 'GB'
            timer_str = f"Left to process: {time_gb} GB"
            self.server_timer_labels[server_index].config(text=timer_str)
            self.master.after(1000, update_timer)  # Schedule the next update after 1 second
         else:
             self.server_timer_labels[server_index].config(text="Left to process: 00 GB")

        update_timer()

    def view_logs(self):
     try:
        with open('server_logs.log', 'r') as log_file:
            logs = log_file.read()

        log_window = tk.Toplevel(self.master)
        log_window.title("Server Logs")

        log_text = tk.Text(log_window, height=30, width=80)
        log_text.pack()

        log_text.insert(tk.END, logs)
        log_text.config(state=tk.DISABLED)  # Disable text editing

        # Button to clear logs
        clear_logs_button = tk.Button(log_window, text="Clear Logs", command=self.clear_logs)
        clear_logs_button.pack()

     except FileNotFoundError:
        messagebox.showerror("Error", "Log file not found.")

    def clear_logs(self):
     try:
        open('server_logs.log', 'w').close()  # Clear the log file by opening in write mode, which truncates the file
        messagebox.showinfo("Logs Cleared", "Logs have been cleared.")
     except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    def start_auto_process(self):
        self.auto_process_running = True
        self.start_auto_process_button.config(state=tk.DISABLED)  # Disable the start button
        self.stop_auto_process_button.config(state=tk.NORMAL)  # Enable the stop button

        # Call a method to start automatic process assignment
        self.auto_assign_process()

    def stop_auto_process(self):
        self.auto_process_running = False
        self.stop_auto_process_button.config(state=tk.DISABLED)  # Disable the stop button
        self.start_auto_process_button.config(state=tk.NORMAL)  # Enable the start button

    def auto_assign_process(self):
        # Check if the automatic process is running
        if self.auto_process_running:
            assigned = False
            for server in self.servers:
                if not server.allow_adding_process():
                    continue  # Skip servers with ongoing processes

                selected_index = self.servers.index(server)

                process = next(self.process_generator)  # Get the next process from the generator
                adjusted_time = process.estimated_time / server.processing_speed

                server.add_process(process)
                self.start_timer(selected_index, adjusted_time)
                self.display_server_status()
                self.server_timer_labels[selected_index].pack()
                assigned = True
                break  # Exit loop once a process is assigned
         
            # Schedule the next automatic process assignment after a delay (in milliseconds)
            self.master.after(1000, self.auto_assign_process)  # Change 5000 to desired delay in milliseconds

    def add_process_to_server(self):
        if not self.auto_process_running:
            selected_index = self.selected_server_index.get()
            server = self.servers[selected_index]

            if server.allow_adding_process():
                process = next(self.process_generator)  # Get the next process from the generator

                adjusted_time = process.estimated_time / server.processing_speed

                server.add_process(process)
                self.start_timer(selected_index, adjusted_time)
                self.display_server_status()
                self.server_timer_labels[selected_index].pack()
            else:
                messagebox.showerror("Error", "Cannot add a new process. Server already has an ongoing process.")
        else:
            messagebox.showinfo("Automatic Process Running", "Automatic process assignment is currently running. Use the Stop Automatic Process button to stop.")


    def display_server_status(self):
        selected_index = self.selected_server_index.get()
        server = self.servers[selected_index]
        status = f"Server Performance: {server.processing_speed}\nServer Temperature: {server.temperature}\n\n"

        # Display racks' required speed and list hardware
        racks_info = ""
        for i, rack in enumerate(server.rack_list):
            required_speed = rack.get_required_performance_speed()
            racks_info += f"Rack {i+1} Required Speed: {required_speed}\n"
            racks_info += f"Hardware in Rack {i+1}:\n"
            for hardware in rack.get_hardware_list():
                racks_info += f"{hardware.name} (Required Speed: {hardware.required_processing_speed})\n"
            racks_info += "\n"

        # Display total required speed of all racks
        total_rack_speed = sum(rack.get_required_performance_speed() for rack in server.rack_list)
        racks_info += f"Total Required Speed of Racks: {total_rack_speed}"

        status += f"Racks Info:\n{racks_info}"
        #self.server_status_label.config(text=status)
        self.update_progress_bars()  # Start updating progress bars
        # Update the server status using a Text widget within a Scrollbar
        if hasattr(self, 'server_status_text'):
            self.server_status_text.config(state=tk.NORMAL)
            self.server_status_text.delete(1.0, tk.END)
            self.server_status_text.insert(tk.END, status)
            self.server_status_text.config(state=tk.DISABLED)
        else:
            status_frame = tk.LabelFrame(self.master, text="Server Status")
            status_frame.pack(side=tk.TOP, padx=10, pady=10)  # Positioned at the top

            scrollbar = tk.Scrollbar(status_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            self.server_status_text = tk.Text(status_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
            self.server_status_text.pack(expand=True, fill=tk.BOTH)
            self.server_status_text.insert(tk.END, status)
            self.server_status_text.config(state=tk.DISABLED)

            scrollbar.config(command=self.server_status_text.yview)

    def adjust_performance(self):
        selected_index = self.selected_server_index.get()
        new_speed = int(tk.simpledialog.askstring("Adjust Performance", "Enter new processing speed:"))
        self.servers[selected_index].adjust_performance(new_speed)
        self.display_server_status()


    def add_rack(self):
     selected_index = self.selected_server_index.get()
     server = self.servers[selected_index]

     if len(server.rack_list) < 8:
        server.add_rack()
        self.display_server_status()  # Force GUI update after adding a rack
     else:
        messagebox.showerror("Error", "Maximum rack limit reached.")

    def remove_rack(self):
        selected_index = self.selected_server_index.get()
        server = self.servers[selected_index]
        
        if len(server.rack_list) > 1:
            server.remove_rack()
            self.display_server_status()
        else:
            messagebox.showerror("Error", "Server must have at least one rack.")

    def add_hardware_to_rack(self):
        selected_index = self.selected_server_index.get()
        num_racks = len(self.servers[selected_index].rack_list)
        rack_index = int(tk.simpledialog.askstring("Add Hardware", f"Enter rack index (1 to {num_racks}):"))

        if 1 <= rack_index <= num_racks:
            preset_hardware = [
                Hardware("CPU", 20),
                Hardware("RAM", 10),
                Hardware("Storage", 15),
                Hardware("Network Card", 5),
                Hardware("GPU", 30)
            ]

            hardware_choices = "\n".join(f"{i + 1}. {preset_hardware[i].name} (Required Speed: {preset_hardware[i].required_processing_speed})"
                                         for i in range(len(preset_hardware)))

            hardware_choice = simpledialog.askinteger("Select Hardware", f"Preset Hardware Options:\n{hardware_choices}\nEnter hardware choice:")
            quantity = simpledialog.askinteger("Enter Quantity", "Enter the quantity of hardware to add:")

            if 1 <= hardware_choice <= len(preset_hardware) and quantity is not None and quantity > 0:
                selected_hardware = preset_hardware[hardware_choice - 1]
                server = self.servers[selected_index]

                # Store current server speed
                current_speed = server.processing_speed

                # Add hardware to the specified rack
                for _ in range(quantity):
                    server.add_hardware_to_rack(rack_index - 1, selected_hardware)  # Adjust rack_index to 0-based indexing

                # Check if the total required speed exceeds the current server speed
                if sum(rack.get_required_performance_speed() for rack in server.rack_list) > current_speed:
                    messagebox.showwarning("Speed Adjustment Required", "The combined required speed of racks exceeds the current server speed. Please readjust the server speed.")

                self.display_server_status()
                messagebox.showinfo("Success", f"Successfully added {quantity} {selected_hardware.name}(s) to Rack {rack_index}")  # Display success message
            else:
                messagebox.showerror("Error", "Invalid hardware choice or quantity. Please choose a valid hardware and quantity.")
        else:
            messagebox.showerror("Error", f"Invalid rack index. Please enter a valid rack index (1 to {num_racks}).")

    def remove_hardware_from_rack(self):
        selected_index = self.selected_server_index.get()
        rack_index = int(tk.simpledialog.askstring("Remove Hardware", "Enter rack index:"))

        server = self.servers[selected_index]

        if 0 <= rack_index - 1 < len(server.rack_list):
         rack = server.rack_list[rack_index - 1]
         if not rack.is_empty():
            server.remove_hardware_from_rack(rack_index - 1)
            self.display_server_status()
         else:
            messagebox.showerror("Error", "There is no hardware to be removed from the rack. The rack is empty.")
        else:
         print("Invalid rack index.")

    def check_room_temperature(self):
        # Calculate the total temperature as the sum of server temperatures divided by 4
        total_temp = sum(server.temperature / 4 for server in self.servers)

        # Update the label with the current room temperature
        self.room_temperature = total_temp  # Set room temperature to the calculated total
        self.room_temp_label.config(text=f"Room Temperature: {self.room_temperature}")

        self.master.after(1000, self.check_room_temperature)  # Check every 1 second

    def update_room_temperature(self):
        # Calculate the room temperature based on server temperatures
        total_temp = sum(server.temperature for server in self.servers)
        self.room_temperature = total_temp
        self.room_temp_label.config(text=f"Room Temperature: {self.room_temperature}")

    def load_state(self):
        if os.path.exists("server_state.txt"):
            with open("server_state.txt", "r") as file:
                lines = file.readlines()
                servers_data = []
                selected_server_index = 0

                i = 0
                while i < len(lines):
                    processing_speed, temperature = map(int, lines[i].split())
                    racks = []

                    i += 1
                    while lines[i].strip() != "-1":
                        hardware_name, required_processing_speed = lines[i].split()
                        racks.append(Hardware(hardware_name, int(required_processing_speed)))
                        i += 1

                    i += 1  # Move to the next line after "-1"

                    if i < len(lines) and lines[i].strip() != "-1":
                        selected_server_index = int(lines[i])
                    else:
                        selected_server_index = 0

                    server = Server(processing_speed, temperature)
                    for rack in racks:
                        server.add_hardware_to_rack(racks.index(rack), rack)
                    servers_data.append(server)

                    i += 1  # Move to the next server data or EOF

                self.servers = servers_data
                self.selected_server_index = tk.IntVar(value=selected_server_index)
                print("State loaded successfully.")
        else:
            print("No saved state found. Starting with default state.")

    def save_state(self):
        with open("server_state.txt", "w") as file:
            for i, server in enumerate(self.servers):
                file.write(f"{server.processing_speed} {server.temperature}\n")
                for rack in server.rack_list:
                    for hardware in rack.get_hardware_list():
                        file.write(f"{hardware.name} {hardware.required_processing_speed}\n")
                    file.write("-1\n")  # Separator for racks
                file.write("-1\n")  # Separator for servers
                if i == self.selected_server_index.get():
                    file.write(f"{i}\n")

            print("State saved successfully.")

    def toggle_emergency(self):
        if self.emergency_module.is_emergency:
            self.emergency_module.resolve_emergency()
        else:
            self.emergency_module.trigger_emergency()

        self.update_emergency_status()

        if self.emergency_module.is_emergency:
            messagebox.showwarning("Emergency Triggered", "Emergency alert sent!")
        else:
            messagebox.showinfo("Emergency Resolved", "Emergency resolved.")

    def update_emergency_status(self):
        status_text = "ON" if self.emergency_module.is_emergency else "OFF"
        self.emergency_status_label.config(text=f"Emergency Status: {status_text}", fg="red" if status_text == "ON" else "black")

        if status_text == "ON":
            self.master.configure(bg="red")  # Change window color to red when emergency is ON
        else:
            self.master.configure(bg="white")  # Change window color back to white when emergency is OFF

class VentilationGUI:
    ALLOWED_FLOORS = [str(i) for i in range(1, 5)]
    ALLOWED_ROOMS = [chr(i) for i in range(ord('a'), ord('e') + 1)]

    def __init__(self, master):
        self.master = master
        font_size = 12
        self.floor_var = tk.StringVar()
        self.room_var = tk.StringVar()
        self.floor_var.set("1")
        self.room_var.set("a")

        self.ventilation_modules = {}
        self.current_key = None

        self.master.title("Home Control")
        self.master.geometry("400x200")
        self.emergency_module = EmergencyModule()

        self.setup_user()
        
        #creating a button for energy graph
        self.energy_button = tk.Button(master, text='Energy Graph', command=self.open_energy_consumed_graph, font=("Helvetica", font_size))
        # Pack the button to the top-left corner
        self.energy_button.pack(side=tk.LEFT, anchor=tk.NW)
        
        self.room_info_label = tk.Label(master, text=f"Floor: {self.floor_var.get()}, Room: {self.room_var.get()}")
        self.room_info_label.pack()

        self.change_room_button = tk.Button(master, text="Change Room", command=self.change_room)
        self.change_room_button.pack()

        self.ventilation_button = tk.Button(master, text="Ventilation", command=self.open_ventilation_control)
        self.ventilation_button.pack()

        self.lights_button = tk.Button(master, text="Lights", command=self.open_lighting_control)
        self.lights_button.pack()


        self.emergency_status_label = tk.Label(master, text="Emergency Status: OFF", fg="black")
        self.emergency_status_label.pack()

        self.emergency_button = tk.Button(master, text="Trigger/Resolve Emergency", command=self.toggle_emergency)
        self.emergency_button.pack()

    def open_energy_consumed_graph(self):
        energy_gui_window = tk.Toplevel(self.master)
        energy_gui_window = EnergyConsumedGUI(energy_gui_window)

    def toggle_emergency(self):
        if self.emergency_module.is_emergency:
            self.emergency_module.resolve_emergency()
        else:
            self.emergency_module.trigger_emergency()

        self.update_emergency_status()

        if self.emergency_module.is_emergency:
            messagebox.showwarning("Emergency Triggered", "Emergency alert sent!")
        else:
            messagebox.showinfo("Emergency Resolved", "Emergency resolved.")

    def update_emergency_status(self):
        status_text = "ON" if self.emergency_module.is_emergency else "OFF"
        self.emergency_status_label.config(text=f"Emergency Status: {status_text}", fg="red" if status_text == "ON" else "black")

        if status_text == "ON":
            self.master.configure(bg="red")  # Change window color to red when emergency is ON
        else:
            self.master.configure(bg="white")  # Change window color back to white when emergency is OFF    

    def setup_user(self):
        floor_input = simpledialog.askstring("Enter Floor", "Enter the floor number (1-4):", initialvalue=self.floor_var.get())
        if floor_input is None:
            messagebox.showwarning("Warning", "Floor selection canceled. Exiting.")
            self.master.destroy()
            return

        room_input = simpledialog.askstring("Enter Room Number", "Enter the room number (a-e):", initialvalue=self.room_var.get())
        if room_input is None:
            messagebox.showwarning("Warning", "Room selection canceled. Exiting.")
            self.master.destroy()
            return

        if floor_input in self.ALLOWED_FLOORS and room_input in self.ALLOWED_ROOMS:
            self.floor_var.set(floor_input)
            self.room_var.set(room_input)
            self.current_key = (self.floor_var.get(), self.room_var.get())
            ventilation_module = Ventilation(self.floor_var.get(), self.room_var.get())
            lighting_module = LightingModule()
            self.ventilation_modules[self.current_key] = {'ventilation': ventilation_module, 'lighting': lighting_module}
        else:
            messagebox.showerror("Error", "Invalid floor or room. Exiting.")
            self.master.destroy()

    def open_ventilation_control(self):
        current_module = self.get_current_module()
        if current_module is None:
            messagebox.showwarning("Warning", "No module selected. Please select a room first.")
            return

        self.master.withdraw()
        ventilation_control_window = VentilationControlWindow(self.master, current_module['ventilation'], self.ventilation_modules)
        ventilation_control_window.protocol("WM_DELETE_WINDOW", self.on_control_window_close)
        ventilation_control_window.mainloop()
        self.master.deiconify()

    def open_lighting_control(self):
        current_module = self.get_current_module()
        if current_module is None:
            messagebox.showwarning("Warning", "No module selected. Please select a room first.")
            return

        self.master.withdraw()
        lighting_control_window = LightingControlWindow(self.master, current_module['lighting'])
        lighting_control_window.protocol("WM_DELETE_WINDOW", self.on_control_window_close)
        lighting_control_window.mainloop()
        self.master.deiconify()

    def on_control_window_close(self):
        if self.master:
            self.master.deiconify()

    def get_current_module(self):
        return self.ventilation_modules.get(self.current_key)

    def on_room_selected(self, event):
        self.current_key = (self.floor_var.get(), self.room_var.get())
        self.room_info_label.config(text=f"Floor: {self.floor_var.get()}, Room: {self.room_var.get()}")
        current_module = self.get_current_module()
        if current_module:
            ventilation_status_text = "On" if current_module['ventilation'].get_ventilation_status() else "Off"
            print(f"Ventilation in room {self.current_key} - {ventilation_status_text}")

    def change_room(self):
        self.master.withdraw()
        self.setup_user()
        self.room_info_label.config(text=f"Floor: {self.floor_var.get()}, Room: {self.room_var.get()}")
        current_module = self.get_current_module()
        if current_module:
            ventilation_status_text = "On" if current_module['ventilation'].get_ventilation_status() else "Off"
            print(f"Ventilation in room {self.current_key} - {ventilation_status_text}")
        self.master.deiconify()

class VentilationControlWindow(tk.Toplevel):
    def __init__(self, master, ventilation_module, ventilation_modules):
        tk.Toplevel.__init__(self, master)
        self.title("Ventilation Control")
        self.geometry("300x200")

        self.ventilation_module = ventilation_module
        self.ventilation_modules = ventilation_modules

        self.ventilation_status_label = tk.Label(self, text="")
        self.ventilation_status_label.pack()

        self.toggle_button = tk.Button(self, text="Toggle Ventilation", command=self.toggle_ventilation)
        self.toggle_button.pack()

        self.ventilation_modes_button = tk.Button(self, text="Ventilation Modes", command=self.open_ventilation_modes)
        self.ventilation_modes_button.pack()

        self.ventilation_status_button = tk.Button(self, text="Ventilation Status", command=self.open_ventilation_status)
        self.ventilation_status_button.pack()

    def toggle_ventilation(self):
        ventilation_status = self.ventilation_module.toggle_ventilation()
        status_text = "On" if ventilation_status else "Off"
        self.ventilation_status_label.config(text=f"Ventilation Status: {status_text}")

    def open_ventilation_modes(self):
        if self.ventilation_module.get_ventilation_status():
            self.master.withdraw()
            ventilation_modes_window = VentilationModesWindow(self.master, self.ventilation_module)
            ventilation_modes_window.protocol("WM_DELETE_WINDOW", self.on_modes_window_close)
            ventilation_modes_window.mainloop()
            self.master.deiconify()
        else:
            messagebox.showwarning("Warning", "Cannot change ventilation modes when ventilation is off.")

    def open_ventilation_status(self):
        ventilated_rooms = [key for key, modules in self.ventilation_modules.items() if
                            modules['ventilation'].get_ventilation_status()]

        ventilated_rooms_str = ", ".join([f"{key[0]}{key[1]}" for key in ventilated_rooms])
        messagebox.showinfo("Ventilation Status", f"Rooms with Ventilation On: {ventilated_rooms_str}")

    def on_modes_window_close(self):
        if self.master:
            self.master.deiconify()

class VentilationModesWindow(tk.Toplevel):
    def __init__(self, master, ventilation_module):
        tk.Toplevel.__init__(self, master)
        self.title("Ventilation Modes")
        self.geometry("300x200")

        self.ventilation_module = ventilation_module
        self.mode_var = tk.StringVar()
        self.mode_var.set(self.ventilation_module.get_hvac_mode_as_string())

        self.mode_combobox = ttk.Combobox(self, textvariable=self.mode_var, values=[
            HVACMode.Ventilation, HVACMode.FanOnly, HVACMode.Auto, HVACMode.AC])
        self.mode_combobox.pack()

        self.set_mode_button = tk.Button(self, text="Set Mode", command=self.set_ventilation_mode)
        self.set_mode_button.pack()

    def set_ventilation_mode(self):
        new_mode = self.mode_var.get()
        try:
            self.ventilation_module.set_hvac_mode(new_mode)
            messagebox.showinfo("Mode Change", f"Ventilation mode in room {self.ventilation_module.floor}-{self.ventilation_module.room_number} changed to {new_mode}")
            self.destroy()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

class LightingControlWindow(tk.Toplevel):
    def __init__(self, master, lighting_module):
        tk.Toplevel.__init__(self, master)
        self.title("Lighting Control")
        self.geometry("300x200")

        self.lighting_module = lighting_module

        self.status_label = tk.Label(self, text=f"Lighting Status: {'On' if self.lighting_module.is_light_on else 'Off'}")
        self.status_label.pack()

        self.toggle_button = tk.Button(self, text="Toggle Lighting", command=self.toggle_lighting)
        self.toggle_button.pack()

    def toggle_lighting(self):
        self.lighting_module.toggle_light()
        status_text = "On" if self.lighting_module.is_light_on else "Off"
        self.status_label.config(text=f"Lighting Status: {status_text}")

class SecurityGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Security System")
        self.security_system = SecurityModule()
        self.logged_in = False  # Flag to track login status
        self.load_security_personnel()
        self.load_camera_locations()
        self.load_user_profiles()

        self.login_button = tk.Button(root, text="Login", command=self.show_login)
        self.login_button.pack()

        # Create a text widget to display function returns
        self.terminal_text = tk.Text(root, height=10, width=80)
        self.terminal_text.pack()

        # Initialize create_profile_button
        self.create_profile_button = tk.Button(root, text="Create Profile", command=self.create_profile)
        self.create_profile_button.pack()
         # Initialize attribute placeholders for buttons
        self.add_personnel_button = None
        self.remove_personnel_button = None
        self.add_camera_button = None
        self.display_personnel_button = None
        self.display_camera_feeds_button = None
        self.create_profile_button = None
        self.view_profiles_button = None

        self.toggle_function_buttons(False)  # Initially hide function buttons
    
    def toggle_function_buttons(self, state):
        buttons = [
            self.add_personnel_button,
            self.remove_personnel_button,
            self.add_camera_button,
            self.display_personnel_button,
            self.display_camera_feeds_button,
            self.create_profile_button
        ]
        for button in buttons:
            if button is not None:  # Check if the button is not None
                if state:
                    button.pack()  # Show buttons
                else:
                    button.pack_forget()  # Hide buttons

    def load_security_personnel(self):
        self.security_system.load_security_personnel_from_file()

    def load_camera_locations(self):
        self.security_system.load_camera_locations_from_file()

    def load_user_profiles(self):
        self.security_system.load_user_profiles()

    def show_login(self):
     username = simpledialog.askstring("Login", "Enter username:")
     password = simpledialog.askstring("Login", "Enter password:", show='*') if username else None

     if username and password:
        if self.security_system.login_user(username, password):
            self.logged_in = True
            self.show_main_menu()
        else:
            if username in self.security_system.user_profiles:
                messagebox.showinfo("Login Failed", "Incorrect password. Please try again.")
            else:
                create_profile = messagebox.askyesno("Profile Not Found", "Profile not found. Create a new profile?")
                if create_profile:
                    self.create_user_profile(username, password)
                    self.logged_in = True
                    self.show_main_menu()
                else:
                    messagebox.showinfo("Login Failed", "Login failed. Try again.")

    def create_user_profile(self, username, password):
        self.security_system.create_user_profile(username, password) 

    def show_main_menu(self):
        self.login_button.pack_forget()

        # Hide create profile button if logged in
        if self.create_profile_button:
         self.create_profile_button.pack_forget()

        # Hide the button if the user is logged in and it's not needed in the main menu
        if self.logged_in and self.create_profile_button:
         self.create_profile_button.pack_forget()
        else:
         # Add a button to create a profile during login if it doesn't exist
         self.create_profile_button = tk.Button(self.root, text="Create Profile", command=self.create_profile)
         self.create_profile_button.pack()

       # Hide the button if the user is logged in and it's not needed in the main menu
        if self.logged_in and self.create_profile_button:
         self.create_profile_button.pack_forget()

        self.add_personnel_button = tk.Button(self.root, text="Add Security Personnel", command=self.add_security_personnel)
        self.add_personnel_button.pack()

        self.remove_personnel_button = tk.Button(self.root, text="Remove Security Personnel", command=self.remove_security_personnel)
        self.remove_personnel_button.pack()

        self.add_camera_button = tk.Button(self.root, text="Add Virtual Camera", command=self.add_virtual_camera)
        self.add_camera_button.pack()

        self.display_personnel_button = tk.Button(self.root, text="Display Security Personnel", command=self.display_security_personnel)
        self.display_personnel_button.pack()

        self.display_camera_feeds_button = tk.Button(self.root, text="Display Camera Feeds", command=self.display_camera_feeds)
        self.display_camera_feeds_button.pack()

        # Add a button to view stored profiles
        self.view_profiles_button = tk.Button(self.root, text="View Stored Profiles", command=self.view_stored_profiles)
        self.view_profiles_button.pack()

        # Add a button to remove a stored profile
        self.remove_profile_button = tk.Button(self.root, text="Remove Profile", command=self.remove_profile)
        self.remove_profile_button.pack()

        # Add a button to remove a camera location
        self.remove_camera_button = tk.Button(self.root, text="Remove Camera Location", command=self.remove_camera_location)
        self.remove_camera_button.pack()

    def create_profile(self):
        username = simpledialog.askstring("Create Profile", "Enter new username:")
        password = simpledialog.askstring("Create Profile", "Enter new password:", show='*') if username else None

        if username and password:
            if username in self.security_system.user_profiles:
                 messagebox.showinfo("Username Exists", "Username already exists. Please choose a different username.")
            else:
                self.create_user_profile(username, password)
                self.display_terminal_output("Profile Created", "New profile created successfully.")

    def remove_profile(self):
        username = simpledialog.askstring("Remove Profile", "Enter the username of the profile to remove:")
        if username:
            removed = self.security_system.remove_user_profile(username)
            if removed:
                self.display_terminal_output("Profile Removed", f"Profile '{username}' has been removed successfully.")
            else:
                self.display_terminal_output("Profile Not Found", f"Profile '{username}' not found.")

    def view_stored_profiles(self):
        stored_profiles = "\n".join(f"Username: {username}, Password: {password}" for username, password in self.security_system.user_profiles.items())
        self.display_terminal_output("Stored Profiles: ", f"\n{stored_profiles}")

    def show_login_screen(self):
        self.login_button = tk.Button(self.root, text="Login", command=self.user_login)
        self.login_button.pack()

    def hide_login_screen(self):
        self.login_button.pack_forget()

    def add_security_personnel(self):
        name = simpledialog.askstring("Add Security Personnel", "Enter personnel name:")
        role = simpledialog.askstring("Add Security Personnel", "Enter personnel role:")
        if name and role:
            if self.validate_name(name):
                new_personnel = SecurityPersonnel()
                new_personnel.name = name
                new_personnel.role = role
                self.security_system.add_security_personnel(new_personnel)
                self.display_terminal_output("Success", "Security personnel added successfully.")
            else:
                self.display_terminal_output("Invalid Name", "Name should only contain alphabets and spaces.")

    def validate_name(self, name):
        # Check if the name contains only alphabets and spaces
        return all(char.isalpha() or char.isspace() for char in name)

    def remove_security_personnel(self):
        name = simpledialog.askstring("Remove Security Personnel", "Enter the name of personnel to remove:")
        if name:
            self.security_system.remove_security_personnel(name)
            self.display_terminal_output("Success", "Security personnel removed successfully.")

    def add_virtual_camera(self):
        location = simpledialog.askstring("Add Virtual Camera", "Enter camera location:")
        if location:
            if location in self.security_system.virtual_camera_list:
                self.display_terminal_output("Location Exists", "Location already exists. Please enter a different location name.")
            else:
                self.security_system.add_virtual_camera(location)
                self.display_terminal_output("Success", "Virtual camera added successfully.")

    def remove_camera_location(self):
        location = simpledialog.askstring("Remove Camera Location", "Enter the camera location to remove:")
        if location:
            if location in self.security_system.virtual_camera_list:
                self.security_system.virtual_camera_list.remove(location)
                self.security_system.save_camera_locations_to_file()
                self.display_terminal_output("Success", "Camera location removed successfully.")
            else:
                self.display_terminal_output("Not Found", "Camera location not found.")    

    def display_security_personnel(self):
        self.display_terminal_output("Security Personnel", "Displaying Security Personnel:\n")
        for personnel in self.security_system.personnel_list:
            personnel_info = f"Name: {personnel.name}, Role: {personnel.role}\n"
            self.display_terminal_output("Security Personnel", personnel_info)

    def display_camera_feeds(self):
        if not self.security_system.virtual_camera_list:
            self.display_terminal_output("No Entries", "There are no camera locations.")
        else:
            camera_feeds_text = "Camera Feeds:\n"
            for camera in self.security_system.virtual_camera_list:
                camera_feed = self.security_system.generate_camera_feed(camera)
                camera_feeds_text += camera_feed + "\n"
            
            self.display_terminal_output("", camera_feeds_text)

    def display_terminal_output(self, title, message):
        self.terminal_text.insert(tk.END, f"{title}\n{message}\n\n")
        self.terminal_text.see(tk.END)
        
class MainPageGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Page")

        # Set font size
        font_size = 12

        # Create and place widgets for the main page
        self.label = tk.Label(master, text="THE BUILDING AUTOMATION SYSTEM MAIN HOME PAGE", fg="green", font=("Helvetica", font_size))
        self.label.pack(pady=10)

        # Create a button to open the TemperatureGUI
        self.temperature_button = tk.Button(master, text="Heating/Cooling Units", command=self.open_temperature_gui, font=("Helvetica", font_size))
        self.temperature_button.pack(pady=10)

        # Create a button to open the VentilationGUI
        self.vent_button = tk.Button(master, text="Air Vents", command=self.open_ventilation_gui, font=("Helvetica", font_size))
        self.vent_button.pack(pady=10)

        # Create a button to open the MotionDetectionGUI
        self.motion_button = tk.Button(master, text="Sensors", command=self.monitor_motion_detection, font=("Helvetica", font_size))
        self.motion_button.pack(pady=10)

        #Create button to open server room
        self.serverroom_button = tk.Button(master, text="Server Room", command=self.open_serverroom_gui, font=("Helvetica", font_size))
        self.serverroom_button.pack(pady=10)

        #Create button to open security
        self.security_button = tk.Button(master, text="Security", command=self.open_security_gui, font=("Helvetica", font_size))
        self.security_button.pack(pady=10)
        
        # Center the widgets vertically and horizontally
        for widget in [self.label, self.temperature_button, self.vent_button, self.motion_button, self.serverroom_button, self.security_button]:
            widget.pack(side="top", fill="both", expand=True)

    def open_temperature_gui(self): 
        # Create a new window for the TemperatureGUI
        temperature_gui_window = tk.Toplevel(self.master)
        temperature_gui = TemperatureGUI(temperature_gui_window)

    def open_ventilation_gui(self):
        vent_gui_window = tk.Toplevel(self.master)
        vent_gui_window = VentilationGUI(vent_gui_window)

    def monitor_motion_detection(self):
        # Define the building structure with 4 floors and 5 rooms on each floor
        floors = [Floor(i, 5) for i in range(1, 5)]
        motion_detection_window = tk.Toplevel(self.master)
        motion_detection_window = SensorClassGUI(motion_detection_window, floors)

    def open_serverroom_gui(self):
        serverroom_gui_window = tk.Toplevel(self.master)
        serverroom_gui = ServerManagerApp(serverroom_gui_window)
        serverroom_gui.display_server_status()

    def open_security_gui(self):
        security_gui_window = tk.Toplevel(self.master)
        security_gui = SecurityGUI(security_gui_window)

if __name__ == "__main__":
    root = tk.Tk()
    font_size_main_window = 11
    root.option_add("*Font", f"Helvetica {font_size_main_window}")
    app = MainPageGUI(root)
    root.mainloop()
