namespace advent_of_code.solutions._2025._07;

class Solution(string inputDirectory, string testInputDirectory) : BaseSolution(inputDirectory, testInputDirectory)
{
    protected override int Year => 2025;
    protected override int Day => 7;
    
    protected override string PartOneTestAnswer => "21";
    protected override string PartTwoTestAnswer => "40";

    protected override string SolvePartOne(string[] input)
    {
        HashSet<int> beamLocationIndices = [];
        int numberOfSplits = 0;
        
        for (int i = 0; i < input[0].Length; i++)
        {
            char c = input[0][i];
            if (c == 'S')
            {
                beamLocationIndices.Add(i);
            }
        }
        
        foreach (string line in input[1..])
        {
            HashSet<int> newBeamLocationIndices = [];

            for (int i = 0; i < line.Length; i++)
            {
                char c = line[i];
                if (c == '^')
                {
                    if (beamLocationIndices.Contains(i))
                    {
                        numberOfSplits++;
                        newBeamLocationIndices.Add(i + 1);
                        newBeamLocationIndices.Add(i - 1);
                    }
                } 
                else if (beamLocationIndices.Contains(i))
                {
                    newBeamLocationIndices.Add(i);
                }
            }

            beamLocationIndices = newBeamLocationIndices;
        }
        return numberOfSplits.ToString();
    }

    protected override string SolvePartTwo(string[] input)
    {
        long[] numberOfTimelinesAtIndex = new long[input[0].Length];
    
        for (int i = 0; i < input[0].Length; i++)
        {
            char c = input[0][i];
            if (c == 'S')
            {
                numberOfTimelinesAtIndex[i] = 1;
            }
            else
            {
                numberOfTimelinesAtIndex[i] = 0;
            }
        }
        
        foreach (string line in input[1..])
        {
            long[] newNumberOfTimelinesAtIndex = new long[numberOfTimelinesAtIndex.Length];
            for (int i = 0; i < newNumberOfTimelinesAtIndex.Length; i++) newNumberOfTimelinesAtIndex[i] = 0;

            for (int i = 0; i < line.Length; i++)
            {
                char c = line[i];
                if (c == '^')
                {
                    if (numberOfTimelinesAtIndex[i] > 0)
                    {
                        newNumberOfTimelinesAtIndex[i - 1] += numberOfTimelinesAtIndex[i];
                        newNumberOfTimelinesAtIndex[i + 1] += numberOfTimelinesAtIndex[i];
                    }
                } 
                else if (numberOfTimelinesAtIndex[i] > 0)
                {
                    newNumberOfTimelinesAtIndex[i] += numberOfTimelinesAtIndex[i];
                }
            }

            numberOfTimelinesAtIndex = newNumberOfTimelinesAtIndex;
        }

        return numberOfTimelinesAtIndex.Sum().ToString();
    }
}
