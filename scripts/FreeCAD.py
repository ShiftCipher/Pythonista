# Macro Begin: C:\Users\Windows\AppData\Roaming\FreeCAD\Export.FCMacro +++++++++++++++++++++++++++++++++++++++++++++++++
import FreeCAD
import Mesh
import getpass

user = getpass.getuser()

counter = 1

for obj in FreeCAD.ActiveDocument.Objects:
  objs =[]
  objName = obj.Name
  objs.append(FreeCAD.getDocument("Unnamed").getObject(objName))
  Mesh.export(objs,"C:/Users/" + user + "/Desktop/" + str(counter) + ".obj")
  del objs
  counter = counter + 1
  FreeCAD.ActiveDocument.recompute()

