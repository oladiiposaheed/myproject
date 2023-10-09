import os
os.mkdir('first_directory')
print(os.listdir())
os.rmdir('first_directory')
print(os.listdir())