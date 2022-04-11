def trip_planner_welcome(name):
  print('Welcome to tripplanner v1.0 ' + name)
trip_planner_welcome('')

#Step 2
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time
estimate = estimated_time_rounded(10.4)

#Step 3 message for users' planner 
def destination_setup(origin, destination, estimated_time, mode_of_transport = 'Car'):

#Step 4 print statements
  print('Your trip starts off in ' + origin)
  print('And you are traveling to ' + destination)
  print('You will be traveling by ' + mode_of_transport)
  print('It will take approximately ' + str(estimated_time), 'hours.')

# destination_setup('Bangkok', 'Chiang Mai', estimate, 'Car')

# Call the function here. Input the info 
trip_planner_welcome("Joe")
estimate = estimated_time_rounded(3.55)
destination_setup("Hua Hin.", "Bangkok.", estimate, "Van.")

 
