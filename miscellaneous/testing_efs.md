
This is a quick walkthrough of how to set up EFS and test it.

1. Create EFS (in the management console)
1.1 Customized workflow
1.2 For each mount target in the subnet choose a security group that allows access from your EC2. Rule-Example: Type: NFS; Protocol: TCP; Port: 2049; Source: 0.0.0.0/0 [1]

2. Launch 2 EC2 instances 
2.1 Same subnets and default SG is sufficient
2.2 User data from below [2]
2.3 (Optional) Change Name Tag (just to show that these are two different instances)

3 Test by opening an SSH session on each of the instances
``` bash
df -h
cd /efs
sudo touch file.txt
```

[1] https://docs.aws.amazon.com/efs/latest/ug/accessing-fs-create-security-groups.html

[2] User data
``` bash
#!/bin/bash
sudo mkdir /efs
mount [...] (copy second connection string from from EFS service site (can be found under "Connect") but change the ending (folder to mount the target to) to: [...].com:/ /efs)
```


