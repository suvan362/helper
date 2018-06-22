print(' welcome to hiyacfw installer (some name) ')
print(' v1.0')
print(' this version is ealry in developemt. Proceed with caution')

while True:
  
  ans = input('Are you going to use the default downloads folder for your downloads? [Y/N]').lower()
  if ans in ['y', 'yes', 'yep', 'yeah why not', 'alright', 'fine']:
    break
  elif ans in ['n', 'no', 'nope', 'no way', 'not a chance', 'not happening']:
    dwndir = 'C:\\' + input('Downloads directory = C:\\')
    # %USERPROFILE%\Downloads\ by default
    break
