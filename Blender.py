import os
import bpy
import getpass

user = getpass.getuser()

for item in bpy.data.objects:  
	if item.type == "MESH":

candidates = [item.name for item in bpy.data.objects if item.type != "MESH"]

for object_name in candidates:
  bpy.data.objects[object_name].select = True

bpy.ops.object.delete()

# put the location to the folder where the objs are located here in this fashion
path_to_obj_dir = os.path.join('C:\\', 'Users', user, 'Desktop')

# get list of all files in directory
file_list = sorted(os.listdir(path_to_obj_dir))

# get a list of files ending in 'obj'
obj_list = [item for item in file_list if item[-3:] == 'obj']

# loop through the strings in obj_list and add the files to the scene
for item in obj_list:
    path_to_file = os.path.join(path_to_obj_dir, item)
    bpy.ops.import_scene.obj(filepath = path_to_file)

candidates = [item.name for item in bpy.data.objects if item.type == "MESH"]

for object_name in candidates:
	bpy.data.objects[object_name].select = True
	bpy.data.objects[object_name].scale = (0.001, 0.001, 0.001)
	bpy.data.objects[object_name].rotation_euler.x = -0.0