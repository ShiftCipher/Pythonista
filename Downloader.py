import os
from time import sleep

file = open("Pluralsight.txt", "r")
counter = 0

for course in file:
	
	if counter % 2 == 0: 
		username = 'andrew-thomps'
		password = 'Shockwave7'
	else 
		username = ''
		password = ''

    if course.startswith( '#' ):
    	counter = counter + 1
    	pass
    elif course.startswith( ' ' ):
    	counter = counter + 1
    	pass
    else:
    	os.system('youtube-dl --min-sleep-interval 120 --max-sleep-interval 180 --username ' +  username + ' --password ' + password + ' -o  "/Volumes/LaCie/Pluralsight/Download/%(playlist_title)s/%(playlist_index)s-%(title)s.%(ext)s" ' + course)
    	counter = counter + 1