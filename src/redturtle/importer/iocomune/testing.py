# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import redturtle.importer.iocomune


class RedturtleImporterIocomuneLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=redturtle.importer.iocomune)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'redturtle.importer.iocomune:default')


REDTURTLE_IMPORTER_IOCOMUNE_FIXTURE = RedturtleImporterIocomuneLayer()


REDTURTLE_IMPORTER_IOCOMUNE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(REDTURTLE_IMPORTER_IOCOMUNE_FIXTURE,),
    name='RedturtleImporterIocomuneLayer:IntegrationTesting',
)


REDTURTLE_IMPORTER_IOCOMUNE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(REDTURTLE_IMPORTER_IOCOMUNE_FIXTURE,),
    name='RedturtleImporterIocomuneLayer:FunctionalTesting',
)


REDTURTLE_IMPORTER_IOCOMUNE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        REDTURTLE_IMPORTER_IOCOMUNE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='RedturtleImporterIocomuneLayer:AcceptanceTesting',
)
