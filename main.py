from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.IFSelect import IFSelect_RetDone, IFSelect_ItemsByEntity
from OCC.Display.SimpleGui import init_display
from OCC.Core.ShapeExtend import ShapeExtend_CompositeSurface
from OCC.Core.StepData import StepData_StepModel as stepmodel
from OCC.Core.Law import Law_BSpline
from OCC.Core.TopoDS import TopoDS_Iterator

import sys

extend = ShapeExtend_CompositeSurface()
step_reader = STEPControl_Reader()
status = step_reader.ReadFile('bunger3.stp')
step_reader.TransferRoots()
model = step_reader.StepModel().Entities()
for i in range(100):
    model.Next()
    entity = model.Value()
    if isinstance(entity, Law_BSpline):
        print('hooray')


if status == IFSelect_RetDone:  # check status
    failsonly = False
    step_reader.PrintCheckLoad(failsonly, IFSelect_ItemsByEntity)
    step_reader.PrintCheckTransfer(failsonly, IFSelect_ItemsByEntity)

    ok = step_reader.TransferRoot(1)
    _nbs = step_reader.NbShapes()
    aResShape = step_reader.Shape(1)
    print("start")
    print(aResShape)
    print("end")
else:
    print("Error: can't read file.")
    sys.exit(0)
display, start_display, add_menu, add_function_to_menu = init_display()
display.DisplayShape(aResShape, update=True)
start_display()