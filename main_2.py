from table_builders.table_builder import TableBuilder

a = TableBuilder('Example')
a.speak()

from table_builders.model_elements.customers.CustomersBuilder import CustomersBuilder
b = CustomersBuilder()
b.speak()
