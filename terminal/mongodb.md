# MongoDB

I first ran mongodb on the command line to find out that mongo was listening on a
nonstandard port. I ran ps -ef to find the port it was listening on, then ran:

`mongodb 127.0.0.1:12012`

When there, I first enumerated the databases:

`show databases`

Which showed a database named "elfu." I then connected to it:

`use elfu`

Then enumerated the collections:

`db.getCollectionNames()`

And discovered a collection named "solution"

I dumped that collection:

`db.solution.find()`
