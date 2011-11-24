from zope.component import getUtility

from plone.registry.interfaces import IRegistry
from Products.Five import BrowserView

from collective.tinymceplugins.imagebrowser.interfaces import \
        ITinyMCELibrariesImageResources


class ImagebrowserResources(BrowserView):

    @property
    def resources(self):
        """Returns a list of all tinymce imagebrowser resources.
           A resource is a list ([id,title,path_to_folder]).
        """

        registry = getUtility(IRegistry)
        registry = registry.forInterface(ITinyMCELibrariesImageResources)
        resources = registry.imagebrowser_resources

        resources = [x.split('|') for x in resources]
        resources = filter(lambda x: len(x) >= 3, resources)

        return resources
