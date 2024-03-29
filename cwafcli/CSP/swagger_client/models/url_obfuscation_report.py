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

class UrlObfuscationReport(object):
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
        'uri': 'str',
        'codehash': 'str',
        'script': 'str',
        'obfuscated': 'bool',
        'failed': 'bool'
    }

    attribute_map = {
        'uri': 'uri',
        'codehash': 'codehash',
        'script': 'script',
        'obfuscated': 'obfuscated',
        'failed': 'failed'
    }

    def __init__(self, uri=None, codehash=None, script=None, obfuscated=None, failed=None):  # noqa: E501
        """UrlObfuscationReport - a model defined in Swagger"""  # noqa: E501
        self._uri = None
        self._codehash = None
        self._script = None
        self._obfuscated = None
        self._failed = None
        self.discriminator = None
        if uri is not None:
            self.uri = uri
        if codehash is not None:
            self.codehash = codehash
        if script is not None:
            self.script = script
        if obfuscated is not None:
            self.obfuscated = obfuscated
        if failed is not None:
            self.failed = failed

    @property
    def uri(self):
        """Gets the uri of this UrlObfuscationReport.  # noqa: E501


        :return: The uri of this UrlObfuscationReport.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this UrlObfuscationReport.


        :param uri: The uri of this UrlObfuscationReport.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def codehash(self):
        """Gets the codehash of this UrlObfuscationReport.  # noqa: E501


        :return: The codehash of this UrlObfuscationReport.  # noqa: E501
        :rtype: str
        """
        return self._codehash

    @codehash.setter
    def codehash(self, codehash):
        """Sets the codehash of this UrlObfuscationReport.


        :param codehash: The codehash of this UrlObfuscationReport.  # noqa: E501
        :type: str
        """

        self._codehash = codehash

    @property
    def script(self):
        """Gets the script of this UrlObfuscationReport.  # noqa: E501


        :return: The script of this UrlObfuscationReport.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this UrlObfuscationReport.


        :param script: The script of this UrlObfuscationReport.  # noqa: E501
        :type: str
        """

        self._script = script

    @property
    def obfuscated(self):
        """Gets the obfuscated of this UrlObfuscationReport.  # noqa: E501


        :return: The obfuscated of this UrlObfuscationReport.  # noqa: E501
        :rtype: bool
        """
        return self._obfuscated

    @obfuscated.setter
    def obfuscated(self, obfuscated):
        """Sets the obfuscated of this UrlObfuscationReport.


        :param obfuscated: The obfuscated of this UrlObfuscationReport.  # noqa: E501
        :type: bool
        """

        self._obfuscated = obfuscated

    @property
    def failed(self):
        """Gets the failed of this UrlObfuscationReport.  # noqa: E501


        :return: The failed of this UrlObfuscationReport.  # noqa: E501
        :rtype: bool
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this UrlObfuscationReport.


        :param failed: The failed of this UrlObfuscationReport.  # noqa: E501
        :type: bool
        """

        self._failed = failed

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
        if issubclass(UrlObfuscationReport, dict):
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
        if not isinstance(other, UrlObfuscationReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
