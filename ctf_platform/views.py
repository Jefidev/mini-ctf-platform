from django_quicky import view
from django.shortcuts import get_object_or_404
from ctf_platform.models import Challenge, Team, FlagSubmission
from .forms import FlagSubmissionForm


@view(render_to='ctf_platform/index.html')
def index(request):
    challenges = Challenge.objects.all()
    scoreboard = list(Team.objects.filter(enabled=True))[:5]
    scoreboard.sort(key=lambda x: x.points(), reverse=True)
    return {"challenges": challenges, "scoreboard": scoreboard}


@view(render_to='ctf_platform/challenge.html')
def challenge(request, challenge_id):

    chall = get_object_or_404(Challenge, chall_id=challenge_id)

    form = FlagSubmissionForm(request.POST or None)
    if form.is_valid():
        team = form.cleaned_data['team']
        pwd = form.cleaned_data['pwd']
        flag = form.cleaned_data['flag']

        posted = True
        teams = Team.objects.filter(name=team, pwd=pwd, enabled=True)
        is_team_ok = len(teams) > 0
        if is_team_ok:
            submission = FlagSubmission(team=teams[0], challenge=chall, submitted=flag)
            submission.save()
            is_flag_ok = submission.validate()

    scoreboard = list(Team.objects.filter(enabled=True))[:5]
    scoreboard.sort(key=lambda x: x.points(), reverse=True)
    return locals()
