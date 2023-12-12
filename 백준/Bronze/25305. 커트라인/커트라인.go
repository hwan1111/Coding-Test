package main

import (
	"fmt"
	"sort"
)

func main() {
	var n, k int
	fmt.Scan(&n, &k)

	x := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&x[i])
	}

	sort.Sort(sort.Reverse(sort.IntSlice(x)))
	fmt.Println(x[k-1])
}
