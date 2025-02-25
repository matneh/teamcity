# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.model_property import ModelProperty  # noqa: F401,E501


class Properties(TeamCityObject):
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
        'href': 'str',
        'count': 'int',
        '_property': 'list[ModelProperty]'
    }

    attribute_map = {
        'href': 'href',
        'count': 'count',
        '_property': 'property'
    }

    def __init__(self, href=None, count=None, _property=None, teamcity=None):  # noqa: E501
        """Properties - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._count = None
        self.__property = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if count is not None:
            self.count = count
        if _property is not None:
            self._property = _property
        super(Properties, self).__init__(teamcity=teamcity)

    @property
    def href(self):
        """Gets the href of this Properties.  # noqa: E501


        :return: The href of this Properties.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Properties.


        :param href: The href of this Properties.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def count(self):
        """Gets the count of this Properties.  # noqa: E501


        :return: The count of this Properties.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Properties.


        :param count: The count of this Properties.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def _property(self):
        """Gets the _property of this Properties.  # noqa: E501


        :return: The _property of this Properties.  # noqa: E501
        :rtype: list[ModelProperty]
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this Properties.


        :param _property: The _property of this Properties.  # noqa: E501
        :type: list[ModelProperty]
        """

        self.__property = _property
