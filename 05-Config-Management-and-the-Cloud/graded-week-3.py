# Week 3 Graded Quiz

# Create GCP VM, then
# git clone https://www.github.com/google/it-cert-automation-practice.git
# cd ~/it-cert-automation-practice/Course5/Lab3
# ls

# In order to enable hello_cloud.py to run on boot, copy the file hello_cloud.py to the /usr/local/bin/ location:
# sudo cp hello_cloud.py /usr/local/bin/

# Also copy hello_cloud.service to the /etc/systemd/system/ location:
# sudo cp hello_cloud.service /etc/systemd/system

# Now, use the systemctl command to enable the service hello_cloud:
# sudo systemctl enable hello_cloud.service

# Restart the VM


# Create VMs using a template
# Navigation menu > Compute Engine > Images > Create Image
# Navigation menu > Compute Engine > Instance templates:


# On GCLOUD CLI
# gcloud compute instances create --zone us-west4-a --source-instance-template vm1-template vm2 vm3 vm4 vm5 vm6 vm7 vm8
# gcloud compute instances list
