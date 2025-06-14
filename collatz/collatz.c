#include <stdio.h>
#include <stdbool.h>
#include "uthash.h"

typedef struct {
    int key;
    long long value;
    UT_hash_handle hh;
} IntLongMap;

bool isEven(long long number) {
    return number % 2 == 0;
}
long long advance(long long number) {
    if (isEven(number)) {
        return number / 2;
    } else {
        return number * 3 + 1;
    }
}

int howManySteps(long long number) {
    if (number <= 0) {
        return -1;
    }
    int stepCount = 1;
    while (number != 1) {
        //printf("Step %d: %lld => %lld\n", stepCount, number, advance(number));
        number = advance(number);
        if (number == 1) {
            break;
        }
        stepCount += 1;
    }
    return stepCount;
}

void printMap(IntLongMap *map) {
    IntLongMap *entry;
    for (entry = map; entry != NULL; entry = entry->hh.next) {
        printf("{%d Steps: %lld} ", entry->key, entry-> value);
    }
}


long long lowestNumberThatReachesStep(int highestStepCount) {
    long long startingNumber = 2;
    while (howManySteps(startingNumber) < highestStepCount) {
        startingNumber += 1;
    }
    return startingNumber;
}

int sortByKey(IntLongMap *a, IntLongMap *b) {
    return (a->key - b-> key);
}

void popLowest(IntLongMap **mapPtr) {
    IntLongMap *first = *mapPtr;
    if (first) {
        HASH_DEL(*mapPtr, first);
        free(first);
    }
}

IntLongMap* TopListOfNumbersToStep(int highestStepCount, long long startingNumber, int dictLength) {
    IntLongMap *map = NULL;
    int stepsOfNumber = howManySteps(startingNumber);
    while (stepsOfNumber < highestStepCount) {
        IntLongMap *existing;
        IntLongMap *entry = malloc(sizeof(IntLongMap));
        HASH_FIND_INT(map, &stepsOfNumber, existing);
        if (existing == NULL) {
            entry->key = stepsOfNumber;
            entry->value = startingNumber;
            HASH_ADD_INT(map, key, entry);
        }
        if (HASH_COUNT(map) == dictLength) {
            HASH_SORT(map, sortByKey);
            popLowest(&map);
        }
        startingNumber += 1; // Increment
        stepsOfNumber = howManySteps(startingNumber); // Update
    }
    return map;
}



long long main() {
    //prlong longf("%d\n", 8);
    //printf("%d\n", howManySteps(1234567891234567891LL));
    printMap(TopListOfNumbersToStep(393,1,10));
    //printf("%d\n", lowestNumberThatReachesStep(402));
    return 0;
}