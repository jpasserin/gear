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
    Url:        http://gear.jeremiepasserin.com
    Date:       2010 / 11 / 15

'''

## @package gear.xsi.operator
# @author Jeremie Passerin
#

##########################################################
# GLOBAL
##########################################################
from gear.xsi import xsi, c, XSIFactory

##########################################################
# XSI OPERATORS APPLY
##########################################################
# getOperatorFromStack ===================================
## Return an operator of given type from the deformer stack of given geometry
# @param obj Geometry - The geometry to check.
# @param opType String - The type of the operator to find.
# @param firstOnly Boolean - Only return first matching operator.
# @return An operator if firstOnly is true, a collection of operator if it's false, False if there is no such operator.
def getOperatorFromStack(obj, opType, firstOnly=True):

     operators = XSIFactory.CreateObject("XSI.Collection")

     for nested in obj.ActivePrimitive.NestedObjects:
          if nested.IsClassOf(c.siOperatorID):
                if nested.Type == opType:
                     if firstOnly:
                          return nested
                     else:
                          operators.Add(nested)

     if operators.Count:
          return operators

     return False
