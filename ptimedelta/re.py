import re

NUMBER_REGEX = r"\d+(\.\d+)?"


def _create_regex(name, specifier, number_regex=NUMBER_REGEX):
    return r"(?P<{name}>{number}){specifier}".format(
        name=name, specifier=specifier, number=number_regex
    )


TIME_PERIOD_REGEX = (
    r"^"
    r"({days})?"
    r"({hours})?"
    r"({minutes})?"
    r"({seconds})?"
    r"({milliseconds})?"
    r"$"
).format(
    days=_create_regex("days", specifier="d"),
    hours=_create_regex("hours", specifier="h"),
    minutes=_create_regex("minutes", specifier="m"),
    seconds=_create_regex("seconds", specifier="s"),
    milliseconds=_create_regex("milliseconds", specifier="ms"),
)

TIME_PERIOD_PATTERN = re.compile(TIME_PERIOD_REGEX)
