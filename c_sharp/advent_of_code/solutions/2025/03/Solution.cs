namespace advent_of_code.solutions._2025._03;

class Solution(string inputDirectory, string testInputDirectory) : BaseSolution(inputDirectory, testInputDirectory)
{
    protected override int Year => 2025;
    protected override int Day => 3;
    
    protected override string PartOneTestAnswer => "357";
    protected override string PartTwoTestAnswer => "3121910778619";


    private static long LargestNumber(string line, int digitCount)
    {
        int[] largestNumberIndices = new int[digitCount];
        for (int i = 0; i < digitCount; i++)
        {
            largestNumberIndices[i] = i;
        }
        for (int testCharIndex = 1; testCharIndex < line.Length; testCharIndex++)
        {
            char charToTest = line[testCharIndex];

            int firstDigitWithSpaceLeft = 0;
            if (line.Length - testCharIndex < digitCount)
            {
                firstDigitWithSpaceLeft = digitCount - (line.Length - testCharIndex);
            }

            for (int j = firstDigitWithSpaceLeft; j < largestNumberIndices.Length && largestNumberIndices[j] < testCharIndex; j++)
            {
                if (charToTest > line[largestNumberIndices[j]])
                {
                    for (int k = 0; k < largestNumberIndices.Length - j; k++)
                    {
                        largestNumberIndices[j + k] = testCharIndex + k;
                    }

                    break;
                }
            }
        }
        char[] largestNumber = largestNumberIndices.Select(i => line[i]).ToArray();
        return long.Parse(new string(largestNumber));
    }
    
    
    protected override string SolvePartOne(string[] input)
    {
        return input.Sum(line => LargestNumber(line, 2)).ToString();
    }

    protected override string SolvePartTwo(string[] input)
    {
        return input.Sum(line => LargestNumber(line, 12)).ToString();
    }
}