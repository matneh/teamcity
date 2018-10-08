# coding: utf-8

from teamcity.custom.model import TeamcityObject


# from teamcity.models.license_key import LicenseKey  # noqa: F401,E501


class LicenseKeys(TeamcityObject):
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
        'href': 'str',
        'license_key': 'list[LicenseKey]'
    }

    attribute_map = {
        'count': 'count',
        'href': 'href',
        'license_key': 'licenseKey'
    }

    def __init__(self, count=None, href=None, license_key=None):  # noqa: E501
        """LicenseKeys - a model defined in Swagger"""  # noqa: E501
        super(LicenseKeys, self).__init__()

        self._count = None
        self._href = None
        self._license_key = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if href is not None:
            self.href = href
        if license_key is not None:
            self.license_key = license_key

    @property
    def count(self):
        """Gets the count of this LicenseKeys.  # noqa: E501


        :return: The count of this LicenseKeys.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this LicenseKeys.


        :param count: The count of this LicenseKeys.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def href(self):
        """Gets the href of this LicenseKeys.  # noqa: E501


        :return: The href of this LicenseKeys.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this LicenseKeys.


        :param href: The href of this LicenseKeys.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def license_key(self):
        """Gets the license_key of this LicenseKeys.  # noqa: E501


        :return: The license_key of this LicenseKeys.  # noqa: E501
        :rtype: list[LicenseKey]
        """
        return self._license_key

    @license_key.setter
    def license_key(self, license_key):
        """Sets the license_key of this LicenseKeys.


        :param license_key: The license_key of this LicenseKeys.  # noqa: E501
        :type: list[LicenseKey]
        """

        self._license_key = license_key

