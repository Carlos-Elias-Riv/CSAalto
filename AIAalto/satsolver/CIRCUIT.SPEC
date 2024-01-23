# Organizing a Party
#
# Which combinations of five friends could be invited
# to a party, if there are some constraint that prevent
# inviting them all?

# Declare a propositional variable for each friend.
# Variable X being TRUE means "X is invited" and
# X being FALSE means "X is not invited".
#

variables i0, i1, i2, i3, o0, o1, o2, o3, a1, a2, a3, c;

# first variable
i0 and i1 <-> a1;

# second variable
a1 and i2 <-> a2;

# third variable
a2 and i3 <-> a3;

# output 0
not i0 <-> o0;

# output 1
i0 xor  i1  <-> o1;

# output 2
a1 xor i2 <-> o2;

# output 3
a2 xor i3 <-> o3;

# control variable
a3 <-> c;
