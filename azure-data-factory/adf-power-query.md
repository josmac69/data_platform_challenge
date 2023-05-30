# Azure Data Factory Power Query

* Power Query is a data connectivity and data preparation technology that enables end users to seamlessly import and reshape data from within a wide range of Microsoft products, including Excel, Power BI, Analysis Services, Dataverse, and more.

## Key features of Power Query:

1. **Data Connectivity**:
* Power Query provides a wide range of connectors to various data sources, allowing you to import data from a variety of places.
* This includes databases, Excel files, web pages, APIs, and more.

2. **Data Transformation**: Power Query provides a user-friendly interface for reshaping and cleaning data. You can filter rows, merge data, change data types, split columns, and more, all without needing to write any code.

3. **Integration with Microsoft Products**: Power Query is integrated into several Microsoft products, including Excel and Power BI. This means you can use Power Query to import and transform data directly within these tools.

4. **Dataflows**: Power Query dataflows are a form of ETL (Extract, Transform, Load) that enable you to prepare and transform data for use in Power BI. Dataflows are created and managed in the Power BI service.

5. **M Language**: Power Query uses a functional language known as M. While you can use Power Query's interface to perform most tasks, you can also write M code to perform more complex transformations.

6. **Query Folding**: This is an optimization technique used by Power Query where operations are pushed back to the source database, reducing the amount of data that needs to be loaded into Power Query.

In Azure Data Factory, Power Query can be used as a transformation activity in a pipeline. This allows you to use Power Query's powerful data transformation capabilities within your Azure Data Factory workflows.

For more detailed information, you can refer to the [official Power Query documentation](https://docs.microsoft.com/en-us/power-query/).