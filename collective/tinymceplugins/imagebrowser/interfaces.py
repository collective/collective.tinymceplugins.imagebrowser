from zope import schema 
from zope.interface import Interface
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.tinymceplugins.imagebrowser')


class ITinyMCELibrariesExtended(Interface):  

    imagebrowser_ressources = schema.Text(
        title=_(u"Image Ressources"),
        description=_(u"""Enter a list of ressources to appear in the link image
            dialog. The format is id|title|path_to_folder, one per line."""),
        required=False)    
                           


 
