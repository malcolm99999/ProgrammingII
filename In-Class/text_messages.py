text_messages ={}
def send_message(text_messages, name, message):
    if name in text_messages:
        text_messages[name].append(message)
    else:
        text_messages[name] = [message]
    #text_messages[name] = [message]

def get_messages(text_messages, name):
    return text_messages.get(name)
text_messages ={
    "Jonah" : ["whats up"],
    "Beckett" : ["feed the dog"]
}

send_message(text_messages, "Jonah", "whats up")
send_message(text_messages, "Beckett", "feed the dog")
send_message(text_messages, "Beckett", "what time is dinner?")

print(text_messages)