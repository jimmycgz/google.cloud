#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_cloudscheduler_job
description:
- A scheduled job that can publish a pubsub message or a http request every X interval
  of time, using crontab format string.
- To use Cloud Scheduler your project must contain an App Engine app that is located
  in one of the supported regions. If your project does not have an App Engine app,
  you must create one.
short_description: Creates a GCP Job
version_added: 2.9
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
  name:
    description:
    - The name of the job.
    required: true
    type: str
  description:
    description:
    - A human-readable description for the job. This string must not contain more
      than 500 characters.
    required: false
    type: str
  schedule:
    description:
    - Describes the schedule on which the job will be executed.
    required: false
    type: str
  time_zone:
    description:
    - Specifies the time zone to be used in interpreting schedule.
    - The value of this field must be a time zone name from the tz database.
    required: false
    default: Etc/UTC
    type: str
  retry_config:
    description:
    - By default, if a job does not complete successfully, meaning that an acknowledgement
      is not received from the handler, then it will be retried with exponential backoff
      according to the settings .
    required: false
    type: dict
    suboptions:
      retry_count:
        description:
        - The number of attempts that the system will make to run a job using the
          exponential backoff procedure described by maxDoublings.
        - Values greater than 5 and negative values are not allowed.
        required: false
        type: int
      max_retry_duration:
        description:
        - The time limit for retrying a failed job, measured from time when an execution
          was first attempted. If specified with retryCount, the job will be retried
          until both limits are reached.
        - A duration in seconds with up to nine fractional digits, terminated by 's'.
        required: false
        type: str
      min_backoff_duration:
        description:
        - The minimum amount of time to wait before retrying a job after it fails.
        - A duration in seconds with up to nine fractional digits, terminated by 's'.
        required: false
        type: str
      max_backoff_duration:
        description:
        - The maximum amount of time to wait before retrying a job after it fails.
        - A duration in seconds with up to nine fractional digits, terminated by 's'.
        required: false
        type: str
      max_doublings:
        description:
        - The time between retries will double maxDoublings times.
        - A job's retry interval starts at minBackoffDuration, then doubles maxDoublings
          times, then increases linearly, and finally retries retries at intervals
          of maxBackoffDuration up to retryCount times.
        required: false
        type: int
  pubsub_target:
    description:
    - Pub/Sub target If the job providers a Pub/Sub target the cron will publish a
      message to the provided topic .
    required: false
    type: dict
    suboptions:
      topic_name:
        description:
        - The name of the Cloud Pub/Sub topic to which messages will be published
          when a job is delivered. The topic name must be in the same format as required
          by PubSub's PublishRequest.name, for example projects/PROJECT_ID/topics/TOPIC_ID.
        required: true
        type: str
      data:
        description:
        - The message payload for PubsubMessage.
        - Pubsub message must contain either non-empty data, or at least one attribute.
        required: false
        type: str
      attributes:
        description:
        - Attributes for PubsubMessage.
        - Pubsub message must contain either non-empty data, or at least one attribute.
        required: false
        type: dict
  app_engine_http_target:
    description:
    - App Engine HTTP target.
    - If the job providers a App Engine HTTP target the cron will send a request to
      the service instance .
    required: false
    type: dict
    suboptions:
      http_method:
        description:
        - Which HTTP method to use for the request.
        required: false
        type: str
      app_engine_routing:
        description:
        - App Engine Routing setting for the job.
        required: false
        type: dict
        suboptions:
          service:
            description:
            - App service.
            - By default, the job is sent to the service which is the default service
              when the job is attempted.
            required: false
            type: str
          version:
            description:
            - App version.
            - By default, the job is sent to the version which is the default version
              when the job is attempted.
            required: false
            type: str
          instance:
            description:
            - App instance.
            - By default, the job is sent to an instance which is available when the
              job is attempted.
            required: false
            type: str
      relative_uri:
        description:
        - The relative URI.
        required: true
        type: str
      body:
        description:
        - HTTP request body. A request body is allowed only if the HTTP method is
          POST or PUT. It will result in invalid argument error to set a body on a
          job with an incompatible HttpMethod.
        required: false
        type: str
      headers:
        description:
        - HTTP request headers.
        - This map contains the header field names and values. Headers can be set
          when the job is created.
        required: false
        type: dict
  http_target:
    description:
    - HTTP target.
    - If the job providers a http_target the cron will send a request to the targeted
      url .
    required: false
    type: dict
    suboptions:
      uri:
        description:
        - The full URI path that the request will be sent to.
        required: true
        type: str
      http_method:
        description:
        - Which HTTP method to use for the request.
        required: false
        type: str
      body:
        description:
        - HTTP request body. A request body is allowed only if the HTTP method is
          POST, PUT, or PATCH. It is an error to set body on a job with an incompatible
          HttpMethod.
        required: false
        type: str
      headers:
        description:
        - This map contains the header field names and values. Repeated headers are
          not supported, but a header value can contain commas.
        required: false
        type: dict
  region:
    description:
    - Region where the scheduler job resides .
    required: true
    type: str
