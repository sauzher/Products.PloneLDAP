try:
    from Products.CMFPlone.setuphandlers import HiddenProducts
except ImportError:
    pass
else:
    def getNonInstallableProducts(self):
        return HiddenProducts._getNonInstallableProducts(self) + \
                [ "LDAPUserFolder" ]

    HiddenProducts._getNonInstallableProducts=HiddenProducts.getNonInstallableProducts
    HiddenProducts.getNonInstallableProducts=getNonInstallableProducts


