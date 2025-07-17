# TWStock Application Structure and Instructions

## Overview
TWStock is a Python library for fetching and analyzing Taiwan stock market data from TWSE (Taiwan Stock Exchange) and TPEx (Taipei Exchange). It provides real-time data, historical analysis, and various stock market utilities.

## Project Structure

```
twstock/
├── twstock/                # Main package directory
│   ├── __init__.py        # Package initialization
│   ├── __main__.py        # CLI entry point
│   ├── analytics.py       # Technical analysis and calculations
│   ├── legacy.py          # Legacy compatibility functions
│   ├── proxy.py           # Network proxy handling
│   ├── realtime.py        # Real-time stock data fetching
│   ├── stock.py           # Core stock data class and methods
│   ├── cli/               # Command-line interface tools
│   │   ├── __init__.py
│   │   ├── best_four_point.py  # Best four point analysis CLI
│   │   ├── realtime.py         # Real-time data CLI
│   │   └── stock.py            # Stock data CLI
│   ├── codes/             # Stock code management
│   │   ├── __init__.py
│   │   ├── codes.py            # Stock code utilities
│   │   ├── fetch.py            # Code fetching functions
│   │   ├── tpex_equities.csv   # TPEx stock codes
│   │   └── twse_equities.csv   # TWSE stock codes
│   └── mock/              # Mock data for testing
│       └── __init__.py
├── instruction.md         # This file - project documentation
└── __pycache__/          # Python bytecode cache
```

## Key Components

### 1. Core Modules
- **stock.py**: Main Stock class for historical data, price information, and basic operations
- **realtime.py**: Real-time stock data fetching from Taiwan exchanges
- **analytics.py**: Technical analysis tools including moving averages, trends, and indicators
- **proxy.py**: Network proxy support for data fetching
- **legacy.py**: Backward compatibility functions for older versions

### 2. CLI Interface (`cli/`)
- **stock.py**: Command-line interface for stock data queries
- **realtime.py**: CLI for real-time market data
- **best_four_point.py**: Technical analysis tool for identifying optimal buy/sell points

### 3. Stock Code Management (`codes/`)
- **codes.py**: Stock symbol and code utilities
- **fetch.py**: Functions to retrieve and update stock code lists
- **twse_equities.csv**: Taiwan Stock Exchange listed companies
- **tpex_equities.csv**: Taipei Exchange (OTC) listed companies

### 4. Data Sources
- **TWSE (Taiwan Stock Exchange)**: Main board stocks (大盤)
- **TPEx (Taipei Exchange)**: Over-the-counter stocks (櫃買中心)

## Core Functionality

### Stock Data Features
- Historical stock prices (open, high, low, close, volume)
- Real-time price updates
- Technical indicators and moving averages
- Stock code lookup and validation
- Market trend analysis

### Technical Analysis
- Simple Moving Average (SMA)
- Best four point analysis
- Price trend identification
- Volume analysis
- Support and resistance levels

### Real-time Data
- Live price feeds
- Market status monitoring
- Intraday price movements
- Volume tracking

## Usage Examples

### Basic Stock Data
```python
import twstock

# Get stock data
stock = twstock.Stock('2330')  # TSMC
prices = stock.price
dates = stock.date
```

### Real-time Data
```python
# Get real-time price
realtime = twstock.get_raw('2330')
current_price = realtime['realtime']['latest_trade_price']
```

### Technical Analysis
```python
# Moving average analysis
ma_data = twstock.analytics.moving_average(stock.price, 5)
```

### CLI Usage
```bash
# Get stock information
python -m twstock.cli.stock 2330

# Real-time monitoring
python -m twstock.cli.realtime 2330

# Best four point analysis
python -m twstock.cli.best_four_point 2330
```

## Installation & Setup

### Prerequisites
- Python 3.6+
- Internet connection for data fetching
- Optional: Proxy configuration for network access

### Dependencies
- requests (for HTTP requests)
- lxml (for HTML parsing)
- Additional packages as specified in requirements

### Usage Patterns
1. **Library Usage**: Import as a Python package for data analysis
2. **CLI Usage**: Command-line tools for quick queries
3. **Data Pipeline**: Integration into larger financial analysis systems

## Data Flow

1. **Stock Code Resolution**: Convert stock symbols to internal codes
2. **Data Fetching**: Retrieve data from TWSE/TPEx APIs
3. **Data Processing**: Parse and clean market data
4. **Analysis**: Apply technical indicators and calculations
5. **Output**: Return structured data or CLI results

## Development Notes

### Code Organization
- Modular design with separate concerns
- CLI tools provide user-friendly interfaces
- Mock module supports testing without live data
- Legacy module maintains backward compatibility

### Data Handling
- Efficient caching of stock codes
- Error handling for network issues
- Support for both exchanges (TWSE/TPEx)
- Real-time and historical data integration

### Extension Points
- Custom technical indicators in analytics.py
- Additional CLI tools in cli/ directory
- New data sources through proxy.py
- Enhanced mock data for testing

## Contributing
- Follow existing code patterns
- Add tests for new functionality
- Update stock code CSV files when needed
- Maintain CLI interface consistency

## License
[Specify license type based on project requirements]