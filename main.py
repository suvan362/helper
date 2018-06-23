'''
dsi cfw helper v1.0
'''

#import modules
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

try:
  import os
except ImportError:
  install('os')
  
try:
  from string import ascii_lowercase
except ImportError:
  install('string')
  
alphabet = list(ascii_lowercase)
dsifiles = ['unlau08.zip', 'hbmenu-0.7.1.tar.bz2','twlnf-v0.3.1a.7z','dsi_srl_extract.zip']

#initial messages
print('Welcome to hiyacfw helper (some name) v1.0')
print('This version is early in developemt.')
print('Proceed with caution.')
input('Press enter to continue.')
print('Please install all the packages mentioned below. They can all be found in the README.')
print('1. Unlaunch v0.8. We are using 0.8 as 0.9 has bugs preventing HiyaCFW from working.')
print('2. The latest release of HBMenu.')
print('3. The latest release of ugopwn or flipnote lenny.')
print('4. The latest release of twlnf.')
print('5. The latest release of DSi SRL Extractor.')
input('Press enter to continue.')

#establishes downloads dir
while True:
  ans = input('Are you going to use the default downloads folder for your downloads? [Y/N]').lower()
  if ans in ['y', 'yes', 'yep', 'yeah why not', 'alright', 'fine']:
    dwndir = os.environ['USERPROFILE'] + '\\Downloads\\'
    break
  elif ans in ['n', 'no', 'nope', 'no way', 'not a chance', 'not happening']:
    print('Please enter the directory you will download the files to.')
    dwndir = input('')
    break
    
#establishes sd card drive    
while True:
  print('Please enter your SD Card drive letter. ex: `G`, `H`, `I`')
  sddrive = input('').lower()
  if sddrive in alphabet[2:] or alphabet[:2]:
    break
    
#checks if all files needed for program are downloaded.
for filename in dsifiles:
  checkA = os.path.exists(dwndir + filename)
  checkB = os.path.isfile(dwndir + filename)
  if checkA and checkB:
    pass
  else:
    print(filename + ' not found.')
    input('Press enter to end the program. ')
    quit()


print('Enter 1 if you have ugopwn installed.')
print('Enter 2 if you have flipnote lenny installed.')
ans = input('')

while True:
  if ans == '1':
    checkA = os.path.exists(dwndir + 'ugopwn.zip' )
    checkB = os.path.isfile(dwndir + 'ugopwn.zip')
    if checkA and checkB:
      break
    else:
      print('ugopwn not found.')
      input('Press enter to end the program. ')
      quit()

  elif ans == '2':
   checkA = os.path.exists(dwndir + 'FlipNote-Lenny.zip')
   checkB = os.path.isfile(dwndir + 'FlipNote-Lenny.zip')
   if checkA and checkB:
    break
   else:
    print('flipnote lenny not found.')
    input('Press enter to end the program. ')
    quit()
