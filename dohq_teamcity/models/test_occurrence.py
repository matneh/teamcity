# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.build import Build  # noqa: F401,E501
# from dohq_teamcity.models.mute import Mute  # noqa: F401,E501
# from dohq_teamcity.models.test import Test  # noqa: F401,E501
# from dohq_teamcity.models.test_occurrence import TestOccurrence  # noqa: F401,E501
# from dohq_teamcity.models.test_occurrences import TestOccurrences  # noqa: F401,E501
# from dohq_teamcity.models.test_run_metadata import TestRunMetadata  # noqa: F401,E501


class TestOccurrence(TeamCityObject):
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
        'name': 'str',
        'status': 'str',
        'ignored': 'bool',
        'duration': 'int',
        'run_order': 'str',
        'new_failure': 'bool',
        'muted': 'bool',
        'currently_muted': 'bool',
        'currently_investigated': 'bool',
        'href': 'str',
        'ignore_details': 'str',
        'details': 'str',
        'test': 'Test',
        'mute': 'Mute',
        'build': 'Build',
        'first_failed': 'TestOccurrence',
        'next_fixed': 'TestOccurrence',
        'invocations': 'TestOccurrences',
        'metadata': 'TestRunMetadata',
        'log_anchor': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'ignored': 'ignored',
        'duration': 'duration',
        'run_order': 'runOrder',
        'new_failure': 'newFailure',
        'muted': 'muted',
        'currently_muted': 'currentlyMuted',
        'currently_investigated': 'currentlyInvestigated',
        'href': 'href',
        'ignore_details': 'ignoreDetails',
        'details': 'details',
        'test': 'test',
        'mute': 'mute',
        'build': 'build',
        'first_failed': 'firstFailed',
        'next_fixed': 'nextFixed',
        'invocations': 'invocations',
        'metadata': 'metadata',
        'log_anchor': 'logAnchor'
    }

    def __init__(self, id=None, name=None, status=None, ignored=None, duration=None, run_order=None, new_failure=None, muted=None, currently_muted=None, currently_investigated=None, href=None, ignore_details=None, details=None, test=None, mute=None, build=None, first_failed=None, next_fixed=None, invocations=None, metadata=None, log_anchor=None, teamcity=None):  # noqa: E501
        """TestOccurrence - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._status = None
        self._ignored = None
        self._duration = None
        self._run_order = None
        self._new_failure = None
        self._muted = None
        self._currently_muted = None
        self._currently_investigated = None
        self._href = None
        self._ignore_details = None
        self._details = None
        self._test = None
        self._mute = None
        self._build = None
        self._first_failed = None
        self._next_fixed = None
        self._invocations = None
        self._metadata = None
        self._log_anchor = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if ignored is not None:
            self.ignored = ignored
        if duration is not None:
            self.duration = duration
        if run_order is not None:
            self.run_order = run_order
        if new_failure is not None:
            self.new_failure = new_failure
        if muted is not None:
            self.muted = muted
        if currently_muted is not None:
            self.currently_muted = currently_muted
        if currently_investigated is not None:
            self.currently_investigated = currently_investigated
        if href is not None:
            self.href = href
        if ignore_details is not None:
            self.ignore_details = ignore_details
        if details is not None:
            self.details = details
        if test is not None:
            self.test = test
        if mute is not None:
            self.mute = mute
        if build is not None:
            self.build = build
        if first_failed is not None:
            self.first_failed = first_failed
        if next_fixed is not None:
            self.next_fixed = next_fixed
        if invocations is not None:
            self.invocations = invocations
        if metadata is not None:
            self.metadata = metadata
        if log_anchor is not None:
            self.log_anchor = log_anchor
        super(TestOccurrence, self).__init__(teamcity=teamcity)

    @property
    def id(self):
        """Gets the id of this TestOccurrence.  # noqa: E501


        :return: The id of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TestOccurrence.


        :param id: The id of this TestOccurrence.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this TestOccurrence.  # noqa: E501


        :return: The name of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TestOccurrence.


        :param name: The name of this TestOccurrence.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this TestOccurrence.  # noqa: E501


        :return: The status of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TestOccurrence.


        :param status: The status of this TestOccurrence.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNKNOWN", "NORMAL", "WARNING", "FAILURE", "ERROR"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def ignored(self):
        """Gets the ignored of this TestOccurrence.  # noqa: E501


        :return: The ignored of this TestOccurrence.  # noqa: E501
        :rtype: bool
        """
        return self._ignored

    @ignored.setter
    def ignored(self, ignored):
        """Sets the ignored of this TestOccurrence.


        :param ignored: The ignored of this TestOccurrence.  # noqa: E501
        :type: bool
        """

        self._ignored = ignored

    @property
    def duration(self):
        """Gets the duration of this TestOccurrence.  # noqa: E501


        :return: The duration of this TestOccurrence.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TestOccurrence.


        :param duration: The duration of this TestOccurrence.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def run_order(self):
        """Gets the run_order of this TestOccurrence.  # noqa: E501


        :return: The run_order of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._run_order

    @run_order.setter
    def run_order(self, run_order):
        """Sets the run_order of this TestOccurrence.


        :param run_order: The run_order of this TestOccurrence.  # noqa: E501
        :type: str
        """

        self._run_order = run_order

    @property
    def new_failure(self):
        """Gets the new_failure of this TestOccurrence.  # noqa: E501


        :return: The new_failure of this TestOccurrence.  # noqa: E501
        :rtype: bool
        """
        return self._new_failure

    @new_failure.setter
    def new_failure(self, new_failure):
        """Sets the new_failure of this TestOccurrence.


        :param new_failure: The new_failure of this TestOccurrence.  # noqa: E501
        :type: bool
        """

        self._new_failure = new_failure

    @property
    def muted(self):
        """Gets the muted of this TestOccurrence.  # noqa: E501


        :return: The muted of this TestOccurrence.  # noqa: E501
        :rtype: bool
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        """Sets the muted of this TestOccurrence.


        :param muted: The muted of this TestOccurrence.  # noqa: E501
        :type: bool
        """

        self._muted = muted

    @property
    def currently_muted(self):
        """Gets the currently_muted of this TestOccurrence.  # noqa: E501


        :return: The currently_muted of this TestOccurrence.  # noqa: E501
        :rtype: bool
        """
        return self._currently_muted

    @currently_muted.setter
    def currently_muted(self, currently_muted):
        """Sets the currently_muted of this TestOccurrence.


        :param currently_muted: The currently_muted of this TestOccurrence.  # noqa: E501
        :type: bool
        """

        self._currently_muted = currently_muted

    @property
    def currently_investigated(self):
        """Gets the currently_investigated of this TestOccurrence.  # noqa: E501


        :return: The currently_investigated of this TestOccurrence.  # noqa: E501
        :rtype: bool
        """
        return self._currently_investigated

    @currently_investigated.setter
    def currently_investigated(self, currently_investigated):
        """Sets the currently_investigated of this TestOccurrence.


        :param currently_investigated: The currently_investigated of this TestOccurrence.  # noqa: E501
        :type: bool
        """

        self._currently_investigated = currently_investigated

    @property
    def href(self):
        """Gets the href of this TestOccurrence.  # noqa: E501


        :return: The href of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this TestOccurrence.


        :param href: The href of this TestOccurrence.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def ignore_details(self):
        """Gets the ignore_details of this TestOccurrence.  # noqa: E501


        :return: The ignore_details of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._ignore_details

    @ignore_details.setter
    def ignore_details(self, ignore_details):
        """Sets the ignore_details of this TestOccurrence.


        :param ignore_details: The ignore_details of this TestOccurrence.  # noqa: E501
        :type: str
        """

        self._ignore_details = ignore_details

    @property
    def details(self):
        """Gets the details of this TestOccurrence.  # noqa: E501


        :return: The details of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this TestOccurrence.


        :param details: The details of this TestOccurrence.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def test(self):
        """Gets the test of this TestOccurrence.  # noqa: E501


        :return: The test of this TestOccurrence.  # noqa: E501
        :rtype: Test
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this TestOccurrence.


        :param test: The test of this TestOccurrence.  # noqa: E501
        :type: Test
        """

        self._test = test

    @property
    def mute(self):
        """Gets the mute of this TestOccurrence.  # noqa: E501


        :return: The mute of this TestOccurrence.  # noqa: E501
        :rtype: Mute
        """
        return self._mute

    @mute.setter
    def mute(self, mute):
        """Sets the mute of this TestOccurrence.


        :param mute: The mute of this TestOccurrence.  # noqa: E501
        :type: Mute
        """

        self._mute = mute

    @property
    def build(self):
        """Gets the build of this TestOccurrence.  # noqa: E501


        :return: The build of this TestOccurrence.  # noqa: E501
        :rtype: Build
        """
        return self._build

    @build.setter
    def build(self, build):
        """Sets the build of this TestOccurrence.


        :param build: The build of this TestOccurrence.  # noqa: E501
        :type: Build
        """

        self._build = build

    @property
    def first_failed(self):
        """Gets the first_failed of this TestOccurrence.  # noqa: E501


        :return: The first_failed of this TestOccurrence.  # noqa: E501
        :rtype: TestOccurrence
        """
        return self._first_failed

    @first_failed.setter
    def first_failed(self, first_failed):
        """Sets the first_failed of this TestOccurrence.


        :param first_failed: The first_failed of this TestOccurrence.  # noqa: E501
        :type: TestOccurrence
        """

        self._first_failed = first_failed

    @property
    def next_fixed(self):
        """Gets the next_fixed of this TestOccurrence.  # noqa: E501


        :return: The next_fixed of this TestOccurrence.  # noqa: E501
        :rtype: TestOccurrence
        """
        return self._next_fixed

    @next_fixed.setter
    def next_fixed(self, next_fixed):
        """Sets the next_fixed of this TestOccurrence.


        :param next_fixed: The next_fixed of this TestOccurrence.  # noqa: E501
        :type: TestOccurrence
        """

        self._next_fixed = next_fixed

    @property
    def invocations(self):
        """Gets the invocations of this TestOccurrence.  # noqa: E501


        :return: The invocations of this TestOccurrence.  # noqa: E501
        :rtype: TestOccurrences
        """
        return self._invocations

    @invocations.setter
    def invocations(self, invocations):
        """Sets the invocations of this TestOccurrence.


        :param invocations: The invocations of this TestOccurrence.  # noqa: E501
        :type: TestOccurrences
        """

        self._invocations = invocations

    @property
    def metadata(self):
        """Gets the metadata of this TestOccurrence.  # noqa: E501


        :return: The metadata of this TestOccurrence.  # noqa: E501
        :rtype: TestRunMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this TestOccurrence.


        :param metadata: The metadata of this TestOccurrence.  # noqa: E501
        :type: TestRunMetadata
        """

        self._metadata = metadata

    @property
    def log_anchor(self):
        """Gets the log_anchor of this TestOccurrence.  # noqa: E501


        :return: The log_anchor of this TestOccurrence.  # noqa: E501
        :rtype: str
        """
        return self._log_anchor

    @log_anchor.setter
    def log_anchor(self, log_anchor):
        """Sets the log_anchor of this TestOccurrence.


        :param log_anchor: The log_anchor of this TestOccurrence.  # noqa: E501
        :type: str
        """

        self._log_anchor = log_anchor
