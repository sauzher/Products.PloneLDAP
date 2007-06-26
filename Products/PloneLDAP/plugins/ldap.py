from zope.interface import implementedBy
from AccessControl import ClassSecurityInfo
from App.class_init import default__class_init__ as InitializeClass
from Products.LDAPMultiPlugins.LDAPMultiPlugin import LDAPMultiPlugin
from Products.PluggableAuthService.interfaces.plugins import \
     IUserEnumerationPlugin, IGroupsPlugin, IGroupEnumerationPlugin, \
     IRoleEnumerationPlugin, IUserAdderPlugin
from Products.PluggableAuthService.utils import classImplements
from Products.PlonePAS.interfaces.plugins import IUserManagement
from Products.PloneLDAP.plugins.base import PloneLDAPPluginBaseMixin


class PloneLDAPMultiPlugin(PloneLDAPPluginBaseMixin, LDAPMultiPlugin):
    """Plone LDAP plugin.
    """
    security = ClassSecurityInfo()
    meta_type = "Plone LDAP plugin"

    security.declarePrivate('doAddUser')
    def doAddUser(self , login , password):
        """ Fulfill the UserAdderPlugin requirements """
        acl = self._getLDAPUserFolder()

        if acl is None:
            return False

        attrs = {}
        attrs['dn'] = login
        attrs['user_pw'] = attrs['confirm_pw'] = password
        # For uid and loginname we assume that they are the same. This
        # need not be true, but PlonePAS treats them the same when creating
        # users.
        for key in ( acl._uid_attr, acl._login_attr, acl._rdnattr):
            if key not in attrs:
                attrs[key] = login

        # Evil: grab all schema attributes and will them with a default
        # text. This is needed to be able to create LDAP entries where
        # attributes besides uid, login and rdn are required.
        for (key,name) in acl.getLDAPSchema():
            if key not in attrs:
                attrs[key]="unset"

        res=acl.manage_addUser(kwargs=attrs)

        if res:
            zLOG.LOG('LDAPMP', zLOG.PROBLEM,
                     'manage_addUser failed with %s' % res)

        view_name = self.getId() + '_enumerateUsers'
        self.ZCacheable_invalidate(view_name = view_name,)

        return not res


    security.declarePrivate('doAddUser')
    def doChangeUser(self, login, password, **kw):
        """ Change a user's password. Only implements password changing
        which is required by IUserManagement."""
        acl = self._getLDAPUserFolder()

        if acl is not None:
            user = acl.getUser(login)
            
            if user is not None:
                user_dn = user.getUserDN()
                acl.manage_editUserPassword(user_dn, password)


    security.declarePrivate('doAddUser')
    def doDeleteUser(self , login):
        """ Remove a user record from a User Manager. """
        acl = self._getLDAPUserFolder()

        if acl is not None:
            user = acl.getUser(login)

            if user is not None:
                user_dn = user.getUserDN()

                acl.manage_deleteUsers(dns=[user_dn])


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
