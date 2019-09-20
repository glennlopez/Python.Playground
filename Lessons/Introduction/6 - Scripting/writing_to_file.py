# reading a file
f = open('my_file.txt', 'r')
file_data = f.read()
f.close()

print(file_data)

# writing a file
f = open('new_file.txt', 'w')
f.write('Hello nurse!')
f.close()