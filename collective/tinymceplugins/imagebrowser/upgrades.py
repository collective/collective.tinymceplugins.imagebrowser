from plone.app.upgrade.utils import loadMigrationProfile

def to1beta3(context):
    loadMigrationProfile(context, 'profile-collective.tinymceplugins.imagebrowser:to1beta3')