pkg install -y
pkg update
pkg install -y xorg
pkg install -y zsh
pkg install -y curl
pkg install -y git
pkg install -y i3 i3lock i3status dmenu
pkg install -y tmux
pkg install -y htop bsdinfo
pkg install -y terminology

cat <<EOT>> /etc/rc.conf
hald_enable="YES"
dbus_enable="YES"
EOT

cat <<EOT>> /root/.xinitrc
exec i3
exec dmenu_run
xsetroot -name "XYZOS"
EOT

chsh -s zsh
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
