import logging
from zope.interface import implementedBy
from AccessControl import ClassSecurityInfo
from Globals import InitializeClass
from Products.LDAPMultiPlugins.LDAPMultiPlugin import LDAPMultiPlugin
from Products.PluggableAuthService.interfaces.plugins import \
     IUserEnumerationPlugin, IGroupsPlugin, IGroupEnumerationPlugin, \
     IRoleEnumerationPlugin, IUserAdderPlugin
from Products.PluggableAuthService.utils import classImplements
from Products.PlonePAS.interfaces.capabilities import IDeleteCapability
from Products.PlonePAS.interfaces.capabilities import IPasswordSetCapability
from Products.PlonePAS.interfaces.plugins import IUserManagement
from Products.PloneLDAP.plugins.base import PloneLDAPPluginBaseMixin
from Products.PloneLDAP.mixins import UserAdderMixin
from Products.PloneLDAP.mixins import UserManagementMixin
from Products.PloneLDAP.mixins import UserPropertiesMixin

from Products.PloneLDAP.mixins import GroupCapabilityMixin
from Products.PloneLDAP.mixins import GroupIntrospectionMixin
from Products.PloneLDAP.mixins import GroupManagementMixin

logger = logging.getLogger("PloneLDAP")

class PloneLDAPMultiPlugin(PloneLDAPPluginBaseMixin,
        UserAdderMixin, UserManagementMixin, UserPropertiesMixin, 
        GroupCapabilityMixin, GroupIntrospectionMixin, GroupManagementMixin,
        LDAPMultiPlugin):
    """Plone LDAP plugin. Yeah baby.
    """
    security = ClassSecurityInfo()
    meta_type = "Plone LDAP plugin"


classImplements(PloneLDAPMultiPlugin
               , IUserEnumerationPlugin
               , IGroupsPlugin
               , IUserAdderPlugin
               , IGroupEnumerationPlugin
               , IRoleEnumerationPlugin
               , IDeleteCapability
               , IPasswordSetCapability
               , IUserManagement
               , *implementedBy(LDAPMultiPlugin)
               )
 
InitializeClass(PloneLDAPMultiPlugin)

