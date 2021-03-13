
#The total Numbers of Crime Records from Crime Table
%sql select count(*) from CHICAGO_CRIME_DATA;

#First 10rows from Crime Table 
%sql select * from CHICAGO_CRIME_DATA fetch first 10 rows only;
#%sql select * from CENSUS_DATA fetch first 10 rows only;

#Crime arrest 
%sql select count(ARREST) from CHICAGO_CRIME_DATA WHERE ARREST=TRUE; 

#Crimes reported at gassstaions
%sql select DISTINCT(PRIMARY_TYPE) from CHICAGO_CRIME_DATA WHERE LOCATION_DESCRIPTION ='GAS STATION'; 

#Community that start with the letter 'B' 
%sql select COMMUNITY_AREA_NAME from CENSUS_DATA WHERE COMMUNITY_AREA_NAME LIKE 'B%';

#communities in area 10-15 that are healthy 
%sql select S.NAME_OF_SCHOOL,C.COMMUNITY_AREA_NUMBER,C.COMMUNITY_AREA_NAME,S.healthy_school_certified from CENSUS_DATA as  C \
LEFT OUTER JOIN CHICAGO_PUBLIC_SCHOOL as S \
on UPPER(C.COMMUNITY_AREA_NAME) = UPPER(S.community_area_name) \
where C.COMMUNITY_AREA_NUMBER between 10 and 15 AND \
S.healthy_school_certified = 'Yes';

#What is the average school Safety Score
%sql select AVG(safety_score) as AVG_SCRORE from CHICAGO_PUBLIC_SCHOOLS;

#Top 5 Community Areas by average College Enrollment
%sql select COMMUNITY_AREA_NAME,AVG(COLLEGE_ENROLLMENT) as COLLEGE_ENROLLMENT_AVG \
from CHICAGO_PUBLIC_SCHOOLS GROUP BY COMMUNITY_AREA_NAME order by COLLEGE_ENROLLMENT_AVG desc LIMIT 5;

#Use a sub-query to determine which Community Area has the least value for school Safety Score?
%sql select COMMUNITY_AREA_NAME,SAFETY_SCORE from CHICAGO_PUBLIC_SCHOOLS \
WHERE SAFETY_SCORE = (SELECT MIN(SAFETY_SCORE) FROM CHICAGO_PUBLIC_SCHOOLS);

#The Per Capita Income of the Community Area which has a school Safety Score of 1
%sql select  COMMUNITY_AREA_NAME,per_capita_income \
from CENSUS_DATA \
where community_area_number = (select community_area_number from CHICAGO_PUBLIC_SCHOOLS where safety_score = 1);



