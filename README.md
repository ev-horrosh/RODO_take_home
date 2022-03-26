

viz, sql dump,and aggregated table are in the `output` folder


-----NOTES ABOUT THE DATA----------------

dealership2 has no list price
            has no Certified
            invoice has missing values
because of empty strings instead of ints, had to replace with zeroes to pass the validation

dealership1 msrp has zeroes


----------
TODO:
- more DRY
- csv parsinng(`ParseDataFromCsv`class) can be a bit generalizable given the data is consistent
- implement pydantic data validation
- implement glob list of files
 
