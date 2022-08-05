#buscar por inicial los empleados
employees = model.search([], limit=500)
names = []
for e in employees:
  if e.name[0].lower() == "n": 
    names.append(e.name)
   
raise Warning(names)