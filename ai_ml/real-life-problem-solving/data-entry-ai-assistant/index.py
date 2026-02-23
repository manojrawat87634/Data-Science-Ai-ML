import pandas as pd

# Define the array of institutes
data = [
  {
    "name": "iSchool – Education & Online Courses WordPress Theme",
    "url": "https://themeforest.net/item/ischool-education-online-courses-wordpress-theme/55082435"
  },
  {
    "name": "Udetor – LMS Education WordPress Theme",
    "url": "https://themeforest.net/item/udetor-lms-education-wordpress-theme/20882471"
  },
  {
    "name": "Academee – Education Center & Training Courses Theme",
    "url": "https://themeforest.net/item/academee-education-center-training-courses-theme/20630345"
  },
  {
    "name": "iTeach – Online Courses & Education Theme",
    "url": "https://themeforest.net/item/iteach-online-courses-education-wordpress-theme/47540735"
  },
  {
    "name": "Masterstudy – Education Center Theme",
    "url": "https://themeforest.net/item/masterstudy-education-center-wordpress-theme/12170274"
  }
]


# Convert to DataFrame with proper column names
df = pd.DataFrame(data)
df.columns = ['Name', 'Website']

# Display the DataFrame
# print(df)

# Optional: Save to Excel
df.to_excel("Top_Photography_Institutes.xlsx", index=False)
