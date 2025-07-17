#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Advanced example showing technical analysis for TSMC (2330)
"""
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import twstock
from twstock import BestFourPoint


def main():
    """Advanced example with technical analysis for TSMC (2330)"""
    print("=== Advanced Taiwan Stock Analysis ===")
    print("Fetching and analyzing TSMC (2330)...\n")

    try:
        # Create a Stock instance for TSMC (2330)
        stock = twstock.Stock("2330")

        # Basic information
        print(f"Stock ID: {stock.sid}")

        # Try to get company name if codes are available
        try:
            if hasattr(twstock, "codes") and "2330" in twstock.codes:
                company_info = twstock.codes["2330"]
                print(f"Company: {company_info.name}")
        except (AttributeError, KeyError):
            print("Company: TSMC (Taiwan Semiconductor)")

        print(f"Data points: {len(stock.data)}")
        print("-" * 60)

        if not stock.data:
            print("No data available.")
            return

        # Latest trading info
        latest = stock.data[-1]
        print("Latest Trading Day:")
        print(f"Date: {latest.date}")
        print(f"Open: ${latest.open}")
        print(f"High: ${latest.high}")
        print(f"Low: ${latest.low}")
        print(f"Close: ${latest.close}")
        print(f"Volume: {latest.capacity:,} shares")
        print(f"Turnover: ${latest.turnover:,.0f}")
        print("-" * 60)

        # Price analysis
        print("Price Analysis:")
        if len(stock.price) > 1:
            current_price = stock.price[-1]
            prev_price = stock.price[-2]
            change = current_price - prev_price
            change_pct = (change / prev_price) * 100 if prev_price > 0 else 0

            print(f"Current Price: ${current_price}")
            print(f"Previous Close: ${prev_price}")
            print(f"Change: ${change:.2f} ({change_pct:+.2f}%)")

            # Price statistics
            prices = stock.price
            print(f"All-time High: ${max(prices)}")
            print(f"All-time Low: ${min(prices)}")
            print(f"Average Price: ${sum(prices)/len(prices):.2f}")

        print("-" * 60)

        # Moving averages
        print("Moving Averages:")
        try:
            if len(stock.price) >= 5:
                ma_5 = stock.moving_average(stock.price, 5)
                if ma_5:
                    print(f"5-day MA: ${ma_5[-1]:.2f}")

            if len(stock.price) >= 10:
                ma_10 = stock.moving_average(stock.price, 10)
                if ma_10:
                    print(f"10-day MA: ${ma_10[-1]:.2f}")

            if len(stock.price) >= 20:
                ma_20 = stock.moving_average(stock.price, 20)
                if ma_20:
                    print(f"20-day MA: ${ma_20[-1]:.2f}")

        except Exception as e:
            print(f"Moving average calculation error: {e}")

        print("-" * 60)

        # Technical Analysis
        print("Technical Analysis:")
        try:
            # Continuous days analysis
            continuous_days = stock.continuous(stock.price)
            if continuous_days > 0:
                print(f"Rising for {continuous_days} consecutive days")
            elif continuous_days < 0:
                print(f"Falling for {abs(continuous_days)} consecutive days")
            else:
                print("Price unchanged from previous day")

            # Best Four Point analysis
            bfp = BestFourPoint(stock)

            # Individual signals
            buy_signal = bfp.best_four_point_to_buy()
            sell_signal = bfp.best_four_point_to_sell()

            print(f"Buy Signal: {'YES' if buy_signal else 'NO'}")
            print(f"Sell Signal: {'YES' if sell_signal else 'NO'}")
            # Overall recommendation
            if buy_signal:
                print("📈 Recommendation: BUY")
            elif sell_signal:
                print("📉 Recommendation: SELL")
            else:
                print("📊 Recommendation: HOLD")

        except Exception as e:
            print(f"Technical analysis error: {e}")

        print("-" * 60)

        # Real-time data (if available)
        print("Real-time Data:")
        try:
            realtime_data = twstock.realtime.get("2330")
            if realtime_data and "realtime" in realtime_data:
                rt = realtime_data["realtime"]
                print(f"Real-time Price: ${rt.get('latest_trade_price', 'N/A')}")
                print(f"Real-time Volume: {rt.get('trade_volume', 'N/A'):,}")
                print(f"Best Bid: ${rt.get('best_bid_price', ['N/A'])[0]}")
                print(f"Best Ask: ${rt.get('best_ask_price', ['N/A'])[0]}")
            else:
                print("Real-time data not available (market may be closed)")
        except Exception as e:
            print(f"Real-time data error: {e}")

        print("\n=== Analysis completed! ===")

    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure twstock is installed: pip install twstock")

    except (ConnectionError, TimeoutError) as e:
        print(f"Network error: {e}")
        print("Check your internet connection.")

    except ValueError as e:
        print(f"Data error: {e}")
        print("Stock code might be invalid.")

    except Exception as e:
        print(f"Unexpected error: {e}")
        print("Try updating codes: twstock.__update_codes()")


if __name__ == "__main__":
    main()
