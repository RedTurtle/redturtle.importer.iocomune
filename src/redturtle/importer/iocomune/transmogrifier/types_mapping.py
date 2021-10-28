# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import IPloneSiteRoot
from redturtle.importer.base.interfaces import IPortalTypeMapping
from zope.component import adapter
from zope.interface import implementer
from zope.publisher.interfaces.browser import IBrowserRequest

import logging

logger = logging.getLogger(__name__)


@adapter(IPloneSiteRoot, IBrowserRequest)
@implementer(IPortalTypeMapping)
class IoComuneMapping(object):
    order = 101

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self, item, typekey):
        """ """

        portal_type = item[typekey]
        if portal_type == "News Item":
            item["descrizione_estesa"] = item["text"]
            del item["text"]
        elif portal_type == "Event":
            item["descrizione_estesa"] = item["text"]
            del item["text"]

        return item
