from django.db import models
from django.utils import timezone
from randomuser import RandomUser


class CTF:

    @staticmethod
    def create_teams(nb=1):
        for _ in range(0, nb):
            team = Team.create_random()
            team.save()
            print("Team {} created".format(team.name))

    @staticmethod
    def disable_teams():
        for team in Team.objects.all():
            team.enabled = False
            team.save()

    @staticmethod
    def clear_data():
        for submission in FlagSubmission.objects.all():
            submission.delete()
        for team in Team.objects.all():
            team.delete()

    @staticmethod
    def clear_challenges():
        for chal in Challenge.objects.all():
            chal.delete()


class Challenge(models.Model):
    chall_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    flag = models.CharField(max_length=100)
    points = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Challenge"
        ordering = ['title']

    def __str__(self):
        return self.title


class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)
    challenges_finished = models.ManyToManyField(Challenge, blank=True)

    class Meta:
        verbose_name = "Team"
        ordering = ['name']

    @classmethod
    def create_random(cls):
        user = RandomUser()
        name = user.get_username()
        return Team(name=name, enabled=True)

    def points(self):
        total = 0
        for chal in self.challenges_finished.all():
            total += chal.points
        return total

    def __str__(self):
        return self.name


class FlagSubmission(models.Model):
    submission_id = models.AutoField(primary_key=True)
    team = models.ForeignKey('Team', null=True, on_delete=models.DO_NOTHING)
    challenge = models.ForeignKey('Challenge', null=True, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Submission date")
    submitted = models.CharField(max_length=100, default="Undefined")

    class Meta:
        verbose_name = "Flag submission"
        ordering = ['date']

    def __str__(self):
        return "{} - {}".format(self.team, self.challenge)

    def validate(self):
        flagged = self.challenge.flag == self.submitted
        if flagged:
            self.team.challenges_finished.add(self.challenge)
            self.team.save()
        return flagged
