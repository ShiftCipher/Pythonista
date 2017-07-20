# -*- coding: utf-8 -*-
import os
import json
import urllib2

print "Welcome to the World of Tomorrow"

name = ''
email = ''
computer = ''

# Basic Info
while name == '':
  name = raw_input("What's your Name?\n").strip()

# Basic Info
while computer == '':
  computer = raw_input("What's your Computer Name?\n").strip()

while email == '' or '@' not in email:
  email = raw_input("What's your Email?\n").strip()

print "Welcome. Sr. %s!" % name
print "You'll be asked for your password at a few points in the process"
# Sudo: Spectacle, ZSH, OSX Settings
print "*************************************"
print "Setting up your Mac"
print "*************************************"


# Create a Private Key
if not os.path.isfile(os.path.expanduser("~") + '/.ssh/id_rsa.pub'):
  print "Creating your Private Key"
  os.system('ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N "" -C "%s"' % email)


# Set computer name (as done via System Preferences → Sharing)
os.system('sudo scutil --set ComputerName "%s"' % computer)
os.system('sudo scutil --set HostName "%s"' % computer)
os.system('sudo scutil --set LocalHostName "%s"' % computer)
os.system('sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string "%s"' % computer)


# Check if Xcode Command Line Tools are installed
if os.system('xcode-select -p') != 0:
  print "Installing XCode Tools"
  os.system('xcode-select --install')
  print "*************************************"
  print "Restart your Mac to Continue"
  print "*************************************"
  exit()


