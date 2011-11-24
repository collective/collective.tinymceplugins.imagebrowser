from zope import schema 
from zope.interface import Interface
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.tinymceplugins.imagebrowser')


class ITinyMCELibrariesExtended(Interface):  

    imagebrowser_resources = schema.Text(
        title=_(u"Image Ressources"),
        description=_(u"""Enter a list of resources to appear in the link image
            dialog. The format is id|title|path_to_folder|path_to_icon, one per
            line. An example path_to_folder is "PloneRoot/pictures", an example
            path_to_icon is "/logoIcon.gif". The path_to_icon is optional.
            """),
        required=False)    
                           

#TODO: better message ids with correct english, better interface names
class ITinyMCELibrariesImageResources(Interface):
    """Plone registry entries to register TinyMCE image browser resources.
    """

    imagebrowser_resources = schema.List(title=_(u"Image Ressources"),
                              required=False,
                              value_type=schema.TextLine(),
                              default=[], 
                              missing_value=[]) 
