def test_function():
    return "This is a test module"

def run(params):
    return {"message": test_function(), "status": "success"}