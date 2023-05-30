# Azure Event Hubs - integration with Azure Stream Analytics

Here's a general overview of how real-time analytics can be performed on events using Azure Event Hubs and Azure Stream Analytics:

1. **Data Ingestion:**
* First, events are sent to Azure Event Hubs from various sources.
* These could be logs from web applications, telemetry data from IoT devices, or any other type of event data.
* Event Hubs is designed to handle massive volumes of events in real-time.

2. **Stream Processing with Azure Stream Analytics:**
* Once the data is in Event Hubs, it can be streamed into Azure Stream Analytics.
* This service is designed to analyze incoming data within seconds of the data being produced.
* It uses a SQL-like language for querying the incoming data streams and can handle both simple event processing and complex event processing (CEP) scenarios.

3. **Querying and Analysis:**
* Within Azure Stream Analytics, you can write queries to filter, sort, aggregate, and analyze the incoming data.
* For example, you might write a query to calculate a running average of a telemetry reading, detect anomalies in real-time data, or trigger an alert if a certain condition is met.

4. **Output:**
* The results of these queries can then be sent to various outputs for further processing, storage, or visualization.
* For example, you might send the processed data to Azure Functions to trigger an action, to Azure Cosmos DB for storage, or to Power BI for real-time visualization.

In this way, while Azure Event Hubs itself doesn't perform real-time analytics, it plays a crucial role in the pipeline that enables real-time analytics on event data in Azure.