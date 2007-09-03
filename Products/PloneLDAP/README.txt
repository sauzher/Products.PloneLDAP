The PloneLDAP product is intended to make it easier to use LDAP connections in
a Plone website. It builds upon the excellent LDAPMultiPlugins_ and
"LDAPUserFolder_ products which provide the basic LDAP infrastructure. 

The extra functionality provided by this product require features
beyond that are not part of the standard Pluggable Authentication Service,
which is why they are not included in LDAPMultiPlugins.

.. _LDAPMultiPlugins: http://www.dataflake.org/software/ldapmultiplugins
.. _LDAPUserFolder: http://www.dataflake.org/software/ldapuserfolder


Requirements
============

* Plone 2.5 or later
* python-ldap_
* LDAPUserFolder 2.8
* LDAPMultiPlugins 1.5

.. _python-ldap: http://python-ldap.sourceforge.net/

PloneLDAP has been developed for Plone 3.0. While it does support Plone 2.5
it is highly recommended to use Plone 3.0.


Installation
============

First you need to install the python-ldap package and the LDAPUserFolder,
LDAPMultiPlugins and PloneLDAP products.

PloneLDAP provides PAS plugins that you can use to get your site talking to
LDAP or Active Directory. To install them go the acl_users folder in your
site. Select the right plugin from the dropdown menu in the top right: use
'Plone LDAP Plugin' if you want to connect to a standard LDAP server or
'Plone Active Directory Plugin' if you want to connect to a Microsoft Active
Directory server. 

After selecting the plugin type you will see a screen where you need to
submit the configuration information. Consult your LDAP or AD administrator
if you are not sure what the correct information is.



Credits
=======

Funding
    CentrePoint_

Implementation
    Simplon_, Wichert Akkerman
 

.. _Simplon: http://www.simplon.biz/
.. _CentrePoint: http://centrepoint.org.uk/


Copyright
=========

PloneLDAP is copyright 2007 by Simplon_ and licensed under the GNU General
Public License, version 2.

