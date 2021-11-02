"""Module for finding test results of quarantined people using dual indices."""
from classes2 import Name
import tools

def mergeSort(tested, quarantined):
    results = [None] * len(quarantined)
    if len(tested)>1:
        lefthalf = tested
        righthalf = quarantined
        
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            person = righthalf[i]
            nhi, name, result = lefthalf[i] 
            print(person < name)
            print(name)
            if person <= name:
                results[k]=(person, nhi, result)
                i=i+1
            else:
                results[k]=(person, None, None)
                j=j+1
            k+=1

        while i < len(lefthalf):
            i=i+1
            #k=k+1

        while j < len(righthalf):
            unfound_name = righthalf[j]
            tup = (unfound_name, None, None)
            results[k]=tup
            j=j+1
            k=k+1
    
    return(results)
            
if __name__ == '__main__':
    # put your own simple tests here
    # you don't need to submit this code
    filename = "test_data/test_data-10n-10n-1-a.txt"    
    tested, quarantined, expected_results = tools.read_test_data(filename)
    print(mergeSort(tested, quarantined))
    print(expected_results)
