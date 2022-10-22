#!/usr/bin/env python3

import argparse
import os
import time
from pprint import pprint
import googleapiclient.discovery
import google.auth

# [START create_instance]
def create_instance(compute, project, zone, name, bucket,machine='e2-small'):
    # Get the latest Debian Jessie image.
    image_response = compute.images().getFromFamily(project='ubuntu-os-cloud', family='ubuntu-2204-lts').execute()
    source_disk_image = image_response['selfLink']
    
    # Configure the machine
    machine_type = "zones/%s/machineTypes/%s" % (zone,machine)
    startup_script = open(os.path.join(os.path.dirname(__file__), 'startup-script.sh'),'r').read()

    config = {
        'name': name,
        'machineType': machine_type,

        # Specify the boot disk and the image to use as a source.
        'disks': [
            {
                'boot': True,
                'autoDelete': True,
                'initializeParams': {
                    'sourceImage': source_disk_image,
                }
            }
        ],

        # Specify a network interface with NAT to access the public
        # internet.
        'networkInterfaces': [{
            'network': 'global/networks/default',
            'accessConfigs': [
                {'type': 'ONE_TO_ONE_NAT', 'name': 'External NAT'}
            ]
        }],

        # Allow the instance to access cloud storage and logging.
        'serviceAccounts': [{
            'email': 'default',
            'scopes': [
                'https://www.googleapis.com/auth/devstorage.read_write',
                'https://www.googleapis.com/auth/logging.write'
            ]
        }],

        # Metadata is readable from the instance and allows you to
        # pass configuration from deployment scripts to instances.
        'metadata': {
            'items': [{
                # Startup script is automatically executed by the
                # instance upon startup.
                'key': 'startup-script',
                'value': startup_script
            }, 
            {
                'key': 'bucket',
                'value': bucket
            }]
        }
    }
    return compute.instances().insert(
        project=project,
        zone=zone,
        body=config).execute()
# [END create_instance]

# [START wait_for_operation]
def wait_for_operation(compute, project, zone, operation):
    print('Waiting for operation to finish...')
    while True:
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation).execute()

        if result['status'] == 'DONE':
            print("done.")
            if 'error' in result:
                raise Exception(result['error'])
            return result

        time.sleep(1)
# [END wait_for_operation]

# [START delete_instance]
def delete_instance(compute, project, zone, name):
    return compute.instances().delete(
        project=project,
        zone=zone,
        instance=name).execute()
# [END delete_instance]

def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None


def main(project, bucket, zone, instance_name,d,wait=True):
    compute = googleapiclient.discovery.build('compute', 'v1')
    print('Creating instance.')
    operation = create_instance(compute, project, zone, instance_name, bucket)
    wait_for_operation(compute, project, zone, operation['name'])
    instances = list_instances(compute, project, zone)
    print("Your running instances are:")
    print('Instances in project %s and zone %s:' % (project, zone))
    for instance in instances:
        if instance['name']==instance_name:
            print("ExtIP http://"+instance['networkInterfaces'][0]['accessConfigs'][0]['natIP']+":5000")

if __name__=='__main__':
#
    parser = argparse.ArgumentParser(description=__doc__,formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('project_id', help='Your Google Cloud project ID.')
    parser.add_argument('bucket_name', help='Your Google Cloud Storage bucket name.')
    parser.add_argument('--zone',default='us-central1-f',help='Compute Engine zone to deploy to.')
    parser.add_argument('--name', default='demo-instance', help='New instance name.')
    parser.add_argument('--d',default='True',help='Do you want to delete the instance with "Enter" (True/False)?')
    args = parser.parse_args()
#
    main(args.project_id, args.bucket_name, args.zone, args.name,args.d)
