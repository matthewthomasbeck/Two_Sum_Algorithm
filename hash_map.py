################################################################################
# This code and its associated files were created at the instruction of        #
# professors at the University of Texas at San Antonio during my time as a     #
# student at the university. I, as a student, was not responsible for the idea #
# behind this code (i.e. project guidelines, functionality, and end purpose),  #
# but I, Matthew Thomas Beck, can confirm that myself and any project partners #
# (if applicable) were the ones responsible for writing it.                    #
################################################################################





########################################
############### HASH MAP ###############
########################################


########## TWO SUM FUNCTION ##########

def two_sum(): # function to implement two sum algorithm via hash map

    ##### set variables #####

    num_map = {}

    ##### get user input #####

    nums = list(map(int, input("Enter the input data array items: ").split())) # input data array
    target = int(input("Enter the target value: ")) # target value

    ##### hash map approach #####

    for i, num in enumerate(nums): # loop through input data array

        complement = target - num # calculate complement

        if complement in num_map: # if complement is in hash table...

            print(f"Output: {num_map[complement]} {i}") # print output

            return # end function

        num_map[num] = i # add to hash table

        print(f"Adding to hash table: key:{num}, value: {i}") # print hash table addition


########## RUN FUNCTION ##########

two_sum() # run the function