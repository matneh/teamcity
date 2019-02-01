# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class Permission(TeamCityObject):
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
        'id': 'str',
        'name': 'str',
        '_global': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        '_global': 'global'
    }

    def __init__(self, id=None, name=None, _global=False, teamcity=None):  # noqa: E501
        """Permission - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self.__global = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if _global is not None:
            self._global = _global
        super(Permission, self).__init__(teamcity=teamcity)

    @property
    def id(self):
        """Gets the id of this Permission.  # noqa: E501


        :return: The id of this Permission.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Permission.


        :param id: The id of this Permission.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Permission.  # noqa: E501


        :return: The name of this Permission.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Permission.


        :param name: The name of this Permission.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def _global(self):
        """Gets the _global of this Permission.  # noqa: E501


        :return: The _global of this Permission.  # noqa: E501
        :rtype: bool
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this Permission.


        :param _global: The _global of this Permission.  # noqa: E501
        :type: bool
        """

        self.__global = _global