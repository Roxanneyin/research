library(XML)
library(stringr)
nhl <- NULL
urls <- c()

for (i in 1:length(urls)){
  tables <- readHTMLTable(urls[i])
  n.rows <- unlist(lapply(tables, function(t) dim(t)[1]))
  temp <- tables[[which.max(n.rows)]]
  nhl <- rbind(nhl,temp)
}

names(nhl) <- c()
table(nhl$OTCat)
nh <- nhl[nhl$OTCat!="Get Tickets",]
nhl$OT <- nhl$OTCat == "OT"| nhl$OTCat =="SO"