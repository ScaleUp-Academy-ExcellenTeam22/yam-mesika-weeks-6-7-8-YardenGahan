class File:
    """A File class. Represent a file, can be binary file or text file.

    Args:
        file_name (str): The name of the file.
        user (User): The user who created the file.
        file_size (double): The file size in KB.
        body (str): File content.

    Attributes:
         file_name (str): The name of the file.
        user (User): The user who created the file.
        file_size (double): The file size in KB.
        body (str): File content.
    """

    def __init__(self, file_name, user, file_size, body):
        self.name = file_name
        self.author = user
        self.size = file_size
        self.body = body

    def read(self, user):
        """ Returns the file content of the file only if the user who wants to read is an admin or the file author."""
        if user.user_name == self.author or user.isAdmin:
            return self.body
        else:
            return None


class TextFile(File):

    def count(self, sub_string):
        return self.body.count(sub_string)


class BinaryFile(File):
    pass


class ImageFile(BinaryFile):
    def get_dimensions(self):
        pass


class Directory:
    """A directory class. Represent a directory, can contain any kind of files or directories.

    Attributes:
            files_list (list): holds files
    """

    def __init__(self):
        self.files_list = []

    def add_file(self, file):
        self.files_list.append(file)

    def remove_file(self, file):
        self.files_list.remove(file)


class User:
    """A user class. Represent a user in file systems, can be admin or regular user

    Args:
        user_name (str): name of the user.
        password (str): password.
        is_admin (bool): 'True' if the user is an admin.
    """

    def __init__(self, user_name, password, is_admin=False):
        self.user_name = user_name
        self.password = password
        self.is_admin = is_admin
