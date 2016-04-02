



def search(list, element):
    length = len(list)
    mid =(int)(length/2)
    if(mid == 0 ):
        print('Not Found')
        return 0
    print('First element ',str(list[0]),'last element ',str(list[length-1]),'mid element ',str(list[mid]))
    if list[mid] == element :
        print('element found at index =',str(mid))
        return 1
    elif list[mid] >element:
        print('Left side')
        return search(list[:mid],element)
    else:
        print('Right side')
        return search(list[mid:length],element)



print(search(range(1,10),10))
