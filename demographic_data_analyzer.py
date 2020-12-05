import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset?
    # This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df["sex"] == "Male"]["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(
        df.loc[df["education"] == "Bachelors"]["education"].count()
        / df["education"].count()
        * 100,
        1,
    )

    # What percentage of people with advanced education (`Bachelors`,
    # `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    bachelors = df.loc[df["education"] == "Bachelors"]["education"].count()
    masters = df.loc[df["education"] == "Masters"]["education"].count()
    doctorate = df.loc[df["education"] == "Doctorate"]["education"].count()
    rich_bachelors = (
        df.loc[df["education"] == "Bachelors"]
        .loc[df["salary"] == ">50K"]["salary"]
        .count()
    )
    rich_masters = (
        df.loc[df["education"] == "Masters"]
        .loc[df["salary"] == ">50K"]["salary"]
        .count()
    )
    rich_doctorate = (
        df.loc[df["education"] == "Doctorate"]
        .loc[df["salary"] == ">50K"]["salary"]
        .count()
    )
    rich = df.loc[df["salary"] == ">50K"]["salary"].count()
    rich_high = rich_bachelors + rich_masters + rich_doctorate
    rich_low = rich - rich_high
    high = bachelors + masters + doctorate

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = high
    lower_education = df["education"].count() - higher_education

    # percentage with salary >50K
    higher_education_rich = round((rich_high / high) * 100, 1)
    lower_education_rich = round((rich_low / lower_education) * 100, 1)

    # What is the minimum number of hours a person works per week
    # (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of
    # hours per week have a salary of >50K?
    num_min_workers = df.loc[df["hours-per-week"] == min_work_hours][
        "hours-per-week"
    ].count()
    num_rich_min_workers = (
        df.loc[df["hours-per-week"] == min_work_hours]
        .loc[df["salary"] == ">50K"]["salary"]
        .count()
    )

    rich_percentage = round((num_rich_min_workers / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (
        df.loc[df["salary"] == ">50K"]["native-country"].value_counts()
        / df["native-country"].value_counts()
    ).idxmax()
    highest_earning_country_percentage = round(
        (
            df.loc[df["salary"] == ">50K"]["native-country"].value_counts()
            / df["native-country"].value_counts()
        ).max()
        * 100,
        1,
    )

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = (
        df.loc[df["native-country"] == "India"]
        .loc[df["salary"] == ">50K"]["occupation"]
        .value_counts()
        .idxmax()
    )

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            "Percentage without higher education that earn >50K:"
            f" {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            "Percentage of rich among those who work fewest hours:"
            f" {rich_percentage}%"
        )
        print("Country with highest percentage of rich: {highest_earning_country}")
        print(
            "Highest percentage of rich people in country:"
            f" {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
