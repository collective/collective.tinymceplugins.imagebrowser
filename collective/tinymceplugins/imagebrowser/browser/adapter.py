from rwproperty import getproperty, setproperty

from zope.interface import implements
from zope.component import adapts
from zope.component import getUtility

from plone.registry.interfaces import IRegistry
from Products.TinyMCE.interfaces.utility import ITinyMCELibraries

from collective.tinymceplugins.imagebrowser.browser.interfaces import \
        ITinyMCELibrariesExtended
from collective.tinymceplugins.imagebrowser.interfaces import \
        ITinyMCELibrariesImageResources


class TinyMCEExtendedAdapter(object):

    implements(ITinyMCELibrariesExtended)
    adapts(ITinyMCELibraries)

    def __init__(self, context):
        self.context = context
        registry = getUtility(IRegistry)
        self.registry = registry.forInterface(ITinyMCELibrariesImageResources)

    @getproperty
    def imagebrowser_resources(self):
        resources = self.registry.imagebrowser_resources
        lines = u"\n".join(resources)
        return lines

    @setproperty
    def imagebrowser_resources(self, lines):
        if not lines:
            return
        resources = lines.splitlines()
        self.registry.imagebrowser_resources = resources
