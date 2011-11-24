from zope import schema
from zope.interface import Interface
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.tinymceplugins.imagebrowser')


#TODO: better message ids with correct english, better interface names
class ITinyMCELibrariesImageResources(Interface):
    """Plone registry entries to register TinyMCE image browser resources.
    """

    imagebrowser_resources = schema.List(title=_(u"Image Ressources"),
                              required=False,
                              value_type=schema.TextLine(),
                              default=[],
                              missing_value=[])
