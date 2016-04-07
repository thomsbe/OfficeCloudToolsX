from django.utils.html import format_html

IS_OFFICE_CLOUD = True

def get_name():
    return "Officecloud"

def get_link():
    return "index"

def get_welcome_widget():
    html = '<h4 class="center-align"><i class="mdi mdi-action-home"></i>&nbsp;'+get_name()+'</h4>'
    return format_html(html)
