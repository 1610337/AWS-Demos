from aws_cdk import Duration, Stack
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_rds as rds
from constructs import Construct

class CdkRdsStack(Stack):

    def __init__(self, scope: Construct, id: str, vpc, asg_security_groups, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        db_mysql_easy = rds.DatabaseInstance(self, "MySQL_DB_easy",
                                             engine=rds.DatabaseInstanceEngine.mysql(
                                                 version=rds.MysqlEngineVersion.VER_8_0_32
                                             ),
                                             instance_type=ec2.InstanceType.of(
                                                 ec2.InstanceClass.BURSTABLE2, ec2.InstanceSize.SMALL),
                                             vpc=vpc,
                                             vpc_subnets=ec2.SubnetSelection(subnet_group_name="DB"),
                                             multi_az=False,
                                             allocated_storage=50,
                                             storage_type=rds.StorageType.GP2,
                                             cloudwatch_logs_exports=["audit", "error", "general", "slowquery"],
                                             deletion_protection=False,
                                             delete_automated_backups=False,
                                             backup_retention=Duration.days(7),
                                             parameter_group=rds.ParameterGroup.from_parameter_group_name(
                                                 self, "para-group-mysql",
                                                 parameter_group_name="default.mysql8.0"
                                             )
                                             )
        for asg_sg in asg_security_groups:
            db_mysql_easy.connections.allow_default_port_from(asg_sg, "EC2 Autoscaling Group access MySQL")
