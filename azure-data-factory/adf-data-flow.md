# Azure Data Factory Data Flows

* Azure Data Factory's Data Flow is a visually designed data transformation tool that allows data engineers to develop data transformation logic without writing code.
* The resulting data flows are executed as activities within Azure Data Factory pipelines that use scaled-out Apache Spark clusters.
* Data flow activities can be operationalized using existing Azure Data Factory scheduling, control, flow, and monitoring capabilities.

## Key Features of Data Flow

1. **Visual Design**:
* Data flows provide an entirely visual experience with no coding required.
* Data flows run on ADF-managed execution clusters for scaled-out data processing.
* Azure Data Factory handles all the code translation, path optimization, and execution of data flow jobs.

2. **Debug Mode**:
* Debug mode allows you to interactively see the results of each transformation step while you build and debug data flows.
* The debug session can be used both in when building data flow logic and running pipeline debug runs with data flow activities.

3. **Monitoring**:
* Mapping data flow integrates with existing Azure Data Factory monitoring capabilities.

4. **Data Flow Activity**:
* Mapping data flows are operationalized within ADF pipelines using the data flow activity.
* All a user has to do is specify which integration runtime to use and pass in parameter values.

5. **Available Transformations**:
* View the mapping data flow transformation overview to get a list of available transformations.

6. **Data Types**:
* Data flow data types include array, binary, boolean, complex, decimal (includes precision), date, float, integer, long, map, short, string, timestamp.

## Conclusion
* Data Flow in Azure Data Factory provides a powerful, visual way of transforming data without the need to write code, making it accessible for users who may not have a strong coding background.
* It's a key component of Azure Data Factory's data transformation capabilities.
