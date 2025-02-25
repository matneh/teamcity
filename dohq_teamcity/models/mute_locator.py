# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class MuteLocator(TeamCityObject):
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
        'creation_date': 'datetime',
        'id': 'int',
        'item': 'str',
        'problem': 'str',
        'project': 'str',
        'reporter': 'str',
        'resolution': 'str',
        'test': 'str',
        'type': 'str',
        'unmute_date': 'datetime'
    }

    attribute_map = {
        'affected_project': 'affectedProject',
        'creation_date': 'creationDate',
        'id': 'id',
        'item': 'item',
        'problem': 'problem',
        'project': 'project',
        'reporter': 'reporter',
        'resolution': 'resolution',
        'test': 'test',
        'type': 'type',
        'unmute_date': 'unmuteDate'
    }

    def __init__(self, affected_project=None, creation_date=None, id=None, item=None, problem=None, project=None, reporter=None, resolution=None, test=None, type=None, unmute_date=None, teamcity=None):  # noqa: E501
        """MuteLocator - a model defined in Swagger"""  # noqa: E501

        self._affected_project = None
        self._creation_date = None
        self._id = None
        self._item = None
        self._problem = None
        self._project = None
        self._reporter = None
        self._resolution = None
        self._test = None
        self._type = None
        self._unmute_date = None
        self.discriminator = None

        if affected_project is not None:
            self.affected_project = affected_project
        if creation_date is not None:
            self.creation_date = creation_date
        if id is not None:
            self.id = id
        if item is not None:
            self.item = item
        if problem is not None:
            self.problem = problem
        if project is not None:
            self.project = project
        if reporter is not None:
            self.reporter = reporter
        if resolution is not None:
            self.resolution = resolution
        if test is not None:
            self.test = test
        if type is not None:
            self.type = type
        if unmute_date is not None:
            self.unmute_date = unmute_date
        super(MuteLocator, self).__init__(teamcity=teamcity)

    @property
    def affected_project(self):
        """Gets the affected_project of this MuteLocator.  # noqa: E501

        Project (direct or indirect parent) locator.  # noqa: E501

        :return: The affected_project of this MuteLocator.  # noqa: E501
        :rtype: str
        """
        return self._affected_project

    @affected_project.setter
    def affected_project(self, affected_project):
        """Sets the affected_project of this MuteLocator.

        Project (direct or indirect parent) locator.  # noqa: E501

        :param affected_project: The affected_project of this MuteLocator.  # noqa: E501
        :type: str
        """

        self._affected_project = affected_project

    @property
    def creation_date(self):
        """Gets the creation_date of this MuteLocator.  # noqa: E501

        yyyyMMddTHHmmss+ZZZZ  # noqa: E501

        :return: The creation_date of this MuteLocator.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this MuteLocator.

        yyyyMMddTHHmmss+ZZZZ  # noqa: E501

        :param creation_date: The creation_date of this MuteLocator.  # noqa: E501
        :type: datetime
        """

        self._creation_date = creation_date

    @property
    def id(self):
        """Gets the id of this MuteLocator.  # noqa: E501


        :return: The id of this MuteLocator.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MuteLocator.


        :param id: The id of this MuteLocator.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def item(self):
        """Gets the item of this MuteLocator.  # noqa: E501

        Supply multiple locators and return a union of the results.  # noqa: E501

        :return: The item of this MuteLocator.  # noqa: E501
        :rtype: str
        """
        return self._item

    @item.setter
    def item(self, item):
        """Sets the item of this MuteLocator.

        Supply multiple locators and return a union of the results.  # noqa: E501

        :param item: The item of this MuteLocator.  # noqa: E501
        :type: str
        """

        self._item = item

    @property
    def problem(self):
        """Gets the problem of this MuteLocator.  # noqa: E501

        Problem locator.  # noqa: E501

        :return: The problem of this MuteLocator.  # noqa: E501
        :rtype: str
        """
        return self._problem

    @problem.setter
    def problem(self, problem):
        """Sets the problem of this MuteLocator.

        Problem locator.  # noqa: E501

        :param problem: The problem of this MuteLocator.  # noqa: E501
        :type: str
        """

        self._problem = problem

    @property
    def project(self):
        """Gets the project of this MuteLocator.  # noqa: E501

        Project (direct parent) locator.  # noqa: E501

        :return: The project of this MuteLocator.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this MuteLocator.

        Project (direct parent) locator.  # noqa: E501

        :param project: The project of this MuteLocator.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def reporter(self):
        """Gets the reporter of this MuteLocator.  # noqa: E501

        User who muted this test.  # noqa: E501

        :return: The reporter of this MuteLocator.  # noqa: E501
        :rtype: str
        """
        return self._reporter

    @reporter.setter
    def reporter(self, reporter):
        """Sets the reporter of this MuteLocator.

        User who muted this test.  # noqa: E501

        :param reporter: The reporter of this MuteLocator.  # noqa: E501
        :type: str
        """

        self._reporter = reporter

    @property
    def resolution(self):
        """Gets the resolution of this MuteLocator.  # noqa: E501


        :return: The resolution of this MuteLocator.  # noqa: E501
        :rtype: str
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this MuteLocator.


        :param resolution: The resolution of this MuteLocator.  # noqa: E501
        :type: str
        """
        allowed_values = ["manually", "whenFixed", "atTime"]  # noqa: E501
        if resolution not in allowed_values:
            raise ValueError(
                "Invalid value for `resolution` ({0}), must be one of {1}"  # noqa: E501
                .format(resolution, allowed_values)
            )

        self._resolution = resolution

    @property
    def test(self):
        """Gets the test of this MuteLocator.  # noqa: E501

        Test locator.  # noqa: E501

        :return: The test of this MuteLocator.  # noqa: E501
        :rtype: str
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this MuteLocator.

        Test locator.  # noqa: E501

        :param test: The test of this MuteLocator.  # noqa: E501
        :type: str
        """

        self._test = test

    @property
    def type(self):
        """Gets the type of this MuteLocator.  # noqa: E501


        :return: The type of this MuteLocator.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MuteLocator.


        :param type: The type of this MuteLocator.  # noqa: E501
        :type: str
        """
        allowed_values = ["test", "problem", "anyProblem", "unknown"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def unmute_date(self):
        """Gets the unmute_date of this MuteLocator.  # noqa: E501

        yyyyMMddTHHmmss+ZZZZ  # noqa: E501

        :return: The unmute_date of this MuteLocator.  # noqa: E501
        :rtype: datetime
        """
        return self._unmute_date

    @unmute_date.setter
    def unmute_date(self, unmute_date):
        """Sets the unmute_date of this MuteLocator.

        yyyyMMddTHHmmss+ZZZZ  # noqa: E501

        :param unmute_date: The unmute_date of this MuteLocator.  # noqa: E501
        :type: datetime
        """

        self._unmute_date = unmute_date