extends_documentation_fragment: gcp
notes:
- 'API Reference: U(https://cloud.google.com/scheduler/docs/reference/rest/)'
- 'Official Documentation: U(https://cloud.google.com/scheduler/)'
'''

EXAMPLES = '''
- name: create a job
  gcp_cloudscheduler_job:
    name: job
    region: us-central1
    schedule: "*/4 * * * *"
    description: test app engine job
    time_zone: Europe/London
    app_engine_http_target:
      http_method: POST
      app_engine_routing:
        service: web
        version: prod
        instance: my-instance-001
      relative_uri: "/ping"
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
name:
  description:
  - The name of the job.
  returned: success
  type: str
description:
  description:
  - A human-readable description for the job. This string must not contain more than
    500 characters.
  returned: success
  type: str
schedule:
  description:
  - Describes the schedule on which the job will be executed.
  returned: success
  type: str
timeZone:
  description:
  - Specifies the time zone to be used in interpreting schedule.
  - The value of this field must be a time zone name from the tz database.
  returned: success
  type: str
retryConfig:
  description:
  - By default, if a job does not complete successfully, meaning that an acknowledgement
    is not received from the handler, then it will be retried with exponential backoff
    according to the settings .
  returned: success
  type: complex
  contains:
    retryCount:
      description:
      - The number of attempts that the system will make to run a job using the exponential
        backoff procedure described by maxDoublings.
      - Values greater than 5 and negative values are not allowed.
      returned: success
      type: int
    maxRetryDuration:
      description:
      - The time limit for retrying a failed job, measured from time when an execution
        was first attempted. If specified with retryCount, the job will be retried
        until both limits are reached.
      - A duration in seconds with up to nine fractional digits, terminated by 's'.
      returned: success
      type: str
    minBackoffDuration:
      description:
      - The minimum amount of time to wait before retrying a job after it fails.
      - A duration in seconds with up to nine fractional digits, terminated by 's'.
      returned: success
      type: str
    maxBackoffDuration:
      description:
      - The maximum amount of time to wait before retrying a job after it fails.
      - A duration in seconds with up to nine fractional digits, terminated by 's'.
      returned: success
      type: str
    maxDoublings:
      description:
      - The time between retries will double maxDoublings times.
      - A job's retry interval starts at minBackoffDuration, then doubles maxDoublings
        times, then increases linearly, and finally retries retries at intervals of
        maxBackoffDuration up to retryCount times.
      returned: success
      type: int
pubsubTarget:
  description:
  - Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message
    to the provided topic .
  returned: success
  type: complex
  contains:
    topicName:
      description:
      - The name of the Cloud Pub/Sub topic to which messages will be published when
        a job is delivered. The topic name must be in the same format as required
        by PubSub's PublishRequest.name, for example projects/PROJECT_ID/topics/TOPIC_ID.
      returned: success
      type: str
    data:
      description:
      - The message payload for PubsubMessage.
      - Pubsub message must contain either non-empty data, or at least one attribute.
      returned: success
      type: str
    attributes:
      description:
      - Attributes for PubsubMessage.
      - Pubsub message must contain either non-empty data, or at least one attribute.
      returned: success
      type: dict
