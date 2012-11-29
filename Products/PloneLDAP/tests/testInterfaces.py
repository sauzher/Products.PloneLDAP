from Products.PlonePAS.interfaces.capabilities import IGroupCapability

from Products.PloneLDAP.tests.integrationcase import PloneLDAPIntegrationTestCase
from Products.PloneLDAP.plugins.base import PloneLDAPPluginBaseMixin
from Products.PloneLDAP.plugins.ldap import PloneLDAPMultiPlugin
from Products.PloneLDAP.plugins.ad import PloneActiveDirectoryMultiPlugin


class TestInterfaces(PloneLDAPIntegrationTestCase):
    """Test that the plugins implement the interfaces correctly.

    If we say we implement an interface, we should have the required
    attributes and methods.  Otherwise, we can get errors.  For
    example, the AD plugin used to claim to implement
    IGroupCapability, but it did not have the mixin class that
    delivered the required methods.  So when Plone displays the groups
    of a user that is a member of an AD group, this would give a
    traceback because Plone tried to use one of the advertised
    methods.

    In most cases here we do not mind much if a plugin claims to
    implement an interface or not, but IF it implements it, it must
    fulfill that promise, otherwise we raise an assertion error.

    We would want to use verifyClass, but that fails because the
    PlonePAS interfaces are wrongly defined with 'self', which means a
    test like this would always fail:

    from zope.interface.verify import verifyClass
    self.assertTrue(verifyClass(IGroupCapability, PloneLDAPMultiPlugin))
    """

    def _testGroupCapability(self, plugin_class):
        if IGroupCapability.implementedBy(plugin_class):
            # This may or may not be true, but if it is true, then the
            # following should be true as well.
            self.assertTrue(hasattr(plugin_class, 'allowGroupAdd'))
            self.assertTrue(hasattr(plugin_class, 'allowGroupRemove'))

    def testPloneLDAPPluginBaseMixinInterfaces(self):
        self._testGroupCapability(PloneLDAPPluginBaseMixin)

    def testGroupCapabilityAD(self):
        self._testGroupCapability(PloneActiveDirectoryMultiPlugin)

    def testGroupCapabilityLDAP(self):
        self._testGroupCapability(PloneLDAPMultiPlugin)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite=TestSuite()
    suite.addTest(makeSuite(TestInterfaces))
    return suite
