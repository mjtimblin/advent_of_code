namespace advent_of_code.solutions._2025._04;

class Solution(string inputDirectory, string testInputDirectory) : BaseSolution(inputDirectory, testInputDirectory)
{
    protected override int Year => 2025;
    protected override int Day => 4;
    
    protected override string PartOneTestAnswer => "13";
    protected override string PartTwoTestAnswer => "43";


    private List<List<bool>> _paperGrid = [];

    private void PopulatePaperGrid(string[] input)
    {
        _paperGrid = [];
        foreach (string line in input)
        {
            List<bool> gridLine = line.Select(c => c == '@').ToList();
            _paperGrid.Add(gridLine);
        }
    }

    private int CountSurroundingPaper(int rowIndex, int colIndex)
    {
        int count = 0;

        int maxRows = _paperGrid.Count;
        int maxCols = _paperGrid[rowIndex].Count;

        bool hasTopNeighbor = rowIndex > 0;
        bool hasBottomNeighbor = rowIndex < maxRows - 1;
        bool hasLefthandNeighbor = colIndex > 0;
        bool hasRighthandNeighbor = colIndex < maxCols - 1;
        
        // There is a row above
        if (hasTopNeighbor)
        {
            if (hasLefthandNeighbor)
            {
                // Top left
                count += _paperGrid[rowIndex - 1][colIndex - 1] ? 1 : 0;
            }
            
            // Top middle
            count += _paperGrid[rowIndex - 1][colIndex] ? 1 : 0;
            
            if (hasRighthandNeighbor)
            {
                // Top right
                count += _paperGrid[rowIndex - 1][colIndex + 1] ? 1 : 0;
            }
        }
        
        if (hasLefthandNeighbor)
        {
            // Middle left
            count += _paperGrid[rowIndex][colIndex - 1] ? 1 : 0;
        }
        if (hasRighthandNeighbor)
        {
            // Top right
            count += _paperGrid[rowIndex][colIndex + 1] ? 1 : 0;
        }
        
        if (hasBottomNeighbor)
        {
            if (hasLefthandNeighbor)
            {
                // Top left
                count += _paperGrid[rowIndex + 1][colIndex - 1] ? 1 : 0;
            }
            
            // Bottom middle
            count += _paperGrid[rowIndex + 1][colIndex] ? 1 : 0;
            
            if (hasRighthandNeighbor)
            {
                // Top right
                count += _paperGrid[rowIndex + 1][colIndex + 1] ? 1 : 0;
            }
        }

        return count;
    }

    private List<Tuple<int, int>> GetIndicesOfRemovablePaper()
    {
        List<Tuple<int, int>> removablePaperIndices = [];
        for (int rowNum = 0; rowNum < _paperGrid.Count; rowNum++)
        {
            for (int colNum = 0; colNum < _paperGrid[rowNum].Count; colNum++)
            {
                if (_paperGrid[rowNum][colNum] && CountSurroundingPaper(rowNum, colNum) < 4)
                {
                    removablePaperIndices.Add(new Tuple<int, int>(rowNum, colNum));
                }
            }
        }
        return removablePaperIndices;
    }
    
    
    protected override string SolvePartOne(string[] input)
    {
        PopulatePaperGrid(input);
        return GetIndicesOfRemovablePaper().Count.ToString();
    }

    protected override string SolvePartTwo(string[] input)
    {
        PopulatePaperGrid(input);
        int count = 0;
        bool canRemoveMore = true;
        while (canRemoveMore)
        {
            List<Tuple<int, int>> removablePaperIndices = GetIndicesOfRemovablePaper();
            canRemoveMore = removablePaperIndices.Count > 0;
            foreach (Tuple<int, int> removablePaperIndex in removablePaperIndices)
            {
                _paperGrid[removablePaperIndex.Item1][removablePaperIndex.Item2] = false;
                count++;
            }
        }
        return count.ToString();
    }
}