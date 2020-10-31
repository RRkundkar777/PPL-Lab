import sys
import pygtk
import gtk

TextBox = gtk.TextView()

MenuBar = gtk.MenuBar()

StatusBar = gtk.Statusbar()

Window = gtk.Window(gtk.WINDOW_TOPLEVEL)

class MainForm:

 	    _File = ""

 	    def open_file(menuitem, user_param1):

 	    chooser = gtk.FileChooserDialog(title="Open a file",action=gtk.FILE_CHOOSER_ACTION_OPEN, buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))

 	        chooser.set_default_response(gtk.RESPONSE_OK)

 	    filter = gtk.FileFilter()
# 015
# 	        filter.set_name("Text Files")
# 016
# 	        filter.add_mime_type("text/data")
# 017
# 	        filter.add_pattern("*.txt")
# 018
# 	        chooser.add_filter(filter)
# 019
# 	    filter2 = gtk.FileFilter()
# 020
# 	    filter2.set_name("All Files")
# 021
# 	    filter2.add_pattern("*.*")
# 022
# 	    chooser.add_filter(filter2)
# 023
# 	    response = chooser.run()
# 024
# 	    if response == gtk.RESPONSE_OK:
# 025
# 	        global _File
# 026
# 	        filename = chooser.get_filename()
# 027
# 	        _File = filename
# 028
# 	        textbuffer = TextBox.get_buffer()
# 029
# 	        print "Opened File: " + filename
# 030
# 	        StatusBar.push(0,"Opened File: " + filename)
# 031
# 	        index = filename.replace("\\","/").rfind("/") + 1
# 032
# 	        window.set_title(filename[index:] + " - PyPad")
# 033
# 	        file = open(filename, "r")
# 034
# 	        text = file.read()
# 035
# 	        textbuffer.set_text(text)
# 036
# 	        file.close()
# 037
# 	    elif response == gtk.RESPONSE_CANCEL:
# 038
# 	        chooser.destroy()
# 039
# 	        chooser.destroy()
# 040
# 	    def save_file_as(menuitem,user_param):
# 041
# 	    chooser = gtk.FileChooserDialog(title="Save file",action=gtk.FILE_CHOOSER_ACTION_SAVE, buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_SAVE,gtk.RESPONSE_OK))
# 042
# 	        chooser.set_default_response(gtk.RESPONSE_OK)
# 043
# 	    filter = gtk.FileFilter()
# 044
# 	        filter.set_name("Text Files")
# 045
# 	        filter.add_mime_type("text/data")
# 046
# 	        filter.add_pattern("*.txt")
# 047
# 	        chooser.add_filter(filter)
# 048
# 	    filter2 = gtk.FileFilter()
# 049
# 	    filter2.set_name("All Files")
# 050
# 	    filter2.add_pattern("*.*")
# 051
# 	    chooser.add_filter(filter2)
# 052
# 	    response = chooser.run()
# 053
# 	    if response == gtk.RESPONSE_OK:
# 054
# 	        global _File
# 055
# 	        filename = chooser.get_filename()
# 056
# 	        _File = filename
# 057
# 	        textbuffer = TextBox.get_buffer()
# 058
# 	        print "Saved File: " + filename
# 059
# 	            StatusBar.push(0,"Saved File: " + filename)
# 060
# 	        index = filename.replace("\\","/").rfind("/") + 1
# 061
# 	        text = textbuffer.get_text(textbuffer.get_start_iter() , textbuffer.get_end_iter())
# 062
# 	        window.set_title(filename[index:] + " - PyPad")
# 063
# 	        file = open(filename, "w")
# 064
# 	        file.write(text)
# 065
# 	        file.close()
# 066
# 	    elif response == gtk.RESPONSE_CANCEL:
# 067
# 	        chooser.destroy()
# 068
# 	        chooser.destroy()
# 069
# 	    def reset_new(menuitem,user_param):
# 070
# 	    _File = ""
# 071
# 	        print "PyPad has been reset!"
# 072
# 	    window.set_title("Untitled - PyPad")
# 073
# 	    textbuffer = TextBox.get_buffer()
# 074
# 	    textbuffer.set_text("")
# 075
# 	    def save_file(menuitem,user_param):
# 076
# 	    if _File is not "":
# 077
# 	        textbuffer = TextBox.get_buffer()
# 078
# 	        print "Saved File: " + _File
# 079
# 	            StatusBar.push(0,"Saved File: " + filename)
# 080
# 	        index = filename.replace("\\","/").rfind("/") + 1
# 081
# 	        text = textbuffer.get_text(textbuffer.get_start_iter() , textbuffer.get_end_iter())
# 082
# 	        window.set_title(_File[index:] + " - PyPad")
# 083
# 	        file = open(_File, "r+")
# 084
# 	        file.write(text)
# 085
# 	        file.close()
# 086
# 	    def __init__(self):
# 087
# 	        window.set_title("Untitled - PyPad")
# 088
# 	    window.set_default_size(750,450)
# 089
# 	    window.connect('destroy', gtk.main_quit)
# 090
# 	        TextBox.set_wrap_mode(gtk.WRAP_WORD)
# 091
# 	        TextBox.set_editable(True)
# 092
# 	        TextBox.set_cursor_visible(True)   
# 093
# 	        TextBox.set_border_window_size(gtk.TEXT_WINDOW_LEFT,1)
# 094
# 	        TextBox.set_border_window_size(gtk.TEXT_WINDOW_RIGHT,1)
# 095
# 	        TextBox.set_border_window_size(gtk.TEXT_WINDOW_TOP,1)
# 096
# 	        TextBox.set_border_window_size(gtk.TEXT_WINDOW_BOTTOM,1)
# 097
# 	    vbox = gtk.VBox(False,0)
# 098
# 	    box1 = gtk.VBox(False, 10)
# 099
# 	    box2 = gtk.VBox(False, 20)
# 100
# 	    box3 = gtk.VBox(False, 70)
# 101
# 	    vbox.pack_start(box2, False, False, 0)
# 102
# 	    vbox.pack_start(box1, True, True, 0)
# 103
# 	    vbox.pack_start(box3, False, False, 0)
# 104
# 	    sw = gtk.ScrolledWindow()
# 105
# 	    sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
# 106
# 	    sw.add(TextBox)
# 107
# 	    box1.pack_start(sw)
# 108
# 	    box2.pack_start(MenuBar, True, False, 0)
# 109
# 	    box3.pack_start(StatusBar, True, False, 0)
# 110
# 	    filemenu = gtk.Menu()
# 111
# 	        filem = gtk.MenuItem("File")
# 112
# 	    newm = gtk.MenuItem("New")
# 113
# 	    openm = gtk.MenuItem("Open")
# 114
# 	    savem = gtk.MenuItem("Save")
# 115
# 	    saveasm = gtk.MenuItem("Save As")
# 116
# 	    openm.connect("activate",self.open_file)
# 117
# 	    saveasm.connect("activate",self.save_file_as)
# 118
# 	    newm.connect("activate",self.reset_new)
# 119
# 	    savem.connect("activate",self.save_file)
# 120
# 	    filemenu.append(newm)
# 121
# 	    filemenu.append(openm)
# 122
# 	    filemenu.append(savem)
# 123
# 	    filemenu.append(saveasm)
# 124
# 	        filem.set_submenu(filemenu)
# 125
# 	    MenuBar.append(filem)
# 126
# 	    window.add(vbox)
# 127
# 	    window.show_all()
# 128
# 	def main():
# 129
# 	    gtk.gdk.threads_enter()
# 130
# 	    gtk.main()
# 131
# 	    gtk.gdk.threads_leave()
# 132
	     
# 133
# 	if __name__ == "__main__":
# 134
# 	    Initialize = MainForm()
# 135
	    main()