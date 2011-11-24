from zope.component import getUtility

from plone.app.upgrade.utils import loadMigrationProfile
from Products.TinyMCE.interfaces.utility import ITinyMCE

from collective.tinymceplugins.imagebrowser.browser.interfaces import \
        ITinyMCELibrariesExtended


def to1beta3(context):
    loadMigrationProfile(context, 'profile-collective.tinymceplugins.imagebrowser:to1beta3')


def to1beta4(context):
    tmce = getUtility(ITinyMCE)
    adapter = ITinyMCELibrariesExtended(tmce)
    if hasattr(tmce, "_imagebrowser_ressources"):
        resources_old = tmce._imagebrowser_ressources
        adapter.imagebrowser_resources = resources_old
        delattr(tmce, "_imagebrowser_ressources")
