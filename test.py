print("hello world")
import pandas as pd
student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
df = pd.Dataframe(student_data, columns=['student_id', 'age'])
print(df)