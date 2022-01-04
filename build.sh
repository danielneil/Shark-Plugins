#/usr/bin/bash

# exit when any command fails
set -e

##################################################
# Now run the playbook.
ansible-playbook ./site.yml -i hosts  
