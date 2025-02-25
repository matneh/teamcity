# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.project import Project  # noqa: F401,E501
# from dohq_teamcity.models.properties import Properties  # noqa: F401,E501


class NewProjectDescription(TeamCityObject):
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
        'copy_all_associated_settings': 'bool',
        'projects_ids_map': 'Properties',
        'build_types_ids_map': 'Properties',
        'vcs_roots_ids_map': 'Properties',
        'name': 'str',
        'id': 'str',
        'source_project_locator': 'str',
        'source_project': 'Project',
        'parent_project': 'Project'
    }

    attribute_map = {
        'copy_all_associated_settings': 'copyAllAssociatedSettings',
        'projects_ids_map': 'projectsIdsMap',
        'build_types_ids_map': 'buildTypesIdsMap',
        'vcs_roots_ids_map': 'vcsRootsIdsMap',
        'name': 'name',
        'id': 'id',
        'source_project_locator': 'sourceProjectLocator',
        'source_project': 'sourceProject',
        'parent_project': 'parentProject'
    }

    def __init__(self, copy_all_associated_settings=None, projects_ids_map=None, build_types_ids_map=None, vcs_roots_ids_map=None, name=None, id=None, source_project_locator=None, source_project=None, parent_project=None, teamcity=None):  # noqa: E501
        """NewProjectDescription - a model defined in Swagger"""  # noqa: E501

        self._copy_all_associated_settings = None
        self._projects_ids_map = None
        self._build_types_ids_map = None
        self._vcs_roots_ids_map = None
        self._name = None
        self._id = None
        self._source_project_locator = None
        self._source_project = None
        self._parent_project = None
        self.discriminator = None

        if copy_all_associated_settings is not None:
            self.copy_all_associated_settings = copy_all_associated_settings
        if projects_ids_map is not None:
            self.projects_ids_map = projects_ids_map
        if build_types_ids_map is not None:
            self.build_types_ids_map = build_types_ids_map
        if vcs_roots_ids_map is not None:
            self.vcs_roots_ids_map = vcs_roots_ids_map
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if source_project_locator is not None:
            self.source_project_locator = source_project_locator
        if source_project is not None:
            self.source_project = source_project
        if parent_project is not None:
            self.parent_project = parent_project
        super(NewProjectDescription, self).__init__(teamcity=teamcity)

    @property
    def copy_all_associated_settings(self):
        """Gets the copy_all_associated_settings of this NewProjectDescription.  # noqa: E501


        :return: The copy_all_associated_settings of this NewProjectDescription.  # noqa: E501
        :rtype: bool
        """
        return self._copy_all_associated_settings

    @copy_all_associated_settings.setter
    def copy_all_associated_settings(self, copy_all_associated_settings):
        """Sets the copy_all_associated_settings of this NewProjectDescription.


        :param copy_all_associated_settings: The copy_all_associated_settings of this NewProjectDescription.  # noqa: E501
        :type: bool
        """

        self._copy_all_associated_settings = copy_all_associated_settings

    @property
    def projects_ids_map(self):
        """Gets the projects_ids_map of this NewProjectDescription.  # noqa: E501


        :return: The projects_ids_map of this NewProjectDescription.  # noqa: E501
        :rtype: Properties
        """
        return self._projects_ids_map

    @projects_ids_map.setter
    def projects_ids_map(self, projects_ids_map):
        """Sets the projects_ids_map of this NewProjectDescription.


        :param projects_ids_map: The projects_ids_map of this NewProjectDescription.  # noqa: E501
        :type: Properties
        """

        self._projects_ids_map = projects_ids_map

    @property
    def build_types_ids_map(self):
        """Gets the build_types_ids_map of this NewProjectDescription.  # noqa: E501


        :return: The build_types_ids_map of this NewProjectDescription.  # noqa: E501
        :rtype: Properties
        """
        return self._build_types_ids_map

    @build_types_ids_map.setter
    def build_types_ids_map(self, build_types_ids_map):
        """Sets the build_types_ids_map of this NewProjectDescription.


        :param build_types_ids_map: The build_types_ids_map of this NewProjectDescription.  # noqa: E501
        :type: Properties
        """

        self._build_types_ids_map = build_types_ids_map

    @property
    def vcs_roots_ids_map(self):
        """Gets the vcs_roots_ids_map of this NewProjectDescription.  # noqa: E501


        :return: The vcs_roots_ids_map of this NewProjectDescription.  # noqa: E501
        :rtype: Properties
        """
        return self._vcs_roots_ids_map

    @vcs_roots_ids_map.setter
    def vcs_roots_ids_map(self, vcs_roots_ids_map):
        """Sets the vcs_roots_ids_map of this NewProjectDescription.


        :param vcs_roots_ids_map: The vcs_roots_ids_map of this NewProjectDescription.  # noqa: E501
        :type: Properties
        """

        self._vcs_roots_ids_map = vcs_roots_ids_map

    @property
    def name(self):
        """Gets the name of this NewProjectDescription.  # noqa: E501


        :return: The name of this NewProjectDescription.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewProjectDescription.


        :param name: The name of this NewProjectDescription.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this NewProjectDescription.  # noqa: E501


        :return: The id of this NewProjectDescription.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NewProjectDescription.


        :param id: The id of this NewProjectDescription.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def source_project_locator(self):
        """Gets the source_project_locator of this NewProjectDescription.  # noqa: E501


        :return: The source_project_locator of this NewProjectDescription.  # noqa: E501
        :rtype: str
        """
        return self._source_project_locator

    @source_project_locator.setter
    def source_project_locator(self, source_project_locator):
        """Sets the source_project_locator of this NewProjectDescription.


        :param source_project_locator: The source_project_locator of this NewProjectDescription.  # noqa: E501
        :type: str
        """

        self._source_project_locator = source_project_locator

    @property
    def source_project(self):
        """Gets the source_project of this NewProjectDescription.  # noqa: E501


        :return: The source_project of this NewProjectDescription.  # noqa: E501
        :rtype: Project
        """
        return self._source_project

    @source_project.setter
    def source_project(self, source_project):
        """Sets the source_project of this NewProjectDescription.


        :param source_project: The source_project of this NewProjectDescription.  # noqa: E501
        :type: Project
        """

        self._source_project = source_project

    @property
    def parent_project(self):
        """Gets the parent_project of this NewProjectDescription.  # noqa: E501


        :return: The parent_project of this NewProjectDescription.  # noqa: E501
        :rtype: Project
        """
        return self._parent_project

    @parent_project.setter
    def parent_project(self, parent_project):
        """Sets the parent_project of this NewProjectDescription.


        :param parent_project: The parent_project of this NewProjectDescription.  # noqa: E501
        :type: Project
        """

        self._parent_project = parent_project
