from Globals import InitializeClass
from AccessControl import ClassSecurityInfo

class UserManagementMixin:
    """Implement Products.PlonePAS.interfaces.plugins.IUserManagement
    """
    security = ClassSecurityInfo()

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

InitializeClass(UserManagementMixin)

