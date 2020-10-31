import pygtk
pygtk.require('2.0')
import gtk
w = gtk.Window(gtk.WINDOW_TOPLEVEL)
w.set_size_request(200, 200)
w.set_title("Menu Demo Winodw")
w.connect("delete_event", gtk.main_quit)
def menu_clicked(widget, string):
	print string, "MenuItem was clikced"	
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

root_menu = gtk.MenuItem("File")
root_menu.show()
root_menu.set_submenu(m)

vbox = gtk.VBox(False, 0)
vbox.show()
w.add(vbox)

menu_bar = gtk.MenuBar()
vbox.pack_start(menu_bar, False, False, 2)
menu_bar.show()
menu_bar.append(root_menu)
w.show()
gtk.main()
