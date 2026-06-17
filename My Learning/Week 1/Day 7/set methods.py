# set methods

my_set = {1, 2, 3}

# === ADDING ===
my_set.add(4)           # Add one item → {1, 2, 3, 4}
my_set.update([5, 6])   # Add multiple → {1, 2, 3, 4, 5, 6}

# === REMOVING ===
my_set.remove(4)        # Removes 4, ERROR if not present
my_set.discard(99)      # Removes 99, NO error if not present (safer)
my_set.pop()            # Removes RANDOM item (no order)
my_set.clear()          # Empty the set → set()

# === CHECKING ===
3 in my_set             # True/False
len(my_set)             # Number of items

# === SET OPERATIONS (THE POWER) ===
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a.union(b)              # {1,2,3,4,5,6} (all from both)
a | b                   # Same as union (operator)

a.intersection(b)       # {3, 4} (only common)
a & b                   # Same (operator)

a.difference(b)         # {1, 2} (in a but not b)
a - b                   # Same (operator)

a.symmetric_difference(b)  # {1, 2, 5, 6} (in either, NOT both)
a ^ b                      # Same (operator)

# === RELATIONSHIPS ===
{1, 2}.issubset({1, 2, 3})    # True (all elements in bigger set)
{1, 2, 3}.issuperset({1, 2})  # True (contains all of smaller)
{1, 2}.isdisjoint({3, 4})     # True (no common elements)

# === CONVERSION ===
set([1, 2, 2, 3])       # {1, 2, 3} (from list)
list({1, 2, 3})         # [1, 2, 3] (to list)
set("hello")            # {'h', 'e', 'l', 'o'} (from string)


# BIGGEST MISTAKE
# WRONG:
empty = {}              # This is an empty DICT, not a set!

# RIGHT:
empty = set()           # Empty set

# Once you add items, it becomes a set:
empty.add(1)            # Now it's {1}