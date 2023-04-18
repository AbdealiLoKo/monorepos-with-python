from corridor.data_lake.dataset import Dataset


def test_dataset_read() -> None:
    ownsership_data = Dataset(name="home_ownership")
    df = ownsership_data.read()
    assert list(df.shape) == [10, 3]


def test_dataset_random() -> None:
    ownsership_data = Dataset(name="home_ownership")
    df1 = ownsership_data.read()
    df2 = ownsership_data.generate_random()
    assert df1.shape == df2.shape
    assert dict(df1.dtypes) == dict(df2.dtypes)
