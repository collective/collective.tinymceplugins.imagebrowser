from zope.i18nmessageid import MessageFactory
from plone.fieldsets.fieldsets import FormFieldsets

from Products.TinyMCE.browser.controlpanel import TinyMCEControlPanelForm
from Products.TinyMCE.interfaces.utility import ITinyMCELibraries
from collective.tinymceplugins.imagebrowser.browser.interfaces import \
        ITinyMCELibrariesExtended

_ = MessageFactory('plone.tinymce')


class TinyMCEControlPanelFormExtended(TinyMCEControlPanelForm):
    """We subclass the TinyMCE Control Panel Form to enable the library
    fieldset"""

    tinymcelibraries = FormFieldsets(ITinyMCELibraries, ITinyMCELibrariesExtended)
    tinymcelibraries.id = 'tinymcelibraries'
    tinymcelibraries.label = _(u'Libraries')

    form_fields = FormFieldsets(TinyMCEControlPanelForm.tinymcelayout,
                                TinyMCEControlPanelForm.tinymcetoolbar,
                                TinyMCEControlPanelForm.tinymceresourcetypes,
                                tinymcelibraries)
