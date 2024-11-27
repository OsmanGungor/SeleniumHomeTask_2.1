from collections import namedtuple

TIMEOUT = 10000
CUSTOMER = namedtuple('Customer', ['name', 'lastname', 'postalcode'])
TEST_CUSTOMER = CUSTOMER('Osman', 'Gungor', '38010')
