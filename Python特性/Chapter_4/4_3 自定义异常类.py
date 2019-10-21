class BaseValidationError(ValueError):
    pass


class NameTooShortError(BaseValidationError):
    pass


class NameTooLoogError(BaseValidationError):
    pass


class NameTooCuteError(BaseValidationError):
    pass


def validate(name):
    if len(name) < 6:
        raise NameTooShortError(name)
    if len(name) > 10:
        raise NameTooLoogError(name)


validate('arman')
