# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class BuildCancelRequest(TeamCityObject):
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
        'comment': 'str',
        'readd_into_queue': 'bool'
    }

    attribute_map = {
        'comment': 'comment',
        'readd_into_queue': 'readdIntoQueue'
    }

    def __init__(self, comment=None, readd_into_queue=None, teamcity=None):  # noqa: E501
        """BuildCancelRequest - a model defined in Swagger"""  # noqa: E501

        self._comment = None
        self._readd_into_queue = None
        self.discriminator = None

        if comment is not None:
            self.comment = comment
        if readd_into_queue is not None:
            self.readd_into_queue = readd_into_queue
        super(BuildCancelRequest, self).__init__(teamcity=teamcity)

    @property
    def comment(self):
        """Gets the comment of this BuildCancelRequest.  # noqa: E501


        :return: The comment of this BuildCancelRequest.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this BuildCancelRequest.


        :param comment: The comment of this BuildCancelRequest.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def readd_into_queue(self):
        """Gets the readd_into_queue of this BuildCancelRequest.  # noqa: E501


        :return: The readd_into_queue of this BuildCancelRequest.  # noqa: E501
        :rtype: bool
        """
        return self._readd_into_queue

    @readd_into_queue.setter
    def readd_into_queue(self, readd_into_queue):
        """Sets the readd_into_queue of this BuildCancelRequest.


        :param readd_into_queue: The readd_into_queue of this BuildCancelRequest.  # noqa: E501
        :type: bool
        """

        self._readd_into_queue = readd_into_queue
