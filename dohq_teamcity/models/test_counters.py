# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


class TestCounters(TeamCityObject):
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
        'ignored': 'int',
        'failed': 'int',
        'muted': 'int',
        'success': 'int',
        'all': 'int',
        'new_failed': 'int',
        'duration': 'int'
    }

    attribute_map = {
        'ignored': 'ignored',
        'failed': 'failed',
        'muted': 'muted',
        'success': 'success',
        'all': 'all',
        'new_failed': 'newFailed',
        'duration': 'duration'
    }

    def __init__(self, ignored=None, failed=None, muted=None, success=None, all=None, new_failed=None, duration=None, teamcity=None):  # noqa: E501
        """TestCounters - a model defined in Swagger"""  # noqa: E501

        self._ignored = None
        self._failed = None
        self._muted = None
        self._success = None
        self._all = None
        self._new_failed = None
        self._duration = None
        self.discriminator = None

        if ignored is not None:
            self.ignored = ignored
        if failed is not None:
            self.failed = failed
        if muted is not None:
            self.muted = muted
        if success is not None:
            self.success = success
        if all is not None:
            self.all = all
        if new_failed is not None:
            self.new_failed = new_failed
        if duration is not None:
            self.duration = duration
        super(TestCounters, self).__init__(teamcity=teamcity)

    @property
    def ignored(self):
        """Gets the ignored of this TestCounters.  # noqa: E501


        :return: The ignored of this TestCounters.  # noqa: E501
        :rtype: int
        """
        return self._ignored

    @ignored.setter
    def ignored(self, ignored):
        """Sets the ignored of this TestCounters.


        :param ignored: The ignored of this TestCounters.  # noqa: E501
        :type: int
        """

        self._ignored = ignored

    @property
    def failed(self):
        """Gets the failed of this TestCounters.  # noqa: E501


        :return: The failed of this TestCounters.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this TestCounters.


        :param failed: The failed of this TestCounters.  # noqa: E501
        :type: int
        """

        self._failed = failed

    @property
    def muted(self):
        """Gets the muted of this TestCounters.  # noqa: E501


        :return: The muted of this TestCounters.  # noqa: E501
        :rtype: int
        """
        return self._muted

    @muted.setter
    def muted(self, muted):
        """Sets the muted of this TestCounters.


        :param muted: The muted of this TestCounters.  # noqa: E501
        :type: int
        """

        self._muted = muted

    @property
    def success(self):
        """Gets the success of this TestCounters.  # noqa: E501


        :return: The success of this TestCounters.  # noqa: E501
        :rtype: int
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this TestCounters.


        :param success: The success of this TestCounters.  # noqa: E501
        :type: int
        """

        self._success = success

    @property
    def all(self):
        """Gets the all of this TestCounters.  # noqa: E501


        :return: The all of this TestCounters.  # noqa: E501
        :rtype: int
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this TestCounters.


        :param all: The all of this TestCounters.  # noqa: E501
        :type: int
        """

        self._all = all

    @property
    def new_failed(self):
        """Gets the new_failed of this TestCounters.  # noqa: E501


        :return: The new_failed of this TestCounters.  # noqa: E501
        :rtype: int
        """
        return self._new_failed

    @new_failed.setter
    def new_failed(self, new_failed):
        """Sets the new_failed of this TestCounters.


        :param new_failed: The new_failed of this TestCounters.  # noqa: E501
        :type: int
        """

        self._new_failed = new_failed

    @property
    def duration(self):
        """Gets the duration of this TestCounters.  # noqa: E501


        :return: The duration of this TestCounters.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TestCounters.


        :param duration: The duration of this TestCounters.  # noqa: E501
        :type: int
        """

        self._duration = duration
