import xadmin

from .models import *


class GlobalSettings(object):  # 页面标题
    site_title = "SmartData项目管理"
    site_footer = "SmartData.com"


class BaseSettings(object):  # 页面主题
    enable_themes = True
    use_bootswatch = True


class UserAdmin(object):
    list_display = ["id", "name", "gender", "is_superuser", "employee_id"]
    search_fields = ["id", "name", "gender", "is_superuser", "employee_id"]
    list_filter = ["id", "name", "gender", "is_superuser", "employee_id"]
    list_editable = ["id", "name", "gender", "is_superuser", "employee_id"]


class ItemInformationAdmin(object):
    list_display = ["item_number", "customer_name", "project_name", "project_status", "add_time", "update_time"]
    search_fields = ["item_number", "customer_name", "project_name", "project_status", "add_time", "update_time"]
    list_filter = ["item_number", "customer_name", "project_name", "project_status", "add_time", "update_time"]
    list_editable = ["item_number", "customer_name", "project_name", "project_status", "add_time", "update_time"]


class EmployeeAdmin(object):
    list_display = ["id", "name"]
    search_fields = ["id", "name"]
    list_filter = ["id", "name"]
    list_editable = ["id", "name"]


class ProjectRoleAdmin(object):
    list_display = ["id", "name"]
    search_fields = ["id", "name"]
    list_filter = ["id", "name"]
    list_editable = ["id", "name"]


class EmployeeManagementAdmin(object):
    list_display = ["item_number", "employee_id", "role"]
    search_fields = ["item_number", "employee_id", "role"]
    list_filter = ["item_number", "employee_id", "role"]
    list_editable = ["item_number", "employee_id", "role"]


class ProjectStartAdmin(object):
    list_display = ["item_number", "project_initiation_Materials", "customer_office_address", "working_hours",
                    "project_communication_plan"]
    search_fields = ["item_number", "project_initiation_Materials", "customer_office_address", "working_hours",
                     "project_communication_plan"]
    list_filter = ["item_number", "project_initiation_Materials", "customer_office_address", "working_hours",
                   "project_communication_plan"]
    list_editable = ["project_initiation_Materials", "customer_office_address", "working_hours",
                     "project_communication_plan"]


class FileClassAdmin(object):
    list_display = ["id", "name"]
    search_fields = ["id", "name"]
    list_filter = ["id", "name"]
    list_editable = ["id", "name"]


class RequestingResearchAdmin(object):
    list_display = ["item_number", "requirements_file_name", "requirements_document", "business_carding",
                    "file_class_id", "electronic_file", "paper_signature", "email_screenshot", "remark"]
    search_fields = ["item_number", "requirements_file_name", "requirements_document", "business_carding",
                     "file_class_id", "electronic_file", "paper_signature", "email_screenshot", "remark"]
    list_filter = ["item_number", "requirements_file_name", "requirements_document", "business_carding",
                   "file_class_id", "electronic_file", "paper_signature", "email_screenshot", "remark"]
    list_editable = ["requirements_file_name", "requirements_document", "business_carding",
                     "file_class_id", "electronic_file", "paper_signature", "email_screenshot", "remark"]


class SystemEnvironmentDocumentationAdmin(object):
    list_display = ["item_number", "file_name", "appendix", "remark"]
    search_fields = ["item_number", "file_name", "appendix", "remark"]
    list_filter = ["item_number", "file_name", "appendix", "remark"]
    list_editable = ["file_name", "appendix", "remark"]


class SoftwareInstallationPackageAdmin(object):
    list_display = ["item_number", "software_name", "installation_package", "deployment_documentation", "remark"]
    search_fields = ["item_number", "software_name", "installation_package", "deployment_documentation", "remark"]
    list_filter = ["item_number", "software_name", "installation_package", "deployment_documentation", "remark"]
    list_editable = ["software_name", "installation_package", "deployment_documentation", "remark"]


class ReportDevelopmentAdmin(object):
    list_display = ["item_number", "requirement_name", "screenshot_page", "export_template", "material"]
    search_fields = ["item_number", "requirement_name", "screenshot_page", "export_template", "material"]
    list_filter = ["item_number", "requirement_name", "screenshot_page", "export_template", "material"]
    list_editable = ["requirement_name", "screenshot_page", "export_template", "material"]


class DataDevelopmentAdmin(object):
    list_display = ["item_number", "name", "data_development_script", "development_documentation", "remark"]
    search_fields = ["item_number", "name", "data_development_script", "development_documentation", "remark"]
    list_filter = ["item_number", "name", "data_development_script", "development_documentation", "remark"]
    list_editable = ["name", "data_development_script", "development_documentation", "remark"]


class ProjectPlanDocumentAdmin(object):
    list_display = ["item_number", "project_plan_version", "project_plan_electronic_version", "requirement_name"]
    search_fields = ["item_number", "project_plan_version", "project_plan_electronic_version", "requirement_name"]
    list_filter = ["item_number", "project_plan_version", "project_plan_electronic_version", "requirement_name"]
    list_editable = ["project_plan_version", "project_plan_electronic_version", "requirement_name"]


class RiskManagementAdmin(object):
    list_display = ["item_number", "name", "visit_link", "e_edition", "signed_version", "email_screenshot", "remark"]
    search_fields = ["item_number", "name", "visit_link", "e_edition", "signed_version", "email_screenshot", "remark"]
    list_filter = ["item_number", "name", "visit_link", "e_edition", "signed_version", "email_screenshot", "remark"]
    list_editable = ["name", "visit_link", "e_edition", "signed_version", "email_screenshot", "remark"]


class CommunicationManagementAdmin(object):
    list_display = ["item_number", "datetime", "appendix", "remark"]
    search_fields = ["item_number", "datetime", "appendix", "remark"]
    list_filter = ["item_number", "datetime", "appendix", "remark"]
    list_editable = ["datetime", "appendix", "remark"]


class ProjectSummaryAdmin(object):
    list_display = ["item_number", "project_summary_attachment", "total_project_man_days", "employee_id"]
    search_fields = ["item_number", "project_summary_attachment", "total_project_man_days", "employee_id"]
    list_filter = ["item_number", "project_summary_attachment", "total_project_man_days", "employee_id"]
    list_editable = ["item_number", "project_summary_attachment", "total_project_man_days", "employee_id"]


xadmin.site.register(ItemInformationModel, ItemInformationAdmin)
xadmin.site.register(EmployeeModel, EmployeeAdmin)
xadmin.site.register(ProjectRoleModel, ProjectRoleAdmin)
xadmin.site.register(EmployeeManagementModel, EmployeeManagementAdmin)
xadmin.site.register(ProjectStartModel, ProjectStartAdmin)
xadmin.site.register(FileClassModel, FileClassAdmin)
xadmin.site.register(RequestingResearchModel, RequestingResearchAdmin)
xadmin.site.register(SystemEnvironmentDocumentationModel, SystemEnvironmentDocumentationAdmin)
xadmin.site.register(SoftwareInstallationPackageModel, SoftwareInstallationPackageAdmin)
xadmin.site.register(ReportDevelopmentModel, ReportDevelopmentAdmin)
xadmin.site.register(DataDevelopmentModel, DataDevelopmentAdmin)
xadmin.site.register(ProjectPlanDocumentModel, ProjectPlanDocumentAdmin)
xadmin.site.register(RiskManagementModel, RiskManagementAdmin)
xadmin.site.register(CommunicationManagementModel, CommunicationManagementAdmin)
# xadmin.site.register(ProjectSummaryModel, ProjectSummaryAdmin)


xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
