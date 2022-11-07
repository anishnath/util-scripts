#!/bin/bash

function MemoryUsage() {

    read -r -a arr3 < <(free -h | grep 'Mem' | cut -d' ' -f2- | tr -d 'i')

    memory_total="${arr3[0]}"
    memory_used="${arr3[1]}"
    memory_free="${arr3[2]}"
    memory_shared="${arr3[3]}"
    memory_buffer_cache="${arr3[4]}"
    memory_available="${arr3[5]}"

    echo && echo "Total: $memory_total"
    echo "Used: $memory_used"
    echo "Free: $memory_free"
    echo "Shared: $memory_shared"
    echo "Bufer Cache: $memory_buffer_cache"
    echo "Available: $memory_available"
    echo
}
