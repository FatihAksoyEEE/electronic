from __future__ import annotations

def capacitor_parallel(capacitors: list[float]) -> float:
    """
    Calculates equivalent capacitance for capacitors connected in parallel.

    Formula:
      C_eq = C1 + C2 + ... + Cn

    All capacitor values must be non-negative. Zero-valued capacitors are allowed
    (they simply don't contribute).
    """

    total = 0.0
    for index, capacitor in enumerate(capacitors):
        if capacitor < 0:
            raise ValueError(f"Capacitor at index {index} has a negative value: {capacitor}")
        total += float(capacitor)
    return total


def capacitor_series(capacitors: list[float]) -> float:
    """
    Calculates equivalent capacitance for capacitors connected in series.

    Formula:
      1/C_eq = 1/C1 + 1/C2 + ... + 1/Cn

    All capacitor values must be positive (cannot include zero or negative values)
    because division by zero or negative capacitances are invalid in this context.
    """

    if not capacitors:
        raise ValueError("At least one capacitor is required for series calculation")

    inv_sum = 0.0
    for index, capacitor in enumerate(capacitors):
        if capacitor <= 0:
            raise ValueError(f"Capacitor at index {index} must be > 0 for series calculation: {capacitor}")
        inv_sum += 1.0 / float(capacitor)

    return 1.0 / inv_sum


def get_capacitor_values(required_capacitance: float, count: int) -> dict:
    """
    Given a desired equivalent capacitance and a number of identical capacitors,
    return the per-capacitor value required for both parallel and series
    arrangements.

    Assumptions:
      - All capacitors used are equal-valued.
      - For parallel: C_each = C_required / n
      - For series:  C_each = n * C_required

    Parameters:
      required_capacitance: desired equivalent capacitance (float, > 0)
      count: number of identical capacitors to use (int, >= 1)

    Returns:
      dict with keys:
        - 'per_capacitor_parallel'
        - 'per_capacitor_series'

    Raises:
      ValueError for invalid inputs.
    """

    if count < 1:
        raise ValueError("count must be an integer >= 1")
    if required_capacitance <= 0:
        raise ValueError("required_capacitance must be a positive number")

    per_parallel = float(required_capacitance) / count
    per_series = float(required_capacitance) * count

    return {
        "per_capacitor_parallel": per_parallel,
        "per_capacitor_series": per_series,
    }


if __name__ == "__main__":
    import sys

    def parse_capacitor_list(input_str: str) -> list[float]:
      """Parse a comma/space separated list of numbers into floats, validate non-negativity."""
      if not input_str.strip():
        raise ValueError("No capacitor values provided")
      # Accept commas or spaces as separators
      parts = [p.strip() for p in input_str.replace(',', ' ').split()]
      values: list[float] = []
      for i, p in enumerate(parts):
        try:
          val = float(p)
        except ValueError:
          raise ValueError(f"Could not parse capacitor value at position {i}: '{p}'")
        if val < 0:
          raise ValueError(f"Capacitor at position {i} has negative value: {val}")
        values.append(val)
      return values

    def input_positive_float(prompt: str) -> float:
      while True:
        try:
          s = input(prompt).strip()
          v = float(s)
          if v <= 0:
            print("Please enter a positive number.")
            continue
          return v
        except ValueError:
          print("Invalid number, try again.")

    def input_int_ge1(prompt: str) -> int:
      while True:
        try:
          s = input(prompt).strip()
          v = int(s)
          if v < 1:
            print("Please enter an integer >= 1.")
            continue
          return v
        except ValueError:
          print("Invalid integer, try again.")

    def menu() -> None:
      print("Capacitor equivalence helper\n")
      print("Options:")
      print("  1) Calculate equivalent capacitance from a list of capacitors")
      print("  2) Compute per-capacitor values to achieve a required equivalent")
      print("  q) Quit")

      while True:
        choice = input('\nSelect option (1/2/q): ').strip().lower()
        if choice == '1':
          # ask series or parallel
          mode = input("Series or Parallel? (s/p): ").strip().lower()
          try:
            raw = input("Enter capacitor values (comma or space separated): ")
            caps = parse_capacitor_list(raw)
            if mode == 'p' or mode == 'parallel':
              eq = capacitor_parallel(caps)
              print(f"Equivalent capacitance in parallel: {eq}")
            elif mode == 's' or mode == 'series':
              eq = capacitor_series(caps)
              print(f"Equivalent capacitance in series: {eq}")
            else:
              print("Unknown mode; enter 's' for series or 'p' for parallel.")
          except Exception as e:
            print("Error:", e)
        elif choice == '2':
          try:
            req = input_positive_float("Enter required equivalent capacitance: ")
            n = input_int_ge1("Enter number of identical capacitors: ")
            vals = get_capacitor_values(req, n)
            print(f"To get {req} (with {n} identical capacitors):")
            print(" - per capacitor (parallel):", vals['per_capacitor_parallel'])
            print(" - per capacitor (series):", vals['per_capacitor_series'])
          except Exception as e:
            print("Error:", e)
        elif choice == 'q' or choice == 'quit':
          print("Goodbye")
          return
        else:
          print("Unknown option, try again.")

    try:
      # If arguments provided, run a quick non-interactive example for convenience
      if len(sys.argv) > 1:
        # keep backward compatible: show previous example
        capacitors_parallel = [2.0, 3.0, 4.0]
        capacitors_series = [2.0, 3.0, 4.0]
        print("Equivalent capacitance in parallel:", capacitor_parallel(capacitors_parallel))
        print("Equivalent capacitance in series:", capacitor_series(capacitors_series))
      else:
        menu()
    except (KeyboardInterrupt, EOFError):
      print('\nInterrupted, exiting')

    import doctest
    doctest.testmod()