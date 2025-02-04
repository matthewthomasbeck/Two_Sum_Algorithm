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

def two_sum():
    nums = list(map(int, input("Enter the input data array items: ").split()))
    target = int(input("Enter the target value: "))

    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            print(f"Output: {num_map[complement]} {i}")
            return
        num_map[num] = i
        print(f"Adding to hash table: key:{num}, value: {i}")

# Run the function
two_sum()