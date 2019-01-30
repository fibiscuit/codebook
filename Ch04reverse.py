# Reverse Cipher, via No Starch Press, "Cracking Codes with Python"
# one day I will stop thinking of commenting on codes as being like tagging on Tumblr
# but today is not that day

message = "Three can keep a secret, if two of them are dead."
translated = ""

i = len(message) - 1
while i >= 0:
	translated = translated + message[i]
	i = i - 1
	
print(translated)

#Struan if you're reading this remind me to ask you about square brackets