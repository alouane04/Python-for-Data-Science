from load_csv import load
import matplotlib.pyplot as plt


def convert(value):
    """ Parses strings like '10M', '5k' into numbers"""
    try:
        if isinstance(value, str):
            if value.endswith('B'):
                return float(value[:-1]) * 1_000_000_000
            elif value.endswith('M'):
                return float(value[:-1]) * 1_000_000
            elif value.endswith('k'):
                return float(value[:-1]) * 1_000
        return float(value)
    except ValueError:
        return 0


def main():
    """ calls the load function from the first exercise,
        loads the file population_total.csv, and displays
        the country information of your campus versus other
        country of your choice"""

    file_path = "population_total.csv"

    df = load(file_path)
    if df.empty:
        return

    print(df)

    country_data = df[df["country"] == "France"]
    country_compared_data = df[df["country"] == "Belgium"]

    assert not country_data.empty or not country_compared_data.empty, \
        "countrys Data empty"

    # 3. Get all years and filter for the target
    years = df.columns[1:]
    filter_years = [year for year in years if int(year) <= 2050]

    print(filter_years)

    raw_data = country_data[filter_years].values.flatten()
    raw_compared_data = country_compared_data[filter_years].values.flatten()

    print(raw_data)

    # 4. Convert
    data_convertion = [convert(data) for data in raw_data]
    data_compared_convertion = [convert(data) for data in raw_compared_data]

    #    Convert X-axis (Years) to integers for plotting
    x_axis = [int(year) for year in filter_years]

    # 5. Plot
    plt.plot(x_axis, data_convertion, label='France')
    plt.plot(x_axis, data_compared_convertion, label='Belgium')

    # 1. Define the specific numbers where you want marks
    #    (20 million, 40 million, 60 million)
    y_vals = [20_000_000, 40_000_000, 60_000_000]

    # 2. Define the text labels for those numbers
    y_labels = ["20M", "40M", "60M"]

    # 3. Apply them to the graph
    plt.yticks(y_vals, y_labels)

    # Apply legend to the right lower corner
    plt.legend()
    plt.legend(loc="lower right")

    # 5. Styling
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    # 6. Display
    plt.show()


if __name__ == "__main__":
    main()
