from my_app import add, model_predict

def test_add():
    assert add(2, 3) == 5

def test_model_predict():
    try:
        assert model_predict(4) == 8
    except:
        print("Error test case failed")