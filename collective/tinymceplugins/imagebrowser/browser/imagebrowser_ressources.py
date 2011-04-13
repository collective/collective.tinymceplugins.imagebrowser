from zope.component import getUtility 

from Products.Five import BrowserView
from Products.TinyMCE.interfaces.utility import ITinyMCE

from collective.tinymceplugins.imagebrowser.interfaces import \
        ITinyMCELibrariesExtended 
 

class ImagebrowserRessources(BrowserView):

    @property
    def ressources(self):
        """Returns a list of all tinymce imagebrowser ressources.
           A ressource is a list ([id,title,path_to_folder]).
        """ 
  
        tmce = getUtility(ITinyMCE) 
        tmce_ = ITinyMCELibrariesExtended(tmce) 
        lines =  tmce_.imagebrowser_ressources.splitlines() 

        ressources = [x.split('|') for x in lines]
        ressources = filter(lambda x: len(x) >= 3 , ressources)

        return ressources
        

