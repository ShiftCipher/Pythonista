pkg update
pkg install -y xorg
pkg install -y git
pkg install -y i3 i3status dmenu
pkg install -y tmux
pkg install -y htop bsdinfo

cat <<EOT>> /etc/rc.conf
hald_enable="YES"
dbus_enable="YES"
EOT

cat <<EOT>> /.Xresources
XTerm*background:black
XTerm*foreground:white
XTerm*faceName: DejaVuSansMono
XTerm*faceSize: 12
XTerm.vt100.locale: true
EOT

cat <<EOT>> /root/.xinitrc
xsetroot -name "MR.DATA"
xrdb -merge ~/.Xresources
exec i3
exec dmenu
setxkbmap -layout es -variant mac
EOT

cat <<EOT>> /etc/profile
LANG=es_ES.UTF-8;
export LANG
MM_CHARSET=UTF-8;
export MM_CHARSET
LC_ALL=es_ES.UTF-8;
export LC_ALL
CHARSET=UTF-8;
export CHARSET
EOT

pkg install -y zsh
chsh -s zsh
zsh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

pkg install python
pkg install py27-pip

# Alt i3 Button
