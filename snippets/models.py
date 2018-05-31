# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BcProjectTypeInf(models.Model):
    key = models.CharField(max_length=200, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    project = models.ForeignKey('NewProjects', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bc_project_type_inf'


class EvtEvents(models.Model):
    id = models.IntegerField(primary_key=True)
    amount_descriptive = models.CharField(max_length=32, blank=True, null=True)
    amount_precise = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=16, blank=True, null=True)
    stage = models.CharField(max_length=16, blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True, null=True)
    headline = models.CharField(max_length=200, blank=True, null=True)
    estimated_value = models.CharField(max_length=32, blank=True, null=True)
    date_relased = models.IntegerField(blank=True, null=True)
    industry = models.CharField(max_length=128, blank=True, null=True)
    new_amount_descriptive = models.CharField(max_length=32, blank=True, null=True)
    extract_stage = models.CharField(max_length=16, blank=True, null=True)
    extract_amount = models.CharField(max_length=128, blank=True, null=True)
    extract_investee_name = models.CharField(max_length=128, blank=True, null=True)
    extract_investor_name = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    estimated_value_precise = models.FloatField(blank=True, null=True)
    write_time = models.IntegerField(blank=True, null=True)
    origin = models.CharField(max_length=32, blank=True, null=True)
    describe = models.TextField(blank=True, null=True)
    machine_status = models.IntegerField(blank=True, null=True)
    date_published = models.IntegerField(blank=True, null=True)
    investee_id = models.IntegerField(blank=True, null=True)
    investee_company_id = models.IntegerField(blank=True, null=True)
    project_type = models.ForeignKey('ProjectType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evt_events'


class FinancingHistory(models.Model):
    id = models.IntegerField(primary_key=True)
    financing_stage = models.ForeignKey('NewOptions', models.DO_NOTHING, blank=True, null=True)
    guid = models.ForeignKey('NewCompanies', models.DO_NOTHING, db_column='guid', blank=True, null=True)
    participant = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financing_history'


class FoundingTeam(models.Model):
    name = models.CharField(max_length=200)
    job_description = models.CharField(max_length=200, blank=True, null=True)
    sketch = models.TextField()
    company_guid = models.ForeignKey('NewCompanies', models.DO_NOTHING, db_column='company_guid')

    class Meta:
        managed = False
        db_table = 'founding_team'


class MiddleIndustryPeolpleFocus(models.Model):
    people = models.ForeignKey('NewPeople', models.DO_NOTHING, blank=True, null=True)
    new_options = models.ForeignKey('NewOptions', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'middle_industry_peolple_focus'


class MiddleProjectTypePeopleTags(models.Model):
    people = models.ForeignKey('NewPeople', models.DO_NOTHING, blank=True, null=True)
    bc_project_type = models.ForeignKey('ProjectType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'middle_project_type_people_tags'


class NewCompanies(models.Model):
    status = models.CharField(max_length=16, blank=True, null=True)
    guid = models.IntegerField(primary_key=True)
    cn_name = models.CharField(max_length=200, blank=True, null=True)
    en_name = models.CharField(max_length=200, blank=True, null=True)
    trademark = models.CharField(max_length=200, blank=True, null=True)
    slogan = models.CharField(max_length=200, blank=True, null=True)
    brief_introduction = models.TextField(blank=True, null=True)
    full_introduction = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=200, blank=True, null=True)
    contact_email = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    is_website_valid = models.IntegerField(blank=True, null=True)
    date_established = models.IntegerField(blank=True, null=True)
    registry_date_established = models.CharField(max_length=200, blank=True, null=True)
    registry_date_licensed = models.CharField(max_length=200, blank=True, null=True)
    registry_social_code = models.CharField(max_length=200, blank=True, null=True)
    registry_organization_code = models.CharField(max_length=200, blank=True, null=True)
    registry_registration_number = models.CharField(max_length=200, blank=True, null=True)
    registry_industry = models.ForeignKey('NewOptions', models.DO_NOTHING, db_column='registry_industry', blank=True, null=True)
    registry_scope = models.TextField(blank=True, null=True)
    registry_capital_registered = models.CharField(max_length=200, blank=True, null=True)
    registry_capital_registered_in_number = models.FloatField(blank=True, null=True)
    registry_address = models.CharField(max_length=200, blank=True, null=True)
    registry_type = models.CharField(max_length=200, blank=True, null=True)
    registry_operation_period = models.CharField(max_length=200, blank=True, null=True)
    registry_legal_person = models.CharField(max_length=200, blank=True, null=True)
    registry_bureau = models.CharField(max_length=200, blank=True, null=True)
    city = models.ForeignKey('NewLocations', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('NewLocations', models.DO_NOTHING, blank=True, null=True)
    province = models.ForeignKey('NewLocations', models.DO_NOTHING, blank=True, null=True)
    ico_desc = models.TextField(blank=True, null=True)
    is_ico = models.IntegerField(blank=True, null=True)
    financing_stage = models.ForeignKey('NewOptions', models.DO_NOTHING, db_column='financing_stage', blank=True, null=True)
    company_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_companies'


class NewEntities(models.Model):
    guid = models.AutoField(primary_key=True)
    key = models.CharField(max_length=200, blank=True, null=True)
    subtype = models.CharField(max_length=200)
    headline = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    visibility = models.IntegerField()
    time_created = models.IntegerField(blank=True, null=True)
    time_updated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_entities'


class NewInvestmentEvents(models.Model):
    id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    amount_descriptive = models.CharField(max_length=200, blank=True, null=True)
    amount_precise = models.FloatField(blank=True, null=True)
    headline = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    estimated_value_descriptive = models.CharField(max_length=200, blank=True, null=True)
    estimated_value_precise = models.FloatField(blank=True, null=True)
    date_released = models.IntegerField(blank=True, null=True)
    date_published = models.IntegerField(blank=True, null=True)
    option_currency_id = models.IntegerField(blank=True, null=True)
    option_stage_id = models.IntegerField(blank=True, null=True)
    investee_company_guid = models.IntegerField(blank=True, null=True)
    project_type = models.ForeignKey('ProjectType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_investment_events'


class NewLocations(models.Model):
    father_id = models.IntegerField()
    cn_region = models.CharField(max_length=200, blank=True, null=True)
    en_region = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_locations'


class NewOptions(models.Model):
    type = models.CharField(max_length=200)
    father_id = models.IntegerField()
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'new_options'


class NewPeople(models.Model):
    status = models.CharField(max_length=16, blank=True, null=True)
    guid = models.IntegerField(primary_key=True)
    cn_name = models.CharField(max_length=200, blank=True, null=True)
    en_name = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    mobile = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    date_birth = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_people'


class NewProjects(models.Model):
    status = models.CharField(max_length=16, blank=True, null=True)
    guid = models.ForeignKey(NewEntities, models.DO_NOTHING, db_column='guid', primary_key=True)
    cn_name = models.CharField(max_length=200, blank=True, null=True)
    en_name = models.CharField(max_length=200, blank=True, null=True)
    slogan = models.CharField(max_length=200, blank=True, null=True)
    date_released = models.IntegerField(blank=True, null=True)
    adjective = models.TextField(blank=True, null=True)
    brief_introduction = models.TextField(blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    company_guid = models.ForeignKey(NewCompanies, models.DO_NOTHING, db_column='company_guid', blank=True, null=True)
    official_web = models.TextField(blank=True, null=True)
    white_paper = models.TextField(blank=True, null=True)
    bc_project_type = models.ForeignKey('ProjectType', models.DO_NOTHING, blank=True, null=True)
    contactor = models.CharField(db_column='Contactor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contactor_method = models.CharField(db_column='Contactor_method', max_length=100, blank=True, null=True)  # Field name made lowercase.
    project_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_projects'


class ProjectTeam(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    brief_introduction = models.TextField(blank=True, null=True)
    project = models.ForeignKey(NewProjects, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_team'


class ProjectType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    project_type = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_type'
