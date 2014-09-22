#!/bin/bash

## grep payload, 2 lines
grep -E  "Payload|oslo.message" trace-web.txt >> trace-web-payload.txt

## grep header+property
grep -vE  "Payload|oslo.message" trace-web.txt >> trace-web-header.txt 

# grep all exchanges
grep Exchange: trace-web-header.txt  | awk '{print $2}' >> trace-web-all-exchange.txt

# grep blank exchange with other properties
grep -A 7 -B 4 "Exchange:     $" trace-web-header.txt  >> trace-web-blank-exchange.txt

