
# Simple time-tabling problem for a school with 4 teachers, 3 groups/classes,
# and 14 different subject to teach.

# Predicates
#
# CanTeach(t,c)        Teacher t can teach class c
# ClassTime(c,g,s)     Class c is taught to group g at time slot s.
# ClassDay(c,g,s)      Class c is taught to group g on day d.
# ClassTeacher(c,g,t)  Class c is taught to group g by teacher t.

predicates CanTeach / 2, ClassTime / 3, ClassDay / 3, ClassTeacher / 3;

# Teachers

type teachers = { matti, maija, paavo, ritva };

# Subjects/classes

type courses = { math1, math2, physics1, physics2, chemistry, english1, english2, history, biology, sports1, sports2, swedish1, swedish2 };

# There is teaching on three weekdays.

type days = { monday, tuesday, wednesday };

# The integer range of 1-hour time slots for teaching

type times = [8,12];

# Each of the groups of students (classes) that need to be taught

type groups = { grpA, grpB, grpC };

# What can each teacher teach?

CanTeach(matti,physics1);
CanTeach(matti,physics2);
CanTeach(matti,swedish1);
CanTeach(maija,math1);
CanTeach(maija,math2);
CanTeach(maija,chemistry);
CanTeach(paavo,english1);
CanTeach(paavo,english2);
CanTeach(ritva,biology);
CanTeach(ritva,sports1);
CanTeach(ritva,sports2);
CanTeach(paavo,history);
CanTeach(paavo,swedish1);
CanTeach(paavo,swedish2);

# Each course except swedish1 has exactly one teacher. The following
# is needed to infer that certain teachers CANNOT teach a course.

forall ( c : courses - {swedish1} ) exactly 1 (t : teachers) CanTeach(t,c);

# We listed only 2 teachers as capable of teaching swedish1. Others cannot.

exactly 2 (t : teachers) CanTeach(t,swedish1);

# We could have alternatively listed lots of atomic formulas such as
# not CanTeach(matti,math1); not CanTeach(matti,math2);
# but this would be tedious and error-prone to write.

# The remaining constraints define what is an acceptable schedule.
# 1. The teacher must be qualified for the course.
# 2. A teacher can teach only one course and group at a time.
# 3. A group can be taught only one course at a time.
# 4. Each course&group has a unique weekday, time, and teacher.
#

# Your task is to express the above 4 constraints:
# (Don't change anything above this line!)
# (You are not allowed to explicitly mention any of the
# - groups' names
# - teachers' names
# - classes' names
# Hint: Each constraint is one line, or a couple of lines long only.

# 1. Teacher of a class must be one qualified to teach it
forall (c: courses, t: teachers, g: groups) ClassTeacher(c, g, t) -> CanTeach(t, c);
# 2. Teacher in only one class at a time.
forall (t: teachers, d: days, s: times) atmost 1 (c: courses, g: groups) (ClassTeacher(c, g, t) and ClassDay(c, g, d) and ClassTime(c, g, s));
# 3. Group having only one class at a time.
forall (g: groups, c: courses, d: days, s: times) atmost 1 (t: teachers) (ClassTeacher(c, g, t) and ClassDay(c, g, d) and ClassTime(c, g, s));
# 4. Every group has for every class a unique day, time, teacher.
forall (c: courses, g: groups) exactly 1 (d: days, s: times, t: teachers) (ClassTeacher(c, g, t) and ClassDay(c, g, d) and ClassTime(c, g, s));


# 1. Teacher of a class must be one qualified to teach it

#forall (c: courses, t: teachers, g: groups) ClassTeacher(c, g, t) -> CanTeach(t, c);

# 2. Teacher in only one class at a time.

#forall (t: teachers, d: days, s: times) 
#    atmost 1 (c: courses, g: groups) 
#        ClassTeacher(c, g, t) and ClassDay(c, g, d) and ClassTime(c, g, s);


# 3. Group having only one class at a time.


#forall (g: groups, d: days)
#  atmost 1 (c: courses)
#    ClassDay(c, g, d);

# 4. Every group has for every class a unique day, time, teacher.

#forall (c: courses, g: groups) 
#    exactly 1 (d: days, s: times, t: teachers) 
#        ClassTeacher(c, g, t) and ClassDay(c, g, d) and ClassTime(c, g, s);


# CanTeach(t,c)        Teacher t can teach class c
# ClassTime(c,g,s)     Class c is taught to group g at time slot s.
# ClassDay(c,g,d)      Class c is taught to group g on day d.
# ClassTeacher(c,g,t)  Class c is taught to group g by teacher t.

#The syntax supports the following connectives:
#   not         negation
#   and  &      conjunction
#   or  |       disjunction
#   xor         exclusive or
#   ->  impl    implication
#   <->  eqvi   equivalence

#Additionally, there are the following quantifiers with parameters.

#   forall          Universal quantification
#   exists forsome  Existential quantification
#   atleast N       Cardinality lower bound
#   atmost N        Cardinality upper bound
#   exactly N       Cardinality
