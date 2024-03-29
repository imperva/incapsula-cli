# coding: utf-8

"""
    Imperva Client-Side Protection API

    This is an API for Imperva Client-Side Protection. Gain visibility into the JavaScript services making requests to your application along with their risk factors. Use these APIs to pull data and configure which services should have access to your application. For full feature documentation, see <a style=\"text-decoration:none\" href=\"https://docs.imperva.com/bundle/client-side-protection\">Client-Side Protection</a>  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cwafcli.CSP.swagger_client.api_client import ApiClient


class EmailApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_email(self, body, site_id, **kwargs):  # noqa: E501
        """Add an email address to the notification list  # noqa: E501

        Adds an email address to the event notification recipient list for a specific website. Notifications are reasonably small and limited in frequency  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_email(body, site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Email address (required)
        :param int site_id: The numeric identifier of the site (required)
        :return: EmailList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_email_with_http_info(body, site_id, **kwargs)  # noqa: E501
        else:
            (data) = self.add_email_with_http_info(body, site_id, **kwargs)  # noqa: E501
            return data

    def add_email_with_http_info(self, body, site_id, **kwargs):  # noqa: E501
        """Add an email address to the notification list  # noqa: E501

        Adds an email address to the event notification recipient list for a specific website. Notifications are reasonably small and limited in frequency  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_email_with_http_info(body, site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Email address (required)
        :param int site_id: The numeric identifier of the site (required)
        :return: EmailList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'site_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_email" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_email`")  # noqa: E501
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `add_email`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-API-Id', 'x-API-Key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/sites/{siteId}/settings/emails/add', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmailList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_emails(self, site_id, **kwargs):  # noqa: E501
        """Retrieve the notification recipient list  # noqa: E501

        Retrieves the list of email addresses that are subscribed to event notifications for a specific website.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_emails(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: The numeric identifier of the site (required)
        :return: list[EmailList]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_emails_with_http_info(site_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_emails_with_http_info(site_id, **kwargs)  # noqa: E501
            return data

    def get_emails_with_http_info(self, site_id, **kwargs):  # noqa: E501
        """Retrieve the notification recipient list  # noqa: E501

        Retrieves the list of email addresses that are subscribed to event notifications for a specific website.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_emails_with_http_info(site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int site_id: The numeric identifier of the site (required)
        :return: list[EmailList]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['site_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_emails" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `get_emails`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-API-Id', 'x-API-Key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/sites/{siteId}/settings/emails', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[EmailList]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_email(self, body, site_id, **kwargs):  # noqa: E501
        """Delete an email address from the notification list  # noqa: E501

        Removes the email address from the event notification recipient list for a specific website.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_email(body, site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Email address (required)
        :param int site_id: The numeric identifier of the site (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_email_with_http_info(body, site_id, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_email_with_http_info(body, site_id, **kwargs)  # noqa: E501
            return data

    def remove_email_with_http_info(self, body, site_id, **kwargs):  # noqa: E501
        """Delete an email address from the notification list  # noqa: E501

        Removes the email address from the event notification recipient list for a specific website.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_email_with_http_info(body, site_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: Email address (required)
        :param int site_id: The numeric identifier of the site (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'site_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_email" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `remove_email`")  # noqa: E501
        # verify the required parameter 'site_id' is set
        if ('site_id' not in params or
                params['site_id'] is None):
            raise ValueError("Missing the required parameter `site_id` when calling `remove_email`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'site_id' in params:
            path_params['siteId'] = params['site_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-API-Id', 'x-API-Key']  # noqa: E501

        return self.api_client.call_api(
            '/v1/sites/{siteId}/settings/emails/delete', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
