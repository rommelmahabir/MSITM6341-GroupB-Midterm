"""
test_data_prep.py - Simple checks that the cleaned data is what we expect.



Run with: python3 test_data_prep.py (Mac) or python test_data_prep.py (Windows)
"""



from data_prep import load_clean_data





def test_shape():
    """The cleaned data keeps all 7,043 customers and has 20 columns."""
    df = load_clean_data()
    assert df.shape == (7043, 20), f"Expected (7043, 20), got {df.shape}"





def test_no_missing_values():
    """No column has any missing values after cleaning."""
    df = load_clean_data()
    assert df.isnull().sum().sum() == 0, "Found missing values"





def test_totalcharges_is_number():
    """TotalCharges was text in the raw file; it must now be a number."""
    df = load_clean_data()
    assert df["TotalCharges"].dtype == "float64", "TotalCharges is not a number"





def test_customerid_dropped():
    """customerID is a label, not a feature, so it should be gone."""
    df = load_clean_data()
    assert "customerID" not in df.columns, "customerID is still there"





def test_churn_values():
    """Churn should only ever be Yes or No."""
    df = load_clean_data()
    assert set(df["Churn"].unique()) == {"Yes", "No"}, "Unexpected Churn values"





if __name__ == "__main__":
    test_shape()
    test_no_missing_values()
    test_totalcharges_is_number()
    test_customerid_dropped()
    test_churn_values()
    print("All 5 checks passed")
