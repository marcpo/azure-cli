# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from azure.cli.core.commands import CliCommandType

from azure.cli.command_modules.cosmosdb._client_factory import cf_db_accounts

from azure.cli.command_modules.cosmosdb._format import (
    database_output,
    list_database_output,
    collection_output,
    list_collection_output,
    list_connection_strings_output
)


def load_command_table(self, _):

    cosmosdb_sdk = CliCommandType(
        operations_tmpl='azure.mgmt.cosmosdb.operations#DatabaseAccountsOperations.{}',
        client_factory=cf_db_accounts)

    cosmosdb_custom_sdk = CliCommandType(
        operations_tmpl='azure.cli.command_modules.cosmosdb.custom#{}',
        client_factory=cf_db_accounts
    )

    with self.command_group('cosmosdb', cosmosdb_sdk, client_factory=cf_db_accounts) as g:
        g.show_command('show', 'get')
        g.command('list-keys', 'list_keys', deprecate_info=g.deprecate(redirect='cosmosdb keys list', hide=True))
        g.command('list-read-only-keys', 'list_read_only_keys')
        g.command('list-connection-strings', 'list_connection_strings', table_transformer=list_connection_strings_output)
        g.command('regenerate-key', 'regenerate_key')
        g.command('check-name-exists', 'check_name_exists')
        g.command('delete', 'delete')
        g.command('failover-priority-change', 'failover_priority_change')
        g.custom_command('create', 'cli_cosmosdb_create')
        g.custom_command('update', 'cli_cosmosdb_update')
        g.custom_command('list', 'cli_cosmosdb_list')

    # virtual network rules
    with self.command_group('cosmosdb network-rule', cosmosdb_custom_sdk, client_factory=cf_db_accounts) as g:
        g.custom_command('list', 'cli_cosmosdb_network_rule_list')
        g.custom_command('add', 'cli_cosmosdb_network_rule_add')
        g.custom_command('remove', 'cli_cosmosdb_network_rule_remove')

    # key operations
    with self.command_group('cosmosdb keys', cosmosdb_sdk) as g:
        g.command('list', 'list_keys')

    # # database operations
    with self.command_group('cosmosdb database') as g:
        g.cosmosdb_custom('show', 'cli_cosmosdb_database_show', table_transformer=database_output)
        g.cosmosdb_custom('list', 'cli_cosmosdb_database_list', table_transformer=list_database_output)
        g.cosmosdb_custom('exists', 'cli_cosmosdb_database_exists')
        g.cosmosdb_custom('create', 'cli_cosmosdb_database_create', table_transformer=database_output)
        g.cosmosdb_custom('delete', 'cli_cosmosdb_database_delete')

    # collection operations
    with self.command_group('cosmosdb collection') as g:
        g.cosmosdb_custom('show', 'cli_cosmosdb_collection_show', table_transformer=collection_output)
        g.cosmosdb_custom('list', 'cli_cosmosdb_collection_list', table_transformer=list_collection_output)
        g.cosmosdb_custom('exists', 'cli_cosmosdb_collection_exists')
        g.cosmosdb_custom('create', 'cli_cosmosdb_collection_create', table_transformer=collection_output)
        g.cosmosdb_custom('delete', 'cli_cosmosdb_collection_delete')
        g.cosmosdb_custom('update', 'cli_cosmosdb_collection_update')
