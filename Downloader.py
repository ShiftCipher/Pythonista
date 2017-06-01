import os

username = 'danielfelipe-tara73'
password = 'Shockwave7'

while username == '':
    username = raw_input("What's your Username?\n").strip()

while password == '':
    password = raw_input("What's your Password?\n").strip()

file = open("Courses.txt", "r")

for course in file:
    coursename = course.split("/")
    coursename = coursename.pop()
    os.system('youtube-dl --sleep-interval 35 --max-sleep-interval 120 --username ' +  username + ' --password ' + password + ' -o  "/Volumes/LaCie/Pluralsight/%(playlist_title)s/%(playlist_index)s-%(title)s.%(ext)s" ' + course)
