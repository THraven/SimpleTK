def textcheck(f):
    """this will check if the text given is a """
    def wrapper(*args, **kwargs):
        DisplayText = tk.StringVar()
        if not type(kwargs["text"]) == type(DisplayText):
            DisplayText.set(kwargs["text"])
            kwargs["text"] = DisplayText
        return f(*args, **kwargs)
    return wrapper
