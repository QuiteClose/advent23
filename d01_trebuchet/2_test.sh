#!/bin/bash

EXPECT_RESULT="281"
ACTUAL_RESULT=$(python 2_task.py < 2_sample.txt)

echo "Expected result: $EXPECT_RESULT"
echo "Actual result: $ACTUAL_RESULT"
if [ "$EXPECT_RESULT" == "$ACTUAL_RESULT" ]; then
    echo "Test: Pass"
else
    echo "Test: Fail"
    exit 1
fi
