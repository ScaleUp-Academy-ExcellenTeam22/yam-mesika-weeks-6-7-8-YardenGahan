class PostOffice:
    def __init__(self, usernames):

        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        user_box = self.boxes[recipient]

        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
            'unread': True,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, num_of_meesages=0):
        user_box = self.boxes[username]
        user_messages = []

        if num_of_meesages == 0:
            for message in range(0, self.message_id):
                if user_box[message]['unread']:
                    user_box[message]['unread'] = False
                    user_messages.append(user_box[message]['body'])
        else:
            for message in range(0, num_of_meesages):
                if user_box[message]['unread']:
                    user_box[message]['unread'] = False
                    user_messages.append(user_box[message]['body'])
        return user_messages

    def search_inbox(self, username, part_of_message):
        user_box = self.boxes[username]
        user_messages = []
        for message in range(0, self.message_id):
            if part_of_message in user_box[message]['body']:
                user_messages.append(user_box[message]['body'])
        return user_messages
