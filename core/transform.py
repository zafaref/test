import pandas as pd

# This function creates an empty DataFrame with the specified columns and index.
def create_empty_dataframe(columns):
    """
    Create an empty DataFrame with the specified columns and index.

    Args:
        columns (list): List of column names for the DataFrame.
        index (list, optional): List of index values for the DataFrame. Defaults to None.

    Returns:
        pd.DataFrame: An empty DataFrame with the specified columns and index.
    """
    xx = pd.DataFrame(columns=columns)
    return xx

df = create_empty_dataframe(['a', 'b', 'c'])

# Example usage

# use pandas concat to append rows to the DataFrame
df = pd.concat([df, pd.DataFrame({'a': [1], 'b': [2], 'c': [3]})], ignore_index=True)
df = pd.concat([df, pd.DataFrame({'a': [4], 'b': [5], 'c': [6]})], ignore_index=True)
df = pd.concat([df, pd.DataFrame({'a': [7], 'b': [8], 'c': [9]})], ignore_index=True)

print(df)


import os
name = os.getenv("GITHUB_REPOSITORYD")
print(name)
