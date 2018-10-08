# coding: utf-8

from teamcity.custom.model import TeamcityObject


# from teamcity.models.revision import Revision  # noqa: F401,E501


class Revisions(TeamcityObject):
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
        'revision': 'list[Revision]'
    }

    attribute_map = {
        'count': 'count',
        'revision': 'revision'
    }

    def __init__(self, count=None, revision=None):  # noqa: E501
        """Revisions - a model defined in Swagger"""  # noqa: E501
        super(Revisions, self).__init__()

        self._count = None
        self._revision = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if revision is not None:
            self.revision = revision

    @property
    def count(self):
        """Gets the count of this Revisions.  # noqa: E501


        :return: The count of this Revisions.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Revisions.


        :param count: The count of this Revisions.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def revision(self):
        """Gets the revision of this Revisions.  # noqa: E501


        :return: The revision of this Revisions.  # noqa: E501
        :rtype: list[Revision]
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this Revisions.


        :param revision: The revision of this Revisions.  # noqa: E501
        :type: list[Revision]
        """

        self._revision = revision

