# coding: utf-8

"""
    Comotion Dash API

    Comotion Dash API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from comodash_api_client_lowlevel.models.query_result_result_set_rows_inner_data_inner import QueryResultResultSetRowsInnerDataInner

class TestQueryResultResultSetRowsInnerDataInner(unittest.TestCase):
    """QueryResultResultSetRowsInnerDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueryResultResultSetRowsInnerDataInner:
        """Test QueryResultResultSetRowsInnerDataInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueryResultResultSetRowsInnerDataInner`
        """
        model = QueryResultResultSetRowsInnerDataInner()
        if include_optional:
            return QueryResultResultSetRowsInnerDataInner(
                var_char_value = ''
            )
        else:
            return QueryResultResultSetRowsInnerDataInner(
        )
        """

    def testQueryResultResultSetRowsInnerDataInner(self):
        """Test QueryResultResultSetRowsInnerDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()