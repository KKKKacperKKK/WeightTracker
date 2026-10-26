class EmailAlreadyExists(Exception):
    """E-mail has been taken."""


class InvalidEmailPassword(Exception):
    """Invalid e-mail or password."""


class InvalidAccessToken(Exception):
    """Token damaged or expired."""