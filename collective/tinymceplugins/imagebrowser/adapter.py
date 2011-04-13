from rwproperty import getproperty, setproperty 

from zope.interface import implements
from zope.component import adapts

from Products.TinyMCE.interfaces.utility import ITinyMCELibraries 
from collective.tinymceplugins.imagebrowser.interfaces import \
        ITinyMCELibrariesExtended 


class TinyMCEExtendedAdapter(object):

    implements(ITinyMCELibrariesExtended)
    adapts(ITinyMCELibraries)
    
    def __init__(self, context):
        self.context = context

    @getproperty
    def imagebrowser_ressources(self):
        lines = ""
        if hasattr(self.context, '_imagebrowser_ressources'):
            lines = self.context._imagebrowser_ressources 
        return lines

    @setproperty
    def imagebrowser_ressources(self, lines):
        if not lines:
            return
        self.context._imagebrowser_ressources = lines
