import subprocess
import re

# show all wifi ssid
out = subprocess.check_output("netsh wlan show profiles").decode()

# filter out only profile names
matches = re.findall(r"(All User Profiles)(.*)", out)

# list comprehension to remove any \n\t\r and spaces
profiles = [str(match[1]).split(":")[1].strip() for match in matches]

# creating fil to store the ssids
with open("password.txt", "w+") as f:
    # traversing each profile
    for profile in profiles:
        # using try catch statement to prevent crashing of trhe program when the is an eror
        try:
            # getting password usig key = clear flag
            get_pass = subprocess.check_output(f'netsh wlan show profile "{profiles}" key=clear').decode()
            # get out password line from the output
            password_by_profile = re.search(r"(Key Content)(.*)", get_pass)
            # checking if the password is present or was open
            if password_by_profile:
                password = password_by_profile.group().split(":")[1].strip()
            else:
                password = "the wifi is open"
            # writing the profile name and password to the text file
            f.write(f"{profile} : {password}\n")
        except Exception:
            print(Exception)
            continue