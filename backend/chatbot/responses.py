from .model import load_model

model = load_model()

def get_response(user_input):
    # Process the input and get the model's response
    response = "Sample response based on input: " + user_input
    return response
