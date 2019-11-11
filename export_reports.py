import reports
from printing import *

# Export functions
def export_count(a):
    with open('export_reports.txt', 'a') as out:
        out.write(str(a) + "\n")

def export_decide(a):
    with open('export_reports.txt', 'a') as out:
        out.write(str(a) + "\n")

def export_latest(a):
    with open('export_reports.txt', 'a') as out:
        out.write(str(a) + "\n")

def export_genre(a):
    with open('export_reports.txt', 'a') as out:
        out.write(str(a) + "\n")

def export_title_line_number(a):
    with open('export_reports.txt', 'a') as out:
        out.write(str(a) + "\n")
