import csv

def fetch_times(row):
  times = [
    'Day 1: 11UTC',
    'Day 1: 18UTC',
    'Day 2: 18UTC',
    'Day 2: 24UTC',
    'Day 3: 11UTC',
    'Day 3: 24UTC',
    'Day 4: 11UTC',
  ]
  return ''.join([f'<li>{times[c]}</li>' for c in range(7) if 'x' in row[c+3].strip()])

# load the data.csv with csv library
data = {}
with open('data.csv') as f:
    reader = csv.reader(f)
    for row in list(reader)[3:]:

        awardpre = '(<span style="color:red"><a href="/awards#demo">'
        awardpost = '</a></span>) '
        award = ''
        if row[0] == '382': # machetli
            award = awardpre + '1st Place' + awardpost
        elif row[0] == '377': # planutils
            award = awardpre + '2nd Place' + awardpost
        elif row[0] == '379': # UP
            award = awardpre + '3rd Place' + awardpost

        data[row[0]] = {
            'authors': row[1],
            'title': row[2],
            'pid': row[0],
            'poster': row[11],
            'demo': row[12],
            'award': award,
            'times': fetch_times(row)
        }


TEMPLATE = """
      <section id="demo-{pid}" class="demo">
        <div class="row">
          <div class="12u 12u(mobile)">
            <h1>{award}<span class="demo-title">{title}</span></h1>
            <img src="{pid}.png" alt="{title}" />
            <h2>{authors}</h2>
            <h3>Scheduled Sessions</h3>
            <ul>{times}</ul>
            <a style="margin-left: 10px" class="button float-right-button"
                href="{poster}">Poster</a>
            <a style="margin-left: 10px" class="button float-right-button"
                href="ICAPS_2022_paper_{pid}.pdf">Paper</a>
            <a style="margin-left: 10px" class="button float-right-button"
                href="{demo}">Demo</a>
          </div>
        </div>
      </section>
"""

print('<div class="row"><div id="demo-list-1" class="6u 12u(mobile)">')

ul = ""

count = 0
for pid in data:
    ul += f'<li><a href="#demo-{pid}">{data[pid]["title"]}</a></li>\n'
    print(TEMPLATE.format(**data[pid]))
    count += 1
    if count == 5:
        print('</div><div id="demo-list-2" class="6u 12u(mobile)">')
print('</div></div>')

# print(ul)
