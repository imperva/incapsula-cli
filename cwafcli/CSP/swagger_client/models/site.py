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

class Site(object):
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
        'name': 'str',
        'mode': 'Mode',
        'discovery': 'Discovery',
        'settings': 'SiteSettings',
        'tracking_ids': 'list[Analytics]',
        'instant_block_enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'mode': 'mode',
        'discovery': 'discovery',
        'settings': 'settings',
        'tracking_ids': 'tracking-ids',
        'instant_block_enabled': 'instantBlockEnabled'
    }

    def __init__(self, name=None, mode=None, discovery=None, settings=None, tracking_ids=None, instant_block_enabled=None):  # noqa: E501
        """Site - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._mode = None
        self._discovery = None
        self._settings = None
        self._tracking_ids = None
        self._instant_block_enabled = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if mode is not None:
            self.mode = mode
        if discovery is not None:
            self.discovery = discovery
        if settings is not None:
            self.settings = settings
        if tracking_ids is not None:
            self.tracking_ids = tracking_ids
        if instant_block_enabled is not None:
            self.instant_block_enabled = instant_block_enabled

    @property
    def name(self):
        """Gets the name of this Site.  # noqa: E501


        :return: The name of this Site.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Site.


        :param name: The name of this Site.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def mode(self):
        """Gets the mode of this Site.  # noqa: E501


        :return: The mode of this Site.  # noqa: E501
        :rtype: Mode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Site.


        :param mode: The mode of this Site.  # noqa: E501
        :type: Mode
        """

        self._mode = mode

    @property
    def discovery(self):
        """Gets the discovery of this Site.  # noqa: E501


        :return: The discovery of this Site.  # noqa: E501
        :rtype: Discovery
        """
        return self._discovery

    @discovery.setter
    def discovery(self, discovery):
        """Sets the discovery of this Site.


        :param discovery: The discovery of this Site.  # noqa: E501
        :type: Discovery
        """

        self._discovery = discovery

    @property
    def settings(self):
        """Gets the settings of this Site.  # noqa: E501


        :return: The settings of this Site.  # noqa: E501
        :rtype: SiteSettings
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Site.


        :param settings: The settings of this Site.  # noqa: E501
        :type: SiteSettings
        """

        self._settings = settings

    @property
    def tracking_ids(self):
        """Gets the tracking_ids of this Site.  # noqa: E501


        :return: The tracking_ids of this Site.  # noqa: E501
        :rtype: list[Analytics]
        """
        return self._tracking_ids

    @tracking_ids.setter
    def tracking_ids(self, tracking_ids):
        """Sets the tracking_ids of this Site.


        :param tracking_ids: The tracking_ids of this Site.  # noqa: E501
        :type: list[Analytics]
        """

        self._tracking_ids = tracking_ids

    @property
    def instant_block_enabled(self):
        """Gets the instant_block_enabled of this Site.  # noqa: E501

        Indicates whether or not Instant Block is enabled for this website.  # noqa: E501

        :return: The instant_block_enabled of this Site.  # noqa: E501
        :rtype: bool
        """
        return self._instant_block_enabled

    @instant_block_enabled.setter
    def instant_block_enabled(self, instant_block_enabled):
        """Sets the instant_block_enabled of this Site.

        Indicates whether or not Instant Block is enabled for this website.  # noqa: E501

        :param instant_block_enabled: The instant_block_enabled of this Site.  # noqa: E501
        :type: bool
        """

        self._instant_block_enabled = instant_block_enabled

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
        if issubclass(Site, dict):
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
        if not isinstance(other, Site):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
