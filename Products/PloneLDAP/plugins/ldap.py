import logging
from zope.interface import implementedBy
from AccessControl import ClassSecurityInfo
from Globals import InitializeClass
from Products.LDAPMultiPlugins.LDAPMultiPlugin import LDAPMultiPlugin
from Products.PluggableAuthService.interfaces.plugins import \
     IUserEnumerationPlugin, IGroupsPlugin, IGroupEnumerationPlugin, \
     IRoleEnumerationPlugin, IUserAdderPlugin
from Products.PluggableAuthService.utils import classImplements
from Products.PlonePAS.interfaces.plugins import IUserManagement
from Products.PloneLDAP.plugins.base import PloneLDAPPluginBaseMixin
from Products.PloneLDAP.mixins import UserAdderMixin
from Products.PloneLDAP.mixins import UserManagementMixin
from Products.PloneLDAP.mixins import UserPropertiesMixin

logger = logging.getLogger("PloneLDAP")

class PloneLDAPMultiPlugin(PloneLDAPPluginBaseMixin, UserAdderMixin,
        UserManagementMixin, UserPropertiesMixin, LDAPMultiPlugin):
    """Plone LDAP plugin.
    """
    security = ClassSecurityInfo()
    meta_type = "Plone LDAP plugin"



classImplements(PloneLDAPMultiPlugin
               , IUserEnumerationPlugin
               , IGroupsPlugin
               , IUserAdderPlugin
               , IGroupEnumerationPlugin
               , IRoleEnumerationPlugin
               , IUserManagement
               , *implementedBy(LDAPMultiPlugin)
               )
 
InitializeClass(PloneLDAPMultiPlugin)

