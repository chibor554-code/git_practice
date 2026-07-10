import pandas as pd
df = pd.read_csv(r'C:\Users\NEW USER\Documents\Techrise_cohort3\Week4\ai_student_impact_dataset.csv')
# print(df.head(2))
# print(df.dtypes)
# print(df.info())
# print(df.info)
high_students = df[(df['Post_Semester_GPA'] >3.5) & (df['Skill_Retention_Score'] > 70)]
print(high_students)