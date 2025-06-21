# Extract Transform Load Procedure

 ### At this project there are 5 steps: 
 1) Creation of fake data about devices and insertion in a mysql db.
 2) Creation of fake data about people who have bought the above devices and insertion in a neo4j db.
 3) Connection of the above dbs via kafka-broker.
 4) Insertion of the combined info into a mongodb(at this cause cloud mongodb).
 5) A Flask API in which interacts with the mongodb above.The use can type the name of a person above and see what devices they have bought.
