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

## M Language

* Power Query in Azure Data Factory does support the M language.
* M is a functional language used in Power Query for data transformation.
* It's primarily used in the Power Query editor, which is available in both Power BI and Excel.

## Overview of the M language:

1. **Functional Language**:
* M is a functional language, which means it's designed to handle and transform data as a series of functions.
* Each function takes an input and produces an output without changing the input or affecting anything else.

2. **Case Sensitive**:
* M is case sensitive. This means that "myVariable", "myvariable", and "MYVARIABLE" would be considered three different identifiers.

3. **Data Types**:
* M supports a variety of data types, including text, number, date/time, and more complex types like tables and functions.

4. **Expressions**:
* In M, I write expressions to transform data.
* An expression could be as simple as a literal value (like a number or text), a reference to a variable, or a more complex function call.

### Here's an example of what M code might look like:

```m
let
    Source = Csv.Document(File.Contents("C:\myFolder\myFile.csv"),[Delimiter=",", Columns=3, Encoding=1252, QuoteStyle=QuoteStyle.None]),
    #"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers",{{"Column1", type text}, {"Column2", type text}, {"Column3", type text}})
in
    #"Changed Type"
```

* In this example, we're loading a CSV file, promoting the first row to headers, and then changing the type of the columns to text.
* The `let` keyword is used to define a series of steps, with each step being a transformation of the data.
* The `in` keyword is then used to specify the output of the expression.
* While I can write M code directly, one of the key features of Power Query is that it can automatically generate M code for you as you perform transformations through the Power Query editor's graphical interface. This makes it accessible to users who may not have a strong coding background.