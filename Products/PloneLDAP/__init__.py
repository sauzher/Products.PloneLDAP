from AccessControl.Permissions import add_user_folders
from Products.PluggableAuthService.PluggableAuthService import \
                registerMultiPlugin
from Products.PloneLDAP.plugins.ldap import PloneLDAPMultiPlugin
from Products.PloneLDAP.plugins.ad import PloneActiveMultiPlugin
from Products.PloneLDAP.factory import manage_addPloneLDAPMultiPluginForm,\
                manage_addPloneLDAPMultiPlugin

registerMultiPlugin(PloneLDAPMultiPlugin.meta_type)
registerMultiPlugin(PloneActiveDirectoryMultiPlugin.meta_type)

def initialize(context):

    context.registerClass(
            PloneLDAPMultiPlugin,
            permission=add_user_folders,
            constructors=(manage_addPloneLDAPMultiPluginForm,
                manage_addPloneLDAPMultiPlugin),
            icon="www/ldapmultiplugin.png",
            visibility=None)

