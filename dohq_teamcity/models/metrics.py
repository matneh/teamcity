# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.metric import Metric  # noqa: F401,E501


class Metrics(TeamCityObject):
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
        'metric': 'list[Metric]'
    }

    attribute_map = {
        'count': 'count',
        'metric': 'metric'
    }

    def __init__(self, count=None, metric=None, teamcity=None):  # noqa: E501
        """Metrics - a model defined in Swagger"""  # noqa: E501

        self._count = None
        self._metric = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if metric is not None:
            self.metric = metric
        super(Metrics, self).__init__(teamcity=teamcity)

    @property
    def count(self):
        """Gets the count of this Metrics.  # noqa: E501


        :return: The count of this Metrics.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Metrics.


        :param count: The count of this Metrics.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def metric(self):
        """Gets the metric of this Metrics.  # noqa: E501


        :return: The metric of this Metrics.  # noqa: E501
        :rtype: list[Metric]
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this Metrics.


        :param metric: The metric of this Metrics.  # noqa: E501
        :type: list[Metric]
        """

        self._metric = metric
