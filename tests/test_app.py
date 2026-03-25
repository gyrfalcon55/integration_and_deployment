from my_app import add, model_predict

def test_add():
    assert add(2, 3) == 5

def test_model_predict():
    assert model_predict(4) == 8