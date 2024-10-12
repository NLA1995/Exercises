import maya.cmds as cmds

class SelectionManager:
    def __init__(self, curves):
        self.curves = curves
        self.original_selection = []

    def __enter__(self):
        # Store the original selection
        self.original_selection = cmds.ls(selection=True)
        # Select the specified curves
        cmds.select(self.curves, replace=True)

    def __exit__(self, exc_type, exc_value, traceback):
        # Restore the original selection
        cmds.select(self.original_selection, replace=True)
        print(f"Restored selection: {self.original_selection}")

def create_curves(ctrl_name):
    # Create the first circle (controller)
    ctrl = cmds.circle(name=ctrl_name, radius=3, normal=[0, 1, 0])[0]
    cmds.color(ctrl, rgb=(.78, 0, 0.07))

    # Create the second circle (controller)
    ctrl2 = cmds.circle(name=ctrl_name, radius=2.5, normal=[0, 1, 0])[0]
    cmds.color(ctrl2, rgb=(.8, 0, 1))

    new_position = (5, 5, 0)

    # Use the SelectionManager to move the second circle
    with SelectionManager([ctrl, ctrl2]):
        cmds.xform(ctrl2, translation=new_position, worldSpace=True)
# Usage
create_curves("myCircle")

