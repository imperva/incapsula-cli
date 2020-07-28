# New PyPI package to make the cli a distributable module through pip3.
With this release a user will now be able to install and use the cli with pip command:
## Installation
    pip3 install cwaf-cli
# cwaf-cli
This application provides a simple to use CLI that reflects industry standards (such as the AWS cli), and enables customers to easily integrate into configurations management, orchestration or automation frameworks to support the DevOps model

## Running the CLI

This CLI is a Python 3 application and has been tested with Python 3.6 -> 3.8
## Requirements:
    python 3.6 or higher

## Confirm your version of python if installed:
    Open a terminal
    Enter: python -V or python3 -V

## If your version of python is higher than 3.5 then test the incap app with the following:
      python <path>/incap.py -h

    usage: incap <resource> <command> [options]

    CLI for site, account and security CRUD on Incapsula via API.

    positional arguments:
      {config,site,account}
        config              Use config to add the default API_ID, API_KEY and
                            Account_ID.
        site                Used to add, delete and configure Incapsula sites.
        account             Used to add, delete and configure Incapsula accounts.

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit

## Installing the correct version for environment:
https://www.python.org/downloads/


## Examples:
    incap --help
    incap site --help
    incap site acl --help
    incap site add www.imperva.com
    incap site list_incaprule 123456
    
## Adding your configuration info locally for easy use
#####Basic:
    incap api_id api_key account_id
#####Advanced:
    incap config --profile=special_name --repo=/Users/<username>/your_repo_location --baseurl=https://my.imperva.com 26012 ejf903rie-3983030ie23r2r39j0 2398
View the config with - *cat ~/.incap/config*

## Using environment variables
    Set environment for the following:
    IMPV_API_ID
    IMPV_API_KEY
    IMPV_ACCOUNT_ID
    IMPV_BASEURL
    IMPV_REPO (optional for exporting cwaf site configurations as JSON locally)
    
#### *With three options to apply creds/configs there is a hierarchy that applies and as follows:*
    cmd line args
    Environment variables
    config.ini
    
## Add a site
    incap site add www.imperva.com

## Check a site's status
    incap site status 123456

## Delete a site
    incap site delete 123456

## List all incap_rules
    incap site list_incaprule 123456

## Add an IncapRule to a site
    incap site add_incaprule --name="Testing block crawlers" --action=RULE_ACTION_ALERT --filter="ClientType == Crawler" 123456

## Update IncapRule on a site
    incap site edit_incaprule --name="BA HTTP" --filter='(Method == POST;PUT)' --action=RULE_ACTION_ALERT 123456

## Delete an IncapRule from a site
    incap site del_incaprule 123456

## Update security rule action to block IP for SQL Injection
    incap site security  --security_rule_action=block_ip sql_injection 123456

## Add blacklisted IPs for a site
    incap site acl --ips=107.232.12.4,102.232.22.99 blacklisted_ips 123456

## Add whitelist exceptions to XSS Rule
    incap site whitelist  --urls='/home,/example'  --countries='JM,CA' --continents='AF' --ips='192.168.1.1,172.21.12.0/24' --client_app_types='Browser' --client_apps='68'  --user_agents='curl' cross_site_scripting 123456

## Add never cache resource rule
    incap site cache-rule --never_cache_resource_url=/help,login --never_cache_resource_pattern=prefix,contains 123456

## Get cache mode
    incap site get-cache-mode 123456

## Edit cache mode
    incap site edit-cache-mode --aggressive_cache_duration=5_hr --dynamic_cache_duration=5_days static_and_dynamic 123456

## Set advanced cache async validation to true
    incap site advanced-cache {param} {value} 123456
    incap site advanced-cache async_validation true 123456

## Backup full config, includes incapRules and ADRules
    incap site export –-path=/Users/<name>/backups --filename={site_id}_{domain}
    incap site export –-path=/Users/<name>/backups --filename={domain}_{site_id}
    incap site export –-path=/Users/<name>/backups --filename={site_id}_{date}
    incap site export –-path=/Users/<name>/backups --filename={domain}_{date}
    incap site export –-path=/Users/<name>/backups --filename={site_id}
    incap site export –-path=/Users/<name>/backups --filename={domain}
    incap site export –-path=/Users/<name>/backups --filename={site_id}_{domain}_REV3_1B

 ###### *Back up a single site with --site_id param.*
    incap site export –-site_id=123456

*Path in the backup is option and will use the repo path in the config file or environment variable.*

## Restore site config
    incap site restore --domain=www.example.com /Users/<name>/backups/www.template.com.json

## Upload certificate to site
    incap site upcert --private_key="/<cert_location>/mooreassistance_net_apache-selfsigned.key" "/<cert_location>/www_mooreassistance_net_apache-selfsigned.crt" --passphrase=password SITE_ID

## Delete certificate from site
    incap site delcert 123456
    
## Use this operation to add a data center to a site.
    incap site add-dc name server_address site_id
    
## Use this operation to list a site's data centers including the data centers' servers.
    incap site list-dc site_id
    
## Use this operation to edit a site's data center.
    incap site edit-dc dc_id name
    
## Use this operation to delete a site's data center.
    incap site del-dc dc_id
    
## Use this operation to add a server to a data center.
    incap site add-server server_address dc_id
    
## Use this operation to edit a server in a data center.
    incap site edit-server server_id
    
## Use this operation to delete a server in a data center.
    incap site del-server server_id
    
# Unit Testing
    python3 -m unittest test_incap_cli.py