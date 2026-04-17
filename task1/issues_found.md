In this READme:

In the clean_data function, the drop_duplicates is missing the parentheses to call the function.I have fixed by adding them as drop_duplicates()

When filling the missing values, the mean method to call the mean of assessment score and project score was missing the brackets, I have proceed to add as follows df["assessment_score"].mean() and df["project_score"].mean()

In the def rank_candidates function, the return has the ascending parameter "False" as a string instead of the boolean type False.

The groupby for tracking the final score in the summarize function is using average instead of mean(), I have corrected since average is not allowed in python

After fizing these issues, I added a validation check on  to ensure that the assessment_score and project_score are not negative scores and also to remove the Securitywithcopy warning check, I added a duplicate.copy to remove the error. 
