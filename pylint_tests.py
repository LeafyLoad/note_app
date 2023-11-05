import os


print('pylint database.py checking')
os.system('python -m pylint database.py')
print('pylint menu_executor.py checking')
os.system('python -m pylint menu_executor.py')
print('pylint main.py checking')
os.system('python -m pylint main.py')