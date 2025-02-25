dohq_teamcity.VcsRootApi
######################################

.. note::

   + All ``serve_*`` method have aliases with get: ``serve_something`` == ``get_something``
   + Some API have ``get`` method - default method to get object by locator (e.g ``agent_api.get('id:123')`` return ``Agent`` model by id
   + See more examples on page :doc:`/examples/api/VcsRootApi` and model examples
   + This is autogenerated page, don't change them directly, use template. Read more in :doc:`/development`

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - :ref:`add_vcs_root`
     - **POST** ``/app/rest/vcs-roots``
   * - :ref:`delete_all_vcs_root_properties`
     - **DELETE** ``/app/rest/vcs-roots/{vcsRootLocator}/properties``
   * - :ref:`delete_vcs_root`
     - **DELETE** ``/app/rest/vcs-roots/{vcsRootLocator}``
   * - :ref:`delete_vcs_root_property`
     - **DELETE** ``/app/rest/vcs-roots/{vcsRootLocator}/properties/{name}``
   * - :ref:`get_all_vcs_root_properties`
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}/properties``
   * - :ref:`get_all_vcs_roots`
     - **GET** ``/app/rest/vcs-roots``
   * - :ref:`get_root_endpoints`
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}``
   * - :ref:`get_vcs_root_field`
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}/{field}``
   * - :ref:`get_vcs_root_instances`
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}/instances``
   * - :ref:`get_vcs_root_property`
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}/properties/{name}``
   * - :ref:`get_vcs_root_settings_file`
     - **GET** ``/app/rest/vcs-roots/{vcsRootLocator}/settingsFile``
   * - :ref:`set_vcs_root_field`
     - **PUT** ``/app/rest/vcs-roots/{vcsRootLocator}/{field}``
   * - :ref:`set_vcs_root_properties`
     - **PUT** ``/app/rest/vcs-roots/{vcsRootLocator}/properties``
   * - :ref:`set_vcs_root_property`
     - **PUT** ``/app/rest/vcs-roots/{vcsRootLocator}/properties/{name}``

.. _add_vcs_root:

add_vcs_root
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    body = dohq_teamcity.VcsRoot() # VcsRoot |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        # Add a new VCS root.
        api_response = tc.vcs_root_api.add_vcs_root(body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->add_vcs_root: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **body**
     - `VcsRoot <../models/VcsRoot.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `VcsRoot <../models/VcsRoot.html>`_

`Back to top <#>`_

.. _delete_all_vcs_root_properties:

delete_all_vcs_root_properties
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    vcs_root_locator = 'vcs_root_locator_example' # str | 

    try:
        # Delete all properties of the matching VCS root.
        tc.vcs_root_api.delete_all_vcs_root_properties(vcs_root_locator)
    except ApiException as e:
        print("Exception when calling VcsRootApi->delete_all_vcs_root_properties: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _delete_vcs_root:

delete_vcs_root
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    vcs_root_locator = 'vcs_root_locator_example' # str | 

    try:
        # Remove VCS root matching the locator.
        tc.vcs_root_api.delete_vcs_root(vcs_root_locator)
    except ApiException as e:
        print("Exception when calling VcsRootApi->delete_vcs_root: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _delete_vcs_root_property:

delete_vcs_root_property
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    vcs_root_locator = 'vcs_root_locator_example' # str | 
    name = 'name_example' # str | 

    try:
        # Delete a property of the matching VCS root.
        tc.vcs_root_api.delete_vcs_root_property(vcs_root_locator, name)
    except ApiException as e:
        print("Exception when calling VcsRootApi->delete_vcs_root_property: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _get_all_vcs_root_properties:

get_all_vcs_root_properties
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    vcs_root_locator = 'vcs_root_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        # Get all properties of the matching VCS root.
        api_response = tc.vcs_root_api.get_all_vcs_root_properties(vcs_root_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->get_all_vcs_root_properties: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_

`Back to top <#>`_

.. _get_all_vcs_roots:

get_all_vcs_roots
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        # Get all VCS roots.
        api_response = tc.vcs_root_api.get_all_vcs_roots(locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->get_all_vcs_roots: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `VcsRoots <../models/VcsRoots.html>`_

`Back to top <#>`_

.. _get_root_endpoints:

get_root_endpoints
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    vcs_root_locator = 'vcs_root_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        # Get root endpoints.
        api_response = tc.vcs_root_api.get_root_endpoints(vcs_root_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->get_root_endpoints: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `VcsRoot <../models/VcsRoot.html>`_

`Back to top <#>`_

.. _get_vcs_root_field:

get_vcs_root_field
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    vcs_root_locator = 'vcs_root_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        # Get a field of the matching VCS root.
        api_response = tc.vcs_root_api.get_vcs_root_field(vcs_root_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->get_vcs_root_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    **str**

`Back to top <#>`_

.. _get_vcs_root_instances:

get_vcs_root_instances
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    vcs_root_locator = 'vcs_root_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        # Get all VCS root instances of the matching VCS root.
        api_response = tc.vcs_root_api.get_vcs_root_instances(vcs_root_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->get_vcs_root_instances: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `VcsRootInstances <../models/VcsRootInstances.html>`_

`Back to top <#>`_

.. _get_vcs_root_property:

get_vcs_root_property
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    vcs_root_locator = 'vcs_root_locator_example' # str | 
    name = 'name_example' # str | 

    try:
        # Get a property on the matching VCS root.
        api_response = tc.vcs_root_api.get_vcs_root_property(vcs_root_locator, name)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->get_vcs_root_property: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 

Return type:
    **str**

`Back to top <#>`_

.. _get_vcs_root_settings_file:

get_vcs_root_settings_file
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    vcs_root_locator = 'vcs_root_locator_example' # str | 

    try:
        # Get the settings file of the matching VCS root.
        api_response = tc.vcs_root_api.get_vcs_root_settings_file(vcs_root_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->get_vcs_root_settings_file: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 

Return type:
    **str**

`Back to top <#>`_

.. _set_vcs_root_field:

set_vcs_root_field
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    vcs_root_locator = 'vcs_root_locator_example' # str | 
    field = 'field_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update a field of the matching VCS root.
        api_response = tc.vcs_root_api.set_vcs_root_field(vcs_root_locator, field, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->set_vcs_root_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

`Back to top <#>`_

.. _set_vcs_root_properties:

set_vcs_root_properties
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    vcs_root_locator = 'vcs_root_locator_example' # str | 
    body = dohq_teamcity.Properties() # Properties |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        # Update all properties of the matching VCS root.
        api_response = tc.vcs_root_api.set_vcs_root_properties(vcs_root_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->set_vcs_root_properties: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **body**
     - `Properties <../models/Properties.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_

`Back to top <#>`_

.. _set_vcs_root_property:

set_vcs_root_property
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    vcs_root_locator = 'vcs_root_locator_example' # str | 
    name = 'name_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update a property of the matching VCS root.
        api_response = tc.vcs_root_api.set_vcs_root_property(vcs_root_locator, name, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling VcsRootApi->set_vcs_root_property: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **vcs_root_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 
   * - **body**
     - **str**
     - [optional] 

Return type:
    **str**

`Back to top <#>`_

