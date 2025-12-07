using advent_of_code.solutions;

// Parse command line arguments
string inputDirectory = "";
string testInputDirectory = "";

for (int i = 0; i < args.Length; i++)
{
    if (args[i] == "-i" && i + 1 < args.Length)
    {
        inputDirectory = args[i + 1];
        i++;
    }
    else if (args[i] == "-t" && i + 1 < args.Length)
    {
        testInputDirectory = args[i + 1];
        i++;
    }
}

List<BaseSolution> solutions =
[
    new advent_of_code.solutions._2025._01.Solution(inputDirectory, testInputDirectory),
    new advent_of_code.solutions._2025._02.Solution(inputDirectory, testInputDirectory),
    new advent_of_code.solutions._2025._03.Solution(inputDirectory, testInputDirectory),
    new advent_of_code.solutions._2025._04.Solution(inputDirectory, testInputDirectory),
    new advent_of_code.solutions._2025._05.Solution(inputDirectory, testInputDirectory),
    new advent_of_code.solutions._2025._06.Solution(inputDirectory, testInputDirectory),
    new advent_of_code.solutions._2025._07.Solution(inputDirectory, testInputDirectory),
];

BaseSolution mostRecentSolution = solutions.Last();
mostRecentSolution.TestSolution(1);
mostRecentSolution.RunSolution(1);
mostRecentSolution.TestSolution(2);
mostRecentSolution.RunSolution(2);