appEngineHttpTarget:
  description:
  - App Engine HTTP target.
  - If the job providers a App Engine HTTP target the cron will send a request to
    the service instance .
  returned: success
  type: complex
  contains:
    httpMethod:
      description:
      - Which HTTP method to use for the request.
      returned: success
      type: str
    appEngineRouting:
      description:
      - App Engine Routing setting for the job.
      returned: success
      type: complex
      contains:
        service:
          description:
          - App service.
          - By default, the job is sent to the service which is the default service
            when the job is attempted.
          returned: success
          type: str
        version:
          description:
          - App version.
          - By default, the job is sent to the version which is the default version
            when the job is attempted.
          returned: success
          type: str
        instance:
          description:
          - App instance.
          - By default, the job is sent to an instance which is available when the
            job is attempted.
          returned: success
          type: str
    relativeUri:
      description:
      - The relative URI.
      returned: success
      type: str
    body:
      description:
      - HTTP request body. A request body is allowed only if the HTTP method is POST
        or PUT. It will result in invalid argument error to set a body on a job with
        an incompatible HttpMethod.
      returned: success
      type: str
    headers:
      description:
      - HTTP request headers.
      - This map contains the header field names and values. Headers can be set when
        the job is created.
      returned: success
      type: dict
httpTarget:
  description:
  - HTTP target.
  - If the job providers a http_target the cron will send a request to the targeted
    url .
  returned: success
  type: complex
  contains:
    uri:
      description:
      - The full URI path that the request will be sent to.
      returned: success
      type: str
    httpMethod:
      description:
      - Which HTTP method to use for the request.
      returned: success
      type: str
    body:
      description:
      - HTTP request body. A request body is allowed only if the HTTP method is POST,
        PUT, or PATCH. It is an error to set body on a job with an incompatible HttpMethod.
      returned: success
      type: str
    headers:
      description:
      - This map contains the header field names and values. Repeated headers are
        not supported, but a header value can contain commas.
      returned: success
      type: dict
region:
  description:
  - Region where the scheduler job resides .
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            description=dict(type='str'),
            schedule=dict(type='str'),
            time_zone=dict(default='Etc/UTC', type='str'),
            retry_config=dict(
                type='dict',
                options=dict(
                    retry_count=dict(type='int'),
                    max_retry_duration=dict(type='str'),
                    min_backoff_duration=dict(type='str'),
                    max_backoff_duration=dict(type='str'),
                    max_doublings=dict(type='int'),
                ),
            ),
            pubsub_target=dict(type='dict', options=dict(topic_name=dict(required=True, type='str'), data=dict(type='str'), attributes=dict(type='dict'))),
            app_engine_http_target=dict(
                type='dict',
                options=dict(
                    http_method=dict(type='str'),
                    app_engine_routing=dict(type='dict', options=dict(service=dict(type='str'), version=dict(type='str'), instance=dict(type='str'))),
                    relative_uri=dict(required=True, type='str'),
                    body=dict(type='str'),
                    headers=dict(type='dict'),
                ),
            ),
            http_target=dict(
                type='dict', options=dict(uri=dict(required=True, type='str'), http_method=dict(type='str'), body=dict(type='str'), headers=dict(type='dict'))
            ),
            region=dict(required=True, type='str'),
        ),
        mutually_exclusive=[['app_engine_http_target', 'http_target', 'pubsub_target']],
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    state = module.params['state']

    fetch = fetch_resource(module, self_link(module))
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module))
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module))
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, 'cloudscheduler')
    return return_if_object(module, auth.post(link, resource_to_request(module)))


def update(module, link):
    delete(module, self_link(module))
    create(module, collection(module))


def delete(module, link):
    auth = GcpSession(module, 'cloudscheduler')
    return return_if_object(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'name': module.params.get('name'),
        u'description': module.params.get('description'),
        u'schedule': module.params.get('schedule'),
        u'timeZone': module.params.get('time_zone'),
        u'retryConfig': JobRetryconfig(module.params.get('retry_config', {}), module).to_request(),
        u'pubsubTarget': JobPubsubtarget(module.params.get('pubsub_target', {}), module).to_request(),
        u'appEngineHttpTarget': JobAppenginehttptarget(module.params.get('app_engine_http_target', {}), module).to_request(),
        u'httpTarget': JobHttptarget(module.params.get('http_target', {}), module).to_request(),
    }
    request = encode_request(request, module)
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, 'cloudscheduler')
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://cloudscheduler.googleapis.com/v1/projects/{project}/locations/{region}/jobs/{name}".format(**module.params)


