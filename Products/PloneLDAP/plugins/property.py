from Products.CMFCore.utils import getToolByName
from Products.PluggableAuthService.utils import classImplements
from Products.PluggableAuthService.UserPropertySheet import UserPropertySheet
from Products.PlonePAS.interfaces.propertysheets import IMutablePropertySheet


class LDAPPropertySheet(UserPropertySheet):
    def __init__(self, id, user):
        self.id=id
        acl=self._getLDAPUserFolder(user)
        ldap_user = acl.getUserById(user.getId())
        properties={}

        if ldap_user is None:
            self._ldapschema=[]
        else:
            self._ldapschema=[(x['ldap_name'], x['public_name'],
                            x['multivalued'] and 'lines' or 'string') \
                        for x in acl.getSchemaConfig().values() \
                        if x['public_name']]

        for (ldapname, zopename, type) in self._ldapschema:
            if ldap_user._properties.has_key(ldapname):
                properties[zopename]=ldap_user._properties[ldapname]
            else:
                if type=='lines':
                    properties[ldapname]=[]
                else:
                    properties[ldapname]=""

        UserPropertySheet.__init__(self, id,
                schema=[(x[1],x[2]) for x in self._ldapschema], **properties)


    def setProperty(self, user, id, value):
        self.setProperties(user, {id:value})


    def setProperties(self, user, mapping):
        acl=self._getLDAPUserFolder(user)
        ldap_user = acl.getUserById(user.getId())

        schema=dict([(x[1], (x[0], x[2])) for x in self._ldapschema])
        changes={}

        for (key,value) in mapping.items():
            if key in schema and self._properties[key]!=value:
                if schema[key][1]=="lines":
                    value=[x.strip() for x in value]
                else:
                    value=[value.strip()]
                self._properties[key]=value
                changes[schema[key][0]]=value

        acl._delegate.modify(ldap_user.dn, attrs=changes)
	acl._expireUser(user.getUserName())


    def _getLDAPUserFolder(self, user):
        """ Safely retrieve a LDAPUserFolder to work with """
        portal=getToolByName(user.acl_users, 'portal_url').getPortalObject()
        return portal.acl_users._getOb(self.id).acl_users



classImplements(LDAPPropertySheet,
                            IMutablePropertySheet)

