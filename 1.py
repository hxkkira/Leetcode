import sys

def twoSum( num, target):
    tmp=sorted(num);
    i=0;
    j=len(num)-1;
    while True:
        addup=tmp[i]+tmp[j];
        print target;
        print addup;
        if addup>target:
            j=j-1;
        elif addup<target:
            i=i+1;
        elif addup==target:
            print "break";
            break;
    index1=num.index(tmp[i])+1;
    if tmp[i]==tmp[j]:
        num.pop(index1-1);
        index2=num.index(tmp[j])+2;
    else:
        index2=num.index(tmp[j])+1;
    return (index1,index2);

def main():
    print twoSum([0,4,2,0],0);
if __name__ == '__main__':
    main()
