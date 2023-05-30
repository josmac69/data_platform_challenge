# Azure Data Factory Integration Runtime

* The Integration Runtime (IR) in Azure Data Factory is the compute infrastructure that Azure Data Factory and Azure Synapse pipelines use to provide data integration capabilities across different network environments.
* It serves as the bridge between activities and linked services.

## Key components of the Integration Runtime:

1. **Data Flow**:
* Executes a Data Flow in a managed Azure compute environment.

2. **Data Movement**:
* Copies data across data stores in public or private networks.
* It supports built-in connectors, format conversion, column mapping, and performant and scalable data transfer.

3. **Activity Dispatch**:
* Dispatches and monitors transformation activities running on various compute services such as Azure Databricks, Azure HDInsight, ML Studio (classic), Azure SQL Database, SQL Server, and more.

4. **SSIS Package Execution**:
* Natively executes SQL Server Integration Services (SSIS) packages in a managed Azure compute environment.

## Three types of Integration Runtime (IR):

- **Azure Integration Runtime**:
  - Runs Data Flows in Azure, runs copy activities between cloud data stores, and dispatches transform activities in a public network.

- **Self-hosted Integration Runtime**:
  - Runs copy activity between a cloud data store and a data store in a private network and dispatches transform activities against compute resources in on-premises or Azure Virtual Network.

- **Azure-SSIS Integration Runtime**:
  - Lifts and shifts existing SSIS workload, creating an Azure-SSIS IR to natively execute SSIS packages.

The location of the Integration Runtime defines the location of its back-end compute, and where the data movement, activity dispatching, and SSIS package execution are performed. The IR location can be different from the location of the Data Factory it belongs to.

The Integration Runtime can be created in the Azure Data Factory and Azure Synapse UI via the management hub directly, as well as from any activities, datasets, or data flows that reference them.

For more detailed information, you can refer to the [official Azure documentation](https://docs.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime).