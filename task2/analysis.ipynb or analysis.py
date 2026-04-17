import pandas as pd
df = pd.read_csv("intern_applications.csv")
df.head()

# From the df.info performed, two columns have missing values so I need to identify what is the missing value
missing_assessment_score = df[df['assessment_score'].isnull()]
display(missing_assessment_score)

missing_project_score = df[df['project_score'].isnull()]
display(missing_project_score)
