from sklearn.model_selection import train_test_split

def split_dataset(df, seed: int = 42):
    train_df, temp_df = train_test_split(
        df, test_size=0.15, random_state=seed, shuffle=True
    )
    val_df, test_df = train_test_split(
        temp_df, test_size=2/3, random_state=seed, shuffle=True
    )
    return (
        train_df.reset_index(drop=True),
        val_df.reset_index(drop=True),
        test_df.reset_index(drop=True),
    )
