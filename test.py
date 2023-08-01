import pandas as pd

# Create the initial timestamp
initial_timestamp = pd.to_datetime("2023-07-17 00:00:00")
df = pd.read_csv("new_sys_usage.csv")
df = df.drop(columns={'timestamp'})
# Number of rows in your dataset
num_rows = len(df.index)  # Replace this with the actual number of rows you have in your dataset

# Generate a list of timestamps with 10-second increments
timestamps = [initial_timestamp + pd.Timedelta(seconds=10 * i) for i in range(num_rows)]

# Create a DataFrame with the timestamps

df['timestamp'] = timestamps
cols = df.columns.tolist()
cols = ['timestamp'] + [col for col in cols if col != 'timestamp']
df = df[cols]
# Optionally, you can set 'timestamp' as the index of your DataFrame
# df.set_index('timestamp', inplace=True)

# Now your DataFrame should have a 'timestamp' column with timestamps incrementing by 10 seconds for each row.
df.to_csv("increment.csv", index=False)
