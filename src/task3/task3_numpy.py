import numpy as np
marks=np.array([[78,85,90],[65,70,80],[88,92,95],[55,60,72]])
print('shape:',marks.shape)
print('size:',marks.size)
print("\nstudent averages:",np.round(marks.mean(axis=1),2))
print("\nsubject averages:",np.round(marks.mean(axis=0),2))

grace_marks=marks+5
print("\nmarks after grace mark added:",grace_marks)
weights=np.array([0.5 ,0.3 ,0.2])
weighted_scores=np.dot(marks,weights)
print("\n weighted scores:",np.round(weighted_scores,2))

