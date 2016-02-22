#!/bin/bash
#test the relationship between acl and default permission

export PATH=/sbin:/bin/:/usr/sbin:/usr/bin

echo "First make sure we run this sh with root"
users
echo "Second is cd to the /home/tmp which directory we run the test"
cd /home/tmp
echo "******check pwd****"
pwd
echo "*******************"
echo "change use to a"
su - a -c << EOF
users;
exit;
EOF



