
import sys

def convert(in_file, out_file):
    with open(in_file, 'r') as f:
        lines = [l.strip() for l in f.readlines()]

    new_lines = []

    # First, combine all lines that are not empty
    for line in lines:
        if (line == '') or (line[0] in ['-', '*']):
            new_lines.append(line)
        else:
            new_lines[-1] += ' ' + line

    # Convert the rest
    for i in range(len(new_lines)):
        line = new_lines[i].replace('\t', ' ').replace('\r', '').replace('\n', '').strip()
        if line == '':
            new_lines[i] = ''
        elif line[:2] == '# ':
            new_lines[i] = '<h3>' + line[2:] + '</h3>'
        elif line[0] in ['-', '*']:
            new_lines[i] = '<li>' + line[1:] + '</li>'
        elif line[:3] in [f'{i}. ' for i in range(1,10)]:
            new_lines[i] = '<li>' + line[3:] + '</li>'
        else:
            new_lines[i] = '<p>' + line + '</p>'

    with open(out_file, 'w') as f:
        for line in new_lines:
            f.write(line + '\n')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: convert.py <input_file> <output_file>')
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert(input_file, output_file)

