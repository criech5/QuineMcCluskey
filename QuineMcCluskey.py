#This program aims to find prime implicants through the use of the Quine-McCluskey algorithm.
#Input the number of variables first, followed by the minterms of the logic equation.

def sort_by_ones(list_of_terms, num_vars):
    #This function will sort the given list of minterms by the number of ones it contains.
    #It returns a dictionary, with lists of terms accessed by the number of ones as the keys.
    zeros = []
    ones = []
    twos = []
    threes = []
    fours = []
    fives = []
    sixes = []
    for term in list_of_terms:
        one_count = 0
        for digit in term:
            if digit == '1':
                one_count +=1
        if one_count == 0:
            zeros.append(term)
        if one_count == 1:
            ones.append(term)
        if one_count == 2:
            twos.append(term)
        if one_count == 3:
            threes.append(term)
        if one_count == 4:
            fours.append(term)
        if one_count == 5:
            fives.append(term)
        if one_count == 6:
            sixes.append(term)

    sorted_terms = {}

    if num_vars == 1:
        sorted_terms = {
            0 : zeros,
            1 : ones
        }
    if num_vars == 2:
        sorted_terms = {
            0 : zeros,
            1 : ones,
            2 : twos
        }
    if num_vars == 3:
        sorted_terms = {
            0 : zeros,
            1 : ones,
            2 : twos,
            3 : threes
        }
    if num_vars == 4:
        sorted_terms = {
            0 : zeros,
            1 : ones,
            2 : twos,
            3 : threes,
            4 : fours
        }
    if num_vars == 5:
        sorted_terms = {
            0 : zeros,
            1 : ones,
            2 : twos,
            3 : threes,
            4 : fours,
            5 : fives
        }
    if num_vars == 6:
        sorted_terms = {
            0 : zeros,
            1 : ones,
            2 : twos,
            3 : threes,
            4 : fours,
            5 : fives,
            6: sixes
        }


    return sorted_terms

def define_term(bin_input):
    #This function serves to convert a binary term obtained from Q-M into a term with the provided variables.
    #It returns a string for a single term.

    #NEED TO ADD ERROR CHECKING WITH LESS THAN 1 VARIABLE

    output_str = ""

    #The first variable (A)
    var = bin_input[0]
    if var == '1':
        output_str += 'A'
    elif var == '0':
        output_str += '~A'

    #The second variable (B)
    if len(bin_input) >= 2:
        var = bin_input[1]
        if (var == '1'):
            output_str += 'B'
        elif (var == '0'):
            output_str += '~B'

    #The third variable (C)
    if len(bin_input) >= 3:
        var = bin_input[2]
        if var == '1':
            output_str += 'C'
        elif var == '0':
            output_str += '~C'

    #The fourth variable (D)
    if len(bin_input) >= 4:
        var = bin_input[3]
        if var == '1':
            output_str += 'D'
        elif var == '0':
            output_str += '~D'

    #The fifth variable (E)
    if len(bin_input) >= 5:
        var = bin_input[4]
        if var == '1':
            output_str += 'E'
        elif var == '0':
            output_str += '~E'

    #The sixth variable (F)
    if len(bin_input) >= 6:
        var = bin_input[5]
        if var == '1':
            output_str += 'F'
        elif var == '0':
            output_str += '~F'

    return output_str

def check_if_match(input_1, input_2):
    #This function checks two terms to see if they should be marked off in the method.
    #It returns a boolean value.
    if len(input_1) != len(input_2):
        return False
    term_len = len(input_1)
    count = 0
    for i in range (term_len - 1):
        if input_1[i] != input_2[i]:
            count +=1
    if count == 1:
        return True
    else:
        return False

def match_inputs(input_1, input_2):
    #This function matches two terms if they have been marked off.
    #It returns a string with the modified ("matched") binary term.
    term_len = len(input_1)
    matched_str = ""
    for i in range(term_len):
        if input_1[i] != input_2[i]:
            matched_str += '-'
        else:
            matched_str += input_1[i]
    return matched_str

def parse_and_sort(minterm_string):
    #This function parses the input minterm string and converts it to a list, then sorts using insertion sort.
    #It returns a sorted list of ints.
    min_list = minterm_string.split(',')
    for i in range (len(min_list)):
        point = int(min_list[i])
        while i > 0 and int(min_list[i - 1]) > point:
            min_list[i] = int(min_list[i - 1])
            i -= 1
        min_list[i] = point
    return min_list

def minterm_list_to_bin_list(min_list, num_vars):
    #This function converts a list of minterms into a list of binary strings.
    #It returns a list of binary strings.
    binary_list = []
    for minterm in min_list:
        if num_vars == 1:
            bin_rep = '{0:01b}'.format(int(minterm))
        if num_vars == 2:
            bin_rep = '{0:02b}'.format(int(minterm))
        if num_vars == 3:
            bin_rep = '{0:03b}'.format(int(minterm))
        if num_vars == 4:
            bin_rep = '{0:04b}'.format(int(minterm))
        if num_vars == 5:
            bin_rep = '{0:05b}'.format(int(minterm))
        if num_vars == 6:
            bin_rep = '{0:06b}'.format(int(minterm))
        binary_list.append(bin_rep)
    return binary_list

def quine_mccluskey(num_vars, binary_list):
    #This function takes the number of variables and the binary list to complete the Q-M algorithm.
    #It returns prime implicants in a list of strings.
    sorted_terms = sort_by_ones(binary_list, num_vars)
    new_matches = []
    for i in range (num_vars):
        for j in range (len(sorted_terms.get(i))):
            been_matched = False
            for k in range (len(sorted_terms.get(i + 1))):
                if check_if_match(sorted_terms.get(i)[j], sorted_terms.get(i + 1)[k]):
                    if (match_inputs(sorted_terms.get(i)[j], sorted_terms.get(i + 1)[k]) in new_matches) == False:
                        new_matches.append(match_inputs(sorted_terms.get(i)[j], sorted_terms.get(i + 1)[k]))
                    been_matched = True
            if been_matched == False:
                if (sorted_terms.get(i)[j] in new_matches) == False:
                    new_matches.append(sorted_terms.get(i)[j])
    if new_matches == binary_list:
        return new_matches
    return quine_mccluskey(num_vars, new_matches)

def essential_prime(prime_imps):
    #This function determines the essential prime implicants given a list of the prime implicants.
    #It enumerates all possibilities given '-' and checks if other implicants contain the same minterms.
    #It returns a list of essential prime implicants.
    imp_dict = {}
    for imp in prime_imps:
        imp_list = []



def main():
    num_vars = int(input("How many variables does your expression have? "))
    if num_vars > 6:
        print("Invalid number of variables")
        pass
    minterm_string = input("Minterm representation (comma delimited): ")
    db_list = parse_and_sort(minterm_string)
    bin_list = minterm_list_to_bin_list(parse_and_sort(minterm_string), num_vars)
    qm_list = quine_mccluskey(num_vars, bin_list)

    conv_list = []
    for item in qm_list:
        conv_list.append(define_term(item))
    print(conv_list)

main()
