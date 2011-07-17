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
    Url :       http://gear.jeremiepasserin.com
    Date:       2010 / 11 / 15

'''

## @package gear_curveTools.py
# @author Jeremie Passerin
#

##########################################################
# GLOBAL
##########################################################
import gear

from gear.xsi import xsi, c, dynDispatch

import gear.xsi.primitive as pri
import gear.xsi.curve as cur
import gear.xsi.fcurve as fcv
import gear.xsi.uitoolkit as uit
import gear.xsi.applyop as aop

##########################################################
# XSI LOAD / UNLOAD PLUGIN
##########################################################
# ========================================================
def XSILoadPlugin(in_reg):

    in_reg.Author = "Jeremie Passerin"
    in_reg.Name = "gear_curveTools"
    in_reg.Email = "geerem@hotmail.com"
    in_reg.URL = "http://www.jeremiepasserin.com"
    in_reg.Major = 1
    in_reg.Minor = 0

    # Commands
    in_reg.RegisterCommand("gear_CurveResampler","gear_CurveResampler")
    in_reg.RegisterCommand("gear_ApplyZipperOp","gear_ApplyZipperOp")

    in_reg.RegisterCommand("gear_DrawCnsCurve_Linear","gear_DrawCnsCurve_Linear")
    in_reg.RegisterCommand("gear_DrawCnsCurve_Cubic","gear_DrawCnsCurve_Cubic")

    in_reg.RegisterCommand("gear_MergeCurves","gear_MergeCurves")
    in_reg.RegisterCommand("gear_SplitCurves","gear_SplitCurves")

    # Operators
    in_reg.RegisterOperator("gear_ZipperOp")

    return True

# ========================================================
def XSIUnloadPlugin(in_reg):
    strPluginName = in_reg.Name
    gear.log(str(strPluginName) + str(" has been unloaded."), c.siVerbose)
    return True

##########################################################
# CURVE RESAMPLER
##########################################################
# Execute ================================================
def gear_CurveResampler_Execute():

    if not xsi.Selection.Count or xsi.Selection(0).Type not in ["crvlist"]:
        gear.log("No selection or invalid Selection", gear.sev_error)
        return

    curve = xsi.Selection(0)
    if curve.ActivePrimitive.Geometry.Curves.Count > 1:
        gear.log("Curve Resampler works only with single curve", gear.sev_error)
        return

    ref_crv = uit.pickSession(c.siCurveFilter, "Pick Reference Curve", False)
    if not ref_crv:
        ref_crv = curve

    op = aop.gear_resampler_op(curve, ref_crv, 0, 1)

    xsi.InspectObj(op)

##########################################################
# DRAW CONSTRAINED CURVE LINEAR
##########################################################
# Execute ================================================
def gear_DrawCnsCurve_Linear_Execute():

    if xsi.Selection.Count < 2:
        gear.log("Select enough centers", gear.sev_error)
        return

    cur.addCnsCurve(xsi.ActiveSceneRoot, "crvCns", xsi.Selection, False, 1)

##########################################################
# DRAW CONSTRAINED CURVE CUBIC
##########################################################
# Execute ================================================
def gear_DrawCnsCurve_Cubic_Execute():

    if xsi.Selection.Count < 2:
        gear.log("Select enough centers", gear.sev_error)
        return

    cur.addCnsCurve(xsi.ActiveSceneRoot, "crvCns", xsi.Selection, False, 3)

##########################################################
# MERGE CURVES
##########################################################
# Execute ================================================
def gear_MergeCurves_Execute():

    if not xsi.Selection.Count:
        gear.log("No selection", gear.sev_error)
        return

    curves = [curve for curve in xsi.Selection if curve.Type in ["crvlist"]]
    if not curves:
        gear.log("Invalid selection", gear.sev_error)
        return

    cur.mergeCurves(curves)

##########################################################
# SPLIT CURVES
##########################################################
# Execute ================================================
def gear_SplitCurves_Execute():

    if not xsi.Selection.Count:
        gear.log("No selection", gear.sev_error)
        return

    for curve in xsi.Selection:

        if curve.Type not in ["crvlist"]:
            gear.log("Invalid selection", gear.sev_warning)
            continue

        cur.splitCurve(curve)

##########################################################
# ZIPPER OP
##########################################################
# Define =================================================
def gear_ZipperOp_Define(ctxt):

    op = ctxt.Source
    op.AlwaysEvaluate = False
    op.Debug = 0

    pdef = XSIFactory.CreateParamDef("Zip", c.siDouble, 0, c.siPersistable|c.siAnimatable, "", "",0,0,10,0,1)
    op.AddParameter(pdef)
    pdef = XSIFactory.CreateParamDef("Bias", c.siDouble, 0, c.siPersistable|c.siAnimatable, "", "",0.5,0,1,0,1)
    op.AddParameter(pdef)
    # pdef = XSIFactory.CreateParamDef("Smooth", c.siDouble, 0, c.siPersistable|c.siAnimatable, "", "",0,0,1,0,1)
    # op.AddParameter(pdef)
    pdef = XSIFactory.CreateParamDef("Type", c.siDouble, 0, c.siPersistable|c.siAnimatable, "", "",0,0,1,0,1)
    op.AddParameter(pdef)
    pdef = XSIFactory.CreateParamDef("CurveCombo", c.siInt4, 0, c.siPersistable, "", "",0,0,1,0,1)
    op.AddParameter(pdef)
    pdef = XSIFactory.CreateFCurveParamDef("Start_FCurve")
    op.AddParameter(pdef)
    pdef = XSIFactory.CreateFCurveParamDef("Speed_FCurve")
    op.AddParameter(pdef)

    return True

# Layout =================================================
def gear_ZipperOp_OnInit():

    type_items = ["Points", 0, "Percentage", 1]
    curve_items = ["Start", 0, "Speed", 1]

    layout = PPG.PPGLayout
    layout.Clear()

    layout.AddGroup("Zip")
    layout.AddItem("Mute", "Mute")
    layout.AddItem("Zip", "Zip")
    layout.EndGroup()

    layout.AddGroup("Options")
    layout.AddEnumControl("Type", type_items, "Type", c.siControlCombo)
    layout.AddItem("Bias")
    layout.EndGroup()

    layout.AddGroup("Profile")
    item = layout.AddEnumControl("CurveCombo", curve_items, "Type", c.siControlCombo)
    item.SetAttribute(c.siUINoLabel, True)

    if PPG.CurveCombo.Value == 0:
        item = layout.AddFCurve("Start_FCurve")
        item.SetAttribute(c.siUIFCurveLabelX, "Points")
        item.SetAttribute(c.siUIFCurveLabelY, "Start")
        item.SetAttribute(c.siUIFCurveViewMinX,-.1)
        item.SetAttribute(c.siUIFCurveViewMaxX,1.1)
        item.SetAttribute(c.siUIFCurveViewMinY,-.1)
        item.SetAttribute(c.siUIFCurveViewMaxY,1.1)
        item.SetAttribute(c.siUIFCurveGridSpaceX, .1)
        item.SetAttribute(c.siUIFCurveGridSpaceY, .1)
    else:
        item = layout.AddFCurve("Speed_FCurve")
        item.SetAttribute(c.siUIFCurveLabelX, "Points")
        item.SetAttribute(c.siUIFCurveLabelY, "Speed")
        item.SetAttribute(c.siUIFCurveViewMinX,-.1)
        item.SetAttribute(c.siUIFCurveViewMaxX,2.1)
        item.SetAttribute(c.siUIFCurveViewMinY,-.1)
        item.SetAttribute(c.siUIFCurveViewMaxY,1.1)
        item.SetAttribute(c.siUIFCurveGridSpaceX, .1)
        item.SetAttribute(c.siUIFCurveGridSpaceY, .1)
    layout.EndGroup()

    PPG.Refresh()

    return True

def gear_ZipperOp_CurveCombo_OnChanged():
    gear_ZipperOp_OnInit()

# Update =================================================
def gear_ZipperOp_Update(ctxt):

    # Inputs -----------------------------------------------
    OutPort = ctxt.OutputPort

    crv_geo_A = ctxt.GetInputValue(0, 0, 0).Geometry
    ncrv_A = crv_geo_A.Curves(0)
    crv_geo_B = ctxt.GetInputValue(1, 0, 0).Geometry
    ncrv_B = crv_geo_B.Curves(0)

    zip = ctxt.GetParameterValue("Zip")
    bias = ctxt.GetParameterValue("Bias")
    zip_type = ctxt.GetParameterValue("Type")
    start_fcv = ctxt.GetParameterValue("Start_FCurve")
    speed_fcv = ctxt.GetParameterValue("Speed_FCurve")

    pnt_count_A = crv_geo_A.Points.Count
    pnt_count_B = crv_geo_B.Points.Count

    pos_tuple_A = crv_geo_A.Points.PositionArray
    pos_tuple_B = crv_geo_B.Points.PositionArray

    if zip_type == 0:
        pos_A = [pos_tuple_A[j][i] for i in range(len(pos_tuple_A[0])) for j in range(len(pos_tuple_A))]
        pos_B = [pos_tuple_B[j][i] for i in range(len(pos_tuple_B[0])) for j in range(len(pos_tuple_B))]
    else:
        step = 100  / (pnt_count_B-1.0)
        a = [ncrv_A.EvaluatePositionFromPercentage(i*step)[0].Get2() for i in range(pnt_count_B)]
        pos_A = [ a[j][i] for j in range(len(a)) for i in range(len(a[0])) ]

        step = 100  / (pnt_count_A-1.0)
        a = [ncrv_B.EvaluatePositionFromPercentage(i*step)[0].Get2() for i in range(pnt_count_A)]
        pos_B = [ a[j][i] for j in range(len(a)) for i in range(len(a[0])) ]

    mid_pos = [(pos_A[i]*bias+pos_B[i]*(1-bias)) for i in range(len(pos_A))]

    # Process -----------------------------------------------
    if OutPort.Index == 2:
        t = pos_tuple_A
        p = pnt_count_A
    else:
        t = pos_tuple_B
        p = pnt_count_B

    pos = []
    v = XSIMath.CreateVector3()
    for i in range(p):

        step = 1/(p-1.0)

        v0 = XSIMath.CreateVector3(t[0][i], t[1][i], t[2][i])
        v1 = XSIMath.CreateVector3(mid_pos[i*3+0], mid_pos[i*3+1], mid_pos[i*3+2])
        v.Sub(v1, v0)

        d = start_fcv.Eval(i*step)

        if zip < d:
            y = 0
        else:
            y = changerange(zip, d, d+step, 0, 1)

        y = speed_fcv.Eval(y)

        v.ScaleInPlace(y)

        pos.append(v0.X + v.X)
        pos.append(v0.Y + v.Y)
        pos.append(v0.Z + v.Z)

    # Output ------------------------------------------------

    Out = ctxt.OutputTarget
    Out.Geometry.Points.PositionArray = pos

def changerange(x, a, b, c, d):
    return c + ( x - a ) * (( d-c) / (b-a+0.0))

# Execute ================================================
def gear_ApplyZipperOp_Execute():

    if xsi.Selection.Count < 2:
        gear.log("Select 2 curve", gear.sev_error)
        return

    crv_A = xsi.Selection(0)
    crv_B = xsi.Selection(1)

    if crv_A.Type not in ["crvlist"] or crv_B.Type not in ["crvlist"]:
        gear.log("Select 2 curve", gear.sev_error)
        return


    # Apply Operator ----------------------
    op = XSIFactory.CreateObject("gear_ZipperOp")

    op.AddIOPort(crv_A.ActivePrimitive)
    op.AddIOPort(crv_B.ActivePrimitive)

    pStart_fcv = op.Parameters("Start_FCurve").Value
    fcv.drawFCurve(pStart_fcv, [[0,0],[1,1]], c.siLinearKeyInterpolation)

    pSpeed_fcv = op.Parameters("Speed_FCurve").Value
    fcv.drawFCurve(pStart_fcv, [[0,0],[1,1]], c.siLinearKeyInterpolation)

    op.Connect()

    xsi.InspectObj(op)

    return op