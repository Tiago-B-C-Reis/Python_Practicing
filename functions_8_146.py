# 8.9
def show_messages(message):

    for item in message_list:
        print(item)


message_list = ["Hello", "Good morning", "Good afternoon", "Good evening", "Good by"]
# show_messages(message_list)


# 8.10
def send_messages(message_send, message_sent):

    i = 0
    while i < len(message_send):
        print(message_send[i])
        print(len(message_send))
        message_sent.append(message_send[i])
        message_send.pop(i)

    print(f'send_message {message_send}')
    print(f'sent_message {message_sent}')


send_message = ["Hello", "Good morning", "Good afternoon", "Good evening", "Good by"]
sent_message = []
# send_messages(send_message, sent_message)


# 8.11
def send_messages1(message_send, message_sent):

    print(f'Original send_message = {message_send}')

    i = 0
    while i < len(message_send):
        message_sent.append(message_send[i])
        message_send.pop(i)

    print(f'send_message = {message_send}')
    print(f'sent_message = {message_sent}')


send_message1 = ["Hello", "Good morning", "Good afternoon", "Good evening", "Good by"]
sent_message1 = []
send_messages1(send_message1, sent_message1)
