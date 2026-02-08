"""
Denisy Agent - Chief Data Officer

Expert in data strategy, governance, privacy, analytics, streaming,
data modeling, ETL pipelines, and database design.
"""

import asyncio
from typing import Optional, List, Dict

from ..shared import BaseAgent, TaskResult
from .config import denisy_config


class DenisyAgent(BaseAgent):
    """
    Denisy - Chief Data Officer

    Specializes in:
    - Data strategy & governance
    - Data privacy & compliance (GDPR, CCPA)
    - Analytics & business intelligence
    - Data lineage & observability
    - Streaming data (Kafka, Redis Streams)
    - Data visualization & dashboards
    - Data modeling (star, snowflake, data vault)
    - Data collection & ETL pipelines
    - Database design
    """

    def __init__(self, config=None):
        super().__init__(config or denisy_config)

    async def research_sources(self, topic: str) -> TaskResult:
        """Research data sources for a topic"""
        await self.notify(f"Researching sources for: {topic}")

        prompt = f"""
Research data sources for: {topic}

**Find:**
1. Official websites and databases
2. Public APIs
3. Open data sources
4. Documentation/datasheets
5. Secondary sources

**For each source, document:**

| Source | Type | URL | Access Method | Quality | Update Frequency |
|--------|------|-----|---------------|---------|-----------------|
| ... | API/Web/PDF | ... | GET/Scrape/Download | High/Med/Low | Daily/Weekly/Static |

**Evaluate:**
- Data completeness
- Format consistency
- Terms of service
- Rate limits
- Authentication requirements

**Recommendation:**
1. Primary sources to use
2. Backup sources
3. Sources to avoid (with reason)
"""

        return await self.run_task(prompt)

    async def build_scraper(
        self,
        url: str,
        data_spec: str,
        output_format: str = "json"
    ) -> TaskResult:
        """Build a web scraper"""
        await self.notify(f"Building scraper for: {url}")

        prompt = f"""
Build web scraper for: {url}

**Data to extract:**
{data_spec}

**Output format:** {output_format}

**Create scraper:**

```python
import httpx
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List
import asyncio

@dataclass
class ScrapedData:
    # Define fields based on data_spec
    pass

class Scraper:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.client = httpx.AsyncClient(
            timeout=30,
            headers={{"User-Agent": "DataCollector/1.0"}}
        )

    async def scrape_page(self, url: str) -> ScrapedData:
        response = await self.client.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return self._extract(soup)

    def _extract(self, soup: BeautifulSoup) -> ScrapedData:
        # Extract logic
        pass

    async def scrape_all(self) -> List[ScrapedData]:
        # Pagination/iteration logic
        pass

    async def save(self, data: List[ScrapedData], path: str):
        # Save to {output_format}
        pass
```

**Include:**
- Error handling
- Rate limiting
- Retry logic
- Logging
- robots.txt compliance check
"""

        return await self.run_task(prompt)

    async def design_schema(self, requirements: str) -> TaskResult:
        """Design a database schema"""
        await self.notify(f"Designing schema")

        prompt = f"""
Design database schema for:

{requirements}

**Create PostgreSQL schema:**

```sql
-- Main tables
CREATE TABLE ... (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    ...
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for common queries
CREATE INDEX idx_... ON ...(...);

-- Full-text search (if applicable)
CREATE INDEX idx_search ON ...
    USING gin(to_tsvector('english', ...));

-- Audit table for raw data
CREATE TABLE raw_data (
    id UUID PRIMARY KEY,
    item_id UUID REFERENCES ...(id),
    source_url VARCHAR(2000),
    scraped_at TIMESTAMP DEFAULT NOW(),
    raw_content JSONB
);
```

**Include:**
1. Table relationships (ERD)
2. Indexes for common queries
3. Constraints
4. Sample queries
5. Migration script
"""

        return await self.run_task(prompt)

    async def build_etl_pipeline(
        self,
        source: str,
        destination: str,
        transformations: str = None
    ) -> TaskResult:
        """Build an ETL pipeline"""
        await self.notify(f"Building ETL: {source} -> {destination}")

        prompt = f"""
Build ETL pipeline:
- Source: {source}
- Destination: {destination}
{f"- Transformations: {transformations}" if transformations else ""}

**Create pipeline:**

```python
import asyncio
from dataclasses import dataclass
from typing import AsyncIterator

@dataclass
class PipelineConfig:
    source: str
    destination: str
    batch_size: int = 100

class ETLPipeline:
    def __init__(self, config: PipelineConfig):
        self.config = config

    async def extract(self) -> AsyncIterator[dict]:
        '''Extract data from source'''
        # Extraction logic
        pass

    async def transform(self, data: dict) -> dict:
        '''Transform data'''
        # Transformation logic
        pass

    async def load(self, data: list[dict]):
        '''Load data to destination'''
        # Loading logic
        pass

    async def run(self):
        '''Run the full pipeline'''
        batch = []
        async for record in self.extract():
            transformed = await self.transform(record)
            batch.append(transformed)

            if len(batch) >= self.config.batch_size:
                await self.load(batch)
                batch = []

        if batch:
            await self.load(batch)
```

**Include:**
- Error handling and retries
- Progress logging
- Validation at each stage
- Rollback capability
- Metrics collection
"""

        return await self.run_task(prompt)

    async def validate_data(self, data_path: str, schema: str = None) -> TaskResult:
        """Validate collected data"""
        prompt = f"""
Validate data at: {data_path}
{f"Schema: {schema}" if schema else ""}

**Validation checks:**

1. **Completeness**
   - Missing required fields
   - Null values in critical columns
   - Empty strings

2. **Accuracy**
   - Data type validation
   - Range checks
   - Format validation (emails, URLs, dates)

3. **Consistency**
   - Duplicate detection
   - Referential integrity
   - Cross-field validation

4. **Freshness**
   - Data timestamps
   - Stale records

**Generate report:**

## Validation Report

### Summary
| Metric | Value |
|--------|-------|
| Total Records | ... |
| Valid Records | ... |
| Invalid Records | ... |
| Completeness % | ... |

### Issues Found
| Type | Count | Examples |
|------|-------|----------|
| Missing field X | ... | ... |

### Recommendations
1. [Action to fix issues]
"""

        return await self.run_task(prompt)

    async def data_governance_framework(
        self,
        organization: str,
        domains: List[str]
    ) -> TaskResult:
        """Design a comprehensive data governance framework"""
        await self.notify(f"Designing data governance framework for: {organization}")

        domains_list = "\n".join(f"- {d}" for d in domains)
        prompt = f"""
Design a comprehensive data governance framework for: {organization}

**Data Domains:**
{domains_list}

**Deliver the following:**

### 1. Data Governance Policy
- Vision and objectives
- Scope and applicability
- Roles and responsibilities (Data Owner, Data Steward, Data Custodian)
- Decision rights and escalation paths
- Policy enforcement mechanisms

### 2. Data Ownership Model
- Domain-to-owner mapping
- RACI matrix for data operations (Create, Read, Update, Delete, Share)
- Stewardship assignments per domain
- Accountability framework and review cadence

### 3. Data Quality Standards
For each domain, define:
| Domain | Quality Dimension | Rule | Threshold | Measurement Method |
|--------|------------------|------|-----------|-------------------|
| ... | Completeness | ... | >=99% | ... |
| ... | Accuracy | ... | >=98% | ... |
| ... | Timeliness | ... | <1hr | ... |
| ... | Consistency | ... | 100% | ... |

### 4. Data Catalog Structure
- Catalog taxonomy and hierarchy
- Required metadata fields per asset type
- Business glossary template
- Data dictionary standards
- Tagging and classification scheme
- Search and discovery guidelines

### 5. Governance Operating Model
- Data governance council charter
- Meeting cadence and agenda templates
- KPIs for governance effectiveness
- Maturity assessment criteria
- Continuous improvement roadmap
"""

        return await self.run_task(prompt)

    async def privacy_assessment(
        self,
        data_sources: List[str],
        regulations: List[str]
    ) -> TaskResult:
        """Conduct a data privacy and compliance assessment"""
        await self.notify(f"Conducting privacy assessment for {len(data_sources)} data sources")

        sources_list = "\n".join(f"- {s}" for s in data_sources)
        regs_list = "\n".join(f"- {r}" for r in regulations)
        prompt = f"""
Conduct a comprehensive data privacy and compliance assessment.

**Data Sources:**
{sources_list}

**Applicable Regulations:**
{regs_list}

**Deliver the following:**

### 1. PII Inventory
For each data source:
| Source | PII Field | Category | Sensitivity | Storage Location | Encrypted | Retention |
|--------|-----------|----------|-------------|-----------------|-----------|-----------|
| ... | ... | Direct/Quasi/Sensitive | High/Med/Low | ... | Yes/No | ... |

### 2. Compliance Gap Analysis
For each regulation:
| Requirement | Current State | Gap | Risk Level | Remediation |
|-------------|--------------|-----|-----------|-------------|
| ... | ... | ... | Critical/High/Med/Low | ... |

### 3. Anonymization Recommendations
For each PII category, recommend techniques:
- **Direct identifiers**: Tokenization, pseudonymization approach
- **Quasi-identifiers**: k-anonymity (k>=5), l-diversity strategy
- **Sensitive attributes**: Differential privacy (epsilon recommendations)
- **Free text**: NER-based redaction pipeline

### 4. Consent Requirements
- Consent collection points and mechanisms
- Consent granularity (purpose-specific vs. broad)
- Preference center design
- Consent withdrawal workflow
- Audit trail requirements
- Cross-border transfer consent needs

### 5. Privacy Impact Assessment Summary
- Overall risk rating
- Critical findings requiring immediate action
- 30/60/90 day remediation roadmap
- Ongoing monitoring recommendations
"""

        return await self.run_task(prompt)

    async def design_analytics_dashboard(
        self,
        metrics: List[str],
        audience: str
    ) -> TaskResult:
        """Design an analytics dashboard with KPI framework"""
        await self.notify(f"Designing analytics dashboard for: {audience}")

        metrics_list = "\n".join(f"- {m}" for m in metrics)
        prompt = f"""
Design a comprehensive analytics dashboard.

**Key Metrics:**
{metrics_list}

**Target Audience:** {audience}

**Deliver the following:**

### 1. Dashboard Layout
- Page/tab structure with information hierarchy
- Above-the-fold KPI summary cards
- Drill-down navigation paths
- Filter and date range controls
- Responsive layout for desktop and mobile

### 2. Chart Type Selection
For each metric:
| Metric | Chart Type | Rationale | Dimensions | Filters |
|--------|-----------|-----------|------------|---------|
| ... | Line/Bar/Gauge/Table/... | ... | Time/Category/... | ... |

### 3. KPI Definitions
For each KPI:
- **Name**: Clear business name
- **Formula**: Precise calculation
- **Data source**: Table/column references
- **Granularity**: Time grain and dimensions
- **Benchmarks**: Target, warning, critical thresholds
- **Leading/Lagging**: Indicator type classification

### 4. Refresh Strategy
| Data Layer | Refresh Frequency | Method | SLA |
|-----------|-------------------|--------|-----|
| Real-time metrics | ... | Streaming/WebSocket | ... |
| Hourly aggregates | ... | Scheduled ETL | ... |
| Daily summaries | ... | Batch job | ... |

### 5. Implementation Recommendations
- Recommended tool (Superset / Metabase / Custom)
- Data model requirements (pre-aggregated tables, materialized views)
- Caching strategy
- Access control and row-level security
- Alert configuration for anomalies
"""

        return await self.run_task(prompt)

    async def data_lineage_map(self, pipeline_description: str) -> TaskResult:
        """Map end-to-end data lineage for a pipeline"""
        await self.notify("Mapping data lineage")

        prompt = f"""
Map comprehensive end-to-end data lineage for:

{pipeline_description}

**Deliver the following:**

### 1. End-to-End Lineage Diagram
Document the complete data flow:
```
[Source A] --> [Ingestion] --> [Raw Layer] --> [Transform 1] --> [Staging]
[Source B] --> [Ingestion] --> [Raw Layer] --> [Transform 2] --> [Staging]
[Staging] --> [Business Logic] --> [Curated Layer] --> [Serving Layer]
```

### 2. Column-Level Lineage
| Target Table | Target Column | Source Table | Source Column | Transformation |
|-------------|--------------|-------------|--------------|----------------|
| ... | ... | ... | ... | Direct/Derived/Aggregated: formula |

### 3. Transformation Documentation
For each transformation step:
- **Step name**: Descriptive identifier
- **Input**: Tables/columns consumed
- **Logic**: Business rules applied (SQL/code snippet)
- **Output**: Tables/columns produced
- **Data quality impact**: How this step affects quality metrics

### 4. Quality Checkpoints
| Checkpoint | Location | Validation Rule | Action on Failure |
|-----------|----------|----------------|-------------------|
| ... | After ingestion | Row count delta < 5% | Alert + pause pipeline |
| ... | After transform | No nulls in key columns | Quarantine records |
| ... | Before serving | Schema match | Block promotion |

### 5. Impact Analysis
- Upstream dependency map (what breaks if source changes)
- Downstream consumer map (what is affected if this pipeline fails)
- SLA cascade analysis
- Change management checklist for schema evolution
"""

        return await self.run_task(prompt)

    async def design_streaming_pipeline(
        self,
        sources: List[str],
        destinations: List[str],
        requirements: str
    ) -> TaskResult:
        """Design a real-time streaming data pipeline"""
        await self.notify(f"Designing streaming pipeline: {len(sources)} sources -> {len(destinations)} destinations")

        sources_list = "\n".join(f"- {s}" for s in sources)
        destinations_list = "\n".join(f"- {d}" for d in destinations)
        prompt = f"""
Design a real-time streaming data pipeline.

**Sources:**
{sources_list}

**Destinations:**
{destinations_list}

**Requirements:**
{requirements}

**Deliver the following:**

### 1. Architecture Overview
- Streaming platform selection (Kafka / Redis Streams) with justification
- Producer and consumer topology
- Partitioning strategy and key design
- Consumer group configuration
- Exactly-once vs at-least-once semantics decision

### 2. Event Schema Design
For each event type:
```json
{{
  "event_type": "...",
  "version": "1.0",
  "timestamp": "ISO-8601",
  "source": "...",
  "correlation_id": "uuid",
  "payload": {{
    // Strongly-typed fields
  }},
  "metadata": {{
    // Processing metadata
  }}
}}
```
- Schema registry configuration
- Schema evolution strategy (backward/forward compatibility)

### 3. Pipeline Implementation
```python
# Kafka producer example
from confluent_kafka import Producer
import json

class EventProducer:
    def __init__(self, bootstrap_servers: str, topic: str):
        self.producer = Producer({{
            'bootstrap.servers': bootstrap_servers,
            'enable.idempotence': True,
            'acks': 'all',
        }})
        self.topic = topic

    async def emit(self, key: str, event: dict):
        self.producer.produce(
            self.topic,
            key=key.encode(),
            value=json.dumps(event).encode(),
            callback=self._delivery_report
        )
        self.producer.flush()

# Consumer with error handling
class EventConsumer:
    def __init__(self, bootstrap_servers: str, group_id: str, topics: list):
        self.consumer = Consumer({{
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'auto.offset.reset': 'earliest',
            'enable.auto.commit': False,
        }})
        self.consumer.subscribe(topics)

    async def process(self):
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            try:
                event = json.loads(msg.value())
                await self._handle_event(event)
                self.consumer.commit(msg)
            except Exception as e:
                await self._send_to_dlq(msg, e)
```

### 4. Error Handling & Resilience
- Dead letter queue (DLQ) design and retry policy
- Backpressure handling strategy
- Circuit breaker configuration
- Poison message detection
- Consumer lag monitoring and alerting

### 5. Operational Runbook
- Scaling triggers and procedures
- Rebalancing procedures
- Offset reset procedures
- Monitoring dashboards (consumer lag, throughput, error rates)
- Incident response for common failure modes
"""

        return await self.run_task(prompt)

    async def data_model(
        self,
        requirements: str,
        modeling_approach: str = "dimensional"
    ) -> TaskResult:
        """Design a data model using specified approach"""
        await self.notify(f"Designing {modeling_approach} data model")

        prompt = f"""
Design a comprehensive data model.

**Requirements:**
{requirements}

**Modeling Approach:** {modeling_approach}

**Deliver the following:**

### 1. Conceptual Model
- Entity-relationship overview
- Business process identification
- Grain declaration for each fact table
- Conformed dimension identification

### 2. Logical Model
{"#### Dimensional Model (Kimball)" if modeling_approach == "dimensional" else "#### " + modeling_approach.title() + " Model"}

**Fact Tables:**
```sql
-- Fact table: captures business events at declared grain
CREATE TABLE fact_<process> (
    fact_key BIGSERIAL PRIMARY KEY,
    -- Dimension foreign keys
    date_key INT REFERENCES dim_date(date_key),
    -- Degenerate dimensions
    -- Measures (additive, semi-additive, non-additive)
    amount NUMERIC(18,2),        -- Additive
    balance NUMERIC(18,2),       -- Semi-additive
    conversion_rate NUMERIC(8,4) -- Non-additive
);
```

**Dimension Tables:**
```sql
-- Dimension with SCD Type 2
CREATE TABLE dim_<entity> (
    <entity>_key BIGSERIAL PRIMARY KEY,
    <entity>_id VARCHAR(50) NOT NULL,   -- Natural/business key
    -- Attributes
    name VARCHAR(255),
    category VARCHAR(100),
    -- SCD Type 2 tracking
    effective_date DATE NOT NULL,
    expiration_date DATE DEFAULT '9999-12-31',
    is_current BOOLEAN DEFAULT TRUE,
    -- Audit
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### 3. Slowly Changing Dimensions Strategy
| Dimension | Attribute | SCD Type | Rationale |
|-----------|-----------|----------|-----------|
| ... | ... | Type 1 (Overwrite) | ... |
| ... | ... | Type 2 (History) | ... |
| ... | ... | Type 3 (Previous) | ... |

### 4. Physical Model
- Partitioning strategy (range, hash, list)
- Indexing strategy (B-tree, GIN, BRIN)
- Materialized views for common aggregations
- Table statistics and vacuum configuration
- Storage estimation

### 5. ETL Patterns
- Dimension loading pattern (SCD merge logic)
- Fact table loading pattern (insert-only, late-arriving facts)
- Date dimension generator
- Data quality checks between staging and target
- Incremental vs full refresh strategy per table
"""

        return await self.run_task(prompt)

    async def data_quality_framework(
        self,
        data_sources: List[str]
    ) -> TaskResult:
        """Design a data quality monitoring framework"""
        await self.notify(f"Designing data quality framework for {len(data_sources)} sources")

        sources_list = "\n".join(f"- {s}" for s in data_sources)
        prompt = f"""
Design a comprehensive data quality monitoring framework.

**Data Sources:**
{sources_list}

**Deliver the following:**

### 1. Quality Rules
For each data source, define rules across dimensions:
| Source | Dimension | Rule Name | SQL/Logic | Severity |
|--------|-----------|-----------|-----------|----------|
| ... | Completeness | not_null_<col> | col IS NOT NULL | Critical |
| ... | Accuracy | valid_email | col ~ '^[a-zA-Z0-9.]+@' | High |
| ... | Consistency | fk_exists | EXISTS (SELECT 1 FROM ref...) | Critical |
| ... | Timeliness | fresh_data | max(updated_at) > NOW() - '1h' | High |
| ... | Uniqueness | unique_key | COUNT(*) = COUNT(DISTINCT key) | Critical |
| ... | Validity | valid_range | col BETWEEN min AND max | Medium |

### 2. Monitoring & Alerts
```python
# Data quality check framework
class DataQualityMonitor:
    def __init__(self, connection, alert_channels):
        self.conn = connection
        self.alerts = alert_channels

    async def check_completeness(self, table, columns):
        '''Check for null/empty values in required columns'''
        for col in columns:
            result = await self.conn.execute(f'''
                SELECT
                    COUNT(*) as total,
                    COUNT({{col}}) as non_null,
                    ROUND(COUNT({{col}})::numeric / COUNT(*) * 100, 2) as pct
                FROM {{table}}
            ''')
            if result['pct'] < threshold:
                await self.alerts.send(
                    severity='critical',
                    message=f'Completeness check failed: {{table}}.{{col}} at {{result["pct"]}}%'
                )

    async def check_freshness(self, table, timestamp_col, max_age):
        '''Check data is within freshness SLA'''
        pass

    async def check_volume(self, table, expected_range):
        '''Check record count is within expected range'''
        pass
```

### 3. SLA Definitions
| Data Asset | Dimension | SLA Target | Measurement Window | Escalation |
|-----------|-----------|-----------|-------------------|-----------|
| ... | Freshness | < 1 hour | Rolling 24h | Page on-call |
| ... | Completeness | >= 99.5% | Per batch | Slack alert |
| ... | Accuracy | >= 99.9% | Daily audit | Email + ticket |
| ... | Availability | 99.95% uptime | Monthly | Incident report |

### 4. Remediation Procedures
For each failure type:
- **Detection**: How the issue is identified (automated alert, user report)
- **Triage**: Severity classification and impact assessment
- **Resolution**: Step-by-step remediation runbook
- **Prevention**: Root cause analysis template and preventive measures
- **Communication**: Stakeholder notification templates

### 5. Quality Scorecard
- Overall data health score calculation
- Domain-level quality scores
- Trend analysis and regression detection
- Executive summary dashboard design
- Monthly quality report template
"""

        return await self.run_task(prompt)

    async def work(self, task: str) -> TaskResult:
        """General data work"""
        await self.notify(f"Starting: {task[:50]}...")
        return await self.run_task(task)


