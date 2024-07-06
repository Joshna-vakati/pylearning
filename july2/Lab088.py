# files can broadly be categorized into two types based on their mode of operation:
#
# Text Files: These store data in plain text format. Examples include .txt files.

# Binary Files: These store data in binary format, which is not human-readable.
# Examples include images, videos, and executable files.


#  read a binary file
f = open("demobinaryfile.png", "wb")
f.write(b"this is a binary file\n")
f = open("demobinaryfile.png", "rb")
print(f.read())



