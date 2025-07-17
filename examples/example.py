#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic example to fetch and display Taiwan stock data for TSMC (2330)
"""

import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import twstock


def main():
    print("=== Taiwan Stock Data Example ===")
    print("Fetching data for TSMC (2330)...\n")

    try:
        # Create a Stock instance for TSMC (2330)
        stock = twstock.Stock("2330")

        # Basic stock information
        print(f"Stock ID: {stock.sid}")

        # Check if we have stock code information
        if "2330" in twstock.codes:
            stock_info = twstock.codes["2330"]
            print(f"Company Name: {stock_info.name}")
            print(f"Market: {stock_info.market}")

        print(f"Total trading days: {len(stock.data)}")
        print("-" * 50)

        # Display latest 5 trading days
        print("Latest 5 Trading Days:")
        print("Date\t\tOpen\tHigh\tLow\tClose\tVolume")
        print("-" * 70)

        for i in range(min(5, len(stock.data))):
            data = stock.data[-(i + 1)]  # Get from most recent backwards
            volume_k = data.capacity // 1000 if data.capacity else 0
            print(
                f"{data.date}\t{data.open}\t{data.high}\t{data.low}\t{data.close}\t{volume_k}K"
            )

        print("-" * 70)

        # Price analysis
        if len(stock.price) > 0:
            latest_price = stock.price[-1]
            print(f"Latest Close Price: ${latest_price}")

            if len(stock.price) > 1:
                prev_price = stock.price[-2]
                change = latest_price - prev_price
                change_pct = (change / prev_price) * 100 if prev_price > 0 else 0
                print(f"Price Change: ${change:.2f} ({change_pct:+.2f}%)")

            # Price statistics (last 30 days)
            recent_prices = stock.price[-30:] if len(stock.price) >= 30 else stock.price
            if recent_prices:
                print(f"30-day High: ${max(recent_prices)}")
                print(f"30-day Low: ${min(recent_prices)}")
                print(f"30-day Average: ${sum(recent_prices)/len(recent_prices):.2f}")

        print("-" * 50)

        # Moving averages
        if len(stock.price) >= 5:
            ma_5 = stock.moving_average(stock.price, 5)
            if ma_5:
                print(f"5-day Moving Average: ${ma_5[-1]:.2f}")

        if len(stock.price) >= 20:
            ma_20 = stock.moving_average(stock.price, 20)
            if ma_20:
                print(f"20-day Moving Average: ${ma_20[-1]:.2f}")

        print("\n=== Example completed successfully! ===")

    except (ConnectionError, TimeoutError, ValueError) as e:
        print(f"Error occurred: {e}")
        print("This might be due to:")
        print("1. Network connection issues")
        print("2. Invalid stock code")
        print("3. Market is closed or no data available")
        print("\nTry running: twstock.__update_codes() first to update stock codes")


if __name__ == "__main__":
    main()
