from code_Sequence_programming.Q_5 import Farm, Crop

def test_add_crop():
    """Test adding a crop to the farm. makes sure it is of correct class and stored properly."""
    farm = Farm()

    crop = Crop("Potato", 16, 10, 20000)
    farm.add_crop(crop)

  
    assert "Potato" in farm.crops

    assert farm.crops["Potato"] is crop

    assert isinstance(farm.crops["Potato"], Crop)
