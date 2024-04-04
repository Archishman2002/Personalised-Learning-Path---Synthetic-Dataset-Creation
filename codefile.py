pip install Faker

import pandas as pd
from faker import Faker
import random

fake = Faker()

# List of study domains including bachelor's or college subjects
study_domains = ['Physics', 'Chemistry', 'Mathematics', 'History', 'Geography', 'Economics', 'Biology', 'Computer Science', 'Literature', 'Psychology', 'Sociology', 'Political Science',
                 'Engineering', 'Business Administration', 'Computer Engineering', 'Electrical Engineering', 'Mechanical Engineering', 'Civil Engineering', 'Finance', 'Marketing', 'Accounting',
                 'English Literature', 'Communications', 'Information Technology', 'Environmental Science', 'Philosophy', 'Education', 'Nursing', 'Architecture', 'International Relations']

# Synthetic User Input Data
user_data = {
    'User_ID': [fake.uuid4() for _ in range(1000)],
    'Subjects': [random.choice(study_domains) for _ in range(1000)],
    'Skill': [fake.word() for _ in range(1000)],
    'Career': [fake.word() for _ in range(1000)],
    'Personality_Trait': [fake.word() for _ in range(1000)],
    'Proficiency_Score': [random.randint(1, 100) for _ in range(1000)]
}

user_df = pd.DataFrame(user_data)

# Synthetic Learning Resources Data
resource_data = {
    'Resource_ID': [fake.uuid4() for _ in range(500)],
    'Title': [fake.word() for _ in range(500)],
    'Description': [fake.sentence() for _ in range(500)],
    'Rating': [random.uniform(1, 5) for _ in range(500)],
    'URL': [fake.url() for _ in range(500)]
}

resource_df = pd.DataFrame(resource_data)

# Synthetic Learning Paths Data
path_data = {
    'Path_ID': [fake.uuid4() for _ in range(200)],
    'Path_Description': [fake.sentence() for _ in range(200)],
    'Resources': [random.sample(list(resource_df['Resource_ID']), random.randint(2, 10)) for _ in range(200)]
}

path_df = pd.DataFrame(path_data)

# Synthetic Feedback Data
feedback_data = {
    'Feedback_ID': [fake.uuid4() for _ in range(500)],
    'User_ID': [random.choice(list(user_df['User_ID'])) for _ in range(500)],
    'Path_ID': [random.choice(list(path_df['Path_ID'])) for _ in range(500)],
    'Rating': [random.randint(1, 5) for _ in range(500)]
}

feedback_df = pd.DataFrame(feedback_data)

# Save the synthetic datasets
user_df.to_csv('user_data.csv', index=False)
resource_df.to_csv('resource_data.csv', index=False)
path_df.to_csv('path_data.csv', index=False)
feedback_df.to_csv('feedback_data.csv', index=False)

import pandas as pd

# Load the synthetic datasets
user_df = pd.read_csv('user_data.csv')
resource_df = pd.read_csv('resource_data.csv')
path_df = pd.read_csv('path_data.csv')
feedback_df = pd.read_csv('feedback_data.csv')

# Display the first few rows of each dataset
print("User Data:")
print(user_df.head())

print("\nResource Data:")
print(resource_df.head())

print("\nPath Data:")
print(path_df.head())

print("\nFeedback Data:")
print(feedback_df.head())

#END OF CODE
#COPY MAT KARNA NA PLEASE, UMMMM...... NHI NHI COPY KARLENA PAR EK BAAR BATA DENA CONNECT KARKE IF YOU WISH TO PLEASE PLEASE, THIS IS THE LEAST I CAN EXPECT!
