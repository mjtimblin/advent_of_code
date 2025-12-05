namespace advent_of_code.solutions._2025._05;

class Solution(string inputDirectory, string testInputDirectory) : BaseSolution(inputDirectory, testInputDirectory)
{
    protected override int Year => 2025;
    protected override int Day => 5;
    
    protected override string PartOneTestAnswer => "3";
    protected override string PartTwoTestAnswer => "14";


    private static bool IsNumberValid(long number, List<Tuple<long, long>> ranges)
    {
        return ranges.Any(range => number >= range.Item1 && number <= range.Item2);
    }

    private static Tuple<long, long>? GetUniqueRange(Tuple<long, long> range, List<Tuple<long, long>> ranges)
    {
        long start = range.Item1;
        long end = range.Item2;
        
        foreach (Tuple<long, long> existingRange in ranges)
        {
            // Skip if there is no overlap
            if (end < existingRange.Item1 || start > existingRange.Item2) continue;
            
            // If the range is completely contained within another range, return early
            if (existingRange.Item1 <= start && existingRange.Item2 >= end)
            {
                return null;
            }

            if (existingRange.Item1 <= start && existingRange.Item2 >= start)
            {
                start = existingRange.Item2 + 1;
            }

            if (existingRange.Item1 <= end && existingRange.Item2 >= end)
            {
                end = existingRange.Item1 - 1;
            }
        }
        
        return end < start ? null : new Tuple<long, long>(start, end);
    }
    
    
    protected override string SolvePartOne(string[] input)
    {
        List<Tuple<long, long>> ranges = [];
        List<long> validNumbers = [];

        bool breakFound = false;
        foreach (string line in input)
        {
            if (line == "")
            {
                breakFound = true;
                continue;
            }
            
            if (!breakFound)
            {
                string[] rangeStrings = line.Split('-');
                Tuple<long, long> range = new (long.Parse(rangeStrings[0]), long.Parse(rangeStrings[1]));
                ranges.Add(range);
            }
            else
            {
                long number = long.Parse(line);
                if (IsNumberValid(number, ranges))
                {
                    validNumbers.Add(number);
                }
            }
        }
        return validNumbers.Count.ToString();
    }

    protected override string SolvePartTwo(string[] input)
    {
        List<Tuple<long, long>> ranges = [];

        foreach (string line in input)
        {
            if (line == "")
            {
                break;
            }

            string[] rangeStrings = line.Split('-');
            ranges.Add(new Tuple<long, long>(long.Parse(rangeStrings[0]), long.Parse(rangeStrings[1])));
        }
        
        ranges = ranges.OrderBy(range => range.Item1).ToList();
        List<Tuple<long, long>> filteredRanges = [];
        foreach (Tuple<long, long> range in ranges)
        {
            Tuple<long, long>? modifiedRange = GetUniqueRange(range, filteredRanges);
            if (modifiedRange != null) filteredRanges.Add(modifiedRange);
        }

        long validNumbersCount = filteredRanges.Sum(range => range.Item2 - range.Item1 + 1);
        return validNumbersCount.ToString();
    }
}