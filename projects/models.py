from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class UserModel(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称", null=True, blank=True)
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name = verbose_name


class BaseModel(models.Model):
    add_time = models.DateTimeField(verbose_name="添加时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    user = models.ForeignKey(UserModel, verbose_name='填写人', on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True


class ProjectStatusModel(BaseModel):
    id = models.IntegerField(primary_key=True, verbose_name="状态ID")
    name = models.CharField(verbose_name="状态名称", max_length=100)

    class Meta:
        verbose_name = "项目状态"
        verbose_name_plural = verbose_name


class EmployeeModel(BaseModel):
    id = models.IntegerField(primary_key=True, verbose_name="员工ID")
    name = models.CharField(verbose_name="员工姓名", max_length=100)

    class Meta:
        verbose_name = "人员管理"
        verbose_name_plural = verbose_name

    def test(self):
        return self.name


class ItemInformationModel(BaseModel):
    item_number = models.CharField(primary_key=True, verbose_name="项目编号", max_length=255)
    customer_name = models.CharField(verbose_name="客户名称", max_length=100)
    project_name = models.CharField(verbose_name="项目名称", max_length=100)
    project_status = models.CharField(choices=(("sxqh", "上线切换"), ("xmqd", "项目启动"), ("xmzx", "项目执行"), ("xmqd", "项目启动"), ("xqdy", "需求调研"), ("syx", "试运行"), ("dnbys", "待内部验收")),
                                      verbose_name="项目状态", max_length=10, default="xmqd")

    class Meta:
        verbose_name = "项目信息"
        verbose_name_plural = verbose_name


class ProjectRoleModel(BaseModel):
    id = models.IntegerField(primary_key=True, verbose_name="角色ID")
    name = models.CharField(verbose_name="角色名称", max_length=100)

    class Meta:
        verbose_name = "项目角色"
        verbose_name_plural = verbose_name


class EmployeeManagementModel(BaseModel):
    item_number = models.ForeignKey(ItemInformationModel, on_delete=models.CASCADE, verbose_name="项目编号", related_name='iteminfo_employee')
    employee_id = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, verbose_name="员工姓名", related_name='employee_name')
    # role_id = models.ForeignKey(ProjectRoleModel, on_delete=models.CASCADE, verbose_name="项目角色")
    role = models.SmallIntegerField(choices=((1, "项目经理"), (2, "项目开发工程师")), verbose_name="项目角色", default=1)

    class Meta:
        verbose_name = "项目人员管理"
        verbose_name_plural = verbose_name


class ProjectStartModel(BaseModel):
    item_number = models.ForeignKey(ItemInformationModel, on_delete=models.CASCADE, verbose_name="项目编号")
    project_initiation_Materials = models.FileField(verbose_name="项目启动材料", max_length=255, upload_to="psm/pi/%Y/%m", null=True, blank=True)
    customer_office_address = models.CharField(default="上海市静安市大融城江程资产大厦", verbose_name="客户办公地址", max_length=200)
    working_hours = models.CharField(default="9:00~18:00", verbose_name="办公时间", max_length=100)
    project_communication_plan = models.FileField(verbose_name="项目沟通方案", max_length=255, upload_to="psm/pc/%Y/%m")

    class Meta:
        verbose_name = "项目启动"
        verbose_name_plural = verbose_name


class FileClassModel(BaseModel):
    id = models.IntegerField(verbose_name="文件类别id",primary_key=True)
    name = models.CharField(verbose_name="文件类别名称", max_length=100)

    class Meta:
        verbose_name = "文件类别"
        verbose_name_plural = verbose_name


class RequestingResearchModel(BaseModel):
    item_number = models.ForeignKey(ItemInformationModel, on_delete=models.CASCADE, verbose_name="项目编号")
    requirements_file_name = models.CharField(verbose_name="需求文件名称", max_length=100)
    requirements_document = models.FileField(verbose_name="需求文件", upload_to="rr/rd/%Y/%m")
    business_carding = models.FileField(verbose_name="业务梳理", upload_to="rr/bc/%Y/%m")
    file_class = models.CharField(choices=(("xqqr", "需求确认书"), ("ltfa", "蓝图方案"), ("xqbgjl", "需求变更记录")), verbose_name="文件类别", max_length=10, default="xqqr")
    electronic_file = models.FileField(verbose_name="电子版文件", upload_to="rr/el/%Y/%m")
    paper_signature = models.FileField(verbose_name="纸质签字版", upload_to="rr/ps/%Y/%m")
    email_screenshot = models.ImageField(verbose_name="邮件反馈确认截图", upload_to="rr/es/%Y/%m")
    remark = models.TextField(verbose_name="备注")

    class Meta:
        verbose_name = "需求调研"
        verbose_name_plural = verbose_name


class SystemEnvironmentDocumentationModel(BaseModel):
    item_number = models.ForeignKey(ItemInformationModel, on_delete=models.CASCADE, verbose_name="项目编号")
    file_name = models.CharField(verbose_name="文档名称", max_length=100)
    appendix = models.FileField(verbose_name="附件", upload_to="sed/a/%Y/%m")
    remark = models.TextField(verbose_name="备注")

    class Meta:
        verbose_name = "系统环境文档"
        verbose_name_plural = verbose_name


class SoftwareInstallationPackageModel(BaseModel):
    item_number = models.ForeignKey(ItemInformationModel, on_delete=models.CASCADE, verbose_name="项目编号")
    software_name = models.CharField(verbose_name="软件名称", max_length=100)
    installation_package = models.FileField(verbose_name="安装包", upload_to="sip/ip/%Y/%m")
    deployment_documentation = models.FileField(verbose_name="部署文档", upload_to="sip/dd/%Y/%m")
    remark = models.TextField(verbose_name="备注")

    class Meta:
        verbose_name = "软件安装包"
        verbose_name_plural = verbose_name


class ReportDevelopmentModel(BaseModel):
    item_number = models.ForeignKey(ItemInformationModel, on_delete=models.CASCADE, verbose_name="项目编号")
    requirement_name = models.CharField(verbose_name="需求名称", max_length=100)
    screenshot_page = models.ImageField(verbose_name="页面截图", upload_to="rd/sp/%Y/%m")
    export_template = models.FileField(verbose_name="导出内置数据集模板", upload_to="rd/et/%Y/%m")
    material = models.FileField(verbose_name="素材", upload_to="rd/m/%Y/%m")

    class Meta:
        verbose_name = "报表开发"
        verbose_name_plural = verbose_name


class DataDevelopmentModel(BaseModel):
    item_number = models.ForeignKey(ItemInformationModel, on_delete=models.CASCADE, verbose_name="项目编号")
    name = models.CharField(verbose_name="名称", max_length=100)
    data_development_script = models.FileField(verbose_name="数据开发脚本程序", upload_to="dd/dds/%Y/%m")
    development_documentation = models.FileField(verbose_name="开发文档", upload_to="dd/dd/%Y/%m")
    remark = models.TextField(verbose_name="备注")

    class Meta:
        verbose_name = "数据开发"
        verbose_name_plural = verbose_name


class ProjectPlanDocumentModel(BaseModel):
    item_number = models.ForeignKey(ItemInformationModel, on_delete=models.CASCADE, verbose_name="项目编号")
    project_plan_version = models.CharField(verbose_name="项目计划版本", max_length=100)
    project_plan_electronic_version = models.FileField(verbose_name="项目计划电子版", upload_to="ppd/ppev/%Y/%m")
    requirement_name = models.CharField(verbose_name="需求名称", max_length=100)
    description_of_Requirement = models.TextField(verbose_name="需求描述")

    class Meta:
        verbose_name = "项目计划文件"
        verbose_name_plural = verbose_name


class RiskManagementModel(BaseModel):
    item_number = models.ForeignKey(ItemInformationModel, on_delete=models.CASCADE, verbose_name="项目编号")
    name = models.CharField(verbose_name="名称", max_length=100)
    visit_link = models.CharField(verbose_name="访问链接", null=True, blank=True, max_length=100)
    e_edition = models.FileField(verbose_name="问题清单电子版", upload_to="rm/ee/%Y/%m")
    signed_version = models.FileField(verbose_name="纸质签字版", upload_to="rm/sv/%Y/%m")
    email_screenshot = models.ImageField(verbose_name="邮件反馈确认截图", upload_to="rm/es/%Y/%m")
    remark = models.TextField(verbose_name="备注")

    class Meta:
        verbose_name = "风险管理"
        verbose_name_plural = verbose_name


class CommunicationManagementModel(BaseModel):
    item_number = models.ForeignKey(ItemInformationModel, on_delete=models.CASCADE, verbose_name="项目编号")
    datetime = models.DateTimeField(verbose_name="日期时间", default=datetime.now)
    appendix = models.FileField(verbose_name="附件", upload_to="cm/a/%Y/%m")
    remark = models.TextField(verbose_name="备注")

    class Meta:
        verbose_name = "沟通管理"
        verbose_name_plural = verbose_name


class ProjectSummaryModel(BaseModel):
    item_number = models.ForeignKey(ItemInformationModel, on_delete=models.CASCADE, verbose_name="项目编号")
    project_summary_attachment = models.FileField(verbose_name="项目总结附件", upload_to="ps/pas/%Y/%m")

    class Meta:
        verbose_name = "项目总结"
        verbose_name_plural = verbose_name


class ProjectDayModel(BaseModel):
    item_number = models.ForeignKey(ItemInformationModel, on_delete=models.CASCADE, verbose_name="项目编号")
    project_total_day = models.IntegerField(verbose_name='项目总人天', default="0")
    employee_id = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, verbose_name="员工姓名")
    employee_day = models.IntegerField(verbose_name="人员投入人天", default="0")

    class Meta:
        verbose_name = "项目人天"
        verbose_name_plural = verbose_name


class ExternalStakeholdersModel(BaseModel):
    item_number = models.ForeignKey(ItemInformationModel, on_delete=models.CASCADE, verbose_name="项目编号")
    company_name = models.CharField(verbose_name="公司名称", max_length=100)
    department = models.CharField(verbose_name="部门", max_length=100)
    job = models.CharField(verbose_name="职位", max_length=20)
    name = models.CharField(verbose_name="姓名", max_length=25)
    project_role = models.CharField(verbose_name="项目角色", max_length=15)
    email = models.EmailField(verbose_name="邮箱")
    mobile = models.CharField(verbose_name="手机号", max_length=11)
    remark = models.TextField(verbose_name="备注")

    class Meta:
        verbose_name = "外部干系人"
        verbose_name_plural = verbose_name


