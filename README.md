# OSINT Investigation Framework - 10 Level Analysis

A comprehensive Python framework for multi-level OSINT (Open Source Intelligence) investigations. This framework systematically analyzes email addresses, usernames, and online presence across 10 distinct investigation levels.

## Features

### 10-Level Investigation Hierarchy

1. **Level 1: Email Search** - Discovers profiles across 100+ platforms
2. **Level 2: Username Extraction** - Extracts and generates username variants
3. **Level 3: Domain Lookup** - Queries WHOIS and DNS records
4. **Level 4: Social Graph** - Maps connections and relationships
5. **Level 5: Content Analysis** - Analyzes sentiment and topics
6. **Level 6: Financial Footprint** - Detects payment platforms and crypto
7. **Level 7: Reverse Image** - Analyzes images and metadata
8. **Level 8: Email Reputation** - Checks SPF, DKIM, DMARC
9. **Level 9: Cross-Platform Correlation** - Correlates all findings
10. **Level 10: Intelligence Synthesis** - Final threat assessment and recommendations

## Quick Start

`ash
# Run full investigation
python run_osint_investigation.py nickfoy.design@gmail.com

# Run master orchestrator
python osint_master_orchestrator.py

# Run individual level
python level_1_email_search.py
`

## Files

- **level_1_email_search.py** - Email platform discovery
- **level_2_username_extraction.py** - Username variant generation
- **level_3_domain_lookup.py** - Domain and registrar information
- **level_4_social_graph.py** - Social network mapping
- **level_5_content_analysis.py** - Content sentiment analysis
- **level_6_financial_footprint.py** - Financial footprint detection
- **level_7_reverse_image.py** - Image metadata extraction
- **level_8_email_reputation.py** - Email infrastructure analysis
- **level_9_correlation.py** - Cross-platform correlation
- **level_10_intelligence_synthesis.py** - Threat assessment and recommendations
- **osint_master_orchestrator.py** - Sequential execution of all 10 levels
- **report_generator.py** - HTML/Markdown/JSON report generation
- **run_osint_investigation.py** - Main entry point with error handling

## Requirements

- Python 3.7+

## Installation

`ash
git clone https://github.com/101128013/wubu.git
cd wubu
python run_osint_investigation.py <email>
`

## Output

Each level generates:
- JSON results (level_X_results.json)
- Aggregated findings
- Risk assessments
- Recommendations

## Documentation

See individual level files for detailed documentation and configuration options.

## Legal & Ethical

This framework is for authorized security research and pen testing only. Users are responsible for:
- Obtaining proper authorization
- Complying with applicable laws
- Respecting privacy
- Using results ethically

**Unauthorized surveillance or tracking is illegal in most jurisdictions.**

## Version

1.0 - Initial Release  
March 17, 2026

## License

For authorized security research use only.