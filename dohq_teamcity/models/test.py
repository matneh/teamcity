# coding: utf-8

from dohq_teamcity.custom.base_model import TeamCityObject


# from dohq_teamcity.models.investigations import Investigations  # noqa: F401,E501
# from dohq_teamcity.models.mutes import Mutes  # noqa: F401,E501
# from dohq_teamcity.models.parsed_test_name import ParsedTestName  # noqa: F401,E501
# from dohq_teamcity.models.test_occurrences import TestOccurrences  # noqa: F401,E501


class Test(TeamCityObject):
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
        'mutes': 'Mutes',
        'investigations': 'Investigations',
        'test_occurrences': 'TestOccurrences',
        'parsed_test_name': 'ParsedTestName',
        'href': 'str',
        'locator': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'mutes': 'mutes',
        'investigations': 'investigations',
        'test_occurrences': 'testOccurrences',
        'parsed_test_name': 'parsedTestName',
        'href': 'href',
        'locator': 'locator'
    }

    def __init__(self, id=None, name=None, mutes=None, investigations=None, test_occurrences=None, parsed_test_name=None, href=None, locator=None, teamcity=None):  # noqa: E501
        """Test - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._mutes = None
        self._investigations = None
        self._test_occurrences = None
        self._parsed_test_name = None
        self._href = None
        self._locator = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if mutes is not None:
            self.mutes = mutes
        if investigations is not None:
            self.investigations = investigations
        if test_occurrences is not None:
            self.test_occurrences = test_occurrences
        if parsed_test_name is not None:
            self.parsed_test_name = parsed_test_name
        if href is not None:
            self.href = href
        if locator is not None:
            self.locator = locator
        super(Test, self).__init__(teamcity=teamcity)

    @property
    def id(self):
        """Gets the id of this Test.  # noqa: E501


        :return: The id of this Test.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Test.


        :param id: The id of this Test.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Test.  # noqa: E501


        :return: The name of this Test.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Test.


        :param name: The name of this Test.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def mutes(self):
        """Gets the mutes of this Test.  # noqa: E501


        :return: The mutes of this Test.  # noqa: E501
        :rtype: Mutes
        """
        return self._mutes

    @mutes.setter
    def mutes(self, mutes):
        """Sets the mutes of this Test.


        :param mutes: The mutes of this Test.  # noqa: E501
        :type: Mutes
        """

        self._mutes = mutes

    @property
    def investigations(self):
        """Gets the investigations of this Test.  # noqa: E501


        :return: The investigations of this Test.  # noqa: E501
        :rtype: Investigations
        """
        return self._investigations

    @investigations.setter
    def investigations(self, investigations):
        """Sets the investigations of this Test.


        :param investigations: The investigations of this Test.  # noqa: E501
        :type: Investigations
        """

        self._investigations = investigations

    @property
    def test_occurrences(self):
        """Gets the test_occurrences of this Test.  # noqa: E501


        :return: The test_occurrences of this Test.  # noqa: E501
        :rtype: TestOccurrences
        """
        return self._test_occurrences

    @test_occurrences.setter
    def test_occurrences(self, test_occurrences):
        """Sets the test_occurrences of this Test.


        :param test_occurrences: The test_occurrences of this Test.  # noqa: E501
        :type: TestOccurrences
        """

        self._test_occurrences = test_occurrences

    @property
    def parsed_test_name(self):
        """Gets the parsed_test_name of this Test.  # noqa: E501


        :return: The parsed_test_name of this Test.  # noqa: E501
        :rtype: ParsedTestName
        """
        return self._parsed_test_name

    @parsed_test_name.setter
    def parsed_test_name(self, parsed_test_name):
        """Sets the parsed_test_name of this Test.


        :param parsed_test_name: The parsed_test_name of this Test.  # noqa: E501
        :type: ParsedTestName
        """

        self._parsed_test_name = parsed_test_name

    @property
    def href(self):
        """Gets the href of this Test.  # noqa: E501


        :return: The href of this Test.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Test.


        :param href: The href of this Test.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def locator(self):
        """Gets the locator of this Test.  # noqa: E501


        :return: The locator of this Test.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this Test.


        :param locator: The locator of this Test.  # noqa: E501
        :type: str
        """

        self._locator = locator
