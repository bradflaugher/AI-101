import pandas
from collections import defaultdict
import operator

df = pandas.read_parquet("./sports_fans.snappy.parquet")

segment_count = defaultdict(int)

user_set = set()

count = 0

for index, row in df.iterrows():

    # do not take into account same user_id more than once
    # do not consider empty segments
    if (row["user_id"] not in user_set) and row["segments"] != "":
        if len(row["segments"].split(",")) <= 1:
            segment_count[(row["state"], row["segments"])] += 1

    user_set.add(row["user_id"])


def get_mostt_likely_segment(in_state):
    count_per_state={}
    for items in segment_count.keys():
        if items[0] == in_state:
            count_per_state[items[1]] = segment_count[items]

    if len(count_per_state) == 0:
        return ""

    return max(count_per_state.items(), key=operator.itemgetter(1))[0]

print(get_mostt_likely_segment("New York"))

