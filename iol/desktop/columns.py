from five import grok
from AccessControl import ClassSecurityInfo
from plone.dexterity.content import DexterityContent
from plone import api
from interfaces import IColumn


class dt_column(DexterityContent):
    grok.implements(IColumn)
    security = ClassSecurityInfo()
    def __init__(self):
        DexterityContent.__init__(self)
        trg = self.getParentNode()

        api.content.move(
            source=self,
            target=trg['columns'],
            safe_id=True)

    def __iter__(self):
        for attr, value in self.__dict__.iteritems():
            yield attr, value
