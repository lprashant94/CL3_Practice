import QuickSort



def search(list, element):
    length = len(list)
    mid =(int)(length/2)
    if(length == 0 ):
        print('Not Found')
        return 0
    print('First element ',str(list[0]),'last element ',str(list[length-1]),'mid element ',str(list[mid]))
    if list[mid] == element :
        print('element found at index =',str(mid))
        #this index is not correct as mid is specified here
        return 1
    elif list[mid] >element:
        print('Left side')
        return search(list[:mid],element)
    else:
        print('Right side')
        return search(list[mid:length],element)

l=[1,5,2,3,7,47,9,0]
s=QuickSort.sorting(l)

print(search(s.input_list,0))
