from cwafcli.Roles.role import Role, Assignment, Abilities, User


def role_parse(subparsers):
    role_parser = subparsers.add_parser('role', help='Create and manage roles for your account using the API.',
        usage='incap [options] role <command> [options]')
    role_subparsers = role_parser.add_subparsers(description='valid subcommands',
        help='additional help')
    role_get_parser = role_subparsers.add_parser('get', help='Get Role Details By Account ID, User Email, or Role Name',
        usage='incap [options] role get [options] role_id')
    role_get_parser.add_argument('role_id', help='The role ID of the required role.')
    role_get_parser.set_defaults(func=Role.read)

    role_list_parser = role_subparsers.add_parser('list', help='Retrieve all policies in account',
        usage='incap [options] role list [options]')
    role_list_parser.add_argument('account_id', help='The role ID of the required role.')
    role_list_parser.add_argument('--email', dest="userEmail", default='', help='The email of the required user.')
    role_list_parser.add_argument('--role', dest="roleName", default='', help='The name of the required role.')
    role_list_parser.set_defaults(func=Role.list)

    role_create_parser = role_subparsers.add_parser('create', help='Add a new role or copy an existing role',
        usage='incap [options] role create json')
    role_create_parser.add_argument('json', help='role to save. The supported format JSON.')
    role_create_parser.set_defaults(func=Role.create)

    role_update_parser = role_subparsers.add_parser('update', help='Modify an existing role (partial update)',
        usage='incap [options] role update role_id json')
    role_update_parser.add_argument('role_id', help='The role ID.')
    role_update_parser.add_argument('json', help='role to save. The supported format JSON.')
    role_update_parser.set_defaults(func=Role.update)

    role_delete_parser = role_subparsers.add_parser('delete', help='Delete an existing role.',
        usage='incap [options] role delete role_id')
    role_delete_parser.add_argument('role_id', help='Numeric identifier of the site to operate on.')
    role_delete_parser.set_defaults(func=Role.delete)

    assignment_get_parser = role_subparsers.add_parser('get-assignment',
        help='Get role assignments By User Email And Account ID',
        usage='incap [options] role get-assignment email account_id')
    assignment_get_parser.add_argument('userEmail', help='The email of the required user')
    assignment_get_parser.add_argument('account_id', help='Unique ID of the required account.')
    assignment_get_parser.set_defaults(func=Assignment.read)

    assignment_create_parser = role_subparsers.add_parser('create-assignment',
        help='Assign Users To Roles or Delete Existing Assignment',
        usage='incap [options] role get-assignment email account_id')
    assignment_create_parser.add_argument('json', help='The details required for the new assignments.')
    assignment_create_parser.set_defaults(func=Assignment.create)

    user_create_parser = role_subparsers.add_parser('create-user', help='Create new user.',
        usage='incap [options] role create json')
    user_create_parser.add_argument('json', help='The details required to create new user.')
    user_create_parser.set_defaults(func=User.create)

    user_get_parser = role_subparsers.add_parser('get-user',
        help='Get role assignments By User Email And Account ID',
        usage='incap [options] role get-user email account_id')
    user_get_parser.add_argument('userEmail', help='The email of the required user.')
    user_get_parser.add_argument('account_id', help='Unique ID of the required account.')
    user_get_parser.set_defaults(func=User.read)

    user_delete_parser = role_subparsers.add_parser('delete-user', help='Delete User Details By User Email.',
        usage='incap [options] role delete-user email account_id')
    user_delete_parser.add_argument('userEmail', help='The email of the required user.')
    user_delete_parser.add_argument('account_id', help='Unique ID of the required account.')
    user_delete_parser.set_defaults(func=User.delete)

    ability_get_parser = role_subparsers.add_parser('get-abilities', help='Get ole management APIs for abilities '
                                                                          'management',
        usage='incap role get-abilities account_id')
    ability_get_parser.add_argument('account_id', help='Unique ID of the required account.')
    ability_get_parser.set_defaults(func=Abilities.read)
