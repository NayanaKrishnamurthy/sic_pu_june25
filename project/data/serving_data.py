import pandas as pd
import matplotlib.pyplot as plt

def read_serving_data():
    file_path ="C:\\learning\\sic_pu_june25\\project\\data\\serving_data.csv"
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def blockwise_daily_analysis():
    df = read_serving_data()
    print(f"Available data range: {df['Date'].min().date()} to {df['Date'].max().date()}")
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")

    try:
        start_date = pd.to_datetime(start)
        end_date = pd.to_datetime(end)
    except:
        print("Invalid date format.")
        return

    df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    if df.empty:
        print("No data for this range.")
        return

    daily_summary = df.groupby(['Date', 'Block'])['Wasted_kg'].sum().unstack()
    daily_summary.plot(kind='line', figsize=(10, 5))
    plt.title("Daily Block-wise Waste")
    plt.xlabel("Date")
    plt.ylabel("Wasted (kg)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    latest_date = df['Date'].max()
    latest_data = df[df['Date'] == latest_date].groupby('Block')['Wasted_kg'].sum()
    max_block = latest_data.idxmax()
    min_block = latest_data.idxmin()

    print(f"On {latest_date.date()}, Highest Waste: {max_block}, Lowest Waste: {min_block}")
    print("Suggestion: Address over-preparation or portioning in high-waste blocks.\n")

def blockwise_weekly_analysis():
    df = read_serving_data()
    year = input("Enter year (e.g., 2024): ")
    month = input("Enter month (1–12): ")

    try:
        year = int(year)
        month = int(month)
        start = pd.to_datetime(f"{year}-{month:02d}-01")
        end = start + pd.offsets.MonthEnd(1)
    except:
        print("Invalid input.")
        return

    df = df[(df['Date'] >= start) & (df['Date'] <= end)]
    if df.empty:
        print("No data for this month.")
        return

    df['Week'] = ((df['Date'].dt.day - 1) // 7) + 1
    weekly_summary = df.groupby(['Week', 'Block'])['Wasted_kg'].sum().unstack()

    # Line plot for all blocks together
    plt.figure(figsize=(10, 5))
    for block in weekly_summary.columns:
        plt.plot(weekly_summary.index, weekly_summary[block], marker='o', label=block)

    plt.title(f"Weekly Waste Comparison – {start.strftime('%B %Y')}")
    plt.xlabel("Week")
    plt.ylabel("Waste (kg)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    block_totals = df.groupby('Block')['Wasted_kg'].sum()
    max_block = block_totals.idxmax()
    min_block = block_totals.idxmin()

    print(f"Weekly Waste Totals – Highest: {max_block}, Lowest: {min_block}")
    print("Suggestion: Monitor menu demand and coordinate distribution across blocks.\n")

def blockwise_monthly_analysis():
    df = read_serving_data()
    year = input("Enter year (e.g., 2024): ")

    try:
        year = int(year)
    except:
        print("Invalid year.")
        return

    df = df[df['Date'].dt.year == year]
    if df.empty:
        print("No data for this year.")
        return

    df['Month'] = df['Date'].dt.month
    monthly_summary = df.groupby(['Month', 'Block'])['Wasted_kg'].sum().unstack()

    # Line plot for all blocks together
    plt.figure(figsize=(10, 5))
    for block in monthly_summary.columns:
        plt.plot(monthly_summary.index, monthly_summary[block], marker='o', label=block)

    plt.title(f"Monthly Waste Comparison – {year}")
    plt.xlabel("Month")
    plt.ylabel("Waste (kg)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    block_totals = df.groupby('Block')['Wasted_kg'].sum()
    max_block = block_totals.idxmax()
    min_block = block_totals.idxmin()

    print(f"Monthly Waste Totals – Highest: {max_block}, Lowest: {min_block}")
    print("Suggestion: High monthly waste in some blocks. Reassess food planning.\n")

def show_serving_menu():
    while True:
        print("\nSERVING DATA ANALYSIS MENU")
        print("--------------------------")
        print("1. Daily Block-wise Waste")
        print("2. Weekly Block-wise Waste")
        print("3. Monthly Block-wise Waste")
        print("4. Exit")

        choice = input("Enter your choice (1–4): ")

        if choice == '1':
            blockwise_daily_analysis()
        elif choice == '2':
            blockwise_weekly_analysis()
        elif choice == '3':
            blockwise_monthly_analysis()
        elif choice == '4':
            print("Exiting Serving Data Analysis.")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    show_serving_menu()
