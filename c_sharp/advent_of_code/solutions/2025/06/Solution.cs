using System.Text.RegularExpressions;

namespace advent_of_code.solutions._2025._06;

class Solution(string inputDirectory, string testInputDirectory) : BaseSolution(inputDirectory, testInputDirectory)
{
    protected override int Year => 2025;
    protected override int Day => 6;
    
    protected override string PartOneTestAnswer => "4277556";
    protected override string PartTwoTestAnswer => "3263827";
    
    private List<long> GetNumbersFromLine(string line)
    {
        List<long> numbers = [];
        MatchCollection matches = Regex.Matches(line, "([0-9]+)");
        foreach (Match match in matches)
        {
            numbers.Add(long.Parse(match.Value));
        }
        return numbers;
    }

    private List<string> GetOperatorsFromLine(string line)
    {
        List<string> operators = [];
        MatchCollection matches = Regex.Matches(line, "([-+/*])");
        foreach (Match match in matches)
        {
            operators.Add(match.Value);
        }
        return operators;
    }

    private List<long> GetCephalopodNumbersFromList(List<string> numbers, int columnWidth)
    {
        string[] workingNumbers = numbers.ToArray();
        List<long> cephalopodNumbers = [];
        
        for (int i = columnWidth - 1; i >= 0; i--)
        {
            string currentDigit = "";
            for (int j = 0; j < workingNumbers.Length; j++)
            {
                if (workingNumbers[j].Last() != ' ')
                {
                    currentDigit += workingNumbers[j].Last();
                }
                workingNumbers[j] = workingNumbers[j][0..^1];
            }
            cephalopodNumbers.Add(long.Parse(currentDigit));
        }

        return cephalopodNumbers;
    }
    
    
    protected override string SolvePartOne(string[] input)
    {
        List<long> columns = GetNumbersFromLine(input[0]);
        List<string> operators = GetOperatorsFromLine(input.Last());

        foreach (string line in input[1..^1])
        {
            List<long> numbers = GetNumbersFromLine(line);
            for (int i = 0; i < numbers.Count; i++)
            {
                switch (operators[i])
                {
                    case "+":
                        columns[i] += numbers[i];
                        break;
                    case "-":
                        columns[i] -= numbers[i];
                        break;
                    case "*":
                        columns[i] *= numbers[i];
                        break;
                    case "/":
                        columns[i] /= numbers[i];
                        break;
                }
            }
        }
        
        return columns.Sum().ToString();
    }

    protected override string SolvePartTwo(string[] input)
    {
        List<List<string>> columns = [];
        List<int> columnWidths = [];
        List<string> operators = GetOperatorsFromLine(input.Last());

        int currentWidth = 1;
        foreach (char c in input.Last().Skip(1))
        {
            if (c == ' ')
            {
                currentWidth += 1;
            }
            else
            {
                columnWidths.Add(currentWidth - 1);
                currentWidth = 1;
            }
        }
        columnWidths.Add(currentWidth);
        
        string firstLine = input[0];
        int index = 0;
        foreach (int width in columnWidths)
        {
            columns.Add([firstLine.Substring(index, width)]);
            index += (width + 1);
        }

        foreach (string line in input[1..^1])
        {
            index = 0;
            for (int i = 0; i < columns.Count; i++)
            {
                columns[i].Add(line.Substring(index, columnWidths[i]));
                index += columnWidths[i] + 1;
            }
        }


        List<List<long>> cephalopodNumbers = [];
        List<long> solutions = [];

        for (int i = 0; i < columns.Count; i++)
        {
            List<long> numbers = GetCephalopodNumbersFromList(columns[i], columnWidths[i]);
            solutions.Add(numbers.First());
            numbers.RemoveAt(0);
            cephalopodNumbers.Add(numbers);
        }
        
        for (int i = 0; i < solutions.Count; i++)
        {
            foreach (long number in cephalopodNumbers[i]) {
                switch (operators[i])
                {
                    case "+":
                        solutions[i] += number;
                        break;
                    case "-":
                        solutions[i] -= number;
                        break;
                    case "*":
                        solutions[i] *= number;
                        break;
                    case "/":
                        solutions[i] /= number;
                        break;
                }
            }
        }

        return solutions.Sum().ToString();
    }
}