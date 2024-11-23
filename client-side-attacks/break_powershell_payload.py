# This script is useful for creating malicious macros for microsoft office documents
# You might be using long powershell payloads to get reverse shell.
# However for creating macros you cannot use long payloads in one line.
# So it is essential to break the payload in multiple lines
# This script will break your payload in multiple lines and display the same.

str = "<paste_your_powershell_payload_here>"

n = 50 # Number of characters in each line

for i in range(0, len(str), 50):
	print(f"Str = Str + \"{str[i:i+n]}\"")
