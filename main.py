'''

dsi cfw helper v1.0

'''

try:
  import pip
except ImportError:
  input('pip not installed! pip must be installed to run this program. Press enter to end the program.')
  quit()

def install(package):
  pip.main(['install', package])

try:
  import time
except ImportError:
  install('time')

try:
  import os.path
except ImportError:
  install('os.path')

dsifiles = ['file1', 'file2', 'file3']

#initial messages
print('Welcome to hiyacfw helper (some name) v1.0')
time.sleep(0.5)
print('This version is early in developemt.')
time.sleep(0.5)
print('Proceed with caution')
time.sleep(0.5)

#establishes downloads dir
while True:
  ans = input('Are you going to use the default downloads folder for your downloads? [Y/N]').lower()
  if ans in ['y', 'yes', 'yep', 'yeah why not', 'alright', 'fine']:
    dwndir = '%USERPROFILE%\\Downloads\\'
    break
  elif ans in ['n', 'no', 'nope', 'no way', 'not a chance', 'not happening']:
    print(' please enter the directory of the folder.')
    dwndir = 'C:\\' + input('Downloads directory = C:\\')
    break
    
#checks if all files needed for program are downloaded
for filename in dsifiles:
  checkA = os.path.exists(dwndir + filename)
  checkB = os.path.isfile(dwndir + filename)
  if checkA and checkB:
    pass
  else:
    print('file ' + 'file_needed.zip' + ' not found')
    input('Press enter to end the program.')
    quit()
