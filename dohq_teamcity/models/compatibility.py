# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.agent import Agent  # noqa: F401,E501
# from dohq_teamcity.models.build_type import BuildType  # noqa: F401,E501
# from dohq_teamcity.models.requirements import Requirements  # noqa: F401,E501


class Compatibility(TeamCityObject):
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
        'compatible': 'bool',
        'agent': 'Agent',
        'build_type': 'BuildType',
        'unmet_requirements': 'Requirements'
    }

    attribute_map = {
        'compatible': 'compatible',
        'agent': 'agent',
        'build_type': 'buildType',
        'unmet_requirements': 'unmetRequirements'
    }

    def __init__(self, compatible=None, agent=None, build_type=None, unmet_requirements=None, teamcity=None):  # noqa: E501
        """Compatibility - a model defined in Swagger"""  # noqa: E501

        self._compatible = None
        self._agent = None
        self._build_type = None
        self._unmet_requirements = None
        self.discriminator = None

        if compatible is not None:
            self.compatible = compatible
        if agent is not None:
            self.agent = agent
        if build_type is not None:
            self.build_type = build_type
        if unmet_requirements is not None:
            self.unmet_requirements = unmet_requirements
        super(Compatibility, self).__init__(teamcity=teamcity)

    @property
    def compatible(self):
        """Gets the compatible of this Compatibility.  # noqa: E501


        :return: The compatible of this Compatibility.  # noqa: E501
        :rtype: bool
        """
        return self._compatible

    @compatible.setter
    def compatible(self, compatible):
        """Sets the compatible of this Compatibility.


        :param compatible: The compatible of this Compatibility.  # noqa: E501
        :type: bool
        """

        self._compatible = compatible

    @property
    def agent(self):
        """Gets the agent of this Compatibility.  # noqa: E501


        :return: The agent of this Compatibility.  # noqa: E501
        :rtype: Agent
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this Compatibility.


        :param agent: The agent of this Compatibility.  # noqa: E501
        :type: Agent
        """

        self._agent = agent

    @property
    def build_type(self):
        """Gets the build_type of this Compatibility.  # noqa: E501


        :return: The build_type of this Compatibility.  # noqa: E501
        :rtype: BuildType
        """
        return self._build_type

    @build_type.setter
    def build_type(self, build_type):
        """Sets the build_type of this Compatibility.


        :param build_type: The build_type of this Compatibility.  # noqa: E501
        :type: BuildType
        """

        self._build_type = build_type

    @property
    def unmet_requirements(self):
        """Gets the unmet_requirements of this Compatibility.  # noqa: E501


        :return: The unmet_requirements of this Compatibility.  # noqa: E501
        :rtype: Requirements
        """
        return self._unmet_requirements

    @unmet_requirements.setter
    def unmet_requirements(self, unmet_requirements):
        """Sets the unmet_requirements of this Compatibility.


        :param unmet_requirements: The unmet_requirements of this Compatibility.  # noqa: E501
        :type: Requirements
        """

        self._unmet_requirements = unmet_requirements
