# unordered, unindexed, no dulicates, mutable
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

x1 = {"a", "b", "c"}
x2 = {"b", "c", "d"}

# union
print(x1.union(x2))

# metszet
print(x1.intersection(x2))

# különbség
print(x1.difference(x2))

# szimetrikus különbség
print(x1.symmetric_difference(x2))

# részhalmaz-e
print(x1.issubset({"a", "b", "c", "d"}))

# szuperhalmaz-e
print(x1.issuperset({"a", "b"}))

# vannak e közös elemek
print({"b"}.isdisjoint(x2))


x1 | x2
# .union() method will take any iterable as an argument, convert it to a set, and then perform the union
x1.union(x2)

# intersection
x1.intersection(x2)
x1 & x2

# difference
x1.difference(x2)
x1 - x2

# symmetric_difference
# return the set of all elements in either x1 or x2, but not both
x1.symmetric_difference(x2)
x1 ^ x2

# isdisjoint
# returns True if x1 and x2 have no elements in common
{"b"}.isdisjoint(x2)
x2 - {"b"}

# issubset
# Determine whether one set is a subset of the other.
x1.issubset({"a", "b", "c", "d"})
x1 <= x2

# x1 > x2 returns True if x1 is a proper superset of x2:
# x1 = {'foo', 'bar', 'baz'}
# x2 = {'foo', 'bar'}
# x1 > x2

x1.issuperset({"foo", "bar"})
x1 >= x2
