from django.utils.translation import ugettext_lazy as _
from jet.dashboard import modules
from jet.dashboard.dashboard import Dashboard, AppIndexDashboard


class CustomIndexDashboard(Dashboard):
    columns = 3

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)
        self.children.append(modules.LinkList(
            _('Support'),
            children=[
                {
                    'title': _('Django documentation'),
                    'url': 'http://docs.djangoprojects.com/',
                    'external': True,
                },
                {
                    'title': _('Django "django-users" mailing users'),
                    'url': 'http://groups.google.com/group/django-users',
                    'external': True,
                },
            ],
            column=0,
            order=0
        ))