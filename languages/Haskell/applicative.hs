import qualified Data.Char
import qualified Data.List

main = do line <- fmap reverse getLine
          putStrLn $ "You said " ++ line ++ " backwards!"

main2 = do line <- fmap (Data.List.intersperse '-' . reverse . map Data.Char.toUpper) getLine
           putStrLn line

data CMaybe a = CNothing | CJust Int a deriving (Show)

instance Functor CMaybe where
    fmap f CNothing = CNothing
    fmap f (CJust counter x) = CJust (counter+1) (f x)
