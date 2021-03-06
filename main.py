'''
dsi cfw helper v1.0
'''

#import modules
try:
  from pip import main as pipmain
except:
  try:
    from pip._internal import main as pipmain 
  except ImportError:
    input('pip not installed! pip must be installed to run this program. Press enter to end the program.')
    quit()

def install(package):
  pipmain(['install', '--user', package])

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
  
dsifiles = ['unlau08.zip', 'hbmenu-0.7.1.tar.bz2', 'fwtool.nds']

#initial messages
print('Welcome to hiyacfw helper (some name) v1.0')
print('This version is early in developemt.')
print('Proceed with caution.')
input('Press enter to continue.')
print('Please download everything mentioned below. All download links can be found in the README:')
print('')
print('1. Unlaunch v0.8. We are using 0.8 as 0.9 has bugs preventing HiyaCFW from working.')
print('2. The latest release of HBMenu.')
print('3. The latest release of ugopwn or flipnote lenny.')
print('4. The latest release of fwTool.')
print('5. The latest release of fuse-3ds.')
print('6. The latest release of OSFMount.')
print('7. The latest release of HiyaCFW.')
print('8. The latest release of NUSDownloader.')
print('9. The latest release of HiyaCFW Helper.')
print('')
print('Press enter to continue.')
input('')
print('MAKE SURE YOU HAVE READ THE README BEFORE CONTINUING.')
input('')

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

#checks if all files needed for program are downloaded.
for filename in dsifiles:
  while True:
    checkA = os.path.exists(dwndir + filename)
    checkB = os.path.isfile(dwndir + filename)
    if checkA and checkB:
      break
    else:
      print(filename + ' not found.')
      input('Press press enter once you have downloaded the file.')


print('Enter 1 if you have ugopwn installed.')
print('Enter 2 if you have flipnote lenny installed.')
ans = input('')
if ans == '1':
  while True:
    checkA = os.path.exists(dwndir + 'ugopwn.zip' )
    checkB = os.path.isfile(dwndir + 'ugopwn.zip')
    if checkA and checkB:
      break
    else:
      print('ugopwn not found.')
      input('Press press enter once you have downloaded the file.')

elif ans == '2':
  while True:
   checkA = os.path.exists(dwndir + 'FlipNote-Lenny.zip')
   checkB = os.path.isfile(dwndir + 'FlipNote-Lenny.zip')
   if checkA and checkB:
    break
   else:
    print('flipnote lenny not found.')
    input('Press press enter once you have downloaded the file.')

#establishes sd card drive    
while True:
  print('Please enter your SD Card drive letter. ex: `G`, `H`, `I`')
  sddrive = input('')
  if os.path.exists(sddrive+':\\'):
    break
  elif sddrive == 'c':
    print('That\'s your computer drive! Press enter to try again.')
    input('')
  else:
    print('The specified drive does not exist. Press enter to try again.')
    input('')
    
print('Setup complete!')
input('Press enter start the program.')

#extract ugopwn content to sd
print('Done!')
#copy fwtool.nds to sd
print('Done!')
#extract boot.nds from hbmenu.tar.bz2/hbmenu to sd
print('Done!')

print('You may now eject your SD card and insert it in your DSi.')
print('Follow the steps under "Creating a NAND backup" @ dsi.cfw.guide')
print('Press enter once you have completed these steps.')
input('')

print('Insert your sd back into your computer (make sure to use the same port if you have multiple).')
print('Press enter once your sd is inserted.')
input('')

#extract unlaunch.dsi to sd as unlaunch.nds
print('Done!')

print('Insert your sd back in your DSi then coninue from step 5 of "Installation".')
print('Press enter once you have completed these steps.')
input('')


