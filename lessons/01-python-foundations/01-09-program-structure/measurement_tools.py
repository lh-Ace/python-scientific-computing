def offset_reading(value, offset):
    return value + offset

def within_limits(reading, minimum, maximum):
    if minimum <= reading <= maximum:
        return True
    else:
        return False

if __name__ == "__main__":
    print("Initializing measurement tools")
    print("Measurement tools ready")
    print(f"Module name: {__name__}")
    print("Running measurement tools directly")
    print(within_limits(22, 18, 26))