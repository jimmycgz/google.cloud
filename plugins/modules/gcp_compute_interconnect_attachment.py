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
module: gcp_compute_interconnect_attachment
description:
- Represents an InterconnectAttachment (VLAN attachment) resource. For more information,
  see Creating VLAN Attachments.
short_description: Creates a GCP InterconnectAttachment
version_added: 2.8
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
  interconnect:
    description:
    - URL of the underlying Interconnect object that this attachment's traffic will
      traverse through. Required if type is DEDICATED, must not be set if type is
      PARTNER.
    required: false
    type: str
  description:
    description:
    - An optional description of this resource.
    required: false
    type: str
  edge_availability_domain:
    description:
    - Desired availability domain for the attachment. Only available for type PARTNER,
      at creation time. For improved reliability, customers should configure a pair
      of attachments with one per availability domain. The selected availability domain
      will be provided to the Partner via the pairing key so that the provisioned
      circuit will lie in the specified domain. If not specified, the value will default
      to AVAILABILITY_DOMAIN_ANY.
    required: false
    type: str
  type:
    description:
    - The type of InterconnectAttachment you wish to create. Defaults to DEDICATED.
    - 'Some valid choices include: "DEDICATED", "PARTNER", "PARTNER_PROVIDER"'
    required: false
    type: str
  router:
    description:
    - URL of the cloud router to be used for dynamic routing. This router must be
      in the same region as this InterconnectAttachment. The InterconnectAttachment
      will automatically connect the Interconnect to the network & region within which
      the Cloud Router is configured.
    - 'This field represents a link to a Router resource in GCP. It can be specified
      in two ways. First, you can place a dictionary with key ''selfLink'' and value
      of your resource''s selfLink Alternatively, you can add `register: name-of-resource`
      to a gcp_compute_router task and then set this router field to "{{ name-of-resource
      }}"'
    required: true
    type: dict
  name:
    description:
    - Name of the resource. Provided by the client when the resource is created. The
      name must be 1-63 characters long, and comply with RFC1035. Specifically, the
      name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
      which means the first character must be a lowercase letter, and all following
      characters must be a dash, lowercase letter, or digit, except the last character,
      which cannot be a dash.
    required: true
    type: str
  candidate_subnets:
    description:
    - Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress
      and customerRouterIpAddress for this attachment.
    - All prefixes must be within link-local address space (169.254.0.0/16) and must
      be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29
      from the supplied candidate prefix(es). The request will fail if all possible
      /29s are in use on Google's edge. If not supplied, Google will randomly select
      an unused /29 from all of link-local space.
    required: false
    type: list
  vlan_tag8021q:
    description:
    - The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using
      PARTNER type this will be managed upstream.
    required: false
    type: int
  region:
    description:
    - Region where the regional interconnect attachment resides.
    required: true
    type: str
extends_documentation_fragment: gcp
'''

EXAMPLES = '''
- name: create a interconnect attachment
  gcp_compute_interconnect_attachment:
    name: test_object
    region: us-central1
    project: test_project
    auth_kind: serviceaccount
    interconnect: https://googleapis.com/compute/v1/projects/test_project/global/interconnects/...
    router: https://googleapis.com/compute/v1/projects/test_project/regions/us-central1/routers/...
    service_account_file: "/tmp/auth.pem"
    state: present
  register: disk
'''

RETURN = '''
cloudRouterIpAddress:
  description:
  - IPv4 address + prefix length to be configured on Cloud Router Interface for this
    interconnect attachment.
  returned: success
  type: str
customerRouterIpAddress:
  description:
  - IPv4 address + prefix length to be configured on the customer router subinterface
    for this interconnect attachment.
  returned: success
  type: str
interconnect:
  description:
  - URL of the underlying Interconnect object that this attachment's traffic will
    traverse through. Required if type is DEDICATED, must not be set if type is PARTNER.
  returned: success
  type: str
description:
  description:
  - An optional description of this resource.
  returned: success
  type: str
edgeAvailabilityDomain:
  description:
  - Desired availability domain for the attachment. Only available for type PARTNER,
    at creation time. For improved reliability, customers should configure a pair
    of attachments with one per availability domain. The selected availability domain
    will be provided to the Partner via the pairing key so that the provisioned circuit
    will lie in the specified domain. If not specified, the value will default to
    AVAILABILITY_DOMAIN_ANY.
  returned: success
  type: str
pairingKey:
  description:
  - '[Output only for type PARTNER. Not present for DEDICATED]. The opaque identifier
    of an PARTNER attachment used to initiate provisioning with a selected partner.
    Of the form "XXXXX/region/domain" .'
  returned: success
  type: str
partnerAsn:
  description:
  - "[Output only for type PARTNER. Not present for DEDICATED]. Optional BGP ASN for
    the router that should be supplied by a layer 3 Partner if they configured BGP
    on behalf of the customer."
  returned: success
  type: str
