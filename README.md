# incapsula-cli
This application provides a simple to use CLI that reflects industry standards (such as the AWS cli), and enables customers to easily integrate into configurations management, orchestration or automation frameworks to support the DevOps model

## Running the Incap CLI

This CLI is a Python 3 application and has been tested with Python 3.5 -> 3.7
# Requirements:
    python 3.5.0 or higher

# Confirm your version of python if installed:
    Open a terminal
    Enter: python -V or python3 -V

# If your version of python is higher than 3.5 then test the incap app with the following:
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


# Examples:
    incap --help
    incap site --help
    incap site acl --help
    incap site add www.saic.com
    incap site list_incaprule 26621616

Add a site
    incap site add www.saic.com

Check a site's status
    incap site status SITE_ID

Delete a site
    incap site delete SITE_ID

List all incap_rules
    incap site list_incaprule SITE_ID


Add an IncapRule to a site
    incap site add_incaprule --name="Testing block crawlers" --action=RULE_ACTION_ALERT --filter="ClientType == Crawler" SITE_ID

Update IncapRule on a site
    incap site edit_incaprule --name="BA HTTP" --filter='(Method == POST;PUT)' --action=RULE_ACTION_ALERT RULE_ID

Delete an IncapRule from a site
    incap site del_incaprule RULE_ID

Update security rule action to block IP for SQL Injection
    incap site security  --security_rule_action=block_ip sql_injection SITE_ID

Add blacklisted IPs for a site
    incap site acl --ips=107.232.12.4,102.232.22.99 blacklisted_ips SITE_ID

Backup full config (does not include ADR rules yet)
    incap site list --export=true –path=/Users/<name>/backups

Restore site config
    incap site restore --domain=www.example.com /Users/<name>/backups/www.template.com.json
