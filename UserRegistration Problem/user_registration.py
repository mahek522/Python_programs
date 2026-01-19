import re

class UserRegistration:

    def validate_email(self, email):
        # some text + @ + some text + . + some text
        pattern = r'.+@.+\..+'
        return re.match(pattern, email) is not None

    def validate_password(self, password):
        # length check
        if len(password) < 8:
            return False

        # Check for required character types
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'\d', password):
            return False
        if not re.search(r'[@#$%!]', password):
            return False

        return True
