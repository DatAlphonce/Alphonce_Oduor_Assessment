import pandas as pd

def load_data(path):
    data = pd.read_csv(path)
    return data

def clean_data(df):
    # remove duplicates
    df = df.drop_duplicates

    # standardize track names
    df["track"] = df["track"].replace({
        "Data science": "Data Science",
        "Software Eng": "Software Engineering"
    })

    # fill missing numeric values
    df["assessment_score"] = df["assessment_score"].fillna(df["assessment_score"].mean)
    df["project_score"] = df["project_score"].fillna(df["project_score"].mean)

    # remove rows with impossible scores
    df = df[df["assessment_score"] < 1000]

    # normalize gender
    df["gender"] = df["gender"].replace({
        "Male": "M",
        "Female": "F"
    })

    return df

def rank_candidates(df):
    # higher scores are better, missing documents and older applications are worse
    df["final_score"] = (
        df["assessment_score"] * 0.6 +
        df["project_score"] * 0.4 -
        df["missing_documents"] * 5 -
        df["days_since_application"] / 2
    )
    return df.sort_values("final_score", ascending="False")

def summarize(df):
    print("Candidate count:", len(df))
    print("Average assessment score:", df["assessment_score"].mean())
    print("Average project score:", df["project_score"].mean())
    print("\nTop 5 candidates:")
    print(df[["candidate_id", "name", "track", "final_score"]].head(5))

    print("\nAverage score by track:")
    print(df.groupby("track")["final_score"].average())

def main():
    df = load_data("intern_application.csv")
    df = clean_data(df)
    ranked = rank_candidates(df)
    summarize(ranked)

main
