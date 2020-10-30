import pygtk
pygtk.require('2.0')
import gtk
w = gtk.Window(gtk.WINDOW_TOPLEVEL)
w.set_position(gtk.WIN_POS_CENTER)
w.show()
#observe: All class names are in "Title case".
#Line below: b becomes an object of type Button with the text
# Hello PPL on in.
b = gtk.Button("Hello PPL")
b.set_focus_on_click(True)
label = gtk.Entry(255)
w.add(label)
label.show()
# this adds the button to the window. Try commenting the line below.
w.add(b)
#the button should also show itself. Try commenting the line below and see the result.
b.show()
gtk.main()
