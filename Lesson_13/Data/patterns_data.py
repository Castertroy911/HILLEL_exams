class PatternsData:
    URL_PATTERN: str = r'^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6}[\/\w\.-]*)\/?$'
    HTTPS_PATTERN: str = r'(https?:\/\/)'
    LINK_PATTERN: str = r'(https?:\/\/[\da-z\.-]+\.[a-z\.]{2,6}[\/\w\.-]*)\/?'