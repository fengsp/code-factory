xs = [(1,3),(4,3),(2,4),(5,3),(5,6),(3,1)]
xsr = [a+b | (a,b) <- xs]

head' :: [a] -> a
head' [] = error "Can't call head on empty list!"
head' (x:_) = x

tell :: (Show a) => [a] -> String
tell [] = "This list is empty"
tell (x:[]) = "The list has one element: " ++ show x
tell (x:_) = "This list is long."

firstLetter :: String -> String
firstLetter "" = "Empty string, whoops!"
firstLetter all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x]

bmiTell :: Double -> String
bmiTell bmi
    | bmi <= 18.5 = "Under"
    | bmi <= 25.0 = "Normal"
    | bmi <= 30.0 = "Over"
    | otherwise = "Pig?"

max' :: (Ord a) => a -> a -> a
max' a b
    | a <= b = b
    | otherwise = a

bmiSay :: Double -> Double -> String
bmiSay weight height
    | bmi <= 18.5 = "Under"
    | bmi <= 25.0 = "Normal"
    | bmi <= 30.0 = "Fat"
    | otherwise = "Pig?"
    where bmi = weight / height ^ 2

initials :: String -> String -> String
initials firstname lastname = [f] ++ ". " ++ [l] ++ "."
    where (f:_) = firstname
          (l:_) = lastname


cylinder :: Double -> Double -> Double
cylinder r h = 
    let sideArea = 2 * pi * r * h
        topArea = pi * r ^ 2
    in sideArea + 2 * topArea

r = let boot x y z = x * y + z in boot 3 4 2
