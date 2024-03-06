import sys
import platform
import distro

## https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input/3041990#3041990
def query(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")

print('''
----------------------------------------------------------------------------------------------------------
|                                                                                                        |
| ______     __  __       ___   __       ___   __       ______       __           ______     ________    |
|/_____/\   /_/\/_/\     /__/\ /__/\    /__/\ /__/\    /_____/\     /_/\         /_____/\   /_______/\   |
|\::::_\/_  \:\ \:\ \    \::\_ \  \ \   \::\_\   \ \   \::::_\/_    \:\ \        \:::_ \ \  \__.::._\/   |
| \:\/___/\  \:\ \:\ \    \:. `-\  \ \   \:. `-\  \ \   \:\/___/\    \:\ \        \:(_) \ \    \::\ \    |
|  \:::._\/   \:\ \:\ \    \:. _    \ \   \:. _    \ \   \::___\/_    \:\ \____    \: ___\/    _\::\ \__ |
|   \:\ \      \:\_\:\ \    \. \`-\  \ \   \. \`-\  \ \   \:\____/\    \:\/___/\    \ \ \     /__\::\__/\|
|    \_\/       \_____\/     \__\/ \__\/    \__\/ \__\/    \_____\/     \_____\/     \_\/     \________\/|
|                                                                                                        |
----------------------------------------------------------------------------------------------------------
                                             Installer Script                                             
''')

print("\n\n\n This script will setup this device for use as a FunnelPi, aka a raspberry pi powered weather station ")

if query("Begin the install?", default="yes") == False:
    exit(0)

print("\n")

print("Checking Device!")

if platform.machine != "aarch64" or platform.machine != "armv7l":
    print("ARM Not Detected!")
    exit(0)

print("\n")

print("Checking OS!")

print(distro.name(pretty=True))