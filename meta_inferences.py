#In the meta inference, Always use a touple for the inference rules
# Example (a, (b)) - even if b is the only thing that is needed. This helps
#in the searching process.
Inferences = []
Inferences.append(("Similar",("Angle_Angle", "Angle_Angle")))
Inferences.append((("Angle_Angle"),( "Intersect_lines")))


