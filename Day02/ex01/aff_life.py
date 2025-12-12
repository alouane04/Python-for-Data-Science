from load_csv import load
import matplotlib.pyplot as plt


def main():
    """ load function from the previous exercise, loads
    the file life_expectancy_years.csv, and displays the
    country information of your campus"""

    file_path = "life_expectancy_years.csv"

    df = load(file_path)
    if df is None:
        return

    print(df)

    country_data = df[df["country"] == "France"]

    assert not country_data.empty, "France Data empty"

    # 3. Prepare X and Y axes
    # X-axis: The years are the column names (skipping the first one 'country')
    years = df.columns[1:].astype(int)

    # Y-axis: The values for France (skipping the first column 'France')
    life_expectancy = country_data.iloc[0, 1:]

    # 4. Plot
    plt.plot(years, life_expectancy)

    # 5. Styling
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")

    # 6. Display
    plt.show()


if __name__ == "__main__":
    main()
