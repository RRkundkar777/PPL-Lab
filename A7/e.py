import pygtk
pygtk.require('2.0')
import gtk

# the line below cretes an object of type Window. gtk.WINDOW_TOPLEVEL means 
# it is a normal window that we see.
w = gtk.Window(gtk.WINDOW_TOPLEVEL)

# this tells the window to show itself. The window does not display itself right now.
# this happens when the gtk.main() function tries to draw everything that has called
# to show itself.
w.show()

# note: the one below is a normal method call. gtk is a module and main() is 
# just a function in that module. This function does a lot of work - like setting
# colour of frame, default size of frame, show close-minimize-maximize buttons, 
# etc.
gtk.main()
