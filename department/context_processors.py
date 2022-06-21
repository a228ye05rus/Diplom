import sys
sys.path.append('..')
from department.models import Section


def section(request):
    return {'sects': Section.objects.all()}
