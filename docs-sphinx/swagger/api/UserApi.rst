dohq_teamcity.UserApi
######################################

.. note::

   + All ``serve_*`` method have aliases with get: ``serve_something`` == ``get_something``
   + Some API have ``get`` method - default method to get object by locator (e.g ``agent_api.get('id:123')`` return ``Agent`` model by id
   + See more examples on page :doc:`/examples/api/UserApi` and model examples
   + This is autogenerated page, don't change them directly, use template. Read more in :doc:`/development`

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Method
     - HTTP request
   * - :ref:`add_role_to_user`
     - **POST** ``/app/rest/users/{userLocator}/roles``
   * - :ref:`add_role_to_user_at_scope`
     - **PUT** ``/app/rest/users/{userLocator}/roles/{roleId}/{scope}``
   * - :ref:`add_user`
     - **POST** ``/app/rest/users``
   * - :ref:`add_user_token`
     - **POST** ``/app/rest/users/{userLocator}/tokens``
   * - :ref:`delete_user`
     - **DELETE** ``/app/rest/users/{userLocator}``
   * - :ref:`delete_user_field`
     - **DELETE** ``/app/rest/users/{userLocator}/{field}``
   * - :ref:`delete_user_token`
     - **DELETE** ``/app/rest/users/{userLocator}/tokens/{name}``
   * - :ref:`get_all_user_groups`
     - **GET** ``/app/rest/users/{userLocator}/groups``
   * - :ref:`get_all_user_roles`
     - **GET** ``/app/rest/users/{userLocator}/roles``
   * - :ref:`get_all_users`
     - **GET** ``/app/rest/users``
   * - :ref:`get_user`
     - **GET** ``/app/rest/users/{userLocator}``
   * - :ref:`get_user_field`
     - **GET** ``/app/rest/users/{userLocator}/{field}``
   * - :ref:`get_user_group`
     - **GET** ``/app/rest/users/{userLocator}/groups/{groupLocator}``
   * - :ref:`get_user_permissions`
     - **GET** ``/app/rest/users/{userLocator}/permissions``
   * - :ref:`get_user_properties`
     - **GET** ``/app/rest/users/{userLocator}/properties``
   * - :ref:`get_user_property`
     - **GET** ``/app/rest/users/{userLocator}/properties/{name}``
   * - :ref:`get_user_roles_at_scope`
     - **GET** ``/app/rest/users/{userLocator}/roles/{roleId}/{scope}``
   * - :ref:`get_user_tokens`
     - **GET** ``/app/rest/users/{userLocator}/tokens``
   * - :ref:`remove_user_from_group`
     - **DELETE** ``/app/rest/users/{userLocator}/groups/{groupLocator}``
   * - :ref:`remove_user_property`
     - **DELETE** ``/app/rest/users/{userLocator}/properties/{name}``
   * - :ref:`remove_user_remember_me`
     - **DELETE** ``/app/rest/users/{userLocator}/debug/rememberMe``
   * - :ref:`remove_user_role_at_scope`
     - **DELETE** ``/app/rest/users/{userLocator}/roles/{roleId}/{scope}``
   * - :ref:`replace_user`
     - **PUT** ``/app/rest/users/{userLocator}``
   * - :ref:`set_user_field`
     - **PUT** ``/app/rest/users/{userLocator}/{field}``
   * - :ref:`set_user_groups`
     - **PUT** ``/app/rest/users/{userLocator}/groups``
   * - :ref:`set_user_property`
     - **PUT** ``/app/rest/users/{userLocator}/properties/{name}``
   * - :ref:`set_user_roles`
     - **PUT** ``/app/rest/users/{userLocator}/roles``

.. _add_role_to_user:

add_role_to_user
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    body = dohq_teamcity.Role() # Role |  (optional)

    try:
        # Add a role to the matching user.
        api_response = tc.user_api.add_role_to_user(user_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->add_role_to_user: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **body**
     - `Role <../models/Role.html>`_
     - [optional] 

Return type:
    `Role <../models/Role.html>`_

`Back to top <#>`_

.. _add_role_to_user_at_scope:

add_role_to_user_at_scope
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    role_id = 'role_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        # Add a role with the specific scope to the matching user.
        api_response = tc.user_api.add_role_to_user_at_scope(user_locator, role_id, scope)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->add_role_to_user_at_scope: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **role_id**
     - **str**
     - 
   * - **scope**
     - **str**
     - 

Return type:
    `Role <../models/Role.html>`_

`Back to top <#>`_

.. _add_user:

add_user
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    body = dohq_teamcity.User() # User |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        # Create a new user.
        api_response = tc.user_api.add_user(body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->add_user: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **body**
     - `User <../models/User.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `User <../models/User.html>`_

`Back to top <#>`_

.. _add_user_token:

add_user_token
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    body = dohq_teamcity.Token() # Token |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        # Create a new authentication token for the matching user.
        api_response = tc.user_api.add_user_token(user_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->add_user_token: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **body**
     - `Token <../models/Token.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Token <../models/Token.html>`_

`Back to top <#>`_

.. _delete_user:

delete_user
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 

    try:
        # Delete user matching the locator.
        tc.user_api.delete_user(user_locator)
    except ApiException as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _delete_user_field:

delete_user_field
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        # Remove a property of the matching user.
        tc.user_api.delete_user_field(user_locator, field)
    except ApiException as e:
        print("Exception when calling UserApi->delete_user_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _delete_user_token:

delete_user_token
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    name = 'name_example' # str | 

    try:
        # Remove an authentication token from the matching user.
        tc.user_api.delete_user_token(user_locator, name)
    except ApiException as e:
        print("Exception when calling UserApi->delete_user_token: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _get_all_user_groups:

get_all_user_groups
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        # Get all groups of the matching user.
        api_response = tc.user_api.get_all_user_groups(user_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_all_user_groups: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Groups <../models/Groups.html>`_

`Back to top <#>`_

.. _get_all_user_roles:

get_all_user_roles
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 

    try:
        # Get all user roles of the matching user.
        api_response = tc.user_api.get_all_user_roles(user_locator)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_all_user_roles: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 

Return type:
    `Roles <../models/Roles.html>`_

`Back to top <#>`_

.. _get_all_users:

get_all_users
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        # Get all users.
        api_response = tc.user_api.get_all_users(locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_all_users: %s\n" % e)



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
    `Users <../models/Users.html>`_

`Back to top <#>`_

.. _get_user:

get_user
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        # Get user matching the locator.
        api_response = tc.user_api.get_user(user_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `User <../models/User.html>`_

`Back to top <#>`_

.. _get_user_field:

get_user_field
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    field = 'field_example' # str | 

    try:
        # Get a field of the matching user.
        api_response = tc.user_api.get_user_field(user_locator, field)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **field**
     - **str**
     - 

Return type:
    **str**

`Back to top <#>`_

.. _get_user_group:

get_user_group
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    group_locator = 'group_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        # Get a user group of the matching user.
        api_response = tc.user_api.get_user_group(user_locator, group_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user_group: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **group_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Group <../models/Group.html>`_

`Back to top <#>`_

.. _get_user_permissions:

get_user_permissions
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    locator = 'locator_example' # str |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        # Get all permissions effective for the matching user.
        api_response = tc.user_api.get_user_permissions(user_locator, locator=locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user_permissions: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **locator**
     - **str**
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `PermissionAssignments <../models/PermissionAssignments.html>`_

`Back to top <#>`_

.. _get_user_properties:

get_user_properties
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        # Get all properties of the matching user.
        api_response = tc.user_api.get_user_properties(user_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user_properties: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Properties <../models/Properties.html>`_

`Back to top <#>`_

.. _get_user_property:

get_user_property
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    name = 'name_example' # str | 

    try:
        # Get a property of the matching user.
        api_response = tc.user_api.get_user_property(user_locator, name)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user_property: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 

Return type:
    **str**

`Back to top <#>`_

.. _get_user_roles_at_scope:

get_user_roles_at_scope
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    role_id = 'role_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        # Get a user role with the specific scope from the matching user.
        api_response = tc.user_api.get_user_roles_at_scope(user_locator, role_id, scope)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user_roles_at_scope: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **role_id**
     - **str**
     - 
   * - **scope**
     - **str**
     - 

Return type:
    `Role <../models/Role.html>`_

`Back to top <#>`_

.. _get_user_tokens:

get_user_tokens
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        # Get all authentication tokens of the matching user.
        api_response = tc.user_api.get_user_tokens(user_locator, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->get_user_tokens: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Tokens <../models/Tokens.html>`_

`Back to top <#>`_

.. _remove_user_from_group:

remove_user_from_group
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    group_locator = 'group_locator_example' # str | 
    fields = 'fields_example' # str |  (optional)

    try:
        # Remove the matching user from the specific group.
        tc.user_api.remove_user_from_group(user_locator, group_locator, fields=fields)
    except ApiException as e:
        print("Exception when calling UserApi->remove_user_from_group: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **group_locator**
     - **str**
     - 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _remove_user_property:

remove_user_property
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    name = 'name_example' # str | 

    try:
        # Remove a property of the matching user.
        tc.user_api.remove_user_property(user_locator, name)
    except ApiException as e:
        print("Exception when calling UserApi->remove_user_property: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **name**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _remove_user_remember_me:

remove_user_remember_me
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 

    try:
        # Remove the RememberMe data of the matching user.
        tc.user_api.remove_user_remember_me(user_locator)
    except ApiException as e:
        print("Exception when calling UserApi->remove_user_remember_me: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _remove_user_role_at_scope:

remove_user_role_at_scope
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    role_id = 'role_id_example' # str | 
    scope = 'scope_example' # str | 

    try:
        # Remove a role with the specific scope from the matching user.
        tc.user_api.remove_user_role_at_scope(user_locator, role_id, scope)
    except ApiException as e:
        print("Exception when calling UserApi->remove_user_role_at_scope: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **role_id**
     - **str**
     - 
   * - **scope**
     - **str**
     - 

Return type:
    void (empty response body)

`Back to top <#>`_

.. _replace_user:

replace_user
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    body = dohq_teamcity.User() # User |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        # Update user matching the locator.
        api_response = tc.user_api.replace_user(user_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->replace_user: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **body**
     - `User <../models/User.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `User <../models/User.html>`_

`Back to top <#>`_

.. _set_user_field:

set_user_field
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    field = 'field_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update a field of the matching user.
        api_response = tc.user_api.set_user_field(user_locator, field, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->set_user_field: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
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

.. _set_user_groups:

set_user_groups
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    body = dohq_teamcity.Groups() # Groups |  (optional)
    fields = 'fields_example' # str |  (optional)

    try:
        # Update groups of the matching user.
        api_response = tc.user_api.set_user_groups(user_locator, body=body, fields=fields)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->set_user_groups: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **body**
     - `Groups <../models/Groups.html>`_
     - [optional] 
   * - **fields**
     - **str**
     - [optional] 

Return type:
    `Groups <../models/Groups.html>`_

`Back to top <#>`_

.. _set_user_property:

set_user_property
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    name = 'name_example' # str | 
    body = 'body_example' # str |  (optional)

    try:
        # Update a property of the matching user.
        api_response = tc.user_api.set_user_property(user_locator, name, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->set_user_property: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
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

.. _set_user_roles:

set_user_roles
-----------------

.. code-block:: python

    from pprint import pprint
    from dohq_teamcity import TeamCity, ApiException

    # username/password authentication
    tc = TeamCity("https://teamcity.example.com", auth=('username', 'password'))

    user_locator = 'user_locator_example' # str | 
    body = dohq_teamcity.Roles() # Roles |  (optional)

    try:
        # Update user roles of the matching user.
        api_response = tc.user_api.set_user_roles(user_locator, body=body)
       pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserApi->set_user_roles: %s\n" % e)



.. list-table::
   :widths: 20 20 60
   :header-rows: 1

   * - Name
     - Types
     - Notes

   * - **user_locator**
     - **str**
     - 
   * - **body**
     - `Roles <../models/Roles.html>`_
     - [optional] 

Return type:
    `Roles <../models/Roles.html>`_

`Back to top <#>`_

