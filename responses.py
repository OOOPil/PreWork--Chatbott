from data import ai

class Chat:
  #creating a response class to find a response for the user message
  def __init__(self, message):
    self.message = message
    
  def findResponse(self):
    result = ai(self.message)
    #finding response from data.py
    return result
    
  def respond(self):
    return self.findResponse()
  