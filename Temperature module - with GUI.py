DAYS_IN_A_MONTH = 31
DAYS_IN_A_WEEK = 7
MONTHS_IN_A_YEAR = 12
ENERGY_RATE = 2.8
from datetime import datetime, date, timedelta
import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from dateutil.relativedelta import relativedelta
import tkinter as tk
from tkinter import simpledialog, messagebox

def get_current_day_of_the_week():
    current_date_time = datetime.now().date() #get current date
    day_of_week = current_date.weekday() # Use weekday() method to get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # A list of days of the week
    return days_of_week[day_of_week]

def get_todays_date():
    return date.today()

def get_current_time():
    current_time = datetime.now().time()
    formatted_time = current_time.strftime("%H:%M")
    return formatted_time


def calculate_new_date(days_to_add):
    # Get the current date and time
    current_date = datetime.now().date()
    # Calculate the new date by adding days_to_add to the current date
    new_date = current_date + timedelta(days_to_add)
    return new_date

def calculate_months (months_to_add):
    # Get the current date
    current_date = datetime.now().date()
    # Create a relativedelta representing three months
    months = relativedelta(months_to_add)
    # Calculate the date months from now
    future_date_months = current_date + months
  
class Temperature:
    def __init__(self):
        self.tempDegree = 0
        self.serverTemp = 0

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
    #FOR SERVER ROOM
    def OverheatingServer(self, degree):
        self.serverTemp = degree
        if (self.serverTemp >= 60):
            raise Exception ("EMERGENCY!!!!!! EMERGENCY!!!!!!")

    def setServerTemp(self, celsius_degree):
        self.serverTemp = celsius_degree

    def getSensorTemp(self):
        return self.serverTemp

    def increase_server_temp(self):
        self.serverTemp += 1
        if self.serverTemp <= 100:
            return self.serverTemp

    def decrease_server_temp(self):
        self.serverTemp -= 1
        if self.serverTemp >= 20:
             return self.serverTemp

    
class Heating_Cooling_Unit(Temperature):
    def __init__(self):
        super().__init__()
        self.state = False
    
    def setState(self, status):
        self.state = status
    
    def getState(self):
        return self.state

class Scheduling():
    def __init__(self):
        self.secondsTimer = 0
        self.minutesTimeFrame = 0
        self.secondsLeft = 0

    def getSecondsLeft(self, TimeLeft = 0): #the seconds running as minutes pass
        self.secondsLeft = TimeLeft
        return self.secondsLeft

    def getTimerInSeconds(self, timedIntervals = 0):
        self.secondsTimer = timedIntervals
        #if timedIntervals <= 60:
        return self.secondsTimer

    def getTimeFrameInMinutes(self, timeframe = 0):
        self.minutesTimeFrame = timeframe
        return self.minutesTimeFrame


def minutes_to_sec_converter(mins):
    MinToSec = mins * 60
    return MinToSec

def save_to_txt_file(): #COME BACK TO THE POSSIBILITY OF THIS
    pass #self, Date = 0, avg_ec = 0, Min_frame = 0, Sec_timer = 0,): 
##        Avg_EC = avg_ec
##        date = Date
##        mins_frame = Min_frame
##        sec_timer = Sec_timer
    
class EnergyConsumption(Scheduling):
    def __init__(self):
        super().__init__()
        self.Energy_Consumed_In_A_Week_From_Temp = [0] * DAYS_IN_A_WEEK
        self.Energy_Consumed_In_A_Month_From_Temp = [0] * DAYS_IN_A_MONTH
        self.Energy_Consumed_In_A_Year_From_Temp = [0] * MONTHS_IN_A_YEAR

    def AverageEnergyConsumed(self, Tmins = 0 , Usecs = 0):
        T_in_secs = minutes_to_sec_converter(Tmins)
        M = (T_in_secs + Usecs)/ENERGY_RATE
        E = round(M, 2)
        return E

    def monitor_energy_table(self, txt_file): #table using dataframes
        #data frame
        dataframe = pd.DataFrame()
        # Add columns to the DataFrame using dictionaries
        column1 = {'Date': None,
                   'Energy Consumed': None,
                   'Duration (min)': None,
                   'Runtime (sec)': None}

        #read text file to temporary data frame
        temp_df = pd.read_csv(txt_file, sep=',')
        #append temporary dataframe to the existing one
        dataframe = dataframe._append(temp_df, ignore_index = True)

        return dataframe

##    def displayWeeklyConsumption(self):
##        pass
##
##    def displayMonthlyConsumption(self):
##        pass
##
##    def displayYearlyConsumption(self):
##        pass
    

class TemperatureGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Heating/Cooling Control")

        self.temperature = Temperature()
        # Set font size
        font_size = 14

        #creating a button for energy graph
        self.energy_button = tk.Button(master, text='Energy Graph', command=self.open_energy_consumed_graph, font=("Helvetica", font_size))
        # Pack the button to the top-left corner
        self.energy_button.pack(side=tk.LEFT, anchor=tk.NW)

        #ON HEATING/COOLING UNITS
        # A button to power on the Heating/Cooling Units
        self.heatcool_button = tk.Button(master, text="Press to Power-On Heaters/Coolers", command=self.open_heatcool_gui, font=("Helvetica", font_size))
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
        
        # A button to open the SchedulingGUI
        self.scheduling_button = tk.Button(master, text="Schedule Heating/Cooling Units", command=self.open_scheduling_gui, font=("Helvetica", font_size))
        self.scheduling_button.pack(pady=10)

        # Centralize widgets
        for widget in [self.label, self.error_label, self.increase_button, self.decrease_button, self.label_prompt, self.entry, self.set_button]:
            widget.pack(side="top", fill="both", expand=True)

        
    def update_label(self):
        self.label.config(text=f"Current Temperature: {self.temperature.getTemp()}°C")

    def clear_error_label(self):
        self.error_label.config(text="")

    def update_error_label(self, message):
        self.error_label.config(text=message)
        # Schedule the error label to be cleared after 10 seconds
        self.master.after(5000, self.clear_error_label)

    def increase_temp(self):
        try:
            tempp = self.temperature.increase_temp()
            if (tempp != float(self.entry.get())):
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(tempp))
                self.update_error_label("")  # Clear any previous error message
        except ValueError as temperature_error:
            self.update_error_label(str(temperature_error))

    def decrease_temp(self):   
        try:
            tempp = self.temperature.decrease_temp()
            if (tempp != float(self.entry.get())):
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(tempp))
                self.update_error_label("")  # Clear any previous error message
        except ValueError as temperature_error:
            self.update_error_label(str(temperature_error))

    def set_temperature(self):
        try:
            temperature_value = float(self.entry.get())
            self.temperature.setTemp(temperature_value)
            self.update_label()
            self.update_error_label("")  # Clear any previous error message
        except ValueError:
             self.update_error_label("Invalid input. Please enter a numeric value.")
        except Exception as BigInputError:
             self.update_error_label(str(BigInputError))

    def overheating(self):
        try:
            overheating = self.temperature.OverheatingServer()
        except Exception as Fire:
            self.update_error_label(str(Fire))
            
             
    def open_heatcool_gui(self): 
        # Create a new window for the SchedulingGUI
        heatcool_gui_window = tk.Toplevel(self.master)
        heatcool_gui = HeatCoolGUI(heatcool_gui_window)

    def open_scheduling_gui(self): 
        # Create a new window for the SchedulingGUI
        scheduling_gui_window = tk.Toplevel(self.master)
        scheduling_gui = SchedulingGUI(scheduling_gui_window)

    def open_energy_consumed_graph(self):
        energy_gui_window = tk.Toplevel(self.master)
        energy_gui_window = EnergyConsumedGUI(energy_gui_window)

            
class HeatCoolGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("POWER HEATING/COOLING")
        self.heatcool = Heating_Cooling_Unit()
        # Set font size
        font_size = 14
        #create a heating/cooling button
        self.toggle_button = tk.Button(master, text="ON Heating/Cooling Units", command=self.toggle_visibility, font=("Helvetica", font_size))
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
            self.update_info_label("")
            self.update_info_label("Heating/Cooling Units are ON")
    

class SchedulingGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Scheduling Units")
        self.sch = Scheduling()
        font_size = 14
        self.timer_running = False
        self.minutesFrame = self.sch.getTimeFrameInMinutes()
        self.secTimer = self.sch.getTimerInSeconds()
        self.secLeft = self.sch.getSecondsLeft()
        
        # Create and place widgets
        #for seconds
        self.label = tk.Label(master, text="Timer: 0 seconds")
        self.label.pack(pady=10)
        
        self.start_button = tk.Button(master, text="Start Timer", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop Timer", command=self.stop_timer)
        self.stop_button.pack(pady=10)

        self.set_time_button = tk.Button(master, text="Set Time", command=self.set_time)
        self.set_time_button.pack(pady=10)
    
        self.info_label = tk.Label(master, text="", fg="blue", font=("Helvetica", font_size))
        self.info_label.pack(pady=10)

        #for minutes
        self.min_label = tk.Label(master, text="Timer 00:00", font=("Helvetica", font_size))
        self.min_label.pack(pady=20)
        
        self.start_min_button = tk.Button(master, text="Start Minutes Timer", command=self.start_min_timer)
        self.start_min_button.pack(pady=10)

        self.stop_min_button = tk.Button(master, text="Stop Minutes Timer", command=self.stop_min_timer)
        self.stop_min_button.pack(pady=10)

        self.set_min_time_button = tk.Button(master, text="Set Time", command=self.set_min_timer)
        self.set_min_time_button.pack(pady=10)

    def clear_info_label(self):
        self.info_label.config(text="")

    def update_info_label(self, message):
        self.info_label.config(text=message)
        # Schedule the info label to be cleared after 10 seconds
        self.master.after(5000, self.clear_info_label)

    #creating time frame in minutes timer
    def start_min_timer(self):
        if not self.timer_running and self.minutesFrame > 0:
            self.timer_running = True
            self.update_min_timer()

    def stop_min_timer(self):
        self.timer_running = False

    def set_min_timer(self):
        # Get input from the user for total time
        total_min_time_str = simpledialog.askstring("Set Time", "Enter total time in minutes:")
        try:
            # Get input from the user for total time
            self.minutesFrame = int(total_min_time_str)
            #self.min_label.config(text=f"Timer: {minutesFrame: self.seconds} minutes")
            self.secLeft = 0
            self.min_label.config(text=self.format_time())
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")

    def update_min_timer(self):
        if self.timer_running and (self.minutesFrame > 0 or self.secLeft > 0):
            if self.secLeft == 0:
                self.minutesFrame -= 1
                self.secLeft = 59
            else:
                self.secLeft -= 1

            self.min_label.config(text=self.format_time())
            self.master.after(1000, self.update_min_timer)  # Schedule the next iteration after 1000 milliseconds (1 second)
        elif self.timer_running:
            self.update_info_label("")
            self.update_info_label("Timer completed")
            self.timer_running = False
            self.min_label.config(text="00:00")
            
    def format_time(self):
        return f"{self.minutesFrame:02d}:{self.secLeft:02d}"
    
    #creating timer in secinds timer
    def set_time(self):
        # Get input from the user for total time
        total_time_str = simpledialog.askstring("Set Time", "Enter total time in seconds:")

        try:
            # Convert input to integer
            self.secTimer = int(total_time_str)
            self.label.config(text=f"Timer: {self.secTimer} seconds")
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")
            
    def start_timer(self):
        if self.secTimer > 0:
            self.run_timer()

    def stop_timer(self):
        pass  # this method stops the timer

    def run_timer(self):
        if self.secTimer > 0:
            self.secTimer -= 1
            self.label.config(text=f"Timer: {self.secTimer} seconds")
            self.master.after(1000, self.run_timer)  # Schedule the next iteration after 1000 milliseconds (1 second)
        else:
            self.update_info_label("")
            self.update_info_label("Timer completed")
            self.label.config(text="Timer: 0 seconds")
            
        
class EnergyConsumedGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Energy Consumption Graphs")
        self.ec = EnergyConsumption()
        font_size = 14
        # Button to plot the graph
        self.plot_button = tk.Button(master, text='Show Energy Graph', command=self.plot_graph, font=("Helvetica", font_size))
        self.plot_button.pack(pady=10)

    def plot_graph(self):
        self.energy_table = self.ec.monitor_energy_table("C:/Users/Ehinomhen/Documents/energy_consumption_doc.txt")
        plt.bar(self.energy_table['Date'], self.energy_table['Energy Consumed (Watts)'])
        plt.xlabel('Date')
        plt.ylabel('Watts')
        plt.title('Energy consumed over time by Heaters/Coolers')

        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.master)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
 

class MainPageGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Page")

        # Set font size
        font_size = 16

        # Create and place widgets for the main page
        self.label = tk.Label(master, text="Welcome to the Building Automation System", font=("Helvetica", font_size))
        self.label.pack(pady=10)

        # Create a button to open the TemperatureGUI
        self.temperature_button = tk.Button(master, text="Heating/Cooling", command=self.open_temperature_gui, font=("Helvetica", font_size))
        self.temperature_button.pack(pady=10)

        # Center the widgets vertically and horizontally
        for widget in [self.label, self.temperature_button]:
            widget.pack(side="top", fill="both", expand=True)

    def open_temperature_gui(self): 
        # Create a new window for the TemperatureGUI
        temperature_gui_window = tk.Toplevel(self.master)
        temperature_gui = TemperatureGUI(temperature_gui_window)         

#///////MAIN////////
# Create the main application window
root = tk.Tk()

# Set font size for the main window
font_size_main_window = 18
root.option_add("*Font", f"Helvetica {font_size_main_window}")

# Create an instance of the MainPageGUI class
main_page = MainPageGUI(root)

# Start the main loop
root.mainloop()
