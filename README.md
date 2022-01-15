<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/shark_ui_patches/logofullsize.png?raw=true">
</p>

# Shark Plugins

These are the plugins to use with the Shark algorithmic trading platform. 

For more information about Shark, see [here](https://github.com/danielneil/Shark).

## yahoo_finance_data

Obtains historical instrument data from Yahoo! finance and imports it into Shark.

```
  - name: yahoo_finance_data
    desc: "Yahoo Finance [ BTC-USD Historical Data File ]"
    group: "Yahoo Finance [ Historical Data ]"
    period1: 1597479263
    period2: 1629015263
    interval: 1d
    includeAdjustedClose: true
```
## sma

Computes a simple moving average. 

```
  - name: sma
    desc: "Simple Moving Average - 50 Days"
    group: "SMA: [ 50 Day ]"
    period: 50
    data_format: yahoo_finance_data
```
## backtest

Runs custom backtest code. 

```
  - name: backtest
    desc: "BACKTEST: [ Moving Averages ]"
    group: "Backtesting"
    file: backtest_moving_averages.py
    shares: 1000
    capital: 1000000
    data_format: yahoo_finance_data
    period: 50
```
