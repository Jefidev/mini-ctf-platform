from django_quicky import view
from django.shortcuts import get_object_or_404
from ctf_platform.models import Challenge, Team, FlagSubmission, AlreadyFlaggedException
from .forms import FlagSubmissionForm
from .parameters import site_name


@view(render_to='ctf_platform/index.html')
def index(request):
    challenges = Challenge.objects.all()
    scoreboard = list(Team.objects.filter(enabled=True))
    scoreboard.sort(key=lambda x: x.points(), reverse=True)

    solved_challenges = list()
    if "team_name" in request.session:
        print(request.session["team_name"])
        teams = Team.objects.filter(name=request.session["team_name"])
        if len(teams) == 1:
            team = teams[0]
            solved_challenges = team.challenges_finished.all()

    return {"challenges": challenges,
            "scoreboard": scoreboard[:5],
            "site_name": site_name,
            "solved_challenges": solved_challenges}


@view(render_to='ctf_platform/challenge.html')
def challenge(request, challenge_id):

    chall = get_object_or_404(Challenge, chall_id=challenge_id)

    solved_challenges = list()
    if "team_name" in request.session:
        print(request.session["team_name"])
        teams = Team.objects.filter(name=request.session["team_name"])
        if len(teams) == 1:
            team = teams[0]
            solved_challenges = team.challenges_finished.all()

    form = FlagSubmissionForm(request.POST or None)
    if form.is_valid():
        team = form.cleaned_data['team']
        flag = form.cleaned_data['flag']

        posted = True
        teams = Team.objects.filter(name=team, enabled=True)
        is_team_ok = len(teams) > 0
        if is_team_ok:

            request.session["team_name"] = team

            submission = FlagSubmission(team=teams[0], challenge=chall, submitted=flag, already_flagged=False)
            submission.save()
            try:
                is_flag_ok = submission.validate()
            except AlreadyFlaggedException:
                already_flagged = True
                submission.already_flagged = True
                submission.save()

    scoreboard = list(Team.objects.filter(enabled=True))
    scoreboard.sort(key=lambda x: x.points(), reverse=True)
    scoreboard = scoreboard[:5]

    render_data = locals()
    render_data["site_name"] = site_name
    render_data["solved_challenged"] = solved_challenges

    return render_data


@view(render_to='ctf_platform/scoreboard.html')
def scoreboard(request):
    scoreboard = list(Team.objects.filter(enabled=True))
    scoreboard.sort(key=lambda x: x.points(), reverse=True)

    limited_scoreboard = list(Team.objects.filter(enabled=True))
    limited_scoreboard.sort(key=lambda x: x.points(), reverse=True)

    return {"scoreboard": scoreboard, "limited_scoreboard": limited_scoreboard[:5], "site_name": site_name}


@view(render_to='ctf_platform/team.html')
def team(request, team_id):
    team = get_object_or_404(Team, team_id=team_id)

    limited_scoreboard = list(Team.objects.filter(enabled=True))
    limited_scoreboard.sort(key=lambda x: x.points(), reverse=True)

    return {"limited_scoreboard": limited_scoreboard[:5], "selected_team": team, "site_name": site_name}