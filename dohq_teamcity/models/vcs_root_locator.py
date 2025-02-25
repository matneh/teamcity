# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class VcsRootLocator(TeamCityObject):
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
        'affected_project': 'str',
        'count': 'int',
        'id': 'str',
        'internal_id': 'int',
        'item': 'str',
        'lookup_limit': 'int',
        'name': 'str',
        'project': 'str',
        '_property': 'str',
        'start': 'int',
        'type': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'affected_project': 'affectedProject',
        'count': 'count',
        'id': 'id',
        'internal_id': 'internalId',
        'item': 'item',
        'lookup_limit': 'lookupLimit',
        'name': 'name',
        'project': 'project',
        '_property': 'property',
        'start': 'start',
        'type': 'type',
        'uuid': 'uuid'
    }

    def __init__(self, affected_project=None, count=None, id=None, internal_id=None, item=None, lookup_limit=None, name=None, project=None, _property=None, start=None, type=None, uuid=None, teamcity=None):  # noqa: E501
        """VcsRootLocator - a model defined in Swagger"""  # noqa: E501

        self._affected_project = None
        self._count = None
        self._id = None
        self._internal_id = None
        self._item = None
        self._lookup_limit = None
        self._name = None
        self._project = None
        self.__property = None
        self._start = None
        self._type = None
        self._uuid = None
        self.discriminator = None

        if affected_project is not None:
            self.affected_project = affected_project
        if count is not None:
            self.count = count
        if id is not None:
            self.id = id
        if internal_id is not None:
            self.internal_id = internal_id
        if item is not None:
            self.item = item
        if lookup_limit is not None:
            self.lookup_limit = lookup_limit
        if name is not None:
            self.name = name
        if project is not None:
            self.project = project
        if _property is not None:
            self._property = _property
        if start is not None:
            self.start = start
        if type is not None:
            self.type = type
        if uuid is not None:
            self.uuid = uuid
        super(VcsRootLocator, self).__init__(teamcity=teamcity)

    @property
    def affected_project(self):
        """Gets the affected_project of this VcsRootLocator.  # noqa: E501

        Project (direct or indirect parent) locator.  # noqa: E501

        :return: The affected_project of this VcsRootLocator.  # noqa: E501
        :rtype: str
        """
        return self._affected_project

    @affected_project.setter
    def affected_project(self, affected_project):
        """Sets the affected_project of this VcsRootLocator.

        Project (direct or indirect parent) locator.  # noqa: E501

        :param affected_project: The affected_project of this VcsRootLocator.  # noqa: E501
        :type: str
        """

        self._affected_project = affected_project

    @property
    def count(self):
        """Gets the count of this VcsRootLocator.  # noqa: E501

        For paginated calls, how many entities to return per page.  # noqa: E501

        :return: The count of this VcsRootLocator.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this VcsRootLocator.

        For paginated calls, how many entities to return per page.  # noqa: E501

        :param count: The count of this VcsRootLocator.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def id(self):
        """Gets the id of this VcsRootLocator.  # noqa: E501

        Entity ID.  # noqa: E501

        :return: The id of this VcsRootLocator.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VcsRootLocator.

        Entity ID.  # noqa: E501

        :param id: The id of this VcsRootLocator.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def internal_id(self):
        """Gets the internal_id of this VcsRootLocator.  # noqa: E501


        :return: The internal_id of this VcsRootLocator.  # noqa: E501
        :rtype: int
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this VcsRootLocator.


        :param internal_id: The internal_id of this VcsRootLocator.  # noqa: E501
        :type: int
        """

        self._internal_id = internal_id

    @property
    def item(self):
        """Gets the item of this VcsRootLocator.  # noqa: E501

        Supply multiple locators and return a union of the results.  # noqa: E501

        :return: The item of this VcsRootLocator.  # noqa: E501
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this VcsRootLocator.

        Supply multiple locators and return a union of the results.  # noqa: E501

        :param item: The item of this VcsRootLocator.  # noqa: E501
        :type: str
        """

        self._item = item

    @property
    def lookup_limit(self):
        """Gets the lookup_limit of this VcsRootLocator.  # noqa: E501

        Limit processing to the latest `<lookupLimit>` entities.  # noqa: E501

        :return: The lookup_limit of this VcsRootLocator.  # noqa: E501
        :rtype: int
        """
        return self._lookup_limit

    @lookup_limit.setter
    def lookup_limit(self, lookup_limit):
        """Sets the lookup_limit of this VcsRootLocator.

        Limit processing to the latest `<lookupLimit>` entities.  # noqa: E501

        :param lookup_limit: The lookup_limit of this VcsRootLocator.  # noqa: E501
        :type: int
        """

        self._lookup_limit = lookup_limit

    @property
    def name(self):
        """Gets the name of this VcsRootLocator.  # noqa: E501


        :return: The name of this VcsRootLocator.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VcsRootLocator.


        :param name: The name of this VcsRootLocator.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project(self):
        """Gets the project of this VcsRootLocator.  # noqa: E501

        Project (direct parent) locator.  # noqa: E501

        :return: The project of this VcsRootLocator.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this VcsRootLocator.

        Project (direct parent) locator.  # noqa: E501

        :param project: The project of this VcsRootLocator.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def _property(self):
        """Gets the _property of this VcsRootLocator.  # noqa: E501


        :return: The _property of this VcsRootLocator.  # noqa: E501
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this VcsRootLocator.


        :param _property: The _property of this VcsRootLocator.  # noqa: E501
        :type: str
        """
        allowed_values = ["exists", "not-exists", "equals", "does-not-equal", "starts-with", "contains", "does-not-contain", "ends-with", "any", "matches", "does-not-match", "more-than", "no-more-than", "less-than", "no-less-than", "ver-more-than", "ver-no-more-than", "ver-less-than", "ver-no-less-than"]  # noqa: E501
        if _property not in allowed_values:
            raise ValueError(
                "Invalid value for `_property` ({0}), must be one of {1}"  # noqa: E501
                .format(_property, allowed_values)
            )

        self.__property = _property

    @property
    def start(self):
        """Gets the start of this VcsRootLocator.  # noqa: E501

        For paginated calls, from which entity to start rendering the page.  # noqa: E501

        :return: The start of this VcsRootLocator.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this VcsRootLocator.

        For paginated calls, from which entity to start rendering the page.  # noqa: E501

        :param start: The start of this VcsRootLocator.  # noqa: E501
        :type: int
        """

        self._start = start

    @property
    def type(self):
        """Gets the type of this VcsRootLocator.  # noqa: E501

        Type of VCS (e.g. jetbrains.git).  # noqa: E501

        :return: The type of this VcsRootLocator.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VcsRootLocator.

        Type of VCS (e.g. jetbrains.git).  # noqa: E501

        :param type: The type of this VcsRootLocator.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uuid(self):
        """Gets the uuid of this VcsRootLocator.  # noqa: E501


        :return: The uuid of this VcsRootLocator.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this VcsRootLocator.


        :param uuid: The uuid of this VcsRootLocator.  # noqa: E501
        :type: str
        """

        self._uuid = uuid
