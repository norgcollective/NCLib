import gi;
gi.require_version("Gtk","4.0");
gi.require_version("Adw", "1");
from gi.repository import Gtk, Adw;

def AddAndReset(min, max, first, second): # if a+b > max -> min + ( b - (max - a))

    if second > max or first > max or second < min or first < min:
        raise Exception("Maximum " + str(max) + "\nMinimum " + str(min) + "\nFrist" + str(first) + "\nSecond " + str(second))

    if second <0: raise Exception("AddAndReset: Subtraction is not allowed")

    result = None

    if first + second > max:
        result = min + (second - (max - first))
    else:
        result = first + second

    return result

def SubAndReset(min, max, first, second): # if a-b < min -> max - ( b - a )

    if second > max or first > max or second < min or first < min:
        raise Exception("Maximum " + str(max) + "\nMinimum " + str(min) + "\nFrist" + str(first) + "\nSecond " + str(second))

    if second <0: raise Exception("SubAndReset: Addition is not allowed")

    result = None

    if first - second < min:
        result = max - (second - first)
    else:
        result = first - second

    return result

def CreateAdwApplicationWindow(app, title, edition, devel_mode=False,silent=False):
        if not silent: print("NCLIB: Called NCLIB.CreateAdwApplicationWindow")
        MainWindow = Adw.ApplicationWindow(application=app)
        if devel_mode: MainWindow.add_css_class('devel')

        WindowContent   = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        widget_TitleBar = Adw.HeaderBar()
        widget_Title    = Adw.WindowTitle(title=title, subtitle=edition)

        WindowContent.append(widget_TitleBar)

        widget_TitleBar.set_title_widget(widget_Title)

        return (MainWindow, WindowContent)
        ## How To Use: (of course, in Adw.Appication Class)
        
        #cache = NCLib.CreateAdwApplicationWindow(app, "Project Rain", "Developer Edition", devel_mode=True)
        #self.MainWindow    = cache[0]
        #self.WindowContent = cache[1]
        #del cache

        #self.MainWindow.set_content(self.WindowContent) ## THIS IS IMPORTANT