# Install Brew
print "Installing Brews"
os.system('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
os.system('brew install mas curl wget python python3 git')

# Install Cask
print "Installing Brew & Brew Cask"
os.system('brew tap homebrew/services')
os.system('brew tap homebrew/versions')
os.system('brew tap caskroom/cask')
<<<<<<< HEAD:Setup.py

# Install PHP7
print "Install PHP7"
os.system('brew tap homebrew/dupes')
os.system('brew tap homebrew/homebrew-php')
os.system('brew unlink php56')
os.system('brew install php70')

# Install NVM and Node.js
print "Installing Node.js"
os.system('brew install nvm')
os.system('export NVM_DIR="$HOME/.nvm"')
os.system('. "/usr/local/opt/nvm/nvm.sh"')
os.system('brew install yarn')
os.system('nvm use system')
os.system('brew link --overwrite git node python python3')

# Install Mac Store Apps
print "Installing Mac Store Apps"
os.system('mas install 970502923') # Typeeto
os.system('mas install 407963104') # Pixelmator
os.system('mas install 1107421413') # 1Blocker
os.system('mas install 404705039') # Graphic
os.system('mas install 409201541') # Pages
os.system('mas install 1176895641') # Spark
os.system('mas install 434290957') # Motion
os.system('mas install 425424353') # The Unarchiver
os.system('mas install 409203825') # Numbers
os.system('mas install 443987910') # 1Password

# Installing Yarn Packages
print "Installing Yarn Packages"
os.system('yarn global add \
=======
os.system('brew update && brew upgrade && brew cleanup && brew cask cleanup')

# Install PHP7 
os.system('brew tap homebrew/dupes')
os.system('brew tap homebrew/homebrew-php')
os.system('brew unlink php56') 
os.system('brew install php70')

# Brew Autoupdate
print "Enabling Automatic Brew Updates & Upgrades"
os.system('brew tap domt4/autoupdate')
os.system('brew autoupdate --start --upgrade')

# Brew Install
print "Installing Brews"
os.system('brew install curl wget git-flow')

# Install Git and Ruby
print "Installing Git and Ruby"
os.system('brew install git ruby')

# Install NVM and Node.js 
print "Installing Git and Ruby"
os.system('brew install nvm')
os.system('nvm install node')
os.system('nvm use node')

# Install Python2 and Python3
os.system('brew install python python3')
os.system('brew link --overwrite git node python python3 ruby')

# Installing Node CLI Packages
print "Installing Node CLI Packages"
os.system('npm isntall -g \
node-gyp \
express-generator \
>>>>>>> 2e51b81116acc77b1f751f79c25596976298cacd:iSetup.py
pug \
pug-cli \
gulp-cli \
nodemon \
browser-sync \
bower \
<<<<<<< HEAD:Setup.py
webpack \
=======
gulp \
postcss-cli \
autoprefixer \
uglify-js \
clean-css \
imagemin \
imagemin-cli \
node-inspector \
>>>>>>> 2e51b81116acc77b1f751f79c25596976298cacd:iSetup.py
pm2 \
istanbul \
babel-cli \
testling \
karma-cli \
browserify \
<<<<<<< HEAD:Setup.py
tap-colorize
=======
tap-colorize \
caminte-cli\
>>>>>>> 2e51b81116acc77b1f751f79c25596976298cacd:iSetup.py
')

# OSX Tweaks & Essentials
print "Installing Quicklook Helpers"
<<<<<<< HEAD:Setup.py
os.system('brew cask install quicklook-csv quicklook-json')

# print "Installing Fonts"
# os.system('brew cask install robofont fontforge birdfont skyfonts trufont')

print "Installing Essential Apps"
os.system('brew cask install \
fastlane \
blender \
freecad \
kicad \
sketchup \
fritzing \
sketchup \
dropbox \
odrive \
=======
os.system('brew cask install qlmarkdown quicklook-csv quicklook-json')

print "Installing Fonts"
os.system('brew cask install robofont fontforge birdfont skyfonts trufont')

print "Installing Essential Apps"
os.system('brew cask install \
whatsapp \
blender \
freecad \
kicad \
sketchup \ 
fritzing \
sketchup \
dropbox \
>>>>>>> 2e51b81116acc77b1f751f79c25596976298cacd:iSetup.py
spectacle \
the-unarchiver \
pdfexpert \
evernote \
rescuetime \
google-chrome \
duet \
skype \
<<<<<<< HEAD:Setup.py
=======
1password \
>>>>>>> 2e51b81116acc77b1f751f79c25596976298cacd:iSetup.py
parallels-desktop \
slack \
gitter \
airserver \
beamer \
paw \
screens \
screens-connect \
reveal \
epic-games-launcher \
openemu \
ifunbox \
<<<<<<< HEAD:Setup.py
cakebrew \
gitup \
vagrant-manager \
cheatsheet \
numi \
=======
>>>>>>> 2e51b81116acc77b1f751f79c25596976298cacd:iSetup.py
')

print "Installing Designer Tools"
os.system('brew cask install \
<<<<<<< HEAD:Setup.py
invisionsync \
iconjar \
=======
adobe-creative-cloud \
adobe-photoshop-cc \
adobe-illustrator-cc \
adobe-indesign-cc \
schnapps \
invisionsync \
iconjar \
sketch-tool \
>>>>>>> 2e51b81116acc77b1f751f79c25596976298cacd:iSetup.py
sketch-toolbox \
framer-studio \
origami \
principle \
')

print "Installing Developer Tools"
os.system('brew cask install \
<<<<<<< HEAD:Setup.py
iterm2 \
atom \
=======
atom \
gitkraken \
>>>>>>> 2e51b81116acc77b1f751f79c25596976298cacd:iSetup.py
postgres \
pgadmin3 \
redis \
mamp \
<<<<<<< HEAD:Setup.py
shuttle \
webstorm \
=======
iterm2 \
shuttle \
webstorm \
phpstorm \
>>>>>>> 2e51b81116acc77b1f751f79c25596976298cacd:iSetup.py
clion \
appcode \
datagrip \
ngrok \
spyder \
')

print "Installing Atom Plugins"
os.system('apm install \
jshint \
<<<<<<< HEAD:Setup.py
lenguage-api-blueprint \
linter-api-blueprint \
file-icons \
git-time-machine\
jupyter-notebook \
language-pug \
=======
file-icons \
git-time-machine\
jupyter-notebook \
language-pug \
>>>>>>> 2e51b81116acc77b1f751f79c25596976298cacd:iSetup.py
color-picker \
hydrogen \
dash \
emmet \
git-plus \
git-status \
pigments \
source-preview-sass \
language-blade \
minimap \
linter-php \
linter \
php-server \
terminal-plus \
api-workbench \
')

print "Installing iOS Tools"
os.system('sudo gem install cocoapods')

# Oh-My-ZSH. Dracula Theme for iTerm2 needs to be installed manually
print "Installing Oh-My-Zsh with Dracula Theme"
os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')
os.system('brew install zsh-syntax-highlighting zsh-autosuggestions')
os.system('pip install pygments')

if not os.path.isfile(os.path.expanduser("~") + '/.zshrc'):
os.system('cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc &> /dev/null')

# Agnoster Theme
os.system('sed -i -e \'s/robbyrussell/agnoster/g\' ~/.zshrc &> /dev/null')
# Plugins
os.system('sed -i -e \'s/plugins=(git)/plugins=(git git-flow brew sublime python node bower npm gem pip pod docker zsh-autosuggestions zsh-syntax-highlighting colorize colored-man-pages copydir copyfile extract)/g\' ~/.zshrc &> /dev/null')

# Customizations
os.system('echo "source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ~/.zshrc')
os.system('echo "source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh" >> ~/.zshrc')
os.system('echo "alias dog=\'colorize\'" >> ~/.zshrc')

os.system('chsh -s /bin/zsh &> /dev/null')

os.system('git clone https://github.com/zenorocha/dracula-theme/ ~/Desktop/dracula-theme/')

# Random OSX Settings
print "Tweaking OSX Settings"

# Finder: show hidden files by default
#os.system('defaults write com.apple.finder AppleShowAllFiles -bool true')
# Finder: show all filename extensions
os.system('defaults write NSGlobalDomain AppleShowAllExtensions -bool true')

# Finder: allow text selection in Quick Look
os.system('defaults write com.apple.finder QLEnableTextSelection -bool true'# Check for software updates daily
os.system('defaults write com.apple.SoftwareUpdate ScheduleFrequency -int 1')
# Require password immediately after sleep or screen saver begins
os.system('defaults write com.apple.screensaver askForPassword -int 1')
os.system('defaults write com.apple.screensaver askForPasswordDelay -int 0')
# Show the ~/Library folder
os.system('chflags nohidden ~/Library')
# Don’t automatically rearrange Spaces based on most recent use
os.system('defaults write com.apple.dock mru-spaces -bool false')
# Prevent Time Machine from prompting to use new hard drives as backup volume
os.system('defaults write com.apple.TimeMachine DoNotOfferNewDisksForBackup -bool true')
# Mute startup sound
os.system('sudo nvram SystemAudioVolume=", "')


print "Tweaking System Animations"
os.system('defaults write NSGlobalDomain NSWindowResizeTime -float 0.1')
os.system('defaults write com.apple.dock expose-animation-duration -float 0.15')
os.system('defaults write com.apple.dock autohide-time-modifier -float 0.2')
os.system('defaults write NSGlobalDomain com.apple.springing.delay -float 0.5')

# Make Google Chrome the default browser
os.system('open -a "Google Chrome" --args --make-default-browser')

# Clean Up
os.system('brew cleanup && brew cask cleanup')

print "*************************************"
print "Your SSH Public Key Is:"
with open(os.path.expanduser("~") + '/.ssh/id_rsa.pub', 'r') as f:
  print f.read()
print ""

print "*************************************"
print "Remember to set up iTerm2:"
print "* Go to iTerm2 > Preferences > Profiles > Colors Tab"
print "  * Load Presets..."
print "  * Import..."
print "  * Pick Desktop > dracula-theme > iterm > Dracula.itermcolors"
print "* Go to iTerm2 > Preferences > Profiles > Text Tab"
print "  * Regular Font"
print "  * 12pt Menlo for Powerline Font"
print ""

print "*************************************"
print "Remember to restart your Mac"
print "*************************************"
