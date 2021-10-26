import maya.cmds as cmds

cmds.polySphere(axis=[0,1,0], radius=2,
                subdivisionsX=20, subdivisionsY=20)
cmds.move(0,1,0)

cmds.polySphere(axis=[0,1,0], radius=1.5,
                subdivisionsX=20, subdivisionsY=20)
cmds.move(0,3.5,0)

cmds.polySphere(axis=[0,1,0], radius=1,
                subdivisionsX=20, subdivisionsY=20)
cmds.move(0,5.5,0)

cmds.polyCone(axis=[1,0,0], height=1.75, radius=0.15,
              subdivisionsY=15)
cmds.move(1.75,5.3,0)

cmds.polyCylinder(axis=[0,0,1], height=2.5, radius=0.1)
cmds.move(0,4.5,2)
cmds.rotate(-45,0,0)

cmds.polyCylinder(axis=[0,0,1], height=2.5, radius=0.1)
cmds.move(0,4.5,-2)
cmds.rotate(45,0,0)

cmds.polyCylinder(axis=[0,1,0], height=0.2, radius=1.5,
                  subdivisionsCaps=2)
cmds.move(0,6.1,0)
cmds.select('pCylinder3.f[80:99]')
cmds.polyExtrudeFacet(localTranslateZ=1.3)
