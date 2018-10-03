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

# from swagger_client.models.groups import Groups  # noqa: F401,E501
# from swagger_client.models.properties import Properties  # noqa: F401,E501
# from swagger_client.models.roles import Roles  # noqa: F401,E501


class User(object):
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
        'email': 'str',
        'groups': 'Groups',
        'has_password': 'bool',
        'href': 'str',
        'id': 'int',
        'last_login': 'str',
        'locator': 'str',
        'name': 'str',
        'password': 'str',
        'properties': 'Properties',
        'realm': 'str',
        'roles': 'Roles',
        'username': 'str'
    }

    attribute_map = {
        'email': 'email',
        'groups': 'groups',
        'has_password': 'hasPassword',
        'href': 'href',
        'id': 'id',
        'last_login': 'lastLogin',
        'locator': 'locator',
        'name': 'name',
        'password': 'password',
        'properties': 'properties',
        'realm': 'realm',
        'roles': 'roles',
        'username': 'username'
    }

    def __init__(self, email=None, groups=None, has_password=False, href=None, id=None, last_login=None, locator=None, name=None, password=None, properties=None, realm=None, roles=None, username=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._groups = None
        self._has_password = None
        self._href = None
        self._id = None
        self._last_login = None
        self._locator = None
        self._name = None
        self._password = None
        self._properties = None
        self._realm = None
        self._roles = None
        self._username = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if groups is not None:
            self.groups = groups
        if has_password is not None:
            self.has_password = has_password
        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if last_login is not None:
            self.last_login = last_login
        if locator is not None:
            self.locator = locator
        if name is not None:
            self.name = name
        if password is not None:
            self.password = password
        if properties is not None:
            self.properties = properties
        if realm is not None:
            self.realm = realm
        if roles is not None:
            self.roles = roles
        if username is not None:
            self.username = username

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501


        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.


        :param email: The email of this User.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def groups(self):
        """Gets the groups of this User.  # noqa: E501


        :return: The groups of this User.  # noqa: E501
        :rtype: Groups
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this User.


        :param groups: The groups of this User.  # noqa: E501
        :type: Groups
        """

        self._groups = groups

    @property
    def has_password(self):
        """Gets the has_password of this User.  # noqa: E501


        :return: The has_password of this User.  # noqa: E501
        :rtype: bool
        """
        return self._has_password

    @has_password.setter
    def has_password(self, has_password):
        """Sets the has_password of this User.


        :param has_password: The has_password of this User.  # noqa: E501
        :type: bool
        """

        self._has_password = has_password

    @property
    def href(self):
        """Gets the href of this User.  # noqa: E501


        :return: The href of this User.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this User.


        :param href: The href of this User.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def last_login(self):
        """Gets the last_login of this User.  # noqa: E501


        :return: The last_login of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """Sets the last_login of this User.


        :param last_login: The last_login of this User.  # noqa: E501
        :type: str
        """

        self._last_login = last_login

    @property
    def locator(self):
        """Gets the locator of this User.  # noqa: E501


        :return: The locator of this User.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this User.


        :param locator: The locator of this User.  # noqa: E501
        :type: str
        """

        self._locator = locator

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501


        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.


        :param name: The name of this User.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def password(self):
        """Gets the password of this User.  # noqa: E501


        :return: The password of this User.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this User.


        :param password: The password of this User.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def properties(self):
        """Gets the properties of this User.  # noqa: E501


        :return: The properties of this User.  # noqa: E501
        :rtype: Properties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this User.


        :param properties: The properties of this User.  # noqa: E501
        :type: Properties
        """

        self._properties = properties

    @property
    def realm(self):
        """Gets the realm of this User.  # noqa: E501


        :return: The realm of this User.  # noqa: E501
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this User.


        :param realm: The realm of this User.  # noqa: E501
        :type: str
        """

        self._realm = realm

    @property
    def roles(self):
        """Gets the roles of this User.  # noqa: E501


        :return: The roles of this User.  # noqa: E501
        :rtype: Roles
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this User.


        :param roles: The roles of this User.  # noqa: E501
        :type: Roles
        """

        self._roles = roles

    @property
    def username(self):
        """Gets the username of this User.  # noqa: E501


        :return: The username of this User.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this User.


        :param username: The username of this User.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
