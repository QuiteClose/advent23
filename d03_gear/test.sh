#!/bin/bash

EXPECT_RESULT="4361"
ACTUAL_RESULT=$(python task.py < sample.txt)

echo "Executing 'python task.py < sample.txt'"
echo "Expected result: $EXPECT_RESULT"
echo "Actual result: $ACTUAL_RESULT"
if [ "$EXPECT_RESULT" == "$ACTUAL_RESULT" ]; then
    echo "Test: Pass"
else
    echo "Test: Fail"
    exit 1
fi
