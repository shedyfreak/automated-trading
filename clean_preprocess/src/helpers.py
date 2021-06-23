from local_exceptions import CorruptedFields


# this is a helper fucntion that will take a df and raise an exception if there is any missing value
def clean_helper(df: pd.DataFrame):
    fields = df.isna().sum()
    if sum(fields) != 0:
        raise CorruptedFields
