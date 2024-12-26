import os


def convert_to_binary(input):
    """take a string and convert it to a binary string"""
    return bin(int(input)).replace("0b", "")


def binary_to_hex(input):
    """take a binary string and convert to a hex string"""
    return (hex(int(input, 2))[2:]).upper()


def getOrSet(label: str, value: str) -> str:
    """Get the variable from ENVIRONMENT or set by a default value"""
    if os.getenv(label) is None:
        print(f"setting default value for env var: {label}: {value}")
        os.environ[label] = value
    else:
        print(f"take the value for env var: {label}")
    return os.environ[label]
