def update (data , nama , field , value ) : 
  for item in data : 
    if item [ 'nama' ]   ==   nama : 
      item [ field ]   =   value     
  return   data
