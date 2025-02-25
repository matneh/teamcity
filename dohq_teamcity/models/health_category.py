# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class HealthCategory(TeamCityObject):
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
        'description': 'str',
        'help_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'help_url': 'helpUrl'
    }

    def __init__(self, id=None, name=None, description=None, help_url=None, teamcity=None):  # noqa: E501
        """HealthCategory - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._description = None
        self._help_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if help_url is not None:
            self.help_url = help_url
        super(HealthCategory, self).__init__(teamcity=teamcity)

    @property
    def id(self):
        """Gets the id of this HealthCategory.  # noqa: E501


        :return: The id of this HealthCategory.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HealthCategory.


        :param id: The id of this HealthCategory.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this HealthCategory.  # noqa: E501


        :return: The name of this HealthCategory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HealthCategory.


        :param name: The name of this HealthCategory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this HealthCategory.  # noqa: E501


        :return: The description of this HealthCategory.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HealthCategory.


        :param description: The description of this HealthCategory.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def help_url(self):
        """Gets the help_url of this HealthCategory.  # noqa: E501


        :return: The help_url of this HealthCategory.  # noqa: E501
        :rtype: str
        """
        return self._help_url

    @help_url.setter
    def help_url(self, help_url):
        """Sets the help_url of this HealthCategory.


        :param help_url: The help_url of this HealthCategory.  # noqa: E501
        :type: str
        """

        self._help_url = help_url
