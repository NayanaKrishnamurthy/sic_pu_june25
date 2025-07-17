import tkinter as tk
import sys
import os

# Add parent directory to sys.path to import modules from ../data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.food_data import (
    analyze_daily_waste_user_input,
    analyze_weekly_waste_user_input,
    analyze_monthly_waste_user_input
)

from data.serving_data import (
    blockwise_daily_analysis,
    blockwise_weekly_analysis,
    blockwise_monthly_analysis
)

def show_food_menu_gui():
    window = tk.Toplevel(root)
    window.title("Food Waste Analysis")

    tk.Label(window, text="Food Waste Analysis", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Button(window, text="Daily Waste", width=25, command=analyze_daily_waste_user_input).pack(pady=5)
    tk.Button(window, text="Weekly Waste", width=25, command=analyze_weekly_waste_user_input).pack(pady=5)
    tk.Button(window, text="Monthly Waste", width=25, command=analyze_monthly_waste_user_input).pack(pady=5)
    tk.Button(window, text="Close", width=25, command=window.destroy).pack(pady=10)

def show_serving_menu_gui():
    window = tk.Toplevel(root)
    window.title("Serving Data Analysis")

    tk.Label(window, text="Block-wise Serving Analysis", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Button(window, text="Daily Block-wise Waste", width=30, command=blockwise_daily_analysis).pack(pady=5)
    tk.Button(window, text="Weekly Block-wise Waste", width=30, command=blockwise_weekly_analysis).pack(pady=5)
    tk.Button(window, text="Monthly Block-wise Waste", width=30, command=blockwise_monthly_analysis).pack(pady=5)
    tk.Button(window, text="Close", width=30, command=window.destroy).pack(pady=10)

# Main root window
root = tk.Tk()
root.title("Food Wastage Management System")
root.geometry("400x350")

tk.Label(root, text="Food Wastage Management System", font=("Arial", 16, "bold")).pack(pady=20)

tk.Button(root, text="Food Waste Analysis", width=30, height=2, command=show_food_menu_gui).pack(pady=10)
tk.Button(root, text="Serving Data Analysis", width=30, height=2, command=show_serving_menu_gui).pack(pady=10)
tk.Button(root, text="Exit", width=30, height=2, command=root.destroy).pack(pady=20)

root.mainloop()
