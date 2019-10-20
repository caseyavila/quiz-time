import os

if __name__ == "__main__":
    mode = input('"Create" or "Study"?')

    if mode == "Create":
        import create
    elif mode == "Study":
        import study