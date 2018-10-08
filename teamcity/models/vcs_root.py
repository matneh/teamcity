# coding: utf-8

from teamcity.custom.model import TeamcityObject


# from teamcity.models.items import Items  # noqa: F401,E501
# from teamcity.models.project import Project  # noqa: F401,E501
# from teamcity.models.properties import Properties  # noqa: F401,E501
# from teamcity.models.vcs_root_instances import VcsRootInstances  # noqa: F401,E501


class VcsRoot(TeamcityObject):
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
        'href': 'str',
        'id': 'str',
        'internal_id': 'str',
        'locator': 'str',
        'modification_check_interval': 'int',
        'name': 'str',
        'project': 'Project',
        'project_locator': 'str',
        'properties': 'Properties',
        'repository_id_strings': 'Items',
        'uuid': 'str',
        'vcs_name': 'str',
        'vcs_root_instances': 'VcsRootInstances'
    }

    attribute_map = {
        'href': 'href',
        'id': 'id',
        'internal_id': 'internalId',
        'locator': 'locator',
        'modification_check_interval': 'modificationCheckInterval',
        'name': 'name',
        'project': 'project',
        'project_locator': 'projectLocator',
        'properties': 'properties',
        'repository_id_strings': 'repositoryIdStrings',
        'uuid': 'uuid',
        'vcs_name': 'vcsName',
        'vcs_root_instances': 'vcsRootInstances'
    }

    def __init__(self, href=None, id=None, internal_id=None, locator=None, modification_check_interval=None, name=None, project=None, project_locator=None, properties=None, repository_id_strings=None, uuid=None, vcs_name=None, vcs_root_instances=None):  # noqa: E501
        """VcsRoot - a model defined in Swagger"""  # noqa: E501
        super(VcsRoot, self).__init__()

        self._href = None
        self._id = None
        self._internal_id = None
        self._locator = None
        self._modification_check_interval = None
        self._name = None
        self._project = None
        self._project_locator = None
        self._properties = None
        self._repository_id_strings = None
        self._uuid = None
        self._vcs_name = None
        self._vcs_root_instances = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if id is not None:
            self.id = id
        if internal_id is not None:
            self.internal_id = internal_id
        if locator is not None:
            self.locator = locator
        if modification_check_interval is not None:
            self.modification_check_interval = modification_check_interval
        if name is not None:
            self.name = name
        if project is not None:
            self.project = project
        if project_locator is not None:
            self.project_locator = project_locator
        if properties is not None:
            self.properties = properties
        if repository_id_strings is not None:
            self.repository_id_strings = repository_id_strings
        if uuid is not None:
            self.uuid = uuid
        if vcs_name is not None:
            self.vcs_name = vcs_name
        if vcs_root_instances is not None:
            self.vcs_root_instances = vcs_root_instances

    @property
    def href(self):
        """Gets the href of this VcsRoot.  # noqa: E501


        :return: The href of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this VcsRoot.


        :param href: The href of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this VcsRoot.  # noqa: E501


        :return: The id of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VcsRoot.


        :param id: The id of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def internal_id(self):
        """Gets the internal_id of this VcsRoot.  # noqa: E501


        :return: The internal_id of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this VcsRoot.


        :param internal_id: The internal_id of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._internal_id = internal_id

    @property
    def locator(self):
        """Gets the locator of this VcsRoot.  # noqa: E501


        :return: The locator of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this VcsRoot.


        :param locator: The locator of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._locator = locator

    @property
    def modification_check_interval(self):
        """Gets the modification_check_interval of this VcsRoot.  # noqa: E501


        :return: The modification_check_interval of this VcsRoot.  # noqa: E501
        :rtype: int
        """
        return self._modification_check_interval

    @modification_check_interval.setter
    def modification_check_interval(self, modification_check_interval):
        """Sets the modification_check_interval of this VcsRoot.


        :param modification_check_interval: The modification_check_interval of this VcsRoot.  # noqa: E501
        :type: int
        """

        self._modification_check_interval = modification_check_interval

    @property
    def name(self):
        """Gets the name of this VcsRoot.  # noqa: E501


        :return: The name of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VcsRoot.


        :param name: The name of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project(self):
        """Gets the project of this VcsRoot.  # noqa: E501


        :return: The project of this VcsRoot.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this VcsRoot.


        :param project: The project of this VcsRoot.  # noqa: E501
        :type: Project
        """

        self._project = project

    @property
    def project_locator(self):
        """Gets the project_locator of this VcsRoot.  # noqa: E501


        :return: The project_locator of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._project_locator

    @project_locator.setter
    def project_locator(self, project_locator):
        """Sets the project_locator of this VcsRoot.


        :param project_locator: The project_locator of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._project_locator = project_locator

    @property
    def properties(self):
        """Gets the properties of this VcsRoot.  # noqa: E501


        :return: The properties of this VcsRoot.  # noqa: E501
        :rtype: Properties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this VcsRoot.


        :param properties: The properties of this VcsRoot.  # noqa: E501
        :type: Properties
        """

        self._properties = properties

    @property
    def repository_id_strings(self):
        """Gets the repository_id_strings of this VcsRoot.  # noqa: E501


        :return: The repository_id_strings of this VcsRoot.  # noqa: E501
        :rtype: Items
        """
        return self._repository_id_strings

    @repository_id_strings.setter
    def repository_id_strings(self, repository_id_strings):
        """Sets the repository_id_strings of this VcsRoot.


        :param repository_id_strings: The repository_id_strings of this VcsRoot.  # noqa: E501
        :type: Items
        """

        self._repository_id_strings = repository_id_strings

    @property
    def uuid(self):
        """Gets the uuid of this VcsRoot.  # noqa: E501


        :return: The uuid of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this VcsRoot.


        :param uuid: The uuid of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def vcs_name(self):
        """Gets the vcs_name of this VcsRoot.  # noqa: E501


        :return: The vcs_name of this VcsRoot.  # noqa: E501
        :rtype: str
        """
        return self._vcs_name

    @vcs_name.setter
    def vcs_name(self, vcs_name):
        """Sets the vcs_name of this VcsRoot.


        :param vcs_name: The vcs_name of this VcsRoot.  # noqa: E501
        :type: str
        """

        self._vcs_name = vcs_name

    @property
    def vcs_root_instances(self):
        """Gets the vcs_root_instances of this VcsRoot.  # noqa: E501


        :return: The vcs_root_instances of this VcsRoot.  # noqa: E501
        :rtype: VcsRootInstances
        """
        return self._vcs_root_instances

    @vcs_root_instances.setter
    def vcs_root_instances(self, vcs_root_instances):
        """Sets the vcs_root_instances of this VcsRoot.


        :param vcs_root_instances: The vcs_root_instances of this VcsRoot.  # noqa: E501
        :type: VcsRootInstances
        """

        self._vcs_root_instances = vcs_root_instances

