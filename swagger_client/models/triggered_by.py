# coding: utf-8

"""
    TeamCity REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

# from swagger_client.models.build_type import BuildType  # noqa: F401,E501
# from swagger_client.models.properties import Properties  # noqa: F401,E501
# from swagger_client.models.user import User  # noqa: F401,E501


class TriggeredBy(object):
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
        'build_type': 'BuildType',
        '_date': 'str',
        'details': 'str',
        'properties': 'Properties',
        'raw_value': 'str',
        'type': 'str',
        'user': 'User'
    }

    attribute_map = {
        'build_type': 'buildType',
        '_date': 'date',
        'details': 'details',
        'properties': 'properties',
        'raw_value': 'rawValue',
        'type': 'type',
        'user': 'user'
    }

    def __init__(self, build_type=None, _date=None, details=None, properties=None, raw_value=None, type=None, user=None):  # noqa: E501
        """TriggeredBy - a model defined in Swagger"""  # noqa: E501

        self._build_type = None
        self.__date = None
        self._details = None
        self._properties = None
        self._raw_value = None
        self._type = None
        self._user = None
        self.discriminator = None

        if build_type is not None:
            self.build_type = build_type
        if _date is not None:
            self._date = _date
        if details is not None:
            self.details = details
        if properties is not None:
            self.properties = properties
        if raw_value is not None:
            self.raw_value = raw_value
        if type is not None:
            self.type = type
        if user is not None:
            self.user = user

    @property
    def build_type(self):
        """Gets the build_type of this TriggeredBy.  # noqa: E501


        :return: The build_type of this TriggeredBy.  # noqa: E501
        :rtype: BuildType
        """
        return self._build_type

    @build_type.setter
    def build_type(self, build_type):
        """Sets the build_type of this TriggeredBy.


        :param build_type: The build_type of this TriggeredBy.  # noqa: E501
        :type: BuildType
        """

        self._build_type = build_type

    @property
    def _date(self):
        """Gets the _date of this TriggeredBy.  # noqa: E501


        :return: The _date of this TriggeredBy.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this TriggeredBy.


        :param _date: The _date of this TriggeredBy.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def details(self):
        """Gets the details of this TriggeredBy.  # noqa: E501


        :return: The details of this TriggeredBy.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this TriggeredBy.


        :param details: The details of this TriggeredBy.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def properties(self):
        """Gets the properties of this TriggeredBy.  # noqa: E501


        :return: The properties of this TriggeredBy.  # noqa: E501
        :rtype: Properties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TriggeredBy.


        :param properties: The properties of this TriggeredBy.  # noqa: E501
        :type: Properties
        """

        self._properties = properties

    @property
    def raw_value(self):
        """Gets the raw_value of this TriggeredBy.  # noqa: E501


        :return: The raw_value of this TriggeredBy.  # noqa: E501
        :rtype: str
        """
        return self._raw_value

    @raw_value.setter
    def raw_value(self, raw_value):
        """Sets the raw_value of this TriggeredBy.


        :param raw_value: The raw_value of this TriggeredBy.  # noqa: E501
        :type: str
        """

        self._raw_value = raw_value

    @property
    def type(self):
        """Gets the type of this TriggeredBy.  # noqa: E501


        :return: The type of this TriggeredBy.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TriggeredBy.


        :param type: The type of this TriggeredBy.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def user(self):
        """Gets the user of this TriggeredBy.  # noqa: E501


        :return: The user of this TriggeredBy.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this TriggeredBy.


        :param user: The user of this TriggeredBy.  # noqa: E501
        :type: User
        """

        self._user = user

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
        if issubclass(TriggeredBy, dict):
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
        if not isinstance(other, TriggeredBy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
