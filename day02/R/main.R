library(data.table)
dt <- fread('input.txt')
dt[,
   .(forward = sum((V1 == 'forward') * V2),
     depth = sum((V1 == 'down') * V2 - (V1 == 'up') * V2))][,
       .(part1 = forward * depth)
     ]

dt[,
   .(forward = (V1 == 'forward') * V2,
     aim = cumsum((V1 == 'down') * V2 - (V1 == 'up') * V2))][
       ,
       .(part2 = sum(forward) * sum(forward * aim))
       ]

