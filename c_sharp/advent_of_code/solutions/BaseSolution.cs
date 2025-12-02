namespace advent_of_code.solutions;

public abstract class BaseSolution(string inputDirectory, string testInputDirectory)
{
    protected abstract int Year { get; }
    protected abstract int Day { get; }
    protected abstract string PartOneTestAnswer { get; }
    protected abstract string PartTwoTestAnswer { get; }

    protected abstract string SolvePartOne(string[] input);
    protected abstract string SolvePartTwo(string[] input);

    public void TestSolution(int partToTest=1)
    {
        string[] input = GetInput(true);

        if (partToTest == 1)
        {
            string partOneSolution = SolvePartOne(input);
            if (partOneSolution != PartOneTestAnswer)
            {
                throw new Exception($"Part one test failed. Expected {PartOneTestAnswer}, got {partOneSolution}");
            }
            Console.WriteLine("Part one test passed");
        }
        else
        {
            string partTwoSolution = SolvePartTwo(input);
            if (partTwoSolution != PartTwoTestAnswer)
            {
                throw new Exception($"Part two test failed. Expected {PartTwoTestAnswer}, got {partTwoSolution}");
            }
            Console.WriteLine("Part two test passed");
        }
    }

    public void RunSolution(int partToRun=1)
    { 
        string[] input = GetInput();
        if (partToRun == 1)
        {
            string partOneSolution = SolvePartOne(input);
            Console.WriteLine($"Part one: {partOneSolution}");
        }
        else
        {
            string partTwoSolution = SolvePartTwo(input);
            Console.WriteLine($"Part two: {partTwoSolution}");
        }
    }
    
    private string[] GetInput(bool isTestInput=false)
    {
        string directory = isTestInput ? testInputDirectory : inputDirectory;
        string inputFilePath = $"{directory}/{Year}_{Day:D2}.txt";
        if (!File.Exists(inputFilePath))
        {
            throw new FileNotFoundException($"Input file not found for {Year}_{Day:D2} ({inputFilePath})");
        }
        return File.ReadAllLines(inputFilePath);
    }
}