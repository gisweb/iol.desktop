from zope.schema.vocabulary import SimpleVocabulary
from Products.CMFCore.utils import getToolByName

def listGroups():
    acl_users = getToolByName(self, 'acl_users')
    group_list = acl_users.source_groups.getGroups()
    return SimpleVocabulary.fromItems([(group.title, group.getName()) for group in group_list])

map_position = SimpleVocabulary.fromItems([( 'No Map','nomap',), ( 'Position Top','top',),('Position Bottom','bottom',)])

field_type = SimpleVocabulary.fromItems([( 'Text', 'search_text',), ('Number', 'search_number', ),('Date','search_date',),('Check','search_check',),('List (Dynamic Search)','search_list',),])

users_groups_list = listGroups()