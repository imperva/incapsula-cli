# incapsula-cli
This application provides a simple to use CLI that reflects industry standards (such as the AWS cli), and enables customers to easily integrate into configurations management, orchestration or automation frameworks to support the DevOps model

## Running the Incap CLI

This CLI is a Python 3 application and has been tested with Python 3.5 -> 3.7
## Requirements:
    python 3.5.0 or higher

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
    incap site add www.saic.com
    incap site list_incaprule 26621616
    
## Adding your configuration info locally for easy use
    incap config --profile=special_name --repo=/Users/<username>/your_repo_location --baseurl=https://my.incapsula.com 26012 ejf903rie-3983030ie23r2r39j0 2398
View the config with - *cat ~/.incap/config*

## Using environment variables
    Set environment for the following:
    IMPV_API_ID
    IMPV_API_KEY
    IMPV_ACCOUNT_ID
    IMPV_BASEURL
    IMPV_REPO (optional for export)
    
#### *With three options to apply creds/configs there is a hierarchy that applies and as follows:*
    cmd line args
    Environment variables
    config.ini
    
## Add a site
    incap site add www.saic.com

## Check a site's status
    incap site status SITE_ID

## Delete a site
    incap site delete SITE_ID

## List all incap_rules
    incap site list_incaprule SITE_ID

## Add an IncapRule to a site
    incap site add_incaprule --name="Testing block crawlers" --action=RULE_ACTION_ALERT --filter="ClientType == Crawler" SITE_ID

## Update IncapRule on a site
    incap site edit_incaprule --name="BA HTTP" --filter='(Method == POST;PUT)' --action=RULE_ACTION_ALERT RULE_ID

## Delete an IncapRule from a site
    incap site del_incaprule RULE_ID

## Update security rule action to block IP for SQL Injection
    incap site security  --security_rule_action=block_ip sql_injection SITE_ID

## Add blacklisted IPs for a site
    incap site acl --ips=107.232.12.4,102.232.22.99 blacklisted_ips SITE_ID

## Add whitelist exceptions to XSS Rule
    incap site whitelist  --urls='/home,/example'  --countries='JM,CA' --continents='AF' --ips='192.168.1.1,172.21.12.0/24' --client_app_types='Browser' --client_apps='68'  --user_agents='curl' --log=debug cross_site_scripting SITE_ID

## Add never cache resource rule
    incap site cache-rule --never_cache_resource_url=/help,login --never_cache_resource_pattern=prefix,contains SITE_ID

## Add cache durations and cache mode
    incap site cache-mode --aggressive_cache_duration=5_hr --dynamic_cache_duration=5_days static_and_dynamic SITE_ID

## Set advanced cache async validation to true
    incap site advanced-cache async_validation true SITE_ID

## Backup full config, includes incapRules and ADRules
    incap site export –-path=/Users/<name>/backups --filename={site_id}_{domain}_{date}
    incap site export –-path=/Users/<name>/backups --filename={site_id}_{date}
    incap site export –-path=/Users/<name>/backups --filename={domain}_{date}
    incap site export –-path=/Users/<name>/backups --filename={site_id}
    incap site export –-path=/Users/<name>/backups --filename={site_id}_{domain}_REV3_1B

 ###### *Back up a single site with the --site_id param.*
    incap site export –-site_id=123456


*Path in the backup is option and will use the repo path in the config file or environment variable.*

## Restore site config
    incap site restore --domain=www.example.com /Users/<name>/backups/www.template.com.json

## Upload certificate to site
    incap site upcert --private_key="/<cert_location>/mooreassistance_net_apache-selfsigned.key" "/<cert_location>/www_mooreassistance_net_apache-selfsigned.crt" --passphrase=password SITE_ID

## Delete certificate from site
    incap site delcert SITE_ID

# Unit Testing
    python3 -m unittest test_incap_cli.py