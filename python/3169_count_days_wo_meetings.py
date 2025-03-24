from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        merged_meetings = []
        last_meeting = meetings[0]
        for meeting_start, meeting_end in meetings[1:]:
            if meeting_start <= last_meeting[1] + 1:
                last_meeting[1] = max(meeting_end, last_meeting[1])
            else:
                merged_meetings.append(last_meeting)
                last_meeting = [meeting_start, meeting_end]

        if len(merged_meetings) == 0 or last_meeting != merged_meetings[-1]:
            merged_meetings.append(last_meeting)

        num_of_days_available = days - merged_meetings[-1][1] + merged_meetings[0][0] - 1
        for day_idx in range(len(merged_meetings) - 1):
            num_of_days_available += merged_meetings[day_idx + 1][0] - merged_meetings[day_idx][1] - 1

        return num_of_days_available


if __name__ == '__main__':
    s = Solution()
    inputs = [
        {'days': 10, 'meetings': [[5, 7], [1, 3], [9, 10]]},
        {'days': 5, 'meetings': [[2, 4], [1, 3]]}
    ]

    input_idx = 1
    print(s.countDays(inputs[input_idx]['days'],
                      inputs[input_idx]['meetings']))
