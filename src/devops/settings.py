import os

VIRTUAL_DRIVER = 'devops.driver.libvirt.libvirt_driver'
REAL_DRIVER = 'devops.driver.hardware.ipmi_driver'

INSTALLED_APPS = ['devops']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TEST_CHARSET': 'UTF8'
    }
}
