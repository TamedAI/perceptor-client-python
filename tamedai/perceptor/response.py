class QAResponse:
    
    # The __init__ method initializes the instance variables of the class.
    def __init__(self, text, score):
        self.text = text  # The response text, which is typically an answer to a question asked by the user.
        self.score = score  # The confidence score of the response, which is a measure of how likely the response is to be correct.
    
    # The __str__ method returns a string that represents the object in a readable format.
    def __str__(self) -> str:
        return f"QAResponse({self.text}, {self.score})"