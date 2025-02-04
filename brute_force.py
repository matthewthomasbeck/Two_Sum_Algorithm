################################################################################
# This code and its associated files were created at the instruction of        #
# professors at the University of Texas at San Antonio during my time as a     #
# student at the university. I, as a student, was not responsible for the idea #
# behind this code (i.e. project guidelines, functionality, and end purpose),  #
# but I, Matthew Thomas Beck, can confirm that myself and any project partners #
# (if applicable) were the ones responsible for writing it.                    #
################################################################################





###########################################
############### BRUTE FORCE ###############
###########################################


########## TWO SUM FUNCTION ##########

def two_sum(): # function to implement two sum algorithm via brute force

    ##### get user input #####

    nums = list(map(int, input("Enter the input data array items: ").split()))
    target = int(input("Enter the target value: "))

    ##### brute force approach #####

    for i in range(len(nums)): # loop through input data array

        for j in range(i + 1, len(nums)): # loop through input data array

            if nums[i] + nums[j] == target: # if sum of two numbers equals target...

                print(f"Output: {i} {j}") # print output

                return # end function


########## RUN FUNCTION ##########

two_sum() # run the function
