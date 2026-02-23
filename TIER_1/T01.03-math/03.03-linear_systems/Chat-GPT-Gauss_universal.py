import numpy as np

def gauss_solve(A, b, eps=1e-12, verbose=True):
    """
    Gaussian elimination with partial pivoting.
    Returns dict with status and (if possible) one solution.
    status: 'unique', 'infinite', 'none'
    """
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1)

    m, n = A.shape
    if b.shape[0] != m:
        raise ValueError(f"Size mismatch: A is {m}x{n}, b has length {b.shape[0]}")

    Ab = np.column_stack([A, b])

    if verbose:
        print("Initial [A|b]:\n", Ab)
        print("A.shape:", A.shape, "b.shape:", b.shape)

    row = 0
    piv_cols = []

    # Forward elimination
    for col in range(n):
        # Find pivot row
        pivot = row + np.argmax(np.abs(Ab[row:, col]))
        pivot_val = Ab[pivot, col] if row < m else 0.0

        if row >= m:
            break

        if abs(pivot_val) < eps:
            continue  # no pivot in this column

        # Swap
        if pivot != row:
            Ab[[row, pivot]] = Ab[[pivot, row]]
            if verbose:
                print(f"\nSwap R{row+1} <-> R{pivot+1}")
                print(Ab)

        piv_cols.append(col)

        # Eliminate below
        for r in range(row + 1, m):
            factor = Ab[r, col] / Ab[row, col]
            if abs(factor) < eps:
                continue
            Ab[r, :] -= factor * Ab[row, :]
            if verbose:
                print(f"\nR{r+1} <- R{r+1} - ({factor:.6g})*R{row+1}")
                print(Ab)

        row += 1
        if row == m:
            break

    # Check consistency by ranks
    rankA = np.linalg.matrix_rank(Ab[:, :n], tol=eps)
    rankAug = np.linalg.matrix_rank(Ab, tol=eps)

    if verbose:
        print("\nAfter forward elimination [A|b]:\n", Ab)
        print("rank(A):", rankA, "rank([A|b]):", rankAug)

    if rankA < rankAug:
        return {"status": "none", "x": None, "Ab": Ab, "rankA": rankA, "rankAug": rankAug}

    # Back substitution for one solution
    x = np.zeros(n, dtype=float)

    # If rankA == n -> unique
    if rankA == n:
        # make sure we use the first n pivot rows
        for i in range(n - 1, -1, -1):
            # find pivot col for row i: assume pivot in column i after pivoting is not guaranteed
            # We'll locate first nonzero in row i among first n columns
            pivot_col = None
            for c in range(n):
                if abs(Ab[i, c]) > eps:
                    pivot_col = c
                    break
            if pivot_col is None:
                continue
            s = Ab[i, -1] - Ab[i, pivot_col+1:n] @ x[pivot_col+1:n]
            x[pivot_col] = s / Ab[i, pivot_col]

        return {"status": "unique", "x": x, "Ab": Ab, "rankA": rankA, "rankAug": rankAug}

    # Infinite solutions: choose free vars = 0 and solve pivots
    # Identify pivot columns (from Ab after elimination): first nonzero in each nonzero row
    pivot_cols = []
    for r in range(m):
        pc = None
        for c in range(n):
            if abs(Ab[r, c]) > eps:
                pc = c
                break
        if pc is not None:
            pivot_cols.append(pc)

    free_cols = [c for c in range(n) if c not in pivot_cols]

    # set free vars to 0; solve pivot vars from bottom
    for r in range(len(pivot_cols) - 1, -1, -1):
        pc = pivot_cols[r]
        rhs = Ab[r, -1]
        # subtract known terms
        for c in range(pc + 1, n):
            rhs -= Ab[r, c] * x[c]
        x[pc] = rhs / Ab[r, pc]

    return {
        "status": "infinite",
        "x": x,
        "free_cols": free_cols,
        "Ab": Ab,
        "rankA": rankA,
        "rankAug": rankAug
    }
