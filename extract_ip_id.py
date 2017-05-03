import re
# omport regular expressions that we use to parse logs
ip_re = re.compile('\d+\.\d+\.\d+\.\d+')
# ip extrcation is simple, bacause every line starts with ip
id_re = re.compile('(?<=group/).+?/')
# for id extraction we use positive lookbehind assertion
# with the pattern 'group/', which preceeds every id

def extract_digits(import_line):
    ip = ip_re.match(import_line)
    id = id_re.search(import_line)
    return ip, id

f_out = open('output.csv', 'a')
# opening output csv-file in the appending-to-the-end mode

f_log = open('access.log', 'r')
# opening file to process
for line in f_log:
    a, b = extract_digits(line)
#   wtite down the exact numbers in backup variables
    if b:
        f_out.write(a.group(0) + ',' + b.group(0)[:-2] + '\n')
#   adding a string with ip (first) and id (second), if it has id
#   adding [:-2] deletes backspace at the end of id (it looks nicer)
f_log.close()

f_out.close()
