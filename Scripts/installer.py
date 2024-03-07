import sys
import time
import platform
import distro
import os

## https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input/3041990#3041990
def query(question, default="yes"):
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

## https://ask.replit.com/t/how-do-i-make-colored-text-in-python/29288/13
def print_rgb(text, r, g, b):
    color_code = f"\033[38;2;{r};{g};{b}m"
    print(f"{color_code}{text}\033[0m")


os.system("clear")
logo = '''
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
'''

print_rgb(logo + "\n\n\nDevice Qualification Checks \n", 158, 34, 230)

print_rgb("Device Check Beginning! \n", 25 ,70, 255)

if platform.machine() == "aarch64" or platform.machine() == "armv1l":
    print_rgb("ARM Device Detected", 0, 255, 0)
else:
    print_rgb("ARM Device not Detected!",255,20,20)
    os.system("clear")
    print_rgb(logo + "\n\n\nDevice Qualification FAILED: ARM NOT DETECTED \n", 255, 10, 10)
    print_rgb("DEVICE NOT QUALIFIED! PROGRAM WILL EXIT IN 5 SECONDS",255,0,0)
    time.sleep(5)
    exit(0)

print("\n")

print_rgb("Validating OS!", 34, 230, 86)

if distro.name(pretty=True) == "Debian GNU/Linux 12 (bookworm)":
     print_rgb("DEBIAN 12 Detected", 0,255,0)
else:
     os.system("clear")
     print_rgb(logo + "\n\n\nDevice Qualification FAILED: DEBIAN 12 NOT DETECTED!\n", 255, 10, 10)
     print_rgb("DEVICE NOT QUALIFIED! PROGRAM WILL EXIT IN 5 SECONDS",255,0,0)
     time.sleep(5)
     exit(0)

print("\n")

print_rgb("Device Qualified! Screen Clearing in 5 Seconds!", 0, 255, 0)
time.sleep(1)
print("4.")
time.sleep(1)
print("3.")
time.sleep(1)
print("2.")
time.sleep(1)
print("CLEARING SCREEN")
os.system("clear")

print_rgb(logo + "\n\n\nInstallation \n", 158, 34, 230)

if query("Do you wish to begin installation?", default="yes") == False:
    os.system("clear")
    print_rgb(logo + "\n\n\n Install Manually Exited!\n", 255, 10, 10)
    print_rgb("PROGRAM WILL EXIT IN 5 SECONDS",255,0,0)
    time.sleep(5)
    exit(0)
print_rgb("\nInstallation Beginning! Dependancies are now installing!", 255,255,0)
## END POINT (Need to research on what items ill use to make the FunnelPi)
