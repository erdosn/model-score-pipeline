import os


def column_cleaner(col, bad_characters="()*&^@#$%"):
    for ch in bad_characters:
        col = col.replace(ch, "")
    col = col.replace(" ", "_")
    col = col.lower()
    return col

def clean_data(df, write_file=False, filepath=None):
    df.rename(mapper=column_cleaner, axis=1, inplace=True)
    df['pl_pw_ratio'] = df['petal_length_cm']/df['petal_width_cm']
    df['sepal_diff'] = df['sepal_length_cm'] - df['sepal_width_cm']
    df['abs_sepal_diff'] = df['sepal_diff'].abs()
    df['pw_pl_sum'] = df['petal_length_cm'] + df['petal_width_cm']
    if write_file:
        if not filepath:
            print("filepath is empty")
            pass
        else:
            path, filename = os.path.split(filepath)
            if os.path.exists(path):
                pass
            else:
                os.mkdir(path)
            filepath = filepath if filepath.endswith(".csv") else filepath+".csv"
            df.to_csv(filepath, index=False)
    return df


def get_xy(df, target_name='target_names'):
    x = df.drop(columns=[i for i in df.columns if 'target' in i])
    y = df[target_name]
    return x, y