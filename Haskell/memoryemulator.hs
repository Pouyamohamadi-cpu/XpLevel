module MemoryLibrary (
    Memory,
    createMemory,
    readMemory,
    writeMemory
) where

type Memory = [Int]

createMemory :: Int -> Int -> Memory
createMemory size initialValue = replicate size initialValue

readMemory :: Int -> Memory -> Either String Int
readMemory address memory
    | address < 0 || address >= length memory = Left "Error: Invalid address for reading!"
    | otherwise = Right (memory !! address)

writeMemory :: Int -> Int -> Memory -> Either String Memory
writeMemory address value memory
    | address < 0 || address >= length memory = Left "Error: Invalid address for writing!"
    | otherwise = Right (take address memory ++ [value] ++ drop (address + 1) memory)