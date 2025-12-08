from ortools.sat.python import cp_model

model = cp_model.CpModel()

#Maybe can add Saturday too
days=['Mon','Tue','Wed','Thu','Fri']

#Can be inputted in later
rooms=[]
times=[]
teachers=[]

#Feel free to change the structure, but please explain, if you do
shifts={}
