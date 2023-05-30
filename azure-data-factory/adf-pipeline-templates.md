# Azure Data Factory - pipline templates

* Pipeline templates in Azure Data Factory are pre-built pipelines that you can use as a starting point for your own pipelines.
* They are designed to solve common data movement and data transformation scenarios, and can be customized to fit your specific needs.

## Brief overview of how pipeline templates work:

1. **Accessing Templates**:
* I can access pipeline templates in the Azure Data Factory UI.
* When I create a new pipeline, I'll have the option to start with a template.

2. **Variety of Templates**:
* Azure Data Factory provides a variety of templates for different scenarios.
* For example, there are templates for copying data from various sources, transforming data using HDInsight, running SSIS packages, and more.

3. **Customization**:
* Once I've chosen a template, I can customize it to fit me needs.
* This includes changing the source and destination data stores, modifying transformation logic, adding or removing activities, and more.

4. **Parameterization**:
* Many templates are parameterized, meaning they have placeholders for things like connection strings, file paths, table names, etc.
* I can provide values for these parameters when I run the pipeline, making the template reusable for different datasets or environments.

5. **Saving and Sharing**:
* After I've customized a template, I can save it for future use.
* I can also share my customized templates with others by exporting them as a JSON file.

## Summary
* Pipeline templates in Azure Data Factory provide a quick and easy way to get started with creating data pipelines.
* They encapsulate best practices for data movement and transformation, and can save time and effort in building data workflows.
* For more detailed information, refer to the [official Azure Data Factory documentation](https://docs.microsoft.com/en-us/azure/data-factory/quickstart-create-data-factory-portal#create-a-pipeline).
