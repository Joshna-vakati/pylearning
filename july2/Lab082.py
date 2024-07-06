# # supported modes
#
# r: read mode
#
# open an existing file for a read operation
#
# w: write mode
#
# open an existing file for a write operation.
# If the file already contains some data, then it will be overridden but
# if the file is not present then it creates the file as well
#
#
# a: append mode
#
# open an existing file for append operation. It won’t override existing data
#     but it will add data at the end of file
#
# r+ : read and write mode
#
# To read and write data into the file.
# This mode does not override the existing data,
# but you can modify the data starting from the beginning of the file.
#
# It will not create a new file if the file does not exist.
# It will not create a new file if the file does not exist.
#
# w+ : write and read mode
#
# To write and read data.
# It overwrites the previous file if one exists,
# it will truncate the file to zero length or create a file if it does not exist
#
# a+ : append and read mode
#
# To append and read data.
# It does not override the existing data but