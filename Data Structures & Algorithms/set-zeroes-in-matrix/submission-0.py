class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # Dimensions of matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # Special flag for first row
        # because matrix[0][0] is shared by:
        # first row and first column
        rowZero = False

        # STEP 1:
        # Use first row and first column as markers
        for r in range(ROWS):
            for c in range(COLS):

                # Found a zero
                if matrix[r][c] == 0:

                    # Mark corresponding column
                    matrix[0][c] = 0

                    # Mark corresponding row
                    if r > 0:
                        matrix[r][0] = 0

                    # If zero is in first row,
                    # store separately
                    else:
                        rowZero = True

        # STEP 2:
        # Traverse remaining matrix
        # and set values to zero using markers
        for r in range(1, ROWS):
            for c in range(1, COLS):

                # If row OR column marked
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # STEP 3:
        # Handle first column separately
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # STEP 4:
        # Handle first row separately
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0