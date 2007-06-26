from Acquisition import aq_base
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from Products.LDAPUserFolder import manage_addLDAPUserFolder
from Products.PloneLDAP.plugins.ldap import PloneLDAPMultiPlugin


manage_addPloneLDAPMultiPluginForm = PageTemplateFile("www/addLdapPlugin",
                                                        globals())


def manage_addPloneLDAPMultiPlugin(self, id, title, LDAP_server, login_attr,
        uid_attr, users_base, users_scope, roles, groups_base, groups_scope,
        binduid, bindpwd, binduid_usage=1, rdn_attr='cn', local_groups=0,
        use_ssl=0, encryption='SHA', read_only=0, REQUEST=None):
    """Add a Plone LDAP plugin to the site"""

    # Make sure we really are working in our container (the 
    # PluggableAuthService object)
    self = self.this()

    # First we create the plugin
    plugin = PloneLDAPMultiPlugin(id, title)
    self._setObject(id, plugin)
    plugin = getattr(aq_base(self), id)

    # And then we have to create an LDAPUserFolder inside it
    manage_addLDAPUserFolder(plugin)
    luf=getattr(aq_base(plugin), "acl_users")

    # Figure out the LDAP port number to use
    host_elems = LDAP_server.split(':')
    host = host_elems[0]
    if len(host_elems) > 1:
        port = host_elems[1]
    else:
        if use_ssl:
            port = '636'
        else:
            port = '389'

    # Configure the LDAPUserFolder
    luf.manage_addServer(host, port=port, use_ssl=use_ssl)
    luf.manage_edit(title, login_attr, uid_attr, users_base, users_scope,
            roles, groups_base, groups_scope, binduid, bindpwd,
            binduid_usage=binduid_usage, rdn_attr=rdn_attr,
            local_groups=local_groups, encryption=encryption,
            read_only=read_only, REQUEST=None)

    # clean out the __allow_groups__ bit because it is not needed here
    # and potentially harmful
    plugin_base = aq_base(plugin)
    if hasattr(plugin_base, '__allow_groups__'):
        del plugin_base.__allow_groups__


    # Redirect back to the user folder
    if REQUEST is not None:
        return REQUEST["RESPONSE"].redirect("%s/manage_workspace?manage_tabs_message=AutoGroup+plugin+added" %
                self.absolute_url())


