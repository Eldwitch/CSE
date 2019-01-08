class Style:
    BOLD = '\033[1m'
    END = '\033[0m'


print(Style.BOLD + 'This is my text string.' + Style.END)
print("This is my text string.")
