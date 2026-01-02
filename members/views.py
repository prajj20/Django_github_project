from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import MemberForm
from .models import Member


@login_required
def add_member(request):
    tenant = request.user.tenant  # SAFE now

    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.tenant = tenant
            member.save()
            return redirect('list-member')
    else:
        form = MemberForm()

    return render(request, 'members/add_member.html', {'form': form})


@login_required
def list_member(request):
    tenant = request.user.tenant
    members = Member.objects.filter(tenant=tenant)

    return render(request, 'members/list_member.html', {
        'members': members
    })


@login_required
def remove_member(request, id):
    tenant = request.user.tenant
    member = get_object_or_404(Member, id=id, tenant=tenant)
    member.delete()
    return redirect('list-member')
