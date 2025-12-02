namespace advent_of_code.solutions._2025._01;

class Solution(string inputDirectory, string testInputDirectory) : BaseSolution(inputDirectory, testInputDirectory)
{
    protected override int Year => 2025;
    protected override int Day => 1;
    
    protected override string PartOneTestAnswer => "3";
    protected override string PartTwoTestAnswer => "6";


    protected override string SolvePartOne(string[] input)
    {
        int count = 0;
        int num = 50;
        foreach (string line in input)
        {
            bool isAdding = line.StartsWith('R');
            int increment = int.Parse(line[1..]);
            if (isAdding)
            {
                num += increment;
                num %= 100;
            }
            else
            {
                num -= increment;
                num += 100;
                num %= 100;
            }
            
            if (num == 0) count++;
        }
        
        return count.ToString();
    }

    protected override string SolvePartTwo(string[] input)
    {
        int count = 0;
        int num = 50;
        foreach (string line in input)
        {
            bool isAdding = line.StartsWith('R');
            int increment = int.Parse(line[1..]);
            if (isAdding)
            {
                for (int i = 0; i < increment; i++)
                {
                    num += 1;
                    if (num == 100)
                    {
                        num = 0;
                        count += 1;
                    }
                }
            }
            else
            {
                for (int i = 0; i < increment; i++)
                {
                    num -= 1;
                    switch (num)
                    {
                        case -1:
                            num = 99;
                            break;
                        case 0:
                            count += 1;
                            break;
                    }
                }
            }
        }
        
        return count.ToString();
    }
}