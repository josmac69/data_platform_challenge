# Azure Data Factory key objects

Azure Data Factory (ADF) uses several key objects to model and run data transformation workflows.

1. **Datasets**:
* A dataset is a named view of data that simply points or references the data you want to use in your activities as inputs or outputs.
* It does not contain the data itself but is a reference to the data.
* For example, an Azure Blob dataset specifies the blob container and folder in the Azure Blob Storage from which the pipeline should read the data.
* Datasets identify data within different data stores, such as tables, files, folders, and documents.

2. **Activities**:
* Activities represent a processing step in a pipeline.
* For example, you might use a copy activity to copy data from one data store to another data store.
* Similarly, you might use a transformation activity, such as a Hive activity, to run a Hive script on an Azure HDInsight cluster.
* Activities can be categorized into four types:
  * data movement activities,
  * data transformation activities,
  * control activities,
  * pipeline and dataset operation activities.

1. **Pipelines**:
* A pipeline is a logical grouping of activities that together perform a task.
* The activities in a pipeline define actions to perform on your data.
* Data Factory supports three types of activities:
  * data movement activities,
  * data transformation activities,
  * control activities.
* A pipeline can have one or many activities, and each activity performs a specific task.
* For example, a pipeline can contain a group of activities that ingests data from Azure Blob Storage, runs a Hive query on an HDInsight cluster to transform the data, and then runs a stored procedure in Azure SQL Database to load the transformed data.

1. **Linked Services**: Linked services are much like connection strings, which define the connection information that's needed for Data Factory to connect to external resources. Think of it as a data store's connection string. For example, an Azure Storage linked service specifies a connection string to connect to the Azure Storage account. Linked services are used for two reasons in Data Factory: to represent a data store that includes, but is not limited to, SQL Server, Oracle, File Share, Azure Blob Storage, etc., and a compute resource or processing resource, such as Azure HDInsight, Azure Batch, etc.

In summary, a dataset represents the structure of the data within the linked data stores, and linked services define the connection to the data source. Pipelines are used to manage and coordinate the activities, which are the actions to be performed on the data.