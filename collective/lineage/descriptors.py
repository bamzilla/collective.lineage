from zope import interface
from p4a.subtyper import interfaces as stifaces
from collective.lineage import interfaces

class ChildSiteDescriptor(object):
    """A descriptor for the Child Site subtype.
    """
    
    interface.implements(stifaces.IPortalTypedFolderishDescriptor)
    title = u'Child Site'
    description = u'A child site'
    type_interface = interfaces.IChildSite
    # TODO use allowed_child_portal_types?
    for_portal_type = 'Folder'
