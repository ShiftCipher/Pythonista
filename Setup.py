# -*- coding: utf-8 -*-
import os
import json
import urllib2

print "Welcome to the World of Tomorrow"
computer = 'DataiPhone'
computer = 'DataiMac'
computer = 'DataMacMini'
computer = 'DataMacBookPro'

'''
while computer == '':
  computer = raw_input("What's your Computer Name?\n").strip()
''' 

print "*************************************"
print "Setting up your Mac"
print "*************************************"

# Create a Private Key
if not os.path.isfile(os.path.expanduser("~") + '/.ssh/id_rsa.pub'):
  print "Creating your Private Key"
  os.system('ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N "" -y')

# Set Computer Name
os.system('sudo scutil --set ComputerName "%s"' % computer)
os.system('sudo scutil --set HostName "%s"' % computer)
os.system('sudo scutil --set LocalHostName "%s"' % computer)
os.system('sudo defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string "%s"' % computer)

print "Installing Homebrew"
os.system('ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')

print "Installing Cask"
os.system('brew cask')

print "Installing Anonimous Tools"
os.system('brew install tor && brew cask install torbrowser')

print "Installing Virtualization"
print "Installing Docker"
os.system('brew install docker docker-compose docker-machine')
os.system('brew cask install docker-toolbox kitematic')
os.system('brew cask install xquartz')
os.system('\
docker pull kalilinux/kali-linux-docker \
docker pull ubuntu \
docker pull oraclelinux \
docker pull mesosphere/marathon \
')

print "Installing Vagrant"
os.system('brew cask install vagrant vagrant-manager')

print "Installing Databases"
os.system('brew install postgres redis')

# Brews Install
print "Installing Brew Apps"
os.system('brew install \
asciinema \
clib \
cmatrix \
curl \
git \
mas \
ncurses \
python \
python3 \
tmux \
wget \
zplug \
')

print "Installing Cask Apps"
os.system('brew cask install \
airserver \
duet \
screens-connect \
blender \
cakebrew \
dash \
etcher \
hyper \
gitup \
google-chrome \
jaxx \
now \
pdfexpert \
shuttle \
sketch-toolbox \
spectacle \
')

os.system('brew cask install \
lmms \
sunvox \
baudline \
hydrogen \
milkytracker \
vcv-rack \
')

os.system('brew cask install \
sublime-text \
cheatsheet \
invisionsync \
adobe-creative-cloud \
iphone-backup-extractor \
framer \
freecad \
fastlane \
fritzing \
framer-modules \
mactex \
texmaker \
kicad \
openemu \
origami \
principle \
schnapps \
textmaker \
mapbox-studio \
arduino \
importio \
xquartz \
')

# Install Mac Store Apps
print "Installing Mac Store Apps"
os.system('mas install 425424353')   # The Unarchiver
os.system('mas install 1037126344')  # Apple Configurator 2
os.system('mas install 970502923')   # Typeeto
os.system('mas install 407963104')   # Pixelmator
os.system('mas install 404705039')   # Graphic
os.system('mas install 497799835')   # Xcode

os.system('mas install 1176074088')  # Termius
os.system('mas install 409201541')   # Pages
os.system('mas install 409203825')   # Numbers
os.system('mas install 434290957')   # Motion
os.system('mas install 1176895641')  # Spark
os.system('mas install 939343785')   # Icon Set Creator
os.system('mas install 1153157709')  # SpeedTest
os.system('mas install 425264550')   # BlackMagic Disk
os.system('mas install 780544053')   # Hider 2
os.system('mas install 935235287')   # Encrypto

# ZSH Configuration
os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')
os.system('pip3 install --user powerline-status')
os.system('git clone https://github.com/powerline/fonts.git --depth=1 ~/fonts')
os.system('sh ~/fonts/install.sh')
os.system('rm -rf ~/fonts')
os.system('git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k')
os.system('git clone https://github.com/zsh-users/zsh-syntax-highlighting.git')
os.system('echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc')
os.system('git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions')
os.system('curl -L git.io/antigen > ~/antigen.zsh')
os.system('echo "source ~/antigen.zsh" >> ~/.zshrc')


# Install NVM and Node.js
print "Installing Node.js"
os.system('brew install node')
os.system('brew install nvm')
os.system('export NVM_DIR="$HOME/.nvm"')
os.system('. "/usr/local/opt/nvm/nvm.sh"')
os.system('brew install yarn --without-node')
os.system('nvm install node')
os.system('nvm use node')
os.system('brew link --overwrite node')

# Installing Yarn Packages
print "Installing Yarn Packages"
os.system('brew upgrade yarn')

# Installing Node CLI Packages
print "Installing Node CLI Packages"
os.system('npm install -g \
node-gyp \
express-generator \
pug \
pug-cli \
gulp-cli \
nodemon \
browser-sync \
bower \
webpack \
gulp \
postcss-cli \
autoprefixer \
uglify-js \
clean-css \
imagemin \
imagemin-cli \
node-inspector \
pm2 \
istanbul \
babel-cli \
testling \
karma-cli \
browserify \
tap-colorize \
caminte-cli\
ios-deploy \
')

# OSX Tweaks & Essentials
print "Installing Quicklook Helpers"
os.system('brew cask install qlmarkdown quicklook-csv quicklook-json')

print "Installing Fonts"
os.system('brew cask install robofont fontforge birdfont skyfonts trufont')

print "Installing iOS Tools"
os.system('sudo gem install cocoapods')

# Oh-My-ZSH. Dracula Theme for iTerm2 needs to be installed manually

os.system('pip install pygments nyx speedtest-cli')

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
os.system('defaults write NSGlobalDomain NSWindowResizeTime -float 0.0')
os.system('defaults write com.apple.dock expose-animation-duration -float 0.0')
os.system('defaults write com.apple.dock autohide-time-modifier -float 0.0')
os.system('defaults write NSGlobalDomain com.apple.springing.delay -float 0.0')

# Make Google Chrome the default browser
os.system('open -a "Google Chrome" --args --make-default-browser')

# Clean Up
os.system('brew cleanup && brew cask cleanup')

'''
print "*************************************"
print "Your SSH Public Key Is:"
with open(os.path.expanduser("~") + '/.ssh/id_rsa.pub', 'r') as f:
  print f.read()

print "Installing Atom Plugins"
os.system('apm install \
jshint \
lenguage-api-blueprint \
linter-api-blueprint \
file-icons \
git-time-machine\
jupyter-notebook \
language-pug \
file-icons \
git-time-machine\
jupyter-notebook \
language-pug \
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
''' 


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
