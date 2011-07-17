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

## @package gear_menu.py
# @author Jeremie Passerin
#

##########################################################
# GLOBAL
##########################################################
from gear.xsi import xsi, c, dynDispatch, Dispatch
import gear.xsi.plugin as plu

##########################################################
# XSI LOAD / UNLOAD PLUGIN
##########################################################
# ========================================================
def XSILoadPlugin(in_reg):

    in_reg.Author = "Jeremie Passerin"
    in_reg.Name = "gear_menu"
    in_reg.Email = "geerem@hotmail.com"
    in_reg.URL = "http://www.jeremiepasserin.com"
    in_reg.Major = 1
    in_reg.Minor = 0

    # Menu
    in_reg.RegisterMenu(c.siMenuMainTopLevelID, "Gear", False, False)

    return True

# ========================================================
def XSIUnloadPlugin(in_reg):
    strPluginName = in_reg.Name
    xsi.LogMessage(str(strPluginName) + str(" has been unloaded."), c.siVerbose)
    return True

##########################################################
# MENU INIT
##########################################################
def Gear_Init(ctxt):

    menu = ctxt.source

    # Primitive ===========================================
    if plu.pluginExists(["gear_icons", "gear_PSet"]):
        primitive_menu = dynDispatch(menu.AddItem("Primitive", c.siMenuItemSubmenu))

        # Property
        if plu.pluginExists("gear_PSet"):
            property_menu = dynDispatch(primitive_menu.AddItem("Property", c.siMenuItemSubmenu))
            property_menu.AddCommandItem("&New Parameter Set", "gear_PSet_Apply")
            property_menu.AddCommandItem("&Debug Parameter Set", "gear_PSet_Debug")

        # Icons
        if plu.pluginExists("gear_icons"):
            icon_menu = dynDispatch(primitive_menu.AddItem("Icons", c.siMenuItemSubmenu))
            icon_menu.AddCommandItem("&Cube", "gear_DrawCube")
            icon_menu.AddCommandItem("&Pyramid", "gear_DrawPyramid")
            icon_menu.AddCommandItem("&Square", "gear_DrawSquare")
            icon_menu.AddCommandItem("&Flower", "gear_DrawFlower")
            icon_menu.AddCommandItem("&Circle", "gear_DrawCircle")
            icon_menu.AddCommandItem("&Cylinder", "gear_DrawCylinder")
            icon_menu.AddCommandItem("&Compas", "gear_DrawCompas")
            icon_menu.AddCommandItem("&Foil", "gear_DrawFoil")
            icon_menu.AddCommandItem("&Diamond", "gear_DrawDiamond")
            icon_menu.AddCommandItem("&Leash", "gear_DrawLeash")
            icon_menu.AddCommandItem("&Cube With Peak", "gear_DrawCubeWithPeak")
            icon_menu.AddCommandItem("&Sphere", "gear_DrawSphere")
            icon_menu.AddCommandItem("&Arrow", "gear_DrawArrow")
            icon_menu.AddCommandItem("&Cross Arrow", "gear_DrawCrossArrow")
            icon_menu.AddCommandItem("&Bended Arrow", "gear_DrawBendedArrow")
            icon_menu.AddCommandItem("&Bended Arrow 2", "gear_DrawBendedArrow2")
            icon_menu.AddCommandItem("&Cross", "gear_DrawCross")
            icon_menu.AddCommandItem("&Glasses", "gear_DrawGlasses")
            icon_menu.AddCommandItem("&Look At", "gear_DrawLookAt")
            icon_menu.AddCommandItem("&Eye Arrow", "gear_DrawEyeArrow")
            icon_menu.AddCommandItem("&Angle Survey", "gear_DrawAngleSurvey")
            icon_menu.AddCommandItem("&Eye Ball", "gear_DrawEyeBall")
            icon_menu.AddCommandItem("&Rectangle Cube", "gear_DrawRectangleCube")
            icon_menu.AddCommandItem("&Man", "gear_DrawMan")
            icon_menu.AddCommandItem("&Null", "gear_DrawNull")

    # Select ==============================================
    if plu.pluginExists("gear_selectionTools"):
        select_menu = dynDispatch(menu.AddItem("Select", c.siMenuItemSubmenu))

        select_menu.AddCommandItem("&Symmetrize Component Selection", "gear_SymmetrizeSelection")
        select_menu.AddCommandItem("&Mirror Component Selection", "gear_MirrorSelection")
        select_menu.AddSeparatorItem()
        select_menu.AddCommandItem("&Select stars 5", "gear_Select5BranchesStars")
        select_menu.AddCommandItem("&Select stars 6+", "gear_Select6MoreBranchesStars")

    # Curve ===============================================
    if plu.pluginExists("gear_curveTools"):
        curve_menu = dynDispatch(menu.AddItem("Curve", c.siMenuItemSubmenu))

        # curve tools
        curve_menu.AddCommandItem("&Constrained Curve Linear", "gear_DrawCnsCurve_Linear")
        curve_menu.AddCommandItem("&Constrained Curve Cubic", "gear_DrawCnsCurve_Cubic")
        curve_menu.AddSeparatorItem()
        curve_menu.AddCommandItem("&Resample Curve", "gear_CurveResampler")
        curve_menu.AddCommandItem("&Zipper", "gear_ApplyZipperOp")
        curve_menu.AddSeparatorItem()
        curve_menu.AddCommandItem("&Merge Curves", "gear_MergeCurves")
        curve_menu.AddCommandItem("&Split Curves", "gear_SplitCurves")
        
    # Modeling ============================================
    if plu.pluginExists("gear_ModelingTools"):
        modeling_menu = dynDispatch(menu.AddItem("Modeling", c.siMenuItemSubmenu))
        
        modeling_menu.AddCommandItem("&Match Geometry", "gear_MatchGeometry")
        modeling_menu.AddSeparatorItem()
        modeling_menu.AddCommandItem("&Symmetrize Points", "gear_SymmetrizePoints")
        modeling_menu.AddSeparatorItem()
        modeling_menu.AddCommandItem("&Mirror Cluster", "gear_MirrorClusters")
        modeling_menu.AddCommandItem("&Merge With Clusters", "gear_MergeWithClusters")
        modeling_menu.AddCommandItem("&Split Polygon Islands", "gear_SplitPolygonIslands")
        modeling_menu.AddSeparatorItem()
        modeling_menu.AddCommandItem("&Add Cluster Center", "gear_AddClusterCenter")

    # Rigging =============================================
    if plu.pluginExists(["gear_riggingTools", "gear_renamer", "gear_transformTools"]):
        rigging_menu = dynDispatch(menu.AddItem("Rigging", c.siMenuItemSubmenu))

        riggingTools_menu = dynDispatch(rigging_menu.AddItem("Tools", c.siMenuItemSubmenu))
        riggingTools_menu.AddCommandItem("&Get Distance", "gear_GetDistance")
        riggingTools_menu.AddSeparatorItem()
        riggingTools_menu.AddCommandItem("&Draw Axis", "gear_DrawAxis")
        riggingTools_menu.AddSeparatorItem()
        riggingTools_menu.AddCommandItem("&Add Null Parent", "gear_AddNullParent")
        riggingTools_menu.AddCommandItem("&Add Null Child", "gear_AddNullChild")
        riggingTools_menu.AddSeparatorItem()
        riggingTools_menu.AddCommandItem("&Copy WireFrame Color", "gear_CopyWireFrameColor")

        if plu.pluginExists("gear_transformTools"):
            transform_menu = dynDispatch(rigging_menu.AddItem("Transform", c.siMenuItemSubmenu))
            transform_menu.AddCommandItem("&Match All Transform", "gear_MatchSRT")
            transform_menu.AddSeparatorItem()
            transform_menu.AddCommandItem("&Match Translation", "gear_MatchT")
            transform_menu.AddCommandItem("&Match Rotation", "gear_MatchR")
            transform_menu.AddCommandItem("&Match Scaling", "gear_MatchS")
            transform_menu.AddSeparatorItem()
            transform_menu.AddCommandItem("&Match Trn/Rot", "gear_MatchRT")
            transform_menu.AddCommandItem("&Match Scl/Rot", "gear_MatchSR")
            transform_menu.AddCommandItem("&Match Scl/Trn", "gear_MatchST")

        riggingSolvers_menu = dynDispatch(rigging_menu.AddItem("Solvers", c.siMenuItemSubmenu))
        riggingSolvers_menu.AddCommandItem("&Create Spline Kine", "gear_CreateSplineKine")
        riggingSolvers_menu.AddCommandItem("&Create Roll Spline Kine", "gear_CreateRollSplineKine")
        riggingSolvers_menu.AddSeparatorItem()
        riggingSolvers_menu.AddCommandItem("&Apply Curve Slide 2 Op", "gear_CurveSlide2Op")
        riggingSolvers_menu.AddSeparatorItem()
        riggingSolvers_menu.AddCommandItem("&Apply Inter Local Ori Op", "gear_InterLocalOri")
        riggingSolvers_menu.AddSeparatorItem()
        riggingSolvers_menu.AddCommandItem("&Apply Spine Point At Op", "gear_ApplySpinePointAtOp")
        
		
        if plu.pluginExists("gear_renamer"):
            rigging_menu.AddCommandItem("&Renamer", "gear_OpenRenamer")

    # Character ===========================================
    if plu.pluginExists("gear_riggingSystem"):
        character_menu = dynDispatch(menu.AddItem("Character", c.siMenuItemSubmenu))

        character_menu.AddCommandItem("&Build Rig From Selection", "gear_BuildFromSelection")
        character_menu.AddCommandItem("&Build Rig From File", "gear_BuildFromFile")
        character_menu.AddSeparatorItem()
        character_menu.AddCommandItem("&Guide Tools", "gear_GuideTools")
        character_menu.AddCommandItem("&Update Guide", "gear_UpdateGuide")
        character_menu.AddSeparatorItem()
        character_menu.AddCommandItem("&Import Guide", "gear_ImportGuide")
        character_menu.AddCommandItem("&Export Guide", "gear_ExportGuide")

    # Deform ==============================================
    if plu.pluginExists(["gear_envelopeTools", "gear_shapeTools"]):
        deform_menu = dynDispatch(menu.AddItem("Deform", c.siMenuItemSubmenu))

        # Shape
        if plu.pluginExists("gear_shapeTools"):
            shape_menu = dynDispatch(deform_menu.AddItem("Shape", c.siMenuItemSubmenu))
            shape_menu.AddCommandItem("&Select Shape Points", "gear_SelectShapePoints")
            shape_menu.AddCommandItem("&Reset Shape Points", "gear_ResetShapePoints")
            shape_menu.AddCommandItem("&Scale Shape Points", "gear_ScaleShapePoints")
            shape_menu.AddCommandItem("&Smooth Shape Points", "gear_SmoothShapePoints")
            shape_menu.AddCommandItem("&Symmetrize Shape Points", "gear_SymShapePoints")
            shape_menu.AddSeparatorItem()
            shape_menu.AddCommandItem("&Duplicate Shape Key", "gear_DuplicateShapeKey")
            shape_menu.AddCommandItem("&Move Shape Key", "gear_MoveShapeKey")
            shape_menu.AddSeparatorItem()
            shape_menu.AddCommandItem("&Reset Shape Key", "gear_ResetShapeKey")
            shape_menu.AddCommandItem("&Merge Shape Key", "gear_MergeShapeKey")
            shape_menu.AddCommandItem("&Split Shape Key", "gear_SplitShapeKey")
            shape_menu.AddCommandItem("&Mirror Shape Key", "gear_MirrorShapeKey")
            shape_menu.AddCommandItem("&Match Shape Key", "gear_MatchShapeKey")

        # Envelope
        if plu.pluginExists("gear_envelopeTools"):
            envelope_menu = dynDispatch(deform_menu.AddItem("Envelope", c.siMenuItemSubmenu))
            envelope_menu.AddCommandItem("&Select Unnormalized Points", "gear_SelectUnnormalizedPoints")
            envelope_menu.AddCommandItem("&Create Symmetry Mapping Template", "gear_CreateSymmetryMappingTemplate")
            envelope_menu.AddSeparatorItem()
            envelope_menu.AddCommandItem("&Copy Weights point 2 point", "gear_CopyWeights")
            envelope_menu.AddCommandItem("&Copy Weights Average", "gear_CopyWeightsAverage")
            envelope_menu.AddCommandItem("&Average Central Axis Point Weights", "gear_AverageMirrorWeights") #Make the central points to 50% 50%
            envelope_menu.AddCommandItem("&Replace Deformer", "gear_ReplaceDeformer")
            envelope_menu.AddSeparatorItem()
            envelope_menu.AddCommandItem("&Normalize Weights", "gear_NormalizeWeights")
            envelope_menu.AddCommandItem("&Normalize to Deformer", "gear_NormalizeToDeformer")
            envelope_menu.AddCommandItem("&Prune Weights", "gear_PruneWeights")
            envelope_menu.AddCommandItem("&Make Island Rigid", "gear_MakeIslandRigid")
            envelope_menu.AddCommandItem("&Rebuild Envelope", "gear_RebuildEnvelope")
            envelope_menu.AddCommandItem("&Remove Unused Envelope Cls", "gear_RemoveUnusedEnvCls")
            envelope_menu.AddSeparatorItem()
            envelope_menu.AddCommandItem("&Copy Envelope With Gator", "gear_CopyEnvWithGator")
            envelope_menu.AddCommandItem("&Mirror Objects Weights", "gear_MirrorObjectWeights")

        # WeightMap
        if plu.pluginExists("gear_weightMapTools"):
            weightmap_menu = dynDispatch(deform_menu.AddItem("Weight Map", c.siMenuItemSubmenu))
            weightmap_menu.AddCommandItem("&Select WeightMap Points", "gear_SelectWeightMapPoints")
            weightmap_menu.AddCommandItem("&Reset WeightMap Points", "gear_ResetWeightMapPoints")
            weightmap_menu.AddCommandItem("&Set WeightMap Points", "gear_SetWeightMapPoints")
            weightmap_menu.AddCommandItem("&Scale WeightMap Points", "gear_ScaleWeightMapPoints")
            weightmap_menu.AddCommandItem("&Smooth WeightMap Points", "gear_SmoothWeightMapPoints")
            weightmap_menu.AddCommandItem("&Symmetrize WeightMap Points", "gear_SymWeightMapPoints")


    # Animation ===========================================
    if plu.pluginExists(["gear_mirrorAnimation", "gear_synoptic"]):
        animation_menu = dynDispatch(menu.AddItem("Animation", c.siMenuItemSubmenu))

        # Synoptic
        if plu.pluginExists("gear_synoptic"):
            animation_menu.AddCommandItem("&Open Synoptic", "gear_OpenSynoptic")

        if plu.pluginExists(["gear_mirrorAnimation", "gear_synoptic"]):
            animation_menu.AddSeparatorItem()

        # Mirror Animation
        if plu.pluginExists("gear_mirrorAnimation"):
            animation_menu.AddCommandItem("&Mirror Pose", "gear_MirrorPose")
            animation_menu.AddCommandItem("&Mirror Animation", "gear_MirrorAnimation")
            animation_menu.AddCommandItem("&Edit Mirroring Template", "gear_CreateMirrorTemplate")

    # I/O =================================================
    if plu.pluginExists("gear_io"):
        io_menu = dynDispatch(menu.AddItem("Import/Export", c.siMenuItemSubmenu))
        io_menu.AddCommandItem("&Import Skin", "gear_ImportSkin")
        io_menu.AddCommandItem("&Import Envelope", "gear_ImportEnvelope")
        io_menu.AddSeparatorItem()
        io_menu.AddCommandItem("&Export Skin", "gear_ExportSkin")
        io_menu.AddCommandItem("&Export Envelope", "gear_ExportEnvelope")
        io_menu.AddCommandItem("&Export Object", "gear_ExportObject")
        
    menu.AddCallbackItem("Reload Modules", "gear_reloadModules")
    menu.AddCallbackItem("Help", "gear_help")
    
    
def gear_reloadModules(ctxt):
    import gear
    gear.reloadModule()
    
def gear_help(ctxt):
    xsi.OpenNetView( "http://gear.jeremiepasserin.com", True, 1 )
