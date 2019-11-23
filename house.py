from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import sys
import keyboard
import time
import mcpi.block as block

#высота здания

h=10
distance=5
pos=mc.player.getPos()
x=round(pos.x)
y=round(pos.y)
z=round(pos.z)


mc.setBlocks(340,70,94,340+distance,70+h,94,7)
mc.setBlocks(340+distance,70,94,340,70+h,94+distance,7)
mc.setBlocks(346+distance,67,99,340,70+h,94+distance,7)
