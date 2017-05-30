import meta_inferences as mi
import input as inp
C = mi.Inferences
Inference_pool = [] 
#inp.input_rules 
for i in C:
    if i[0] == "Similar" and i[1][0] == "Angle" and i[1][1] == "Angle":
        a1 = inp.angles_one[0]
        a2 = inp.angles_one[1]
        for angle1 in inp.angles_two:
            b1 = angle1
            for angle2 in inp.angles_two:
                if angle2 != angle1:
                    b2 = angle2
                    Inference_pool.append(("Similar", "Angle_Angle", (a1, b1), (a2,
                                                                            b2)))


print Inference_pool



