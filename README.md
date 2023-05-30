# data_platform_challenge
This repository contains data platform challenge I did for the company Y.

## Task
* In this challenge I shall design data platform for unified ancillary market place.
* Idea is to unify different products related to traveling under one user journey.
* When user buys ticket for airplane they can also book taxi, accommodation or buy tickets for events at destination place using the same web platform.
* Integration points are REST API or UI SDK of other companies.

Targeted solution should be:
- unified search
- unified product catalog
- unified payment methods
- unified customer integrations

Ancillaries integrated into system are:
- bus or train tickets
- parking space booking
- accommodation booking
- tickets for events booking
- car sharing
- insurances

Requested features of the data platform are:

* Ancillary Marketplace(AMP) is an API-first ecommerce solution that is composed of various microservices built in alignment with Domain Driven Design principles.
* There are various product catalogs from different service providers that are aggregated in real-time, near-real-time and non-real-time to be sold in various stores within our business partners’ (Lufthansa, Austrian Airlines, Swiss Airlines etc.) web and mobile applications.
* PostgreSQL, MongoDB, AWS S3 and Kafka are used to store and stream data in the platform.
* The platform’s major product groups are lounges, parking, taxis & rides, airport buses and trains, events, car rentals, accommodation etc.
* The system has PII data that needs to be carefully classified and protected

### Task is
Design a system for a modern, scalable and resilient data platform by using data mesh principles on AMP platform. The design should be done by using the services and tools of a major cloud platform like Azure, AWS or GCP. (Azure would be our preferred platform.)

* The design should include a pipeline to store, stream and process data
* The design should cover data governance and classification of PII data
* The design should take into account maintainability, scalability, security, cost-optimization and efficiency.
* The design should include a connection to BI tools to give business the freedom to analyse and visualise data
* The design should include a data strategy for at least one of the product groups(lounges, parking, taxis & rides, airport buses and trains, events, car rentals, accommodation etc.)

## Solution
To be able to design this solution I need to discuss some assumptions:

1. **Data Volume and Velocity:**
  * Q: What is the expected volume and velocity of the data that will be processed by the system?
  * A: System should be used by big airline companies, operating all over the globe. So I can assume very high traffic in some part of year. Ie system must handle highly seasonal traffic with huge spikes.

2. **Data Types and Structures:**
  * Q: What types of data will the system handle? Will it be structured, semi-structured, or unstructured data?
  * A: Based on available description I can presume data are structured but structures are different across different providers. System must be able to handle it.

3. **Data Quality:**
  * Q: What are requirements regarding data quality? Do we need mechanisms for data validation, cleansing, or enrichment?
  * A: Data quality is very important. System must be able to handle data validation, cleansing and enrichment.

4. **Data Security and Compliance:**
  * Q: What are specific requirements regarding data security and compliance?
  * A: System must be able to handle PII data. System must be able to handle GDPR, US regulations and other regulations all around the world.

5. **Business Intelligence Requirements:**
  * Q: What are specific requirements regarding business intelligence?
  * A: System must provide data sources used later by different BI suites. Data platform should be self served, so any BI suite can be used by different 3rd parties for visualization and analysis.

6. **Budget and Resources:**
  * Q: What is the budget for this project? What resources (human, technical, financial) are available for implementing and maintaining the system?
  * A: Budget is not specified. For this phase of design I can assume it is not limited and I can assume there is no limit on human and technical resources either. Idea is to design the best possible solution. We can later discuss how to optimize it.

7. **Existing Systems and Technologies:**
  * Q: What systems and technologies are currently in place? Can they be leveraged in the new system, or do I have to start from scratch?
  * A: There is already some system in place but idea is to design something independent and better.

8. **Preferred Cloud Platform:**
  * Q: Is usage of  Azure cloud platform a strict requirement, or can I use other platforms if they offer significant advantages?
  * A: Azure is preferred platform but I can use other platforms if they offer significant advantages.

### Possible solutions

1. [Pure Azure solution](azure-solution.md)
2.