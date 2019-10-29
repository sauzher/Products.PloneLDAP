from zope.interface import implementer
from Products.CMFQuickInstallerTool.interfaces import INonInstallable

class HiddenLDAPProducts(object):
    implementer(INonInstallable)

    def getNonInstallableProducts(self):
        return [ "LDAPUserFolder" ]
