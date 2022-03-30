from django_filters import rest_framework
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .filters import *
from rest_framework.response import Response


class ItemInformationView(ModelViewSet):
    """定义类视图"""
    # 指定查询集
    queryset = ItemInformationModel.objects.all()
    # 指定序列化器
    serializer_class = ItemInformationSerializer


class GETItemInformationView(ModelViewSet):
    queryset = ItemInformationModel.objects.all()
    # 指定序列化器
    serializer_class = GetItemInformationSerializer


class EmployeeManagementView(ModelViewSet):
    queryset = EmployeeManagementModel.objects.all()
    serializer_class = EmployeeManagementSerializer


class GetEmployeeManagementView(ModelViewSet):
    queryset = EmployeeManagementModel.objects.all()
    serializer_class = GetEmployeeManagementSerializer


class ProjectStarView(ModelViewSet):
    queryset = ProjectStartModel.objects.all()
    serializer_class = ProjectStartSerializer


class GetProjectStarView(ModelViewSet):
    queryset = ProjectStartModel.objects.all()
    serializer_class = GetProjectStartSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = ProjectStartFilter


class RequestingResearchView(ModelViewSet):
    queryset = RequestingResearchModel.objects.all()
    serializer_class = RequestingResearchSerializer


class GetRequestingResearchView(ModelViewSet):
    queryset = RequestingResearchModel.objects.all()
    serializer_class = GetRequestingResearchSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = RequestingResearchFilter


class SystemEnvironmentDocumentationView(ModelViewSet):
    queryset = SystemEnvironmentDocumentationModel.objects.all()
    serializer_class = SystemEnvironmentDocumentationSerializer


class GetSystemEnvironmentDocumentationView(ModelViewSet):
    queryset = SystemEnvironmentDocumentationModel.objects.all()
    serializer_class = GetSystemEnvironmentDocumentationSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = SystemEnvironmentDocumentationFilter


class SoftwareInstallationPackageView(ModelViewSet):
    queryset = SoftwareInstallationPackageModel.objects.all()
    serializer_class = SoftwareInstallationPackageModelSerializer


class GetSoftwareInstallationPackageView(ModelViewSet):
    queryset = SoftwareInstallationPackageModel.objects.all()
    serializer_class = GetSoftwareInstallationPackageModelSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = SoftwareInstallationPackageFilter


class ReportDevelopmentView(ModelViewSet):
    queryset = ReportDevelopmentModel.objects.all()
    serializer_class = ReportDevelopmentSerializer


class GetReportDevelopmentView(ModelViewSet):
    queryset = ReportDevelopmentModel.objects.all()
    serializer_class = GetReportDevelopmentSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = ReportDevelopmentFilter


class DataDevelopmentView(ModelViewSet):
    queryset = DataDevelopmentModel.objects.all()
    serializer_class = DataDevelopmentSerializer


class GetDataDevelopmentView(ModelViewSet):
    queryset = DataDevelopmentModel.objects.all()
    serializer_class = GetDataDevelopmentSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = DataDevelopmentFilter


class ProjectPlanDocumentView(ModelViewSet):
    queryset = ProjectPlanDocumentModel.objects.all()
    serializer_class = ProjectStartSerializer


class GetProjectPlanDocumentView(ModelViewSet):
    queryset = ProjectPlanDocumentModel.objects.all()
    serializer_class = GetProjectPlanDocumentSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = ProjectPlanDocumentFilter


class RiskManagementView(ModelViewSet):
    queryset = RiskManagementModel.objects.all()
    serializer_class = RiskManagementSerializer


class GetRiskManagementView(ModelViewSet):
    queryset = RiskManagementModel.objects.all()
    serializer_class = GetRiskManagementSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = RiskManagementFilter


class CommunicationManagementView(ModelViewSet):
    queryset = CommunicationManagementModel.objects.all()
    serializer_class = CommunicationManagementSerializer


class GetCommunicationManagementView(ModelViewSet):
    queryset = CommunicationManagementModel.objects.all()
    serializer_class = GetCommunicationManagementSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = CommunicationManagementFilter


class ProjectSummaryView(ModelViewSet):
    queryset = ProjectSummaryModel.objects.all()
    serializer_class = ProjectSummarySerializer


class GetProjectSummaryView(ModelViewSet):
    queryset = ProjectSummaryModel.objects.all()
    serializer_class = GetProjectSummarySerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = ProjectSummaryFilter


class ProjectDayView(ModelViewSet):
    queryset = ProjectDayModel.objects.all()
    serializer_class = ProjectDaySerializer


class GetProjectDayView(ModelViewSet):
    queryset = ProjectDayModel.objects.all()
    serializer_class = GetProjectDaySerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = ProjectDayFilter


class ExternalStakeholdersView(ModelViewSet):
    queryset = ExternalStakeholdersModel.objects.all().order_by("-add_time")
    serializer_class = ExternalStakeholdersSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = ExternalStakeholdersFilter


class GetExternalStakeholdersView(ModelViewSet):
    queryset = ExternalStakeholdersModel.objects.all().order_by("-add_time")
    serializer_class = GetExternalStakeholdersSerializer
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_class = ExternalStakeholdersFilter