async def main():
    """CLI entry point"""
    import argparse
    import json

    parser = argparse.ArgumentParser(description="Denisy - Chief Data Officer")
    parser.add_argument("--research", type=str, help="Research sources for topic")
    parser.add_argument("--scrape", type=str, help="Build scraper for URL")
    parser.add_argument("--spec", type=str, help="Data specification for scraper")
    parser.add_argument("--schema", type=str, help="Design database schema")
    parser.add_argument("--etl", type=str, nargs=2, metavar=("SOURCE", "DEST"), help="Build ETL pipeline")
    parser.add_argument("--validate", type=str, help="Validate data at path")
    parser.add_argument("--governance", type=str, help="Design data governance framework for organization")
    parser.add_argument("--domains", type=str, nargs="+", help="Data domains (used with --governance)")
    parser.add_argument("--privacy", type=str, nargs="+", help="Run privacy assessment on data sources")
    parser.add_argument("--regulations", type=str, nargs="+", default=["GDPR", "CCPA"], help="Regulations for privacy assessment")
    parser.add_argument("--dashboard", type=str, nargs="+", help="Design analytics dashboard with metrics")
    parser.add_argument("--audience", type=str, default="executive", help="Dashboard audience (used with --dashboard)")
    parser.add_argument("--lineage", type=str, help="Map data lineage for pipeline description")
    parser.add_argument("--streaming", type=str, nargs="+", help="Design streaming pipeline (sources)")
    parser.add_argument("--streaming-dest", type=str, nargs="+", help="Streaming pipeline destinations")
    parser.add_argument("--streaming-reqs", type=str, help="Streaming pipeline requirements")
    parser.add_argument("--data-model", type=str, help="Design data model for requirements")
    parser.add_argument("--modeling-approach", type=str, default="dimensional", help="Modeling approach (dimensional, star, snowflake, data_vault)")
    parser.add_argument("--quality-framework", type=str, nargs="+", help="Design data quality framework for sources")
    parser.add_argument("--task", type=str, help="Run general task")
    parser.add_argument("--status", action="store_true", help="Show status")

    args = parser.parse_args()

    agent = DenisyAgent()

    if args.status:
        print(json.dumps(agent.get_status(), indent=2))
        return

    if args.research:
        result = await agent.research_sources(args.research)
        print(result.output)
        return

    if args.scrape and args.spec:
        result = await agent.build_scraper(args.scrape, args.spec)
        print(result.output)
        return

    if args.schema:
        result = await agent.design_schema(args.schema)
        print(result.output)
        return

    if args.etl:
        result = await agent.build_etl_pipeline(args.etl[0], args.etl[1])
        print(result.output)
        return

    if args.validate:
        result = await agent.validate_data(args.validate)
        print(result.output)
        return

    if args.governance:
        domains = args.domains or ["default"]
        result = await agent.data_governance_framework(args.governance, domains)
        print(result.output)
        return

    if args.privacy:
        result = await agent.privacy_assessment(args.privacy, args.regulations)
        print(result.output)
        return

    if args.dashboard:
        result = await agent.design_analytics_dashboard(args.dashboard, args.audience)
        print(result.output)
        return

    if args.lineage:
        result = await agent.data_lineage_map(args.lineage)
        print(result.output)
        return

    if args.streaming:
        destinations = args.streaming_dest or ["database"]
        requirements = args.streaming_reqs or "Low latency, high throughput"
        result = await agent.design_streaming_pipeline(args.streaming, destinations, requirements)
        print(result.output)
        return

    if args.data_model:
        result = await agent.data_model(args.data_model, args.modeling_approach)
        print(result.output)
        return

    if args.quality_framework:
        result = await agent.data_quality_framework(args.quality_framework)
        print(result.output)
        return

    if args.task:
        result = await agent.work(args.task)
        print(result.output)
        return

    print("Denisy - Chief Data Officer")
    print("===========================")
    print("Use --help for options")


if __name__ == "__main__":
    asyncio.run(main())
