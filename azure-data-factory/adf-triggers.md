# Azure Data Factory Triggers

* Triggers in Azure Data Factory are a key component that determine when a pipeline execution should be kicked off.
* They define the schedule or the conditions that need to be met for a pipeline run to be created.

## Three types of triggers in Azure Data Factory

1. **Schedule Trigger**:
* This type of trigger fires at a wall-clock time.
* It's based on a schedule, meaning they can set it to run pipeline at a specific time or at regular intervals (for example, every hour or every day at a specific time).
* It is also possible to set a start and end time for the trigger, which means it will only run between these times.

2. **Tumbling Window Trigger**:
* This type of trigger also fires at wall-clock times on a periodic interval, but unlike the Schedule Trigger, it's designed for handling data processing tasks that need to operate over a period of time (the window).
* For example, if I need to process data from the last hour every hour, I would use a Tumbling Window Trigger.
* Each execution of the trigger operates over a distinct period of time, ensuring there are no overlaps in data processing.

3. **Event-based Trigger**:
* This type of trigger fires when an event happens, for example, when a file is created or deleted in Azure Blob Storage.
* This is useful for scenarios where I want pipeline to run in response to an action or event, rather than on a schedule.

## Trigger execution
* When I create a trigger, I can associate it with one or more pipelines.
* Once the trigger is published, it independently fires pipeline runs based on the conditions defined in the trigger.
* I can also manually trigger a pipeline run outside of the defined schedule or event.

## Summary
* Triggers in Azure Data Factory provide a way to automate data pipelines.
* They allow to schedule pipelines to run at specific times or in response to specific events, reducing the need for manual intervention and ensuring data processing tasks run as and when needed.
