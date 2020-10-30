import gtk

class PyApp(gtk.Window):
   def exit(self,widget):
      gtk.main_quit()
   def __init__(self):
      super(PyApp, self).__init__()
      # Window Setting
      self.set_title("Button Box demo")
      self.set_size_request(200,100)
      self.set_position(gtk.WIN_POS_CENTER)
      

      # Vertical Button Box
      vb = gtk.HBox(False, 5)
      box1 = gtk.HButtonBox()
      btn1 = gtk.Button(stock = gtk.STOCK_OK)
      btn2 = gtk.Button(stock = gtk.STOCK_CANCEL)
      btn3 = gtk.Button(stock = "Exit")
      btn3.connect("clicked",self.exit)		
      box1.pack_start(btn1, True, True, 0)
      box1.pack_start(btn2, True, True, 0)
      box1.pack_start(btn3, True, True, 0)
      box1.set_border_width(5)
      valign = gtk.Alignment(0.5,0.25, 0, 0)
      valign.add(vb)	
      vb.add(box1)
      #self.add(vb)
      self.show_all()
      

      	
PyApp()
gtk.main()
