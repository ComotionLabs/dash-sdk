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

from comodash_api_client_lowlevel.models.file_upload_request import FileUploadRequest

class TestFileUploadRequest(unittest.TestCase):
    """FileUploadRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileUploadRequest:
        """Test FileUploadRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileUploadRequest`
        """
        model = FileUploadRequest()
        if include_optional:
            return FileUploadRequest(
                file_key = 'q2c3v8s7djuy2zmetozkhdomha2bae48b9ocvx9o64ow3eg8p7qw_qklp7l5y121fogx.parquet'
            )
        else:
            return FileUploadRequest(
        )
        """

    def testFileUploadRequest(self):
        """Test FileUploadRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
