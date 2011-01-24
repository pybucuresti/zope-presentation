import app

def initialize(context):
    """ """
    context.registerClass(
        app.ExampleApp,
        constructors = (
            app.manage_add, 
        ),
        icon='www/icon.png'
    )
