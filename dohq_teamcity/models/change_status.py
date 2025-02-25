# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.builds import Builds  # noqa: F401,E501


class ChangeStatus(TeamCityObject):
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
        'running_successfully_builds': 'int',
        'pending_build_types': 'int',
        'successful_builds': 'int',
        'total_problems': 'int',
        'new_failed_tests': 'int',
        'other_failed_tests': 'int',
        'queued_builds_count': 'int',
        'critical_builds': 'Builds',
        'not_critical_builds': 'Builds',
        'new_tests_failed_builds': 'Builds',
        'compilation_error_builds': 'Builds',
        'running_builds': 'int',
        'failed_builds': 'int',
        'cancelled_builds': 'int',
        'finished_builds': 'int'
    }

    attribute_map = {
        'running_successfully_builds': 'runningSuccessfullyBuilds',
        'pending_build_types': 'pendingBuildTypes',
        'successful_builds': 'successfulBuilds',
        'total_problems': 'totalProblems',
        'new_failed_tests': 'newFailedTests',
        'other_failed_tests': 'otherFailedTests',
        'queued_builds_count': 'queuedBuildsCount',
        'critical_builds': 'criticalBuilds',
        'not_critical_builds': 'notCriticalBuilds',
        'new_tests_failed_builds': 'newTestsFailedBuilds',
        'compilation_error_builds': 'compilationErrorBuilds',
        'running_builds': 'runningBuilds',
        'failed_builds': 'failedBuilds',
        'cancelled_builds': 'cancelledBuilds',
        'finished_builds': 'finishedBuilds'
    }

    def __init__(self, running_successfully_builds=None, pending_build_types=None, successful_builds=None, total_problems=None, new_failed_tests=None, other_failed_tests=None, queued_builds_count=None, critical_builds=None, not_critical_builds=None, new_tests_failed_builds=None, compilation_error_builds=None, running_builds=None, failed_builds=None, cancelled_builds=None, finished_builds=None, teamcity=None):  # noqa: E501
        """ChangeStatus - a model defined in Swagger"""  # noqa: E501

        self._running_successfully_builds = None
        self._pending_build_types = None
        self._successful_builds = None
        self._total_problems = None
        self._new_failed_tests = None
        self._other_failed_tests = None
        self._queued_builds_count = None
        self._critical_builds = None
        self._not_critical_builds = None
        self._new_tests_failed_builds = None
        self._compilation_error_builds = None
        self._running_builds = None
        self._failed_builds = None
        self._cancelled_builds = None
        self._finished_builds = None
        self.discriminator = None

        if running_successfully_builds is not None:
            self.running_successfully_builds = running_successfully_builds
        if pending_build_types is not None:
            self.pending_build_types = pending_build_types
        if successful_builds is not None:
            self.successful_builds = successful_builds
        if total_problems is not None:
            self.total_problems = total_problems
        if new_failed_tests is not None:
            self.new_failed_tests = new_failed_tests
        if other_failed_tests is not None:
            self.other_failed_tests = other_failed_tests
        if queued_builds_count is not None:
            self.queued_builds_count = queued_builds_count
        if critical_builds is not None:
            self.critical_builds = critical_builds
        if not_critical_builds is not None:
            self.not_critical_builds = not_critical_builds
        if new_tests_failed_builds is not None:
            self.new_tests_failed_builds = new_tests_failed_builds
        if compilation_error_builds is not None:
            self.compilation_error_builds = compilation_error_builds
        if running_builds is not None:
            self.running_builds = running_builds
        if failed_builds is not None:
            self.failed_builds = failed_builds
        if cancelled_builds is not None:
            self.cancelled_builds = cancelled_builds
        if finished_builds is not None:
            self.finished_builds = finished_builds
        super(ChangeStatus, self).__init__(teamcity=teamcity)

    @property
    def running_successfully_builds(self):
        """Gets the running_successfully_builds of this ChangeStatus.  # noqa: E501


        :return: The running_successfully_builds of this ChangeStatus.  # noqa: E501
        :rtype: int
        """
        return self._running_successfully_builds

    @running_successfully_builds.setter
    def running_successfully_builds(self, running_successfully_builds):
        """Sets the running_successfully_builds of this ChangeStatus.


        :param running_successfully_builds: The running_successfully_builds of this ChangeStatus.  # noqa: E501
        :type: int
        """

        self._running_successfully_builds = running_successfully_builds

    @property
    def pending_build_types(self):
        """Gets the pending_build_types of this ChangeStatus.  # noqa: E501


        :return: The pending_build_types of this ChangeStatus.  # noqa: E501
        :rtype: int
        """
        return self._pending_build_types

    @pending_build_types.setter
    def pending_build_types(self, pending_build_types):
        """Sets the pending_build_types of this ChangeStatus.


        :param pending_build_types: The pending_build_types of this ChangeStatus.  # noqa: E501
        :type: int
        """

        self._pending_build_types = pending_build_types

    @property
    def successful_builds(self):
        """Gets the successful_builds of this ChangeStatus.  # noqa: E501


        :return: The successful_builds of this ChangeStatus.  # noqa: E501
        :rtype: int
        """
        return self._successful_builds

    @successful_builds.setter
    def successful_builds(self, successful_builds):
        """Sets the successful_builds of this ChangeStatus.


        :param successful_builds: The successful_builds of this ChangeStatus.  # noqa: E501
        :type: int
        """

        self._successful_builds = successful_builds

    @property
    def total_problems(self):
        """Gets the total_problems of this ChangeStatus.  # noqa: E501


        :return: The total_problems of this ChangeStatus.  # noqa: E501
        :rtype: int
        """
        return self._total_problems

    @total_problems.setter
    def total_problems(self, total_problems):
        """Sets the total_problems of this ChangeStatus.


        :param total_problems: The total_problems of this ChangeStatus.  # noqa: E501
        :type: int
        """

        self._total_problems = total_problems

    @property
    def new_failed_tests(self):
        """Gets the new_failed_tests of this ChangeStatus.  # noqa: E501


        :return: The new_failed_tests of this ChangeStatus.  # noqa: E501
        :rtype: int
        """
        return self._new_failed_tests

    @new_failed_tests.setter
    def new_failed_tests(self, new_failed_tests):
        """Sets the new_failed_tests of this ChangeStatus.


        :param new_failed_tests: The new_failed_tests of this ChangeStatus.  # noqa: E501
        :type: int
        """

        self._new_failed_tests = new_failed_tests

    @property
    def other_failed_tests(self):
        """Gets the other_failed_tests of this ChangeStatus.  # noqa: E501


        :return: The other_failed_tests of this ChangeStatus.  # noqa: E501
        :rtype: int
        """
        return self._other_failed_tests

    @other_failed_tests.setter
    def other_failed_tests(self, other_failed_tests):
        """Sets the other_failed_tests of this ChangeStatus.


        :param other_failed_tests: The other_failed_tests of this ChangeStatus.  # noqa: E501
        :type: int
        """

        self._other_failed_tests = other_failed_tests

    @property
    def queued_builds_count(self):
        """Gets the queued_builds_count of this ChangeStatus.  # noqa: E501


        :return: The queued_builds_count of this ChangeStatus.  # noqa: E501
        :rtype: int
        """
        return self._queued_builds_count

    @queued_builds_count.setter
    def queued_builds_count(self, queued_builds_count):
        """Sets the queued_builds_count of this ChangeStatus.


        :param queued_builds_count: The queued_builds_count of this ChangeStatus.  # noqa: E501
        :type: int
        """

        self._queued_builds_count = queued_builds_count

    @property
    def critical_builds(self):
        """Gets the critical_builds of this ChangeStatus.  # noqa: E501


        :return: The critical_builds of this ChangeStatus.  # noqa: E501
        :rtype: Builds
        """
        return self._critical_builds

    @critical_builds.setter
    def critical_builds(self, critical_builds):
        """Sets the critical_builds of this ChangeStatus.


        :param critical_builds: The critical_builds of this ChangeStatus.  # noqa: E501
        :type: Builds
        """

        self._critical_builds = critical_builds

    @property
    def not_critical_builds(self):
        """Gets the not_critical_builds of this ChangeStatus.  # noqa: E501


        :return: The not_critical_builds of this ChangeStatus.  # noqa: E501
        :rtype: Builds
        """
        return self._not_critical_builds

    @not_critical_builds.setter
    def not_critical_builds(self, not_critical_builds):
        """Sets the not_critical_builds of this ChangeStatus.


        :param not_critical_builds: The not_critical_builds of this ChangeStatus.  # noqa: E501
        :type: Builds
        """

        self._not_critical_builds = not_critical_builds

    @property
    def new_tests_failed_builds(self):
        """Gets the new_tests_failed_builds of this ChangeStatus.  # noqa: E501


        :return: The new_tests_failed_builds of this ChangeStatus.  # noqa: E501
        :rtype: Builds
        """
        return self._new_tests_failed_builds

    @new_tests_failed_builds.setter
    def new_tests_failed_builds(self, new_tests_failed_builds):
        """Sets the new_tests_failed_builds of this ChangeStatus.


        :param new_tests_failed_builds: The new_tests_failed_builds of this ChangeStatus.  # noqa: E501
        :type: Builds
        """

        self._new_tests_failed_builds = new_tests_failed_builds

    @property
    def compilation_error_builds(self):
        """Gets the compilation_error_builds of this ChangeStatus.  # noqa: E501


        :return: The compilation_error_builds of this ChangeStatus.  # noqa: E501
        :rtype: Builds
        """
        return self._compilation_error_builds

    @compilation_error_builds.setter
    def compilation_error_builds(self, compilation_error_builds):
        """Sets the compilation_error_builds of this ChangeStatus.


        :param compilation_error_builds: The compilation_error_builds of this ChangeStatus.  # noqa: E501
        :type: Builds
        """

        self._compilation_error_builds = compilation_error_builds

    @property
    def running_builds(self):
        """Gets the running_builds of this ChangeStatus.  # noqa: E501


        :return: The running_builds of this ChangeStatus.  # noqa: E501
        :rtype: int
        """
        return self._running_builds

    @running_builds.setter
    def running_builds(self, running_builds):
        """Sets the running_builds of this ChangeStatus.


        :param running_builds: The running_builds of this ChangeStatus.  # noqa: E501
        :type: int
        """

        self._running_builds = running_builds

    @property
    def failed_builds(self):
        """Gets the failed_builds of this ChangeStatus.  # noqa: E501


        :return: The failed_builds of this ChangeStatus.  # noqa: E501
        :rtype: int
        """
        return self._failed_builds

    @failed_builds.setter
    def failed_builds(self, failed_builds):
        """Sets the failed_builds of this ChangeStatus.


        :param failed_builds: The failed_builds of this ChangeStatus.  # noqa: E501
        :type: int
        """

        self._failed_builds = failed_builds

    @property
    def cancelled_builds(self):
        """Gets the cancelled_builds of this ChangeStatus.  # noqa: E501


        :return: The cancelled_builds of this ChangeStatus.  # noqa: E501
        :rtype: int
        """
        return self._cancelled_builds

    @cancelled_builds.setter
    def cancelled_builds(self, cancelled_builds):
        """Sets the cancelled_builds of this ChangeStatus.


        :param cancelled_builds: The cancelled_builds of this ChangeStatus.  # noqa: E501
        :type: int
        """

        self._cancelled_builds = cancelled_builds

    @property
    def finished_builds(self):
        """Gets the finished_builds of this ChangeStatus.  # noqa: E501


        :return: The finished_builds of this ChangeStatus.  # noqa: E501
        :rtype: int
        """
        return self._finished_builds

    @finished_builds.setter
    def finished_builds(self, finished_builds):
        """Sets the finished_builds of this ChangeStatus.


        :param finished_builds: The finished_builds of this ChangeStatus.  # noqa: E501
        :type: int
        """

        self._finished_builds = finished_builds
