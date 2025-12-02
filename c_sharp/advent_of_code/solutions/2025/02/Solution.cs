namespace advent_of_code.solutions._2025._02;

class Solution(string inputDirectory, string testInputDirectory) : BaseSolution(inputDirectory, testInputDirectory)
{
    protected override int Year => 2025;
    protected override int Day => 2;
    
    protected override string PartOneTestAnswer => "1227775554";
    protected override string PartTwoTestAnswer => "4174379265";

    
    private static bool IsNumberADouble(long number)
    {
        string numberString = number.ToString();
        if (numberString.Length % 2 == 1) return false;
        string firstHalf = numberString[..(numberString.Length / 2)];
        string secondHalf = numberString[(numberString.Length / 2)..];
        return firstHalf == secondHalf;
    }
    
    private static bool IsNumberMadeOfRepeats(long number)
    {
        string numberString = number.ToString();
        for (int i = 1; i <= (numberString.Length / 2); i++)
        {
            if (numberString.Length % i != 0)
            {
                continue;
            }
            
            string pattern = numberString[..i];
            if (numberString == string.Concat(Enumerable.Repeat(pattern, numberString.Length / i)))
            {
                return true;
            }
        }

        return false;
    }
    

    protected override string SolvePartOne(string[] input)
    {
        long sum = 0;
        string line = input[0];
        string[] ranges = line.Split(',');
        foreach (string range in ranges)
        {
            string[] rangeParts = range.Split('-');
            long min = long.Parse(rangeParts[0]);
            long max = long.Parse(rangeParts[1]);
            for (long i = min; i <= max; i++)
            {
                if (IsNumberADouble(i))
                {
                    sum += i;
                }
            }
        }
        return sum.ToString();
    }

    protected override string SolvePartTwo(string[] input)
    {
        long sum = 0;
        string line = input[0];
        string[] ranges = line.Split(',');
        foreach (string range in ranges)
        {
            string[] rangeParts = range.Split('-');
            long min = long.Parse(rangeParts[0]);
            long max = long.Parse(rangeParts[1]);
            for (long i = min; i <= max; i++)
            {
                if (IsNumberMadeOfRepeats(i))
                {
                    sum += i;
                }
            }
        }
        return sum.ToString();    }
}