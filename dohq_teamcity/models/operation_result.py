# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.related_entity import RelatedEntity  # noqa: F401,E501


class OperationResult(TeamCityObject):
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
        'message': 'str',
        'related': 'RelatedEntity'
    }

    attribute_map = {
        'message': 'message',
        'related': 'related'
    }

    def __init__(self, message=None, related=None, teamcity=None):  # noqa: E501
        """OperationResult - a model defined in Swagger"""  # noqa: E501

        self._message = None
        self._related = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if related is not None:
            self.related = related
        super(OperationResult, self).__init__(teamcity=teamcity)

    @property
    def message(self):
        """Gets the message of this OperationResult.  # noqa: E501


        :return: The message of this OperationResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this OperationResult.


        :param message: The message of this OperationResult.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def related(self):
        """Gets the related of this OperationResult.  # noqa: E501


        :return: The related of this OperationResult.  # noqa: E501
        :rtype: RelatedEntity
        """
        return self._related

    @related.setter
    def related(self, related):
        """Sets the related of this OperationResult.


        :param related: The related of this OperationResult.  # noqa: E501
        :type: RelatedEntity
        """

        self._related = related
