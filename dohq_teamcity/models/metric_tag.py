# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class MetricTag(TeamCityObject):
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
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, name=None, value=None, teamcity=None):  # noqa: E501
        """MetricTag - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        super(MetricTag, self).__init__(teamcity=teamcity)

    @property
    def name(self):
        """Gets the name of this MetricTag.  # noqa: E501


        :return: The name of this MetricTag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetricTag.


        :param name: The name of this MetricTag.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this MetricTag.  # noqa: E501


        :return: The value of this MetricTag.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MetricTag.


        :param value: The value of this MetricTag.  # noqa: E501
        :type: str
        """

        self._value = value
