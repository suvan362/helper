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

dsifiles = ['unlau08.zip', 'file2', 'file3']

#initial messages
print('Welcome to hiyacfw helper (some name) v1.0')
time.sleep(1)
print('This version is early in developemt.')
time.sleep(1)
print('Proceed with caution')
time.sleep(1)
input('Press enter to continue')
print('Please install all the packages mentioned below. They can all be found in the README.')
print('1. The latest release of Unlaunch')
print('2. We are currently using Unlaunch v0.8, as 0.9 has bugs preventing HiyaCFW from working')
print('3. The latest release of HBMenu')
print('4. The latest release of ugopwn or flipnote lenny')
print('5. The latest release of twlnf')
print('6. The latest release of DSi SRL Extractor')
input('Press enter to continue')

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
