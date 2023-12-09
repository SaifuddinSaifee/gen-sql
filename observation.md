## Queries

1. **List the names and ages of passengers who were in the third class, did not survive, and had the lowest fare:**
    
    **3.5**
    
    ```sql
    SELECT Name, Age
    FROM titanic_db
    WHERE PClass = '3rd' AND Survived = 0
    ORDER BY Fare
    LIMIT 1
    ```
    
    **4**
    
    null
    
---
    

2. **Find the percentage of passengers who survived in each passenger class**:
    
    **3.5**
    
    ```sql
    SELECT PClass, (COUNT(*) / (SELECT COUNT(*) FROM titanic_db)) * 100 AS survival_percentage
    FROM titanic_db
    WHERE Survived = 1
    GROUP BY PClass
    ```
    
    **4**
    
    ```sql
    SELECT PClass, 
           (COUNT(CASE WHEN Survived = 1 THEN 1 END) / COUNT(*) * 100) AS SurvivalRate
    FROM titanic_db
    GROUP BY PClass;
    ```
    
---
    
3. **List the top 5 most common ages among passengers who did not survive**:
    
    **3.5**
    
    ```sql
    SELECT Age, COUNT(*) as count
    FROM titanic_db
    WHERE Survived = 0
    GROUP BY Age
    ORDER BY count DESC
    LIMIT 5;
    ```
    
    **4**
    
    ```sql
    SELECT Age, COUNT(*) as count
    FROM titanic_db
    WHERE Survived = 0
    GROUP BY Age
    ORDER BY count DESC
    LIMIT 5;
    ```
    
---
    
4. **Find the average age of passengers for each combination of gender and survival status**:
    
    **3.5**
    
    ```sql
    SELECT Age, COUNT(*) as count
    FROM titanic_db
    WHERE Survived = 0
    GROUP BY Age
    ORDER BY count DESC
    LIMIT 5;
    ```
    
    **4**
    
    ```sql
    SELECT Age, COUNT(*) as count
    FROM titanic_db
    WHERE Survived = 0
    GROUP BY Age
    ORDER BY count DESC
    LIMIT 5;
    ```
    
---
    
5. **Insert 4 more males, all on 2nd class, name: "Jorge", "Bush", "Carter", "Rupert" , two of them survived and other died**:
        
    **3.5**
        
    ```sql
    INSERT INTO titanic_db (Name, PClass, Age, Sex, Survived)
    VALUES ('Jorge', '2nd', NULL, 'male', 1),
           ('Bush', '2nd', NULL, 'male', 1),
           ('Carter', '2nd', NULL, 'male', 0),
           ('Rupert', '2nd', NULL, 'male', 0);
    ```
        
    **4**
        
    ```sql
    INSERT INTO titanic_db (Name, PClass, Age, Sex, Survived)
    VALUES ('Jorge', '2nd', NULL, 'male', 1),
           ('Bush', '2nd', NULL, 'male', 1),
           ('Carter', '2nd', NULL, 'male', 0),
           ('Rupert', '2nd', NULL, 'male', 0);
    ```
    
---
        
    
5. **Insert 4 more males, all on 2nd class, name: "Jorge", "Bush", "Carter", "Rupert" , two of them survived and other died**:
    
    **3.5**
    
    ```sql
    INSERT INTO titanic_db (Name, PClass, Age, Sex, Survived)
    VALUES ('Jorge', '2nd', NULL, 'male', 1),
           ('Bush', '2nd', NULL, 'male', 1),
           ('Carter', '2nd', NULL, 'male', 0),
           ('Rupert', '2nd', NULL, 'male', 0);
    ```
    
    **4**
    
    ```sql
    INSERT INTO titanic_db (Name, PClass, Age, Sex, Survived)
    VALUES ('Jorge', '2nd', NULL, 'male', 1),
           ('Bush', '2nd', NULL, 'male', 1),
           ('Carter', '2nd', NULL, 'male', 0),
           ('Rupert', '2nd', NULL, 'male', 0);
    ```
    
---