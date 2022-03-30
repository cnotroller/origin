import django_filters
from projects.models import *


class ItemListFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = ItemInformationModel
        fields = ["item_number", "project_status", "project_name"]


class ProjectStartFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        models = ProjectStartModel
        fields = ['project_initiation_Materials', 'customer_office_address', 'working_hours', 'project_communication_plan']


class EmployeeManagementFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = EmployeeManagementModel
        fields = ["item_number"]


class RequestingResearchFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = RequestingResearchModel
        fields = ["item_number"]


class SystemEnvironmentDocumentationFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = SystemEnvironmentDocumentationModel
        fields = ["item_number"]


class SoftwareInstallationPackageFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = SoftwareInstallationPackageModel
        fields = ["item_number"]


class ReportDevelopmentFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = ReportDevelopmentModel
        fields = ["item_number"]


class DataDevelopmentFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = DataDevelopmentModel
        fields = ["item_number"]


class ProjectPlanDocumentFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = ProjectPlanDocumentModel
        fields = ["item_number"]


class RiskManagementFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = RiskManagementModel
        fields = ["item_number"]


class CommunicationManagementFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = CommunicationManagementModel
        fields = ["item_number"]


class ProjectSummaryFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = ProjectSummaryModel
        fields = ["item_number"]


class ProjectDayFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = ProjectDayModel
        fields = ["item_number"]


class ExternalStakeholdersFilter(django_filters.rest_framework.FilterSet):
    class Meta:
        model = ExternalStakeholdersModel
        fields = ["item_number"]
