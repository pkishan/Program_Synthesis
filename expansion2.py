import meta_inferences as mi
import input as inp
C = mi.Inferences
Inference_pool = [] 
#inp.input_rules 

for element in inp.User_Rules:
    Inference_pool.append((element, "NULL"))


for i in C:
    if i[0] == "Similar" and i[1][0] == "Angle_Angle" and i[1][1] =="Angle_Angle":
        a1 = inp.angles_one[0]
        a2 = inp.angles_one[1]
        for angle1 in inp.angles_two:
            b1 = angle1
            for angle2 in inp.angles_two:
                if angle2 != angle1:
                    b2 = angle2
                    Inference_pool.append(("Similar",("Angle_Angle", (a1,
                                                                       b1)),
                                           ("Angle_Angle", (a2, b2))))
    if i[0] == "Angle_Angle" and i[1] == "Intersect_lines":
        for angle1 in inp.angles_one:
            a1 = angle1
            for angle2 in inp.angles_two:
                b1 = angle2
                if a1[1] == b1[1]:
                    Inference_pool.append((("Angle_Angle", (a1, b1)),
                                           ("Intersect_lines", ((a1[0], b1[0]),
                                                               (a1[1],
                                                                b1[1])))
                                            ))
                    Inference_pool.append((("Angle_Angle", (a1, b1)),
                                           ("Intersect_lines", ((a1[0], b1[1]),
                                                               (a1[1],
                                                                b1[0])))
                                            ))
                    
    if i[0] == "Angle_Angle" and i[1] == (("Parallel", "Across")):
        for angle1 in inp.angles_one:
            a1 = angle1
            for angle2 in inp.angles_two:
                b1 = angle2
                Inference_pool.append((("Angle_Angle", (a1, b1)), (("Parallel",
                                                                   "Across"),((a1[0],
                                                                             a1[1])),
                                                                  (b1[0],
                                                                   b1[1]),
                                                                   (a1[1],
                                                                    b1[1])) )) 
                Inference_pool.append((("Angle_Angle", (a1, b1)), (("Parallel",
                                                                   "Across"),((a1[0],
                                                                             a1[1])),
                                                                  (b1[0],
                                                                   b1[1]),
                                                                   (b1[1],
                                                                    a1[1])) )) 
                #Note that we have to take all the possible combinations of the
                #vertices so that at least one of them matches the input by the
                #user.
                #Complete this but take care of what to write 
            


for element in Inference_pool:
    print element























