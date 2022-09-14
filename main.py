import responses as chat

print("\033[0;32mChatbot Started Successfully\033[0m\n")

print("-----------------------\n")
while True:
  #looping chatbot
  user_input = input("")  
  result = chat.Chat(user_input)
  print("\033[0m\n"+result.respond()+"\n")
  