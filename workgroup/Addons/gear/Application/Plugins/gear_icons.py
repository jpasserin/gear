'''

    This file is part of GEAR.

    GEAR is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/lgpl.html>.

    Author:     Jeremie Passerin      geerem@hotmail.com
    Company:    Studio Nest (TM)
    Date:       2010 / 11 / 15

'''

## @package gear_icons.py
# @author Jeremie Passerin
#

##########################################################
# GLOBAL
##########################################################
from gear.xsi import xsi, c
import gear.xsi.icon as icon

##########################################################
# XSI LOAD / UNLOAD PLUGIN
##########################################################
# ========================================================
def XSILoadPlugin(in_reg):

    in_reg.Author = "Jeremie Passerin"
    in_reg.Name = "gear_icons"
    in_reg.Email = "geerem@hotmail.com"
    in_reg.URL = "http://www.jeremiepasserin.com"
    in_reg.Major = 1
    in_reg.Minor = 0

    in_reg.RegisterCommand("gear_DrawCube","gear_DrawCube")
    in_reg.RegisterCommand("gear_DrawPyramid","gear_DrawPyramid")
    in_reg.RegisterCommand("gear_DrawSquare","gear_DrawSquare")
    in_reg.RegisterCommand("gear_DrawFlower","gear_DrawFlower")
    in_reg.RegisterCommand("gear_DrawCircle","gear_DrawCircle")
    in_reg.RegisterCommand("gear_DrawCylinder","gear_DrawCylinder")
    in_reg.RegisterCommand("gear_DrawCompas","gear_DrawCompas")
    in_reg.RegisterCommand("gear_DrawFoil","gear_DrawFoil")
    in_reg.RegisterCommand("gear_DrawDiamond","gear_DrawDiamond")
    in_reg.RegisterCommand("gear_DrawLeash","gear_DrawLeash")
    in_reg.RegisterCommand("gear_DrawCubeWithPeak","gear_DrawCubeWithPeak")
    in_reg.RegisterCommand("gear_DrawSphere","gear_DrawSphere")
    in_reg.RegisterCommand("gear_DrawArrow","gear_DrawArrow")
    in_reg.RegisterCommand("gear_DrawCrossArrow","gear_DrawCrossArrow")
    in_reg.RegisterCommand("gear_DrawBendedArrow","gear_DrawBendedArrow")
    in_reg.RegisterCommand("gear_DrawBendedArrow2","gear_DrawBendedArrow2")
    in_reg.RegisterCommand("gear_DrawCross","gear_DrawCross")
    in_reg.RegisterCommand("gear_DrawGlasses","gear_DrawGlasses")
    in_reg.RegisterCommand("gear_DrawLookAt","gear_DrawLookAt")
    in_reg.RegisterCommand("gear_DrawEyeArrow","gear_DrawEyeArrow")
    in_reg.RegisterCommand("gear_DrawAngleSurvey","gear_DrawAngleSurvey")
    in_reg.RegisterCommand("gear_DrawEyeBall","gear_DrawEyeBall")
    in_reg.RegisterCommand("gear_DrawRectangleCube","gear_DrawRectangleCube")
    in_reg.RegisterCommand("gear_DrawMan","gear_DrawMan")
    in_reg.RegisterCommand("gear_DrawNull","gear_DrawNull")

    return True

# ========================================================
def XSIUnloadPlugin(in_reg):

    strPluginName = in_reg.Name
    xsi.LogMessage(str(strPluginName) + str(" has been unloaded."), c.siVerbose)

    return True

##########################################################
# EXECTUTE
##########################################################
# ========================================================
## Cube
def gear_DrawCube_Execute():

    crv = icon.cube()
    xsi.SelectObj(crv)

    return crv

# ========================================================
## Pyramid
def gear_DrawPyramid_Execute():

     crv = icon.pyramid()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Square
def gear_DrawSquare_Execute():

     crv = icon.square()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Flower
def gear_DrawFlower_Execute():

     crv = icon.flower()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Circle
def gear_DrawCircle_Execute():

     crv = icon.circle()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Cylinder
def gear_DrawCylinder_Execute():

     crv = icon.cylinder()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Compas
def gear_DrawCompas_Execute():

     crv = icon.compas()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Foil
def gear_DrawFoil_Execute():

     crv = icon.foil()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Diamond
def gear_DrawDiamond_Execute():

     crv = icon.diamond()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Leash
def gear_DrawLeash_Execute():

     crv = icon.leash()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Cube With Peak
def gear_DrawCubeWithPeak_Execute():

     crv = icon.cubewithpeak()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Sphere
def gear_DrawSphere_Execute():

     crv = icon.sphere()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Arrow
def gear_DrawArrow_Execute():

     crv = icon.arrow()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Cross Arrow
def gear_DrawCrossArrow_Execute():

     crv = icon.crossarrow()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Bended Arrow
def gear_DrawBendedArrow_Execute():

     crv = icon.bendedarrow()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Bended Arrow2
def gear_DrawBendedArrow2_Execute():

     crv = icon.bendedarrow2()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Cross
def gear_DrawCross_Execute():

     crv = icon.cross()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Glasses
def gear_DrawGlasses_Execute():

     crv = icon.glasses()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Look At
def gear_DrawLookAt_Execute():

     crv = icon.lookat()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Eye Arrow
def gear_DrawEyeArrow_Execute():

     crv = icon.eyearrow()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Angle Survey
def gear_DrawAngleSurvey_Execute():

     crv = icon.anglesurvey()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Eye Ball
def gear_DrawEyeBall_Execute():

     crv = icon.eyeball()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Rectangle Cube
def gear_DrawRectangleCube_Execute():

     crv = icon.rectanglecube()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Man
def gear_DrawMan_Execute():

     crv = icon.man()
     xsi.SelectObj(crv)

     return crv

# ========================================================
## Null
def gear_DrawNull_Execute():

     crv = icon.null()
     xsi.SelectObj(crv)

     return crv