def collection(module):
    return "https://cloudscheduler.googleapis.com/v1/projects/{project}/locations/{region}/jobs".format(**module.params)


def return_if_object(module, response, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    result = decode_request(result, module)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)
    request = decode_request(request, module)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'name': module.params.get('name'),
        u'description': module.params.get('description'),
        u'schedule': module.params.get('schedule'),
        u'timeZone': module.params.get('time_zone'),
        u'retryConfig': JobRetryconfig(module.params.get('retry_config', {}), module).to_request(),
        u'pubsubTarget': JobPubsubtarget(module.params.get('pubsub_target', {}), module).to_request(),
        u'appEngineHttpTarget': JobAppenginehttptarget(module.params.get('app_engine_http_target', {}), module).to_request(),
        u'httpTarget': JobHttptarget(module.params.get('http_target', {}), module).to_request(),
    }


def encode_request(request, module):
    request['name'] = "projects/%s/locations/%s/jobs/%s" % (module.params['project'], module.params['region'], module.params['name'])
    return request


def decode_request(response, module):
    if 'name' in response:
        response['name'] = response['name'].split('/')[-1]

    return response


class JobRetryconfig(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'retryCount': self.request.get('retry_count'),
                u'maxRetryDuration': self.request.get('max_retry_duration'),
                u'minBackoffDuration': self.request.get('min_backoff_duration'),
                u'maxBackoffDuration': self.request.get('max_backoff_duration'),
                u'maxDoublings': self.request.get('max_doublings'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'retryCount': self.module.params.get('retry_count'),
                u'maxRetryDuration': self.module.params.get('max_retry_duration'),
                u'minBackoffDuration': self.module.params.get('min_backoff_duration'),
                u'maxBackoffDuration': self.module.params.get('max_backoff_duration'),
                u'maxDoublings': self.module.params.get('max_doublings'),
            }
        )


class JobPubsubtarget(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {u'topicName': self.request.get('topic_name'), u'data': self.request.get('data'), u'attributes': self.request.get('attributes')}
        )

    def from_response(self):
        return remove_nones_from_dict(
            {u'topicName': self.module.params.get('topic_name'), u'data': self.module.params.get('data'), u'attributes': self.module.params.get('attributes')}
        )


class JobAppenginehttptarget(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'httpMethod': self.request.get('http_method'),
                u'appEngineRouting': JobAppenginerouting(self.request.get('app_engine_routing', {}), self.module).to_request(),
                u'relativeUri': self.request.get('relative_uri'),
                u'body': self.request.get('body'),
                u'headers': self.request.get('headers'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'httpMethod': self.module.params.get('http_method'),
                u'appEngineRouting': JobAppenginerouting(self.module.params.get('app_engine_routing', {}), self.module).to_request(),
                u'relativeUri': self.request.get(u'relativeUri'),
                u'body': self.module.params.get('body'),
                u'headers': self.module.params.get('headers'),
            }
        )


class JobAppenginerouting(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {u'service': self.request.get('service'), u'version': self.request.get('version'), u'instance': self.request.get('instance')}
        )

    def from_response(self):
        return remove_nones_from_dict(
            {u'service': self.module.params.get('service'), u'version': self.module.params.get('version'), u'instance': self.module.params.get('instance')}
        )


class JobHttptarget(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'uri': self.request.get('uri'),
                u'httpMethod': self.request.get('http_method'),
                u'body': self.request.get('body'),
                u'headers': self.request.get('headers'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'uri': self.request.get(u'uri'),
                u'httpMethod': self.request.get(u'httpMethod'),
                u'body': self.request.get(u'body'),
                u'headers': self.request.get(u'headers'),
            }
        )


if __name__ == '__main__':
    main()
