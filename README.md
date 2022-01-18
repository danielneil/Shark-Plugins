<p align="center">
  <img src="https://github.com/danielneil/Shark/blob/main/shark/files/shark_ui_patches/logofullsize.png?raw=true">
</p>

# Shark Plugins

These are the plugins to use with the Shark algorithmic trading platform. 

For more information about Shark, see [here](https://github.com/danielneil/Shark).

## Contents
[yahoo_finance_data](#yahoo_finance_data)  
[sma](#sma)  
[ema](#ema)  
[backtest](#backtest)  
[rsi](#rsi)

[correlation](#correlation)

<a name="yahoo_finance_data"/>

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

<a name="sma"/>

## sma

Computes a simple moving average (sma) - the average value of a certain number of previous periods.

```
  - name: sma
    desc: "Simple Moving Average - 50 Days"
    group: "SMA: [ 50 Day ]"
    period: 50
    data_format: yahoo_finance_data
```

<a name="ema"/>

## ema

Computes an exponential moving average (ema) - a moving average that gives more weight to recent observations

```
  - name: ema
    desc: "Exponential Moving Average - 50 Days"
    group: "EMA: [ 50 Day ]"
    period: 50
    data_format: yahoo_finance_data
```

<a name="backtest"/>

## backtest

Handles the execution of customised backtesting code. 

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

<a name="rsi" />

## rsi

Computes the relative strength index (rsi) for the given instrument, with ema or sma moving average parameter.

```
 - name: rsi
   desc: "RSI: 2 Period with EMA"
   group: "RSI" 
   periods: 14
   max: 70
   min: 30
   ma_type: ema
   data_format: yahoo_finance_data
```
