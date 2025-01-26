from django.shortcuts import render
from .forms import GroupForm
from .utils import create_groups

def group_views(request):
    groups = []
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            foreign_count = form.cleaned_data['foreign_count']
            japanese_count = form.cleaned_data['japanese_count']
            groups = create_groups(foreign_count, japanese_count)
    else:
        form = GroupForm()

    return render(request, 'grouping/group_form.html', {'form': form, 'groups':groups})
