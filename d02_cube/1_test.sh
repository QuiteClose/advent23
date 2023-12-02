#!/bin/bash

EXPECT_RESULT="8"
ACTUAL_RESULT=$(python 1_task.py < sample.txt)

echo "Expected result: $EXPECT_RESULT"
echo "Actual result: $ACTUAL_RESULT"
if [ "$EXPECT_RESULT" == "$ACTUAL_RESULT" ]; then
    echo "Test: Pass"
else
    echo "Test: Fail"
fi