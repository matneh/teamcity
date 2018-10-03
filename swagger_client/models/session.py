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

# from swagger_client.models.user import User  # noqa: F401,E501


class Session(object):
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
        'creation_date': 'str',
        'id': 'str',
        'last_accessed_date': 'str',
        'user': 'User'
    }

    attribute_map = {
        'creation_date': 'creationDate',
        'id': 'id',
        'last_accessed_date': 'lastAccessedDate',
        'user': 'user'
    }

    def __init__(self, creation_date=None, id=None, last_accessed_date=None, user=None):  # noqa: E501
        """Session - a model defined in Swagger"""  # noqa: E501

        self._creation_date = None
        self._id = None
        self._last_accessed_date = None
        self._user = None
        self.discriminator = None

        if creation_date is not None:
            self.creation_date = creation_date
        if id is not None:
            self.id = id
        if last_accessed_date is not None:
            self.last_accessed_date = last_accessed_date
        if user is not None:
            self.user = user

    @property
    def creation_date(self):
        """Gets the creation_date of this Session.  # noqa: E501


        :return: The creation_date of this Session.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this Session.


        :param creation_date: The creation_date of this Session.  # noqa: E501
        :type: str
        """

        self._creation_date = creation_date

    @property
    def id(self):
        """Gets the id of this Session.  # noqa: E501


        :return: The id of this Session.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Session.


        :param id: The id of this Session.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_accessed_date(self):
        """Gets the last_accessed_date of this Session.  # noqa: E501


        :return: The last_accessed_date of this Session.  # noqa: E501
        :rtype: str
        """
        return self._last_accessed_date

    @last_accessed_date.setter
    def last_accessed_date(self, last_accessed_date):
        """Sets the last_accessed_date of this Session.


        :param last_accessed_date: The last_accessed_date of this Session.  # noqa: E501
        :type: str
        """

        self._last_accessed_date = last_accessed_date

    @property
    def user(self):
        """Gets the user of this Session.  # noqa: E501


        :return: The user of this Session.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Session.


        :param user: The user of this Session.  # noqa: E501
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
        if issubclass(Session, dict):
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
        if not isinstance(other, Session):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
