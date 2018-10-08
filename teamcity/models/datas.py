# coding: utf-8

from teamcity.custom.model import TeamcityObject


# from teamcity.models.meta_data import MetaData  # noqa: F401,E501


class Datas(TeamcityObject):
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
        'count': 'int',
        'data': 'list[MetaData]'
    }

    attribute_map = {
        'count': 'count',
        'data': 'data'
    }

    def __init__(self, count=None, data=None):  # noqa: E501
        """Datas - a model defined in Swagger"""  # noqa: E501
        super(Datas, self).__init__()

        self._count = None
        self._data = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if data is not None:
            self.data = data

    @property
    def count(self):
        """Gets the count of this Datas.  # noqa: E501


        :return: The count of this Datas.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Datas.


        :param count: The count of this Datas.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def data(self):
        """Gets the data of this Datas.  # noqa: E501


        :return: The data of this Datas.  # noqa: E501
        :rtype: list[MetaData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Datas.


        :param data: The data of this Datas.  # noqa: E501
        :type: list[MetaData]
        """

        self._data = data

