class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # Final answer list
        res = []

        # Traverse all existing intervals
        for i in range(len(intervals)):

            # CASE 1:
            # New interval comes completely BEFORE current interval
            # Example:
            # new = [1,2]
            # curr = [5,7]
            if newInterval[1] < intervals[i][0]:

                # Add merged/new interval
                res.append(newInterval)

                # Remaining intervals are already sorted,
                # so directly return answer
                return res + intervals[i:]

            # CASE 2:
            # New interval comes completely AFTER current interval
            # Example:
            # curr = [1,2]
            # new = [5,7]
            elif newInterval[0] > intervals[i][1]:

                # Current interval has no overlap
                # so keep it as it is
                res.append(intervals[i])

            # CASE 3:
            # Overlapping intervals
            # Example:
            # curr = [1,3]
            # new = [2,5]
            else:

                # Merge intervals by:
                # taking minimum start
                # taking maximum end
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]

        # If new interval belongs at the end
        # add it after loop finishes
        res.append(newInterval)

        return res