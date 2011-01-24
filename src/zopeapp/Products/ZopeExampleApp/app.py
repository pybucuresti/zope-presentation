from OFS.SimpleItem import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile

#Add an object
def manage_add(container, REQUEST=None):
    """ Add a sample app """

    if REQUEST is not None and REQUEST.method == 'GET':
        return PageTemplateFile('zpt/manage_add.zpt', globals()).__of__(container)()

    id = REQUEST.form.get("id", None)
    ob = ExampleApp(id=id)
    container._setObject(id, ob)

    if REQUEST is not None:
        return REQUEST.RESPONSE.redirect(container.absolute_url() +
                                         '/manage_main?update_menu=1')

#Model/Views
class ExampleApp(SimpleItem):
    meta_type = "Example app"

    def __init__(self, id):
        self.id = id

    def index(REQUEST=None):
        """ """
        raise NotImplementedError
