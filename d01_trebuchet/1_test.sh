#!/bin/bash

EXPECT_RESULT="142"
ACTUAL_RESULT=$(python 1_task.py < 1_sample.txt)

echo "Expected result: $EXPECT_RESULT"
echo "Actual result: $ACTUAL_RESULT"
if [ "$EXPECT_RESULT" == "$ACTUAL_RESULT" ]; then
    echo "Test: Pass"
else
    echo "Test: Fail"
fi
