import qualified Data.Map as M
import qualified Data.List as L
import qualified Data.Char
import Geometry

wordNums :: String -> [(String,Int)]
wordNums = map(\ws -> (head ws, length ws)) . L.group . L.sort . words

isIn :: (Eq a) => [a] -> [a] -> Bool
needle `isIn` haystack = any (needle `L.isPrefixOf`) (L.tails haystack)

encode :: Int -> String -> String
encode offset msg = map(\c -> Data.Char.chr $ Data.Char.ord c + offset) msg

decode :: Int -> String -> String
decode shift msg = encode (negate shift) msg

encode' = encode 5
decode' = decode 5

digitSum :: Int -> Int
digitSum = sum . map Data.Char.digitToInt . show

firstTo40 :: Maybe Int
firstTo40 = L.find (\x -> digitSum x == 40) [1..]

phoneBook = 
    [("betty", "55502938")
    ,("bonnie", "452-2928")
    ,("patsy", "493-2928")
    ,("lucille", "205-2928")
    ,("wendy", "939-8282")
    ,("penny", "85302492")
    ]

findKey :: (Eq k) => k -> [(k, v)] -> Maybe v
findKey key xs = foldr (\(k, v) acc -> if key == k then Just v else acc) Nothing xs

phoneBookMap :: M.Map String String
phoneBookMap = M.fromList(phoneBook)
