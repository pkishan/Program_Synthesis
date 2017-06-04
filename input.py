# In this file the user presents his inputs

#Some conventions to be followed while giving the inputs
""" When mentioning a line segment we will align then in the same way as we
defined in the sides array.

When mentioning an angle we will use the same allignments as the one used in
the angles array

"""
#END OF CONVENTIONS

#Creating a list that will contain all the input rules that are given by the
#user

User_Rules = []


#These two lists will have the sides of both the triangles.
sides_one = [("A", "B"), ("B", "C"), ("C", "A")]
sides_two = [("B", "E"), ("E", "F"), ("F", "B")] 

#These are the tow lists that will have the angles from both tirnalges 

angles_one = [("A", "B", "C"), ("B", "C", "A"), ("C", "A", "B")]
angles_two = [("B", "E", "F"), ("E", "F", "B"), ("F", "B", "E")]

User_Rules.append((("Parallel", "Across"), (("A", "C"), ("E", "F"), ("C",
                                                                     "E"))))
