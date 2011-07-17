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

## @package gear_selectionTools.py
# @author Jeremie Passerin
#

##########################################################
# GLOBAL
##########################################################
import gear

from gear.xsi import xsi, c, XSIMath, XSIFactory

import gear.xsi.geometry as geo

##########################################################
# XSI LOAD / UNLOAD PLUGIN
##########################################################
# ========================================================
def XSILoadPlugin(in_reg):

    in_reg.Author = "Jeremie Passerin"
    in_reg.Name = "gear_selectionTools"
    in_reg.Email = "geerem@hotmail.com"
    in_reg.URL = "http://www.jeremiepasserin.com"
    in_reg.Major = 1
    in_reg.Minor = 0

    # Commands
    in_reg.RegisterCommand("gear_SymmetrizeSelection","gear_SymmetrizeSelection")
    in_reg.RegisterCommand("gear_MirrorSelection","gear_MirrorSelection")

    in_reg.RegisterCommand("gear_Select5BranchesStars", "gear_Select5BranchesStars")
    in_reg.RegisterCommand("gear_Select6MoreBranchesStars", "gear_Select6MoreBranchesStars")

    return True

# ========================================================
def XSIUnloadPlugin(in_reg):

    strPluginName = in_reg.Name
    xsi.LogMessage(str(strPluginName) + str(" has been unloaded."), c.siVerbose)

    return True

##########################################################
# SYMMETRIZE SELECTION
##########################################################
# ========================================================
def gear_SymmetrizeSelection_Execute():

    if not xsi.Selection.Count:
        gear.log("No selection", gear.sev_error)
        return

    subComp = xsi.Selection(0)
    if subComp.Type not in ["pntSubComponent", "edgeSubComponent", "polySubComponent"]:
        gear.log("Invalid Selection", gear.sev_error)
        return

    elements = subComp.SubComponent.ElementArray
    mesh = subComp.SubComponent.Parent3DObject

    mirror_elements = geo.getSymSubComponent(elements, subComp.Type, mesh)
    if not mirror_elements:
      return

    points = []
    points.extend(elements)
    points.extend(mirror_elements)

    sub_type = subComp.Type.replace("SubComponent", "")
    xsi.SelectGeometryComponents(mesh.FullName+"."+sub_type+str(points))

##########################################################
# MIRROR SELECTION
##########################################################
# ========================================================
def gear_MirrorSelection_Execute():

    if not xsi.Selection.Count:
        gear.log("No selection", gear.sev_error)
        return

    subComp = xsi.Selection(0)
    if subComp.Type not in ["pntSubComponent", "edgeSubComponent", "polySubComponent"]:
        gear.log("Invalid Selection", gear.sev_error)
        return

    elements = subComp.SubComponent.ElementArray
    mesh = subComp.SubComponent.Parent3DObject

    mirror_elements = geo.getSymSubComponent(elements, subComp.Type, mesh)
    if not mirror_elements:
      return

    sub_type = subComp.Type.replace("SubComponent", "")
    xsi.SelectGeometryComponents(mesh.FullName+"."+sub_type+str(mirror_elements))

###########################################################
# SELECT STARS
###########################################################
# ========================================================
def gear_Select5BranchesStars_Execute():

    if not xsi.Selection.Count:
        gear.log("No selection", gear.sev_error)
        return

    objects = [obj for obj in xsi.Selection if obj.Type in ["polymsh"]]

    if not objects:
        gear.log("Invalid Selection", gear.sev_error)
        return

    xsi.DeselectAll()

    for obj in objects:

        stars = geo.getStars(obj, 5, False)

        if stars:
            gear.log("There is "+str(len(stars))+" stars with 5 branches on "+obj.FullName)
            xsi.AddToSelection(obj.FullName+".pnt"+str(stars), "", True)
        else:
            gear.log("There is no stars with 5 branches on "+obj.FullName)

# ========================================================
def gear_Select6MoreBranchesStars_Execute():

    if not xsi.Selection.Count:
        gear.log("No selection", gear.sev_error)
        return

    objects = [obj for obj in xsi.Selection if obj.Type in ["polymsh"]]

    if not objects:
        gear.log("Invalid Selection", gear.sev_error)
        return

    xsi.DeselectAll()

    for obj in objects:

        stars = geo.getStars(obj, 6, True)

        if stars:
            gear.log("There is "+str(len(stars))+" stars with 6 branches or more on "+obj.FullName)
            xsi.AddToSelection(obj.FullName+".pnt"+str(stars), "", True)
        else:
            gear.log("There is no stars with 6 branches or more on "+obj.FullName)
