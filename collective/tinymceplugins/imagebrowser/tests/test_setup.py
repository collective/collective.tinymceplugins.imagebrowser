# -*- coding: utf-8 -*-
"""Test installation of PLR into Plone."""

import unittest

from Products.CMFCore.utils import getToolByName

from collective.tinymceplugins.imagebrowser import testing

class TestSetup(testing.TestCase):
    """Test installation of collective.tinymceplugins.imagebrowser"""
        
    def test_skin_folder_registered(self):
        """Test if all ./skins folders are registered in order"""
        skins = getToolByName(self.portal, 'portal_skins')
        skin = skins.getSkinPath('Plone Default')
        self.failUnless('tinymce_plugin_imagebrowser' in skin)
        order = skin.find('tinymce_plugin_imagebrowser') < skin.find('tinymce,')
        self.failUnless(order)
        
        
def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
