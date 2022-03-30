from rest_framework import serializers
from projects import models


# 用户
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = ["username", "password"]


# 员工表
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmployeeModel
        fields = ["name"]


# 项目信息序列化器
class ItemInformationSerializer(serializers.ModelSerializer):
    """定义序列化器"""

    class Meta:
        model = models.ItemInformationModel  # 指定序列化从那个模型映射字段
        fields = '__all__'  # 映射那些字段


class GetItemInformationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)
    project_status = serializers.CharField(source='get_project_status_display', read_only=True)

    """定义序列化器"""

    class Meta:
        model = models.ItemInformationModel  # 指定序列化从那个模型映射字段
        fields = '__all__'  # 映射那些字段


# 项目人员管理
class EmployeeManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EmployeeManagementModel
        fields = '__all__'


class GetEmployeeManagementSerializer(serializers.ModelSerializer):
    item_number = serializers.CharField(source='item_number.item_number', read_only=True)
    employee_id = serializers.CharField(source="employee_id.name", read_only=True)
    role = serializers.CharField(source='get_role_display', read_only=True)
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.EmployeeManagementModel
        fields = '__all__'


# 项目启动
class ProjectStartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectStartModel
        fields = '__all__'


class GetProjectStartSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.ProjectStartModel
        fields = '__all__'


# 需求调研
class RequestingResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RequestingResearchModel
        fields = '__all__'


class GetRequestingResearchSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.RequestingResearchModel
        fields = '__all__'


# 系统环境文档
class SystemEnvironmentDocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SystemEnvironmentDocumentationModel
        fields = '__all__'


class GetSystemEnvironmentDocumentationSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.SystemEnvironmentDocumentationModel
        fields = '__all__'


# 软件安装包
class SoftwareInstallationPackageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SoftwareInstallationPackageModel
        fields = '__all__'


class GetSoftwareInstallationPackageModelSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.SoftwareInstallationPackageModel
        fields = '__all__'


# 报表开发
class ReportDevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReportDevelopmentModel
        fields = '__all__'


class GetReportDevelopmentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.ReportDevelopmentModel
        fields = '__all__'


# 数据开发
class DataDevelopmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DataDevelopmentModel
        fields = '__all__'


class GetDataDevelopmentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.DataDevelopmentModel
        fields = '__all__'


# 项目计划文件
class ProjectPlanDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectPlanDocumentModel
        fields = '__all__'


class GetProjectPlanDocumentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.ProjectPlanDocumentModel
        fields = '__all__'


# 风险管理
class RiskManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RiskManagementModel
        fields = '__all__'


class GetRiskManagementSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.RiskManagementModel
        fields = '__all__'


# 沟通管理
class CommunicationManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommunicationManagementModel
        fields = '__all__'


class GetCommunicationManagementSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.CommunicationManagementModel
        fields = '__all__'


# 项目总结
class ProjectSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectSummaryModel
        fields = '__all__'


class GetProjectSummarySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.ProjectSummaryModel
        fields = '__all__'


# 项目人天
class ProjectDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectDayModel
        fields = '__all__'


class GetProjectDaySerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.ProjectDayModel
        fields = '__all__'


# 外部干系人管理
class ExternalStakeholdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExternalStakeholdersModel
        fields = '__all__'


class GetExternalStakeholdersSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = models.ExternalStakeholdersModel
        fields = '__all__'

