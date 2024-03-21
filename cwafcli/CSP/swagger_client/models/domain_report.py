# coding: utf-8

"""
    Imperva Client-Side Protection API

    This is an API for Imperva Client-Side Protection. Gain visibility into the JavaScript services making requests to your application along with their risk factors. Use these APIs to pull data and configure which services should have access to your application. For full feature documentation, see <a style=\"text-decoration:none\" href=\"https://docs.imperva.com/bundle/client-side-protection\">Client-Side Protection</a>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DomainReport(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'document_uri': 'str',
        'source_file': 'str',
        'blocked_uri': 'str',
        'line_number': 'int',
        'source_type': 'str',
        'referrer': 'str',
        'script_sample': 'str',
        'client_application': 'str'
    }

    attribute_map = {
        'document_uri': 'documentUri',
        'source_file': 'sourceFile',
        'blocked_uri': 'blockedUri',
        'line_number': 'lineNumber',
        'source_type': 'sourceType',
        'referrer': 'referrer',
        'script_sample': 'scriptSample',
        'client_application': 'clientApplication'
    }

    def __init__(self, document_uri=None, source_file=None, blocked_uri=None, line_number=None, source_type=None, referrer=None, script_sample=None, client_application=None):  # noqa: E501
        """DomainReport - a model defined in Swagger"""  # noqa: E501
        self._document_uri = None
        self._source_file = None
        self._blocked_uri = None
        self._line_number = None
        self._source_type = None
        self._referrer = None
        self._script_sample = None
        self._client_application = None
        self.discriminator = None
        if document_uri is not None:
            self.document_uri = document_uri
        if source_file is not None:
            self.source_file = source_file
        if blocked_uri is not None:
            self.blocked_uri = blocked_uri
        if line_number is not None:
            self.line_number = line_number
        if source_type is not None:
            self.source_type = source_type
        if referrer is not None:
            self.referrer = referrer
        if script_sample is not None:
            self.script_sample = script_sample
        if client_application is not None:
            self.client_application = client_application

    @property
    def document_uri(self):
        """Gets the document_uri of this DomainReport.  # noqa: E501

        URI of the page requesting the domain dependency.  # noqa: E501

        :return: The document_uri of this DomainReport.  # noqa: E501
        :rtype: str
        """
        return self._document_uri

    @document_uri.setter
    def document_uri(self, document_uri):
        """Sets the document_uri of this DomainReport.

        URI of the page requesting the domain dependency.  # noqa: E501

        :param document_uri: The document_uri of this DomainReport.  # noqa: E501
        :type: str
        """

        self._document_uri = document_uri

    @property
    def source_file(self):
        """Gets the source_file of this DomainReport.  # noqa: E501

        The file requesting the domain dependency.  # noqa: E501

        :return: The source_file of this DomainReport.  # noqa: E501
        :rtype: str
        """
        return self._source_file

    @source_file.setter
    def source_file(self, source_file):
        """Sets the source_file of this DomainReport.

        The file requesting the domain dependency.  # noqa: E501

        :param source_file: The source_file of this DomainReport.  # noqa: E501
        :type: str
        """

        self._source_file = source_file

    @property
    def blocked_uri(self):
        """Gets the blocked_uri of this DomainReport.  # noqa: E501

        The requested external resource URL.  # noqa: E501

        :return: The blocked_uri of this DomainReport.  # noqa: E501
        :rtype: str
        """
        return self._blocked_uri

    @blocked_uri.setter
    def blocked_uri(self, blocked_uri):
        """Sets the blocked_uri of this DomainReport.

        The requested external resource URL.  # noqa: E501

        :param blocked_uri: The blocked_uri of this DomainReport.  # noqa: E501
        :type: str
        """

        self._blocked_uri = blocked_uri

    @property
    def line_number(self):
        """Gets the line_number of this DomainReport.  # noqa: E501

        Line number in the requesting file.  # noqa: E501

        :return: The line_number of this DomainReport.  # noqa: E501
        :rtype: int
        """
        return self._line_number

    @line_number.setter
    def line_number(self, line_number):
        """Sets the line_number of this DomainReport.

        Line number in the requesting file.  # noqa: E501

        :param line_number: The line_number of this DomainReport.  # noqa: E501
        :type: int
        """

        self._line_number = line_number

    @property
    def source_type(self):
        """Gets the source_type of this DomainReport.  # noqa: E501

        The type of content requested, such as script, images, or data transfer.  # noqa: E501

        :return: The source_type of this DomainReport.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this DomainReport.

        The type of content requested, such as script, images, or data transfer.  # noqa: E501

        :param source_type: The source_type of this DomainReport.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALL", "UNKNOWN", "RESOURCE", "FRAME", "IMAGE", "DATA_TRANSFER", "STYLE", "FONT", "SCRIPT", "MANIFEST", "MEDIA", "FORM_ACTION", "FRAME_ANCESTORS"]  # noqa: E501
        if source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

    @property
    def referrer(self):
        """Gets the referrer of this DomainReport.  # noqa: E501

        The address from which your resource has been requested on.  # noqa: E501

        :return: The referrer of this DomainReport.  # noqa: E501
        :rtype: str
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer):
        """Sets the referrer of this DomainReport.

        The address from which your resource has been requested on.  # noqa: E501

        :param referrer: The referrer of this DomainReport.  # noqa: E501
        :type: str
        """

        self._referrer = referrer

    @property
    def script_sample(self):
        """Gets the script_sample of this DomainReport.  # noqa: E501

        The first 40 characters of the requesting inline script.  # noqa: E501

        :return: The script_sample of this DomainReport.  # noqa: E501
        :rtype: str
        """
        return self._script_sample

    @script_sample.setter
    def script_sample(self, script_sample):
        """Sets the script_sample of this DomainReport.

        The first 40 characters of the requesting inline script.  # noqa: E501

        :param script_sample: The script_sample of this DomainReport.  # noqa: E501
        :type: str
        """

        self._script_sample = script_sample

    @property
    def client_application(self):
        """Gets the client_application of this DomainReport.  # noqa: E501

        Client application that sent the content security policy report.  # noqa: E501

        :return: The client_application of this DomainReport.  # noqa: E501
        :rtype: str
        """
        return self._client_application

    @client_application.setter
    def client_application(self, client_application):
        """Sets the client_application of this DomainReport.

        Client application that sent the content security policy report.  # noqa: E501

        :param client_application: The client_application of this DomainReport.  # noqa: E501
        :type: str
        """

        self._client_application = client_application

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DomainReport, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DomainReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other