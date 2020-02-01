def rm_main(data):
    #receive data set as data

    #create new colum showing the experience of a climber by counting the apperance of the unique identifier
    #from a combination of lastname and fristname
    data["climber_experience"] = data.groupby([data["lname_fname"]]).cumcount()+1

    return data