# Connect over TCP to the following server: 'localhost', 10000
# Initiate communication with 'GET' to retrieve the encrypted messages.
# Then return the messages decrypted to the server,
# taking care to ensure each message is split on to a newline
#
import socket

# Define the server host and port
server_host = 'localhost'
server_port = 10000

# Create a socket to connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    try:
        # Connect to the server
        client_socket.connect((server_host, server_port))

        # Send a 'GET' request
        client_socket.sendall(b'GET')

        # Receive and print the server's response
        response = client_socket.recv(1024).decode('utf-8')
        print("Server Response:")
        print(response)

    except ConnectionRefusedError:
        print(f"Connection to {server_host}:{server_port} refused. Ensure the server is running.")
    except Exception as e:
        print(f"Error: {e}")
Server Response:
Return the below codes decrypted. Each sentence should be split with a newline
KYVZI JYLKKVIJ NYZCV YZJ URLXYKVI KYV GIZETVJJ GRJJVU SP FE YVI NRP
WATCHING HIM WHEN THE GAME WAS FINISHED THE MAN BECKONED TO ALADDIN TO
MXX TUE TQMDF

encrypted_messages = [
    "KYVZI JYLKKVIJ NYZCV YZJ URLXYKVI KYV GIZETVJJ GRJJVU SP FE YVI NRP",
    "WATCHING HIM WHEN THE GAME WAS FINISHED THE MAN BECKONED TO ALADDIN TO",
    "MXX TUE TQMDF"
]

# Define a function to decrypt a Caesar cipher
def decrypt_caesar(ciphertext, shift):
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr(((ord(char) - shift - 65) % 26) + 65) if char.isupper() else chr(((ord(char) - shift - 97) % 26) + 97)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

# Decrypt and split the messages by newline characters
decrypted_messages = []
for message in encrypted_messages:
    # Determine the Caesar cipher offset from the first character of the message
    shift = ord(message[0]) - ord('A') if message and message[0].isupper() else ord(message[0]) - ord('a')
    
    # Decrypt the message
    decrypted_message = decrypt_caesar(message, shift)
    decrypted_messages.append(decrypted_message)

# Join the decrypted messages with newline characters
final_decrypted_text = '\n'.join(decrypted_messages)

# Print the decrypted messages
print(final_decrypted_text)
AOLPY ZOBAALYZ DOPSL OPZ KHBNOALY AOL WYPUJLZZ WHZZLK IF VU OLY DHF
AEXGLMRK LMQ ALIR XLI KEQI AEW JMRMWLIH XLI QER FIGOSRIH XS EPEHHMR XS
ALL HIS HEART
