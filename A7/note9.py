import pygtk
pygtk.require('2.0')
import gtk
# Window for Notex
window = gtk.Window(gtk.WINDOW_TOPLEVEL)
# WIndow Size
window.set_size_request(700, 200)
#Window Title
window.set_title("Notex 1.0.0")
# Exiting the Window
window.connect("delete_event", gtk.main_quit)

def menu_clicked(widget, string):
	print string, "MenuItem was clikced"	

mb = gtk.MenuBar()
m = gtk.Menu()

openi = gtk.MenuItem("Open")
m.append(openi)
openi.connect("activate", menu_clicked, "Open")
openi.show()

savei = gtk.MenuItem("Save")
m.append(savei)
savei.connect("activate", menu_clicked, "Save")
savei.show()

closei = gtk.MenuItem("Close")
m.append(closei)
closei.connect("activate", menu_clicked, "Close")
closei.show()

root_menu = gtk.MenuItem("Enforcer")
root_menu.show()
root_menu.set_submenu(m)

m1 = gtk.Menu()

openi1 = gtk.MenuItem("Open")
m1.append(openi1)
openi1.connect("activate", menu_clicked, "Open")
openi1.show()


root_menu1 = gtk.MenuItem("GEforcer")
root_menu1.show()
root_menu1.set_submenu(m1)


vbox = gtk.VBox(False, 0)
vbox.show()
window.add(vbox)

menu_bar = gtk.MenuBar()
vbox.pack_start(menu_bar, False, False, 2)
menu_bar.show()
menu_bar.append(root_menu)
window.show()
gtk.main()