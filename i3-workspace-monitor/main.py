#!/usr/bin/env python3

import i3ipc
import json
import datetime

# Create the Connection object that can be used to send commands and subscribe
# to events.
i3 = i3ipc.Connection()


# Define a callback to be called when you switch workspaces.
def on_workspace_focus(self, e):
    # The first parameter is the connection to the ipc and the second is an object
    # with the data of the event sent from i3.
    if e.current:
        print(e.current.name)

def on_binding_run(self, e):
    print('Binding')

i3.on('binding', on_binding_run)
i3.on('workspace::focus', on_workspace_focus)

i3.main()
