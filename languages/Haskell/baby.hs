doubleMe x = x + x

doubleUs x y = doubleMe x + doubleMe y

doubleSmallNumber x = if x > 100 then x else x * 2

_fsp = "_fsp"

fsp' = "fsp"

lostNumbers = [4, 8, 15, 16, 23, 42]

added = lostNumbers ++ [1]

strAdded = "hello" ++ "world"

l = [5,4,3,2,1]
h = head l
h1 = last l
h2 = tail l
h3 = init l
h4 = take 3 [1,2,3,4,5]
h5 = length [5,1,3]
h6 = null [1,2,2]
h7 = reverse [1,2,3,4]
h8 = drop 3 [1,2,2,3,4,5]
h9 = maximum [1,2,3]
i = minimum[1,2,2]
i1 = take 10 (cycle [1,2,3])
i2 = take 12 (repeat 2)
i3 = replicate 3 10

lCompre = [x*2 | x <- [1..10]]

boomBangs xs = [ if x < 10 then "BOOM!" else "BANG!" | x <- xs, odd x]

length' xs = sum [1 | _ <- xs]

removeNonUppercase st = [c | c <- st, c `elem` ['A'..'Z']]

e = fst (8, 11)
e1 = snd ("Wow", False)
e2 = zip [1,2,3,4,5] [5,5,5,5,5]

factorial :: Integer -> Integer
factorial n = product [1..n]

lucky :: Int -> String
lucky 7 = "LUCKY NUMBER SEVEN!"
lucky x = "Sorry, you're out of luck, pal!"

fac :: Int -> Int
fac 0 = 1
fac n = n * fac (n-1)

charName :: Char -> String
charName 'a' = "Albert"
charName 'b' = "Broseph"
charName 'c' = "Cecil"

addVectors :: (Double, Double) -> (Double, Double) -> (Double, Double)
addVectors (x1, y1) (x2, y2) = (x1 + x2, y1 + y2)

first :: (a,b,c) -> a
first (x,_,_) = x

second :: (a,b,c) -> b
second (_,x,_) = x

third :: (a,b,c) -> c
third (_,_,x) = x
