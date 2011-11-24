import unittest
from zope.component import getUtility
from zope.interface.verify import verifyObject

from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from Products.TinyMCE.interfaces.utility import ITinyMCE

from collective.tinymceplugins.imagebrowser import testing
from collective.tinymceplugins.imagebrowser.browser.interfaces import \
        ITinyMCELibrariesExtended


REGISTRY_KEY = 'collective.tinymceplugins.imagebrowser.interfaces.ITinyMCELibrariesImageResources.imagebrowser_resources'


class TestSetup(testing.TestCase):
    """Test installation of collective.tinymceplugins.imagebrowser"""

    def test_skin_folder_registered(self):
        """Test if all ./skins folders are registered in order"""
        skins = getToolByName(self.portal, 'portal_skins')
        skin = skins.getSkinPath('Plone Default')
        self.failUnless('tinymce_plugin_imagebrowser' in skin)
        order = skin.find('tinymce_plugin_imagebrowser') < skin.find('tinymce,')
        self.failUnless(order)

    def test_plone_registry_entries(self):
        registry = getUtility(IRegistry)
        resources = registry.get(REGISTRY_KEY)
        self.assert_(resources == [])

    def test_tinymce_adapter_interface(self):
        tmce = getUtility(ITinyMCE)
        adapter = ITinyMCELibrariesExtended(tmce)
        self.assert_(ITinyMCELibrariesExtended.providedBy(adapter))
        self.assert_(verifyObject(ITinyMCELibrariesExtended, adapter))

    def test_tinymce_adapter_getting_values(self):
        registry = getUtility(IRegistry)
        tmce = getUtility(ITinyMCE)
        adapter = ITinyMCELibrariesExtended(tmce)
        self.assert_(adapter.imagebrowser_resources == u"")
        registry[REGISTRY_KEY] = [u"id"]
        self.assert_(adapter.imagebrowser_resources == u"id")

    def test_tinymce_adapter_setting_values(self):
        registry = getUtility(IRegistry)
        tmce = getUtility(ITinyMCE)
        adapter = ITinyMCELibrariesExtended(tmce)
        adapter.imagebrowser_resources = u"id2\nid3"
        self.assert_(registry[REGISTRY_KEY] == [u"id2", u"id3"])

    def test_tinymce_controlpanel(self):
        panel = self.portal.unrestrictedTraverse('portal_tinymce/@@tinymce-controlpanel')
        html = panel.render()
        self.assert_(html)

    def test_tinymce_imagebrowser_resource_view(self):
        registry = getUtility(IRegistry)
        registry[REGISTRY_KEY] = [u"id4", u"id5|title|path|iconpath"]
        resources = self.portal.unrestrictedTraverse('portal_tinymce/@@imagebrowser_resources/resources')
        self.assert_([[u'id5', u'title', u'path', u'iconpath']] == resources)

        registry[REGISTRY_KEY] = [u"id4|title|path", u"id5|title|path|iconpath"]
        resources = self.portal.unrestrictedTraverse('portal_tinymce/@@imagebrowser_resources/resources')
        self.assert_([[u'id4', u'title', u'path'], [u'id5', u'title', u'path', u'iconpath']] == resources)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
