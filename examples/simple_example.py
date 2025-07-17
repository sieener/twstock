#!/usr/bin/env python3
# -*- coding: utf-8    -*-
"""
Simple example to fetch and display Taiwan stock data for TSMC (2330)
"""
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import twstock


def main():
    """Simple example to fetch TSMC (2330) stock data"""
    print("=== Taiwan Stock Data Example ===")
    print("Fetching data for TSMC (2330)...\n")

    try:
        # Create a Stock instance for TSMC (2330)
        stock = twstock.Stock("2330")

        # Basic information
        print(f"Stock ID: {stock.sid}")
        print(f"Total trading days: {len(stock.data)}")
        print("-" * 50)

        # Display recent data
        if stock.data and len(stock.data) > 0:
            print("Recent Trading Data:")
            print("Date\t\tClose\tVolume")
            print("-" * 40)

            # Show last 5 days
            recent_data = stock.data[-5:] if len(stock.data) >= 5 else stock.data
            for data_point in recent_data:
                volume_str = (
                    f"{data_point.capacity//1000}K" if data_point.capacity else "N/A"
                )
                print(f"{data_point.date}\t{data_point.close}\t{volume_str}")

            print("-" * 40)

            # Latest price info
            latest_data = stock.data[-1]
            print(f"Latest Date: {latest_data.date}")
            print(f"Latest Price: ${latest_data.close}")
            print(f"Day's Range: ${latest_data.low} - ${latest_data.high}")

            # Price change calculation
            if len(stock.data) > 1:
                prev_close = stock.data[-2].close
                price_change = latest_data.close - prev_close
                change_percent = (
                    (price_change / prev_close) * 100 if prev_close > 0 else 0
                )
                print(f"Price Change: ${price_change:.2f} ({change_percent:+.2f}%)")

            # Simple moving average
            if len(stock.price) >= 5:
                recent_prices = stock.price[-5:]
                ma_5 = sum(recent_prices) / len(recent_prices)
                print(f"5-day Average: ${ma_5:.2f}")

        else:
            print("No data available for this stock.")

        print("\n=== Fetch completed! ===")

    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure twstock is properly installed: pip install twstock")

    except (ConnectionError, TimeoutError) as e:
        print(f"Network error: {e}")
        print("Check your internet connection and try again.")

    except ValueError as e:
        print(f"Data error: {e}")
        print("The stock code might be invalid or no data is available.")

    except Exception as e:
        print(f"Unexpected error: {e}")
        print("Try updating stock codes: twstock.__update_codes()")


if __name__ == "__main__":
    main()
