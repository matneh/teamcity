# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.users import Users  # noqa: F401,E501


class Commiter(TeamCityObject):
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
        'vcs_username': 'str',
        'users': 'Users'
    }

    attribute_map = {
        'vcs_username': 'vcsUsername',
        'users': 'users'
    }

    def __init__(self, vcs_username=None, users=None, teamcity=None):  # noqa: E501
        """Commiter - a model defined in Swagger"""  # noqa: E501

        self._vcs_username = None
        self._users = None
        self.discriminator = None

        if vcs_username is not None:
            self.vcs_username = vcs_username
        if users is not None:
            self.users = users
        super(Commiter, self).__init__(teamcity=teamcity)

    @property
    def vcs_username(self):
        """Gets the vcs_username of this Commiter.  # noqa: E501


        :return: The vcs_username of this Commiter.  # noqa: E501
        :rtype: str
        """
        return self._vcs_username

    @vcs_username.setter
    def vcs_username(self, vcs_username):
        """Sets the vcs_username of this Commiter.


        :param vcs_username: The vcs_username of this Commiter.  # noqa: E501
        :type: str
        """

        self._vcs_username = vcs_username

    @property
    def users(self):
        """Gets the users of this Commiter.  # noqa: E501


        :return: The users of this Commiter.  # noqa: E501
        :rtype: Users
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this Commiter.


        :param users: The users of this Commiter.  # noqa: E501
        :type: Users
        """

        self._users = users
