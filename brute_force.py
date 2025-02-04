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

def two_sum():
    nums = list(map(int, input("Enter the input data array items: ").split()))
    target = int(input("Enter the target value: "))

    # Brute force approach using two loops
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f"Output: {i} {j}")
                return

# Run the function
two_sum()
