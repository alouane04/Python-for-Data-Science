from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


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
    """ and displays the projection of life expectancy in relation
        to the gross national product ofthe year 1900 for each country"""

    df_income = \
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df_life = load("life_expectancy_years.csv")

    if df_income.empty or df_life.empty:
        return
    # print(df_income)
    # print(df_life)

    df_income_proces = df_income[["country", "1900"]].copy()
    df_income_proces["1900"] = df_income_proces["1900"].apply(convert).dropna()
    print(df_income_proces)

    df_life_proces = df_life[["country", "1900"]].copy()
    print(df_life_proces)

    merged = pd.merge(
        df_income_proces,
        df_life_proces,
        on='country',
        suffixes=('_gdp', '_life_exp'),
    )

    merged = merged.dropna()

    print(merged)

    plt.scatter(merged["1900_gdp"], merged["1900_life_exp"])

    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")

    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

    plt.show()


if __name__ == "__main__":
    main()
