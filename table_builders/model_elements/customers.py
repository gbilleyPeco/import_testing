from ..table_builder import TableBuilder

class CustomersBuilderSOIP(TableBuilder):
    def __init__(self):
        TableBuilder.__init__(self, 'Customers')

    def build(self, staging_db_data, pfm_tables, user_inputs):
        self.speak()