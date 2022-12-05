
with open('icaps_schedule_details.csv', 'r') as f:
    lines = f.readlines()

data = {i: {} for i in range(19)}

for line in lines[1:]:
    line = line.split(',')
    data[int(line[0])][line[2]] = line

YELLOW = [
    'Diversity',
    'Social: Get Together',
    'Social: Speed Dating',
    'Social: Speed Gathering',
    'Social: Games',
    'Social: Diversity Follow Up',
    'Social: Pseudonym Get Together',
    'Social: Pub Quiz',
    'Social: Open Discussion',
    'Social: Puzzle Game Team Challenge',
    'Community Meeting',
    'Closing and Final Get Together'
]

GREEN = [
    'Invited Talk: Sven Koenig',
    'Invited Talk: Sidd Srinivasa',
    'Invited Talk: Emma Brunskill',
    'Invited Talk: Tim Miller',
    'Invited Talk: Malte Helmert'
]

BLUE = [
    'Poster and Demo Session',
    'Opening (start: +30min)'
]

RED = [
    'Competition Panel',
    'Industry Panel',
    'Career Development Panel',
]

ROWSPAN = {
    'Community Meeting': 2,
    'User Interfaces for Explainable Planning': 2,
    '31a': 2,
    '31b': 2,
}

print('<table class="schedule-overview" style="min-width: 965px;">')

# Table header with dates from June 21st to June 24th
print('<thead>')
print('<tr style="background-color: rgb(42, 47, 51); color: #F2F5F5;">')
print("""
<th style="padding: 10px;">
<!-- Dropdown selection of time zone -->
<select id="timezone-selector" onchange="updateTimezone()">
<option value="0">UTC</option>
<option value="8">Singapore</option>
<option value="10">Canberra</option>
<option value="2">Paris</option>
<option value="20">NYC</option>
<option value="17">LA</option>
</select>
</th>
""")
for i in range(21, 25):
    print(f'<th colspan="2">June {i}</th>')
print('</tr>')
print('</thead>')

for slot in range(19):
    print('<tr>', end='')
    print(f'<td id="slot-{slot+6}">{slot+6}</td>', end='')
    for day in range(1,5):
        if f'{day}' not in data[slot]:
            print('<td></td><td></td>', end='')
        else:
            line = data[slot][f'{day}']
            rowspan = 1
            if line[5] in ROWSPAN or line[6] in ROWSPAN:
                rowspan = ROWSPAN[line[5]]
            if line[4] == 'Joint':
                style = ''
                if line[5] in YELLOW:
                    style = 'background-color: #FFF9DB;'
                elif line[5] in BLUE:
                    style = 'background-color: #c7f2ff;'
                elif line[5] in GREEN:
                    style = 'background-color: #e8ffea;'
                elif line[5] in RED:
                    style = 'background-color: #fdcdcd;'
                if 'Invited Talk' in line[5]:
                    print(f'<td style="{style}" colspan="2" rowspan="{rowspan}"><a style="color: #900011;" href="/#{line[6]}">{line[5]}</a></td>', end='')
                elif 'Panel' in line[5]:
                    print(f'<td style="{style}" colspan="2" rowspan="{rowspan}"><a style="color: #900011;" href="/panels#{line[6]}">{line[5]}</a></td>', end='')
                elif 'Social' in line[5] and line[5] != 'Social: Get Together':
                    print(f'<td style="{style}" colspan="2" rowspan="{rowspan}"><a style="color: #900011;" href="/social-events#{line[6]}">{line[5]}</a></td>', end='')
                else:
                    extend_by_20min = ""
                    if line[5] == "Community Meeting":
                        extend_by_20min = "<br /> (ends +20min)"
                    print(f'<td style="{style}" colspan="2" rowspan="{rowspan}">{line[5]}{extend_by_20min}</td>', end='')
            elif line[4] == 'Single':
                delay_by_20min = ""
                if line[5] in ['30a', '31a']:
                    delay_by_20min = "<br/><span style='color: #900011;'>(start: +20 min)</span>"
                print(f'<td rowspan="{rowspan}"><a style="color: #900011;" href="#{line[5]}">({line[5]}) {line[7]}</a>{delay_by_20min}</td><td rowspan="{rowspan}"><a style="color: #900011;" href="#{line[6]}">({line[6]}) {line[8]}</a>{delay_by_20min}</td>', end='')
            elif line[4] == 'Empty':
                print('<td colspan="2"></td>', end='')
    print('</tr>')
print('</table>')
