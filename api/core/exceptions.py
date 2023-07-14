
class UserNotFound(ValueError):
    def __init__(self, user_identifier):
        super().__init__(user_identifier)
        self.user_identifier = user_identifier

    def __str__(self):
        return f"User [{self.user_identifier}] not found in the database"