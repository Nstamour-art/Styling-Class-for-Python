class tStyles:
    """
    A class to define common terminal styles and characters for easier legibility and styling of terminal outputs.
    """

    # Names some common terminal characters for easier legibility
    tab = "\t"
    new_line = "\n"

    # define the separator styles
    sep_char = "-"
    sep = sep_char * 20
    tab_sep = tab + sep
    big_sep = sep_char * 40
    small_sep = sep_char * 5

    indent_char = ">>"

    reset = "\33[0m"  # defines the reset character for all styling

    # Define common styling for terminal outputs
    bold = "\33[1m"
    italic = "\33[3m"
    underline = "\33[4m"

    # Define foreground colour options
    red = "\33[31m"
    green = "\33[32m"
    yellow = "\33[33m"
    blue = "\33[34m"
    magenta = "\33[35m"
    cyan = "\33[36m"

    # Defines the terminal bright modified colours
    bright_red = "\33[91m"
    bright_green = "\33[92m"
    bright_yellow = "\33[93m"
    bright_blue = "\33[94m"
    bright_magenta = "\33[95m"
    bright_cyan = "\33[96m"

    # define some common special colour headers
    header_red = "\33[37;41m"
    header_blue = "\33[1;37;44m"
    header_magenta = "\33[1;37;45m"
    header_green = "\33[1;37;42m"
    header_orange = "\33[1;37;48;5;210m"
