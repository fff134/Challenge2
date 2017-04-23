import pandas as pd

#  Get Data
c1 = pd.read_csv('Cleaned Data/clean_Well1B3mths.csv', low_memory=False)
c2 = pd.read_csv('Cleaned Data/clean_Well1D3mths.csv', low_memory=False)
c3 = pd.read_csv('Cleaned Data/clean_Well1F3mths.csv', low_memory=False)
c4 = pd.read_csv('Cleaned Data/clean_Well1G3mths.csv', low_memory=False)
c5 = pd.read_csv('Cleaned Data/clean_Well1H3mths.csv', low_memory=False)
c6 = pd.read_csv('Cleaned Data/clean_Well2A3mths.csv', low_memory=False)

# Limit data
# limit = 100000
c1 = c1.iloc[:, :]
c2 = c2.iloc[:, :]
c3 = c3.iloc[:, :]
c4 = c4.iloc[:, :]
c5 = c5.iloc[:, :]
c6 = c6.iloc[:, :]

# Compile the results
result = c1.append([c2, c3, c4, c5, c6])

# Remove nulls
result = result.dropna()
result.to_csv('all_wells_lim_test.csv', index = False, header = False)
