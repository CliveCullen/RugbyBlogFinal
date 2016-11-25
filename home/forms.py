from django import forms


class HeadToHead(forms.Form):
  #teams = [(1,"Ireland"), (2,"England"), (3, "France"),(4,"Wales"), (5,"Scotland"), (6, "Italy")]
    team1= forms.TextInput()
    team2= forms.TextInput()
