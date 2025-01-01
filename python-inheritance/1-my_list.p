class MyList(list):
  """MyList class that inherits from the built-in list class.

  Provides a custom method to print the list elements in ascending order.
  """

  def print_sorted(self):
    """Prints the list elements in ascending order.

    Sorts a copy of the list to avoid modifying the original list during printing.
    """
    print(sorted(self))
