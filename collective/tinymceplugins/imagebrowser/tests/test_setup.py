import unittest
from zope.component import getUtility 
from zope.interface.verify import verifyObject 

from Products.CMFCore.utils import getToolByName
from Products.TinyMCE.interfaces.utility import ITinyMCE

from collective.tinymceplugins.imagebrowser import testing
from collective.tinymceplugins.imagebrowser.interfaces import \
        ITinyMCELibrariesExtended


class TestSetup(testing.TestCase):
    """Test installation of collective.tinymceplugins.imagebrowser"""
        
    def test_skin_folder_registered(self):
        """Test if all ./skins folders are registered in order"""
        skins = getToolByName(self.portal, 'portal_skins')
        skin = skins.getSkinPath('Plone Default')
        self.failUnless('tinymce_plugin_imagebrowser' in skin)
        order = skin.find('tinymce_plugin_imagebrowser') < skin.find('tinymce,')
        self.failUnless(order)

    def test_tinymce_adapter(self):
        tmce = getUtility(ITinyMCE) 
        tmce_ = ITinyMCELibrariesExtended(tmce)
        self.assert_(ITinyMCELibrariesExtended.providedBy(tmce_))   
        self.assert_(verifyObject(ITinyMCELibrariesExtended, tmce_))
        tmce_.imagebrowser_ressources = "test"
        self.assertEquals("test", tmce_.imagebrowser_ressources)    

    def test_tinymce_controlpanel(self):
        panel = self.portal.unrestrictedTraverse('portal_tinymce/@@tinymce-controlpanel')
        html = panel.render()
        self.assert_(html)   

    def test_tinymce_imagebrowser_ressource_view(self):
        res = self.portal.unrestrictedTraverse('portal_tinymce/@@imagebrowser_ressources/ressources')
        self.assertEquals([], res)    
  
        
def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
