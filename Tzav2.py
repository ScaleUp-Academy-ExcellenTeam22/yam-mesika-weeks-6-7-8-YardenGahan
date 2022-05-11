class Message:
    """Create a new message for Post Office using messages.

        Args:
            message_id (int): the message number increment from the last one
            body (str): The message body.
            sender (str) : The name of the sender
            urgent (bool) : If this massage is in high priority

        Attributes:
            message_id (int): the message number increment from the last one
            body (str): The message body.
            sender (str) : The name of the sender
            urgent (bool) : If this massage is in high priority
            unread (bool) : 'True' if the message have been read already

        """

    def __init__(self, message_id, body, sender, urgent=False):
        self.message_id = message_id
        self.body = body
        self.sender = sender
        self.unread = True
        self.urgent = urgent

    def __str__(self):
        return f'Message #{self.message_id} from {self.sender}: {self.body}'

    def __len__(self):
        return len(self.body)


class PostOffice:
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        user_box = self.boxes[recipient]

        self.message_id = self.message_id + 1
        new_message = Message(self.message_id, message_body, sender, urgent)

        if new_message.urgent:
            user_box.insert(0, new_message)
        else:
            user_box.append(new_message)
        return self.message_id

    def read_inbox(self, recipient, num_of_messages=0):
        user_box = self.boxes[recipient]
        user_messages = []

        if num_of_messages == 0:
            for message in user_box:
                if message.unread:
                    message.unread = False
                    user_messages.append(message.body)
        else:
            for index, message in enumerate(user_box):
                if index < num_of_messages:
                    if message.unread:
                        message.unread = False
                        user_messages.append(message.body)
        return user_messages

    def search_inbox(self, recipient : str, part_of_message : str) ->list:
        """
        this function returns list of messages
        @param recipient: user name who recives the message.
        @param part_of_message: part of message to find
        @return: list of messages that contains the wanted string
        user_box = self.boxes[recipient]
        user_messages = [message.body for message in user_box if part_of_message in message.body]
   
        return user_messages
