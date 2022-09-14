from requests import get
import random


def ai(message):
  result = "Oh haha"
  txt = message.split()
  
  def index(input):
        result = ""
        try:
            r = message.split(input)
            rr = r[1].split()
            result = rr[0]
        except:
            pass
        return result
      
  list = ["my name is", "i am", "my age is", "what is my name"]
  val = False
  for i in list:
    if i in message.lower(): 
      x = i
      if x.lower() == list[0]:
        result = "Hi, that's a great name, " + index(list[0]).capitalize() + "."
        val = True
      elif x.lower() == list[1]:
        result = "Hi, that's a great name, " + index(list[1]).capitalize() + "."
        val = True
      elif x.lower() == list[2]:
        result = "Wow your old at, " + index(list[2]).capitalize() + "."
        val = True
      elif x.lower() == list[3]:
        result = "I don't know your name, what is it?"
        val = True
        
  if val == False:
        #if no responses get response from api
        try:
            m = "+".join(message.split())
            getr = get(
                "http://api.brainshop.ai/get?bid=168040&key=AM0pjHyx4xcwmHJw&uid="
                + str(random.randint(1, 100000)) + "&msg=" + m)
            js = getr.json()
            json = js["cnt"]
            result = json
        except:
            print("\033[0;31mError SendinData to Server... Please Try Again")

  return result
