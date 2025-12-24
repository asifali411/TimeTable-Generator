from ortools.sat.python import cp_model

model = cp_model.CpModel()

#Maybe can add Saturday too
days=['Mon','Tue','Wed','Thu','Fri']

#Can be inputted in later
rooms=['Room101','Room102','Room103','Room104','Room105']
times=['9am','10am','11am','12pm','1pm','2pm','3pm']
teachers=['Bob','Charlie','Alice','Greg','Tracy','Dave','Steve','Harry','Alex','WalterWhite','Lunch','FREE']

#Feel free to change the structure, but please explain, if you do
shifts={}
#The Order is **Teacher,day,room,time**

for t in teachers:
    for d in days:
        for r in rooms:
            for time in times:
                shifts[(t,d,r,time)]= model.NewBoolVar(f"{t}_{d}_{r}_{time}")

#Constraint 1: On a Specific day,a teacher can only occupy one class at a time
for t in teachers:
    if t != 'Lunch':
        for d in days:
            for time in times:
                model.add(sum(shifts[t,d,r,time] for r in rooms) <= 1)

#Constraint 2: All Periods must be filled
for d in days:
    for r in rooms:
        for time in times:
            model.Add(sum(shifts[t,d,r,time] for t in teachers)==1)

#Constraint 3: A teacher can take n classes per week, the total of all should be (no of rooms * no of days * no of time slots) 
teacher_limits = {
    'Bob': 14,    
    'Charlie': 14,
    'Alice': 14,
    'Greg' : 14,
    'Tracy' :14,
    'Dave' : 14,
    'Steve' : 14,
    'Harry' : 14,
    'Alex' : 14,
    'WalterWhite' : 14,
    'FREE': 10,
    'Lunch' : 25
}

for t in teachers:
    my_shifts = [shifts[t,d,r,time] for d in days for r in rooms for time in times]

    model.Add(sum(my_shifts)==teacher_limits[t])

#constraint 4: there should not be more than 1 class of the same teacher on the same room
for d in days:
    for t in teachers:
        for r in rooms:
            model.Add(sum(shifts[t,d,r,time] for time in times) <= 1)

#constraint 5: there should not be a free period in the morning
for d in days:
    for r in rooms:
        model.Add(sum(shifts['FREE',d,r,time] for time in ['9am','10am']) == 0)

# Constraint 6: 12pm is strictly for Lunch
for r in rooms:
    for d in days:
        model.Add(shifts[('Lunch', d, r, '12pm')] == 1)


#-------Solver----------
solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    for d in days:
        print(f"{d}:")
        for time in times:
            print(f"\n{time}:")
            for r in rooms:
                for t in teachers:
                    if solver.Value(shifts[(t, d, r, time)]) == 1:
                        print(f"  {r}: {t}")
        print("\n")
else:
    print("No Solution Found!!!")