import pandas as pd
import matplotlib.pyplot as plt

# Reads food data from a CSV file and parses the 'Date' column into datetime format
def read_food_data():
    file_path = "C:\\Users\\admin\\Downloads\\food_data_2years.csv"
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])  # Convert 'Date' column to datetime
    return df

# Allows the user to input a custom date range and analyzes daily waste
def analyze_daily_waste_user_input():
    df = read_food_data()
    print(f"\nAvailable data: {df['Date'].min().date()} to {df['Date'].max().date()}")
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")

    try:
        start_date = pd.to_datetime(start)
        end_date = pd.to_datetime(end)
    except:
        print("Invalid date format. Please enter in YYYY-MM-DD.")
        return

    filtered = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    if filtered.empty:
        print("No data found for this range.")
        return

    daily = filtered.groupby('Date')['Wasted_kg'].sum()
    avg_waste = daily.mean()

    max_date = daily.idxmax()
    min_date = daily.idxmin()

    plt.figure(figsize=(10, 4))
    plt.plot(daily.index, daily.values, color='orange', linewidth=2, label='Daily Waste')
    plt.scatter([max_date], [daily[max_date]], color='red', label=f"Highest: {daily[max_date]:.1f} kg")
    plt.scatter([min_date], [daily[min_date]], color='green', label=f"Lowest: {daily[min_date]:.1f} kg")
    plt.title(f"Daily Food Waste: {start} to {end}")
    plt.xlabel("Date")
    plt.ylabel("Wasted (kg)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    print("\n--- Smart Suggestion ---")
    if avg_waste > 30:
        print("High average daily waste detected.")
        print("→ Review portion sizes, attendance variations, and menu planning.")
    else:
        print("Daily waste is within expected range.")
        print("→ Continue current food preparation strategies.")

def analyze_weekly_waste_user_input():
    df = read_food_data()
    year = input("Enter year (e.g., 2024): ")
    month = input("Enter month (1–12): ")

    try:
        year = int(year)
        month = int(month)
        start = pd.to_datetime(f"{year}-{month:02d}-01")
        end = start + pd.offsets.MonthEnd(1)
    except:
        print("Invalid year or month.")
        return

    month_df = df[(df['Date'] >= start) & (df['Date'] <= end)]
    if month_df.empty:
        print("No data for that month.")
        return

    month_df['Week'] = ((month_df['Date'].dt.day - 1) // 7) + 1
    weekly = month_df.groupby('Week')['Wasted_kg'].sum()
    max_week = weekly.idxmax()
    min_week = weekly.idxmin()
    max_val = weekly.max()
    min_val = weekly.min()

    plt.figure(figsize=(7, 4))
    bars = plt.bar(weekly.index, weekly.values, color='lightgreen')
    bars[max_week - 1].set_color('red')
    bars[min_week - 1].set_color('blue')
    plt.text(max_week, max_val + 1, f"{max_val:.1f} kg (High)", ha='center', color='red')
    plt.text(min_week, min_val + 1, f"{min_val:.1f} kg (Low)", ha='center', color='blue')
    plt.title(f"Weekly Food Waste – {start.strftime('%B %Y')}")
    plt.xlabel("Week Number")
    plt.ylabel("Total Waste (kg)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    print(f"\n--- Smart Suggestion for {start.strftime('%B %Y')} ---")
    print(f"→ Highest waste: Week {max_week} = {max_val:.1f} kg")
    print(f"→ Lowest waste: Week {min_week} = {min_val:.1f} kg")
    if max_val - min_val > 20:
        print("→ Action: Adjust food quantity based on weekday patterns or events.")
    elif max_val > 35:
        print("→ Action: Investigate spikes and revise overcooking trends.")
    else:
        print("→ Waste level is well balanced across weeks.")

# Monthly analysis for a selected year
def analyze_monthly_waste_user_input():
    df = read_food_data()
    year = input("Enter year (e.g., 2024): ")

    try:
        year = int(year)
    except:
        print("Invalid year.")
        return

    monthly = df[df['Date'].dt.year == year].groupby(df['Date'].dt.month)['Wasted_kg'].sum()
    if monthly.empty:
        print("No data for this year.")
        return

    max_month = monthly.idxmax()
    min_month = monthly.idxmin()
    max_val = monthly.max()
    min_val = monthly.min()

    plt.figure(figsize=(10, 5))
    bars = plt.bar(monthly.index, monthly.values, color='skyblue')
    bars[max_month - 1].set_color('red')
    bars[min_month - 1].set_color('blue')

    plt.text(max_month, max_val + 2, f"{max_val:.1f} kg (High)", ha='center', color='red')
    plt.text(min_month, min_val + 2, f"{min_val:.1f} kg (Low)", ha='center', color='blue')
    plt.title(f"Monthly Food Waste for {year}")
    plt.xlabel("Month")
    plt.ylabel("Total Waste (kg)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    print(f"\n--- Smart Suggestion for {year} ---")
    print(f"→ Highest waste: Month {max_month} = {max_val:.1f} kg")
    print(f"→ Lowest waste: Month {min_month} = {min_val:.1f} kg")
    if max_val > 1000:
        print("→ Action: Investigate events, exam breaks, or holidays causing spikes.")
    elif max_val - min_val > 400:
        print("→ Action: Stabilize cooking plans with more accurate forecasting.")
    else:
        print("→ Waste is controlled. Maintain preparation and tracking habits.")

def show_food_menu():
    while True:
        print("\nFOOD WASTE ANALYSIS MENU")
        print("----------------------------")
        print("1. Daily Waste (give Date Range)")
        print("2. Weekly Waste (Choose Month)")
        print("3. Monthly Waste (Choose Year)")
        print("4. Exit")
        choice = input("Enter your choice (1–4): ")
        if choice == '1':
            analyze_daily_waste_user_input()
        elif choice == '2':
            analyze_weekly_waste_user_input()
        elif choice == '3':
            analyze_monthly_waste_user_input()
        elif choice == '4':
            print("Exiting Food Analysis Menu.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    show_food_menu()
