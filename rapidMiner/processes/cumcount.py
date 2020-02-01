def rm_main(data):
    #receive data set as data

   #Sort data by year of memberclimb to ensure eperience is calculated in correct order
    data.sort_values("myear", axis = 0, ascending = True, 
                 inplace = True, na_position ='last')
    
    #create new colum showing the experience of a climber by counting the apperance of the unique identifier
    #from a combination of lastname and fristname
    data["climber_experience"] = data.groupby([data["lname_fname"]]).cumcount()+1

    return data