# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.audit_action import AuditAction  # noqa: F401,E501
# from dohq_teamcity.models.related_entities import RelatedEntities  # noqa: F401,E501
# from dohq_teamcity.models.user import User  # noqa: F401,E501


class AuditEvent(TeamCityObject):
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
        'timestamp': 'str',
        'comment': 'str',
        'action': 'AuditAction',
        'related_entities': 'RelatedEntities',
        'user': 'User'
    }

    attribute_map = {
        'id': 'id',
        'timestamp': 'timestamp',
        'comment': 'comment',
        'action': 'action',
        'related_entities': 'relatedEntities',
        'user': 'user'
    }

    def __init__(self, id=None, timestamp=None, comment=None, action=None, related_entities=None, user=None, teamcity=None):  # noqa: E501
        """AuditEvent - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._timestamp = None
        self._comment = None
        self._action = None
        self._related_entities = None
        self._user = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if timestamp is not None:
            self.timestamp = timestamp
        if comment is not None:
            self.comment = comment
        if action is not None:
            self.action = action
        if related_entities is not None:
            self.related_entities = related_entities
        if user is not None:
            self.user = user
        super(AuditEvent, self).__init__(teamcity=teamcity)

    @property
    def id(self):
        """Gets the id of this AuditEvent.  # noqa: E501


        :return: The id of this AuditEvent.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuditEvent.


        :param id: The id of this AuditEvent.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def timestamp(self):
        """Gets the timestamp of this AuditEvent.  # noqa: E501


        :return: The timestamp of this AuditEvent.  # noqa: E501
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this AuditEvent.


        :param timestamp: The timestamp of this AuditEvent.  # noqa: E501
        :type: str
        """

        self._timestamp = timestamp

    @property
    def comment(self):
        """Gets the comment of this AuditEvent.  # noqa: E501


        :return: The comment of this AuditEvent.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AuditEvent.


        :param comment: The comment of this AuditEvent.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def action(self):
        """Gets the action of this AuditEvent.  # noqa: E501


        :return: The action of this AuditEvent.  # noqa: E501
        :rtype: AuditAction
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AuditEvent.


        :param action: The action of this AuditEvent.  # noqa: E501
        :type: AuditAction
        """

        self._action = action

    @property
    def related_entities(self):
        """Gets the related_entities of this AuditEvent.  # noqa: E501


        :return: The related_entities of this AuditEvent.  # noqa: E501
        :rtype: RelatedEntities
        """
        return self._related_entities

    @related_entities.setter
    def related_entities(self, related_entities):
        """Sets the related_entities of this AuditEvent.


        :param related_entities: The related_entities of this AuditEvent.  # noqa: E501
        :type: RelatedEntities
        """

        self._related_entities = related_entities

    @property
    def user(self):
        """Gets the user of this AuditEvent.  # noqa: E501


        :return: The user of this AuditEvent.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AuditEvent.


        :param user: The user of this AuditEvent.  # noqa: E501
        :type: User
        """

        self._user = user
