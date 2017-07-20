pkg install -y
pkg update
pkg install -y xorg
pkg install -y curl
pkg install -y git
pkg install -y i3 i3lock i3status dmenu
pkg install -y tmux
pkg install -y htop bsdinfo

cat <<EOT>> /etc/rc.conf
hald_enable="YES"
dbus_enable="YES"
EOT

cat <<EOT>> /root/.xinitrc
exec i3
exec dmenu_run -b
xsetroot -name "XYZOS"
EOT

cat <<EOT>> /.Xresources
xterm*background:black
xterm*foreground:white
EOT

# Alt i3 Button
