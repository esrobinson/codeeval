public class Assignment3
{
    public static void main(String[] args)
    {   
        int[] binary = { 1, 7, 4, 9, 10, 2, 6, 12, 3, 8, 5 };
        // for(int i = 0; i < binary.length; i++)
        // {
        //     System.out.print(binary[i] + " ");
        // }

        System.out.println(ModifiedBinarySearch(binary, binary[1]));
        ModifiedBinaryInsertionSort(binary);

    }

    static int ModifiedBinarySearch(int[] theArray, int theElement)
    {
        int leftIndex = 0;
        int rightIndex = theArray.length - 1;
        int middleIndex = 0;

        while(leftIndex <= rightIndex)
        {
            middleIndex = (leftIndex + rightIndex) / 2;

            if (theElement == theArray[middleIndex])
                return middleIndex;
            else if (theElement < theArray[middleIndex])
                rightIndex = middleIndex - 1;
            else
                leftIndex = middleIndex + 1;
        }

        return middleIndex - 1;
    }

    static void ModifiedBinaryInsertionSort(int[] theArray)
    {
        int i = 0;
        int[] returnArray = new int[theArray.length + 1];

        for(i = 0; i < theArray.length; i++)
        {
            returnArray[ModifiedBinarySearch(theArray, theArray[i])] = theArray[i];
            // System.out.println(ModifiedBinarySearch(theArray, theArray[i]));
        }

        for(i = 0; i < theArray.length; i++)
        {
            // System.out.print(returnArray[i] + " ");
        }
    }
}