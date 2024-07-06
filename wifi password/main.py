import subprocess


# Function to retrieve WiFi passwords on Windows
def get_wifi_passwords():
    try:
        # Run the netsh command to list WiFi profiles
        result = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output=True, text=True, check=True)

        # Get the output of the command
        output = result.stdout

        # Extract profile names from the output
        profile_names = [line.split(":")[1].strip() for line in output.split("\n") if "All User Profile" in line]

        # Iterate through each profile and retrieve its password
        for profile in profile_names:
            try:
                # Run the netsh command to show the profile key (password)
                result = subprocess.run(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear'], capture_output=True,
                                        text=True, check=True)

                # Get the output of the command
                output = result.stdout


                # Find the line containing the Key Content (password)
                password_line = [line for line in output.split("\n") if "Key Content" in line][0]

                # Extract the password from the line
                password = password_line.split(":")[1].strip()

                # Print the profile name and password
                print(f"WiFi Network: {profile}, Password: {password}")
            except Exception as e:
                print(f"Error retrieving password for {profile}: {e}")
    except Exception as e:
        print(f"Error retrieving WiFi profiles: {e}")


# Call the function to retrieve WiFi passwords
get_wifi_passwords()
