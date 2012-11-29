from Products.PloneLDAP.tests.integrationcase import PloneLDAPIntegrationTestCase
from Products.PloneLDAP.plugins.ldap import PloneLDAPMultiPlugin
from Products.PloneLDAP.plugins.ad import PloneActiveDirectoryMultiPlugin


class TestInterfaces(PloneLDAPIntegrationTestCase):

    def testGroupCapabilityAD(self):
        from Products.PlonePAS.interfaces.capabilities import IGroupCapability
        self.assertTrue(IGroupCapability.implementedBy(PloneActiveDirectoryMultiPlugin))

        # If we say we implement an interface, we should have the
        # required attributes and methods.  We would want to use
        # verifyClass, but that fails because the PlonePAS interfaces
        # are wrongly defined with 'self', which means this test would
        # always fail.
        #from zope.interface.verify import verifyClass
        #self.assertTrue(verifyClass(IGroupCapability, PloneLDAPMultiPlugin))
        self.assertTrue(hasattr(PloneActiveDirectoryMultiPlugin, 'allowGroupAdd'))
        self.assertTrue(hasattr(PloneActiveDirectoryMultiPlugin, 'allowGroupRemove'))

    def testGroupCapabilityLDAP(self):
        from Products.PlonePAS.interfaces.capabilities import IGroupCapability
        self.assertTrue(IGroupCapability.implementedBy(PloneLDAPMultiPlugin))
        # If that is true, then the following should be true too.
        self.assertTrue(hasattr(PloneLDAPMultiPlugin, 'allowGroupAdd'))
        self.assertTrue(hasattr(PloneLDAPMultiPlugin, 'allowGroupRemove'))


def test_suite():
    from unittest import TestSuite, makeSuite
    suite=TestSuite()
    suite.addTest(makeSuite(TestInterfaces))
    return suite
