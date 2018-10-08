# coding: utf-8

from teamcity.custom.model import TeamcityObject


# from teamcity.models.user import User  # noqa: F401,E501


class Tag(TeamcityObject):
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
        'owner': 'User',
        'private': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'owner': 'owner',
        'private': 'private'
    }

    def __init__(self, name=None, owner=None, private=False):  # noqa: E501
        """Tag - a model defined in Swagger"""  # noqa: E501
        super(Tag, self).__init__()

        self._name = None
        self._owner = None
        self._private = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if private is not None:
            self.private = private

    @property
    def name(self):
        """Gets the name of this Tag.  # noqa: E501


        :return: The name of this Tag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Tag.


        :param name: The name of this Tag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this Tag.  # noqa: E501


        :return: The owner of this Tag.  # noqa: E501
        :rtype: User
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this Tag.


        :param owner: The owner of this Tag.  # noqa: E501
        :type: User
        """

        self._owner = owner

    @property
    def private(self):
        """Gets the private of this Tag.  # noqa: E501


        :return: The private of this Tag.  # noqa: E501
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this Tag.


        :param private: The private of this Tag.  # noqa: E501
        :type: bool
        """

        self._private = private

