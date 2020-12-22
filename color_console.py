class colors:
    end = "\x1b[0m"
    black = "\x1b[1;30;40m"
    red = "\x1b[1;31;40m"
    green = "\x1b[1;32;40m"
    gold = "\x1b[1;33;40m"
    blue = "\x1b[1;34;40m"
    purple = "\x1b[1;35;40m"
    yellow = "\x1b[1;36;40m"
    white = "\x1b[1;37;40m"
    dark_blue = "\x1b[0;34;40m"
    dark_red = "\x1b[0;31;40m"
    dark_green = "\x1b[0;34;40m"

    def cprint(self, c_color: str, c_msg: str):
        print(c_color + c_msg + colors.end)