def is_valid_url(url):
    # Check if the URL starts with a valid string
    valid_strings = ["http", "https"]
    has_valid_string = any(url.startswith(string) for string in valid_strings)

    # if it does not start with valid string, return False
    if not has_valid_string:
        return False

    # Check if there is a valid domain(the url must have two parts(the one with HTTP or HTTPS)
    parts = url.split("://")
    if len(parts) != 2:
        return False
    # Check if domain is non-empty string
    domain = parts[1].split("/")[0]
    if not domain:
        return False

    # return True if none of the conditions above have been met (False still has not been returned)
    return True
