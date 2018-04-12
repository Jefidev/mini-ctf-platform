from django_quicky import view
from django.shortcuts import get_object_or_404
from ctf_platform.models import Challenge, Team, FlagSubmission, AlreadyFlaggedException
from .forms import FlagSubmissionForm


@view(render_to='ctf_platform/index.html')
def index(request):
    challenges = Challenge.objects.all()
    scoreboard = list(Team.objects.filter(enabled=True))
    scoreboard.sort(key=lambda x: x.points(), reverse=True)
    return {"challenges": challenges, "scoreboard": scoreboard[:5]}


@view(render_to='ctf_platform/challenge.html')
def challenge(request, challenge_id):

    chall = get_object_or_404(Challenge, chall_id=challenge_id)

    form = FlagSubmissionForm(request.POST or None)
    if form.is_valid():
        team = form.cleaned_data['team']
        flag = form.cleaned_data['flag']

        posted = True
        teams = Team.objects.filter(name=team, enabled=True)
        is_team_ok = len(teams) > 0
        if is_team_ok:
            submission = FlagSubmission(team=teams[0], challenge=chall, submitted=flag)
            submission.save()
            try:
                is_flag_ok = submission.validate()
            except AlreadyFlaggedException:
                already_flagged = True

    scoreboard = list(Team.objects.filter(enabled=True))
    scoreboard.sort(key=lambda x: x.points(), reverse=True)
    scoreboard = scoreboard[:5]
    return locals()


@view(render_to='ctf_platform/scoreboard.html')
def scoreboard(request):
    scoreboard = list(Team.objects.filter(enabled=True))
    scoreboard.sort(key=lambda x: x.points(), reverse=True)

    limited_scoreboard = list(Team.objects.filter(enabled=True))
    limited_scoreboard.sort(key=lambda x: x.points(), reverse=True)

    return {"scoreboard": scoreboard, "limited_scoreboard": limited_scoreboard[:5]}


@view(render_to='ctf_platform/team.html')
def team(request, team_id):
    team = get_object_or_404(Team, team_id=team_id)

    limited_scoreboard = list(Team.objects.filter(enabled=True))
    limited_scoreboard.sort(key=lambda x: x.points(), reverse=True)

    return {"limited_scoreboard": limited_scoreboard[:5], "selected_team": team}