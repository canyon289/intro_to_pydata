"""
Parse timing and Sections from markdown file
"""

from collections import namedtuple
import re
import pandas as pd

FILE_NAME = "day_3.md"
# Named tuples are convenient and friendly way to keep track of things

cols = ["Section", "Activity", "Category", "Minutes"]
TIMING_ROW_C = namedtuple("timing_row", cols)

REGEX_PATTERN = "\ (.+)\((\d+)"

# Define regex patterns to parse time and title


def section_name(line):
    """Section Names are on lines with ###"""
    if "###" in line and "Section" in line:
        section_name = line[3:]
        section_name = section_name.rstrip()
        return section_name


def activity_name_and_minutes(line):
    """Parse activity name from each line"""
    if "####" in line:
        match = re.findall(REGEX_PATTERN, line)

        try:
            match = match[0]
            activity, time = match[0], match[1]
        except IndexError:
            raise Exception(f"Broken Line: {line}")

        # Remove leading and trailing whitepaces
        activity = activity.rstrip()

        for category in ("instructor", "break", "buffer", 
                "student", "all", "partner"):
            if category in activity.lower():
                break

        return activity, time, category.capitalize()

    return None, None, None

        
file_handle = open(FILE_NAME, "r")
file_lines = file_handle.readlines()


timing_rows = []
for line in file_lines:
    possible_section_name = section_name(line)

    if possible_section_name: 
        _section_name = possible_section_name

    activity, time, category = activity_name_and_minutes(line)
    if activity:
        assert time, "Activity and time should both appear"
        
        timing_row = TIMING_ROW_C(_section_name, activity, category, time)
        timing_rows.append(timing_row)
        
# Write csv to disk
df = pd.DataFrame(timing_rows)
print(df)
df.to_csv(f"{FILE_NAME}_timing_export.csv")