privateInterconnectInfo:
  description:
  - Information specific to an InterconnectAttachment. This property is populated
    if the interconnect that this is attached to is of type DEDICATED.
  returned: success
  type: complex
  contains:
    tag8021q:
      description:
      - 802.1q encapsulation tag to be used for traffic between Google and the customer,
        going to and from this network and region.
      returned: success
      type: int
type:
  description:
  - The type of InterconnectAttachment you wish to create. Defaults to DEDICATED.
  returned: success
  type: str
state:
  description:
  - "[Output Only] The current state of this attachment's functionality."
  returned: success
  type: str
googleReferenceId:
  description:
  - Google reference ID, to be used when raising support tickets with Google or otherwise
    to debug backend connectivity issues.
  returned: success
  type: str
router:
  description:
  - URL of the cloud router to be used for dynamic routing. This router must be in
    the same region as this InterconnectAttachment. The InterconnectAttachment will
    automatically connect the Interconnect to the network & region within which the
    Cloud Router is configured.
  returned: success
  type: dict
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
id:
  description:
  - The unique identifier for the resource. This identifier is defined by the server.
  returned: success
  type: str
name:
  description:
  - Name of the resource. Provided by the client when the resource is created. The
    name must be 1-63 characters long, and comply with RFC1035. Specifically, the
    name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
    which means the first character must be a lowercase letter, and all following
    characters must be a dash, lowercase letter, or digit, except the last character,
    which cannot be a dash.
  returned: success
  type: str
candidateSubnets:
  description:
  - Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress
    and customerRouterIpAddress for this attachment.
  - All prefixes must be within link-local address space (169.254.0.0/16) and must
    be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29
    from the supplied candidate prefix(es). The request will fail if all possible
    /29s are in use on Google's edge. If not supplied, Google will randomly select
    an unused /29 from all of link-local space.
  returned: success
  type: list
vlanTag8021q:
  description:
  - The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4094. When using
    PARTNER type this will be managed upstream.
  returned: success
  type: int
region:
  description:
  - Region where the regional interconnect attachment resides.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, remove_nones_from_dict, replace_resource_dict
import json
import re
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            interconnect=dict(type='str'),
            description=dict(type='str'),
            edge_availability_domain=dict(type='str'),
            type=dict(type='str'),
            router=dict(required=True, type='dict'),
            name=dict(required=True, type='str'),
            candidate_subnets=dict(type='list', elements='str'),
            vlan_tag8021q=dict(type='int'),
            region=dict(required=True, type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#interconnectAttachment'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind):
    delete(module, self_link(module), kind)
    create(module, collection(module), kind)


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#interconnectAttachment',
        u'interconnect': module.params.get('interconnect'),
        u'description': module.params.get('description'),
        u'edgeAvailabilityDomain': module.params.get('edge_availability_domain'),
        u'type': module.params.get('type'),
        u'router': replace_resource_dict(module.params.get(u'router', {}), 'selfLink'),
        u'name': module.params.get('name'),
        u'candidateSubnets': module.params.get('candidate_subnets'),
        u'vlanTag8021q': module.params.get('vlan_tag8021q'),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/interconnectAttachments/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/interconnectAttachments".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
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

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

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
        u'cloudRouterIpAddress': response.get(u'cloudRouterIpAddress'),
        u'customerRouterIpAddress': response.get(u'customerRouterIpAddress'),
        u'interconnect': response.get(u'interconnect'),
        u'description': response.get(u'description'),
        u'edgeAvailabilityDomain': response.get(u'edgeAvailabilityDomain'),
        u'pairingKey': response.get(u'pairingKey'),
        u'partnerAsn': response.get(u'partnerAsn'),
        u'privateInterconnectInfo': InterconnectAttachmentPrivateinterconnectinfo(response.get(u'privateInterconnectInfo', {}), module).from_response(),
        u'type': response.get(u'type'),
        u'state': response.get(u'state'),
        u'googleReferenceId': response.get(u'googleReferenceId'),
        u'router': response.get(u'router'),
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'id': response.get(u'id'),
        u'name': response.get(u'name'),
        u'candidateSubnets': response.get(u'candidateSubnets'),
        u'vlanTag8021q': response.get(u'vlanTag8021q'),
    }


def region_selflink(name, params):
    if name is None:
        return
    url = r"https://www.googleapis.com/compute/v1/projects/.*/regions/.*"
    if not re.match(url, name):
        name = "https://www.googleapis.com/compute/v1/projects/{project}/regions/%s".format(**params) % name
    return name


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#interconnectAttachment')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation', False)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class InterconnectAttachmentPrivateinterconnectinfo(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({})

    def from_response(self):
        return remove_nones_from_dict({})


if __name__ == '__main__':
    main()
