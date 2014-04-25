import qualified System.IO
import qualified Control.Exception
import Data.Char
import qualified Data.List
import qualified System.Directory
import System.Environment
import qualified Data.ByteString.Lazy as B

main = do
    handle <- System.IO.openFile "girl.txt" System.IO.ReadMode
    contents <- System.IO.hGetContents handle
    putStr contents
    System.IO.hClose handle

main2 = do
    System.IO.withFile "girl.txt" System.IO.ReadMode (\handle -> do
        contents <- System.IO.hGetContents handle
        putStr contents)

withFile' :: FilePath -> System.IO.IOMode -> (System.IO.Handle -> IO a) -> IO a
withFile' name mode f = Control.Exception.bracket (System.IO.openFile name mode)
    (\handle -> System.IO.hClose handle)
    (\handle -> f handle)

main3 = do
    contents <- System.IO.readFile "girl.txt"
    putStr contents

main4 = do
    contents <- System.IO.readFile "girl.txt"
    writeFile "girlcaps.txt" (map toUpper contents)

main5 = do
    todoItem <- getLine
    System.IO.appendFile "todo.txt" (todoItem ++ "\n")

main6 = do
    contents <- System.IO.readFile "todo.txt"
    let todoTasks = lines contents
        numberredTasks = zipWith (\n line -> show n ++ " - " ++ line)
                                    [0..] todoTasks
    putStrLn "These are your TO-DO items:"
    mapM_ putStrLn numberredTasks
    putStrLn "Which one do you want to delete?"
    numberString <- getLine
    let number = read numberString
        newTodoItems = unlines $ Data.List.delete (todoTasks !! number) todoTasks
    (tempName, tempHandle) <- System.IO.openTempFile "." "temp"
    System.IO.hPutStr tempHandle newTodoItems
    System.IO.hClose tempHandle
    System.Directory.removeFile "todo.txt"
    System.Directory.renameFile tempName "todo.txt"

main7 = do
    contents <- System.IO.readFile "todo.txt"
    let todoTasks = lines contents
        numberredTasks = zipWith (\n line -> show n ++ " - " ++ line)
                                    [0..] todoTasks
    putStrLn "These are your TO-DO items:"
    mapM_ putStrLn numberredTasks
    putStrLn "Which one do you want to delete?"
    numberString <- getLine
    let number = read numberString
        newTodoItems = unlines $ Data.List.delete (todoTasks !! number) todoTasks
    Control.Exception.bracketOnError (System.IO.openTempFile "." "temp")
        (\(tempName, tempHandle) -> do
            System.IO.hClose tempHandle
            System.Directory.removeFile tempName)
        (\(tempName, tempHandle) -> do
            System.IO.hPutStr tempHandle newTodoItems
            System.IO.hClose tempHandle
            System.Directory.removeFile "todo.txt"
            System.Directory.renameFile tempName "todo.txt")

main8 = do
    args <- getArgs
    progName <- getProgName
    putStrLn "The arguments are:"
    mapM putStrLn args
    putStrLn "The program name is:"
    putStrLn progName

copy source dest = do
    contents <- B.readFile source
    Control.Exception.bracketOnError
        (System.IO.openTempFile "." "temp")
        (\(tempName, tempHandle) -> do
            System.IO.hClose tempHandle
            System.Directory.removeFile tempName)
        (\(tempName, tempHandle) -> do
            B.hPutStr tempHandle contents
            System.IO.hClose tempHandle
            System.Directory.renameFile tempName dest)
