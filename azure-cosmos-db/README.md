# Azure Cosmos DB

Azure Cosmos DB is a globally distributed, multi-model database service provided by Microsoft for managing data at large scale. It is designed to provide low latency, high availability, and elastic scalability.

**Architecture:**

Azure Cosmos DB is built on a distributed systems architecture which provides automatic and instant scalability. Here are some key components of its architecture:

1. **Globally Distributed:** Cosmos DB is designed to be globally distributed. It allows you to distribute your data across multiple Azure regions worldwide and provides a single system image of your globally distributed data.

2. **Multi-Model:** Cosmos DB supports multiple data models, including key-value, document, column-family, and graph. It natively supports SQL API, MongoDB API, Cassandra API, Gremlin API, and Table API.

3. **Multi-Master Replication:** Cosmos DB supports active-active (multi-master) and active-passive (single-master) replication models. This means you can write and read data from any region.

4. **Partitioning:** Cosmos DB automatically partitions your data to manage and scale it across multiple partitions. It uses two types of partitioning: physical and logical.

5. **Consistency Models:** Cosmos DB offers five consistency models: Strong, Bounded staleness, Session, Consistent prefix, and Eventual. This allows you to choose the right balance between consistency, availability, and performance for your application.

**Underlying Technology:**

Azure Cosmos DB is built on a technology called "atom-record-sequence" (ARS) which enables the multi-model capability. It uses Azure's global network to provide low-latency access to data, no matter where it's accessed from. It also uses a latch-free and write-optimized database engine capable of ingesting massive amounts of data while offering transactional consistency.

**Typical Use Cases:**

1. **IoT and Telemetry:** Cosmos DB's ability to ingest massive amounts of data in real-time, its automatic indexing capabilities, and its globally distributed nature make it an excellent choice for IoT and telemetry scenarios.

2. **Retail and Marketing:** For scenarios like product catalogs, user personalization, and order history where low latency and high availability are crucial, Cosmos DB is a great fit.

3. **Gaming:** Cosmos DB's globally distributed architecture ensures that game state is always nearby and writeable, providing a great gaming experience for players around the world.

4. **Real-Time Analytics:** Cosmos DB's change feed feature enables real-time processing of data, making it suitable for real-time analytics scenarios.

5. **Web and Mobile Applications:** Cosmos DB's global distribution, multi-model support, and scalability make it a good choice for powering responsive and scalable web and mobile applications.

6. **Distributed Systems:** Cosmos DB's support for multi-master replication and tunable consistency models makes it a good fit for distributed systems.

In summary, Azure Cosmos DB is a powerful, globally-distributed, multi-model database service that provides a wide range of capabilities for building scalable, low-latency applications.