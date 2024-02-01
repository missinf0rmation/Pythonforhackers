# Sample Alien Zip file found at /tmp/alien-zip-2092.zip is password protected
# We have worked out they are using three digit code
# Brute force the Zip file to extract to /tmp
#
# Note: The script can timeout if this occurs try narrowing
# down your search
import zipfile
import os

zip_file_path = '/tmp/alien-zip-2092.zip'
extract_path = '/tmp'
text_file_name = 'alien-zip-2092.txt'

# Define the range of three-digit passwords to brute force
password_range = range(100, 1000)

for password in password_range:
    password_str = str(password).zfill(3)  # Convert the password to a 3-digit string

    try:
        # Attempt to extract the ZIP file with the current password
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(path=extract_path, pwd=bytes(password_str, 'utf-8'))

        # Check if the extracted text file exists
        extracted_file_path = os.path.join(extract_path, text_file_name)
        if os.path.exists(extracted_file_path):
            print(f"Password found: {password_str}")
            break  # Break out of the loop if the correct password is found

        # Clean up extracted files if the password is incorrect
        os.remove(extracted_file_path)

    except Exception as e:
        # Password was incorrect, continue trying the next one
        continue

# Print a message if the loop completes without finding the password
else:
    print("Password not found in the given range.")

