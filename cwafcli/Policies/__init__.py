from cwafcli.Policies.policy import Policy, AssetAssociation


def policy_parse(subparsers):
    policy_parser = subparsers.add_parser('policy', help='Create and manage policies for your account using the API.',
        usage='incap [options] policy <command> [options]')
    policy_subparsers = policy_parser.add_subparsers(description='valid subcommands',
        help='additional help')

    policy_get_parser = policy_subparsers.add_parser('get', help='Retrieve policy details',
        usage='incap [options] policy get [options] policy_id')
    policy_get_parser.add_argument('policy_id', help='The Policy ID.')
    policy_get_parser.add_argument('--extended', default=True, help='Optional boolean to get full policy data.')
    policy_get_parser.set_defaults(func=Policy.read)

    policy_list_parser = policy_subparsers.add_parser('list', help='Retrieve all policies in account',
        usage='incap [options] policy list [options]')
    policy_list_parser.add_argument('--extended', default=True, help='Optional boolean to get full policy data.')
    policy_list_parser.set_defaults(func=Policy.list)

    policy_create_parser = policy_subparsers.add_parser('create', help='Add a new policy or copy an existing policy',
        usage='incap [options] policy create json')
    policy_create_parser.add_argument('json', help='Policy to save. The supported format JSON.')
    policy_create_parser.set_defaults(func=Policy.create)

    policy_update_parser = policy_subparsers.add_parser('update', help='Modify an existing policy (partial update)',
        usage='incap [options] policy update policy_id json')
    policy_update_parser.add_argument('policy_id', help='The Policy ID.')
    policy_update_parser.add_argument('json', help='Policy to save. The supported format JSON.')
    policy_update_parser.set_defaults(func=Policy.update)

    policy_override_parser = policy_subparsers.add_parser('override', help='Overwrite an existing policy (full update)',
        usage='incap [options] policy override policy_id json')
    policy_override_parser.add_argument('policy_id', help='The Policy ID.')
    policy_override_parser.add_argument('json', help='Policy to save. The supported format JSON.')
    policy_override_parser.set_defaults(func=Policy.override)

    policy_delete_parser = policy_subparsers.add_parser('delete', help='Delete an existing policy.',
        usage='incap [options] policy delete policy_id')
    policy_delete_parser.add_argument('policy_id', help='Numeric identifier of the site to operate on.')
    policy_delete_parser.set_defaults(func=Policy.delete)

    list_assets_parser = policy_subparsers.add_parser('list-assets',
        help='Retrieve assets to which policy is applied',
        usage='incap [options] policy list-assets policy_id')
    list_assets_parser.add_argument('policy_id', help='The Policy ID.')
    list_assets_parser.set_defaults(func=AssetAssociation.read)

    list_policies_parser = policy_subparsers.add_parser('list-policies', help='Retrieve all policies applied to an asset',
        usage='incap [options] policy list-policies asset_id asset_type [options]')
    list_policies_parser.add_argument('asset_id', help='The Asset ID.')
    list_policies_parser.add_argument('asset_type', help='The Asset Type.')
    list_policies_parser.add_argument('--extended', default=True, help='Optional boolean to get full policy data.')
    list_policies_parser.set_defaults(func=AssetAssociation.list)

    associate_policy_parser = policy_subparsers.add_parser('associate', help='Apply a single policy to a single asset',
        usage='incap [options] policy associate asset_id asset_type policy_id')
    associate_policy_parser.add_argument('asset_id', help='The Asset ID.')
    associate_policy_parser.add_argument('asset_type', help='The Asset Type.')
    associate_policy_parser.add_argument('policy_id', help='Numeric identifier of the site to operate on.')
    associate_policy_parser.set_defaults(func=AssetAssociation.create)

    update_associate_policy_parser = policy_subparsers.add_parser(
        'overwrite-association', help='Applies a single policy to a single asset and removes previously assigned policies.',
        usage='incap [options] policy overwrite-association asset_id asset_type policy_id')
    update_associate_policy_parser.add_argument('asset_id', help='The Asset ID.')
    update_associate_policy_parser.add_argument('asset_type', help='The Asset Type.')
    update_associate_policy_parser.add_argument('policy_id', help='Numeric identifier of the site to operate on.')
    update_associate_policy_parser.set_defaults(func=AssetAssociation.override)

    delete_associate_policy_parser = policy_subparsers.add_parser('remove', help='Remove policy from asset.',
        usage='incap [options] policy delete policy_id')
    delete_associate_policy_parser.add_argument('asset_id', help='The Asset ID.')
    delete_associate_policy_parser.add_argument('asset_type', help='The Asset Type.')
    delete_associate_policy_parser.add_argument('policy_id', help='Numeric identifier of the site to operate on.')
    delete_associate_policy_parser.set_defaults(func=AssetAssociation.delete)
