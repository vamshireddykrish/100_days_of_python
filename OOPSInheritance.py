class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("It's OPEN")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("ITS closed dude")
        self.opened = False


class NetworkStream(Stream):
    def read(self):
        print("ITS READING THE DATA")


def read():
    print("Its Reading Dude")


class FileStream(Stream):
    pass
