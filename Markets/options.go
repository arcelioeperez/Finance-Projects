// Run with 
// go run options.go

package main

import (
 "fmt"
 "math"
)

func calls(S, E, cprice float64) float64 {
    profitability := math.Max(0, S - (E + cprice))
    return profitability
}

func puts(S, E, cprice float64) float64 {
	profitability := math.Max(0, (E - cprice) - S)
	return profitability
}

func main() {
	//Call test 
	var Sc float64 = 110.00
   	var Ec float64 = 90.00
    	var cpricec float64 = 1.20

    	cans := calls(Sc, Ec, cpricec)

    	fmt.Printf("Call Profitability: %.2f ", cans)
	fmt.Printf("\n")

	//Put test
	var S float64 = 90.00
	var E float64 = 100.00
	var cprice float64 = 2.00
	ans := puts(S, E, cprice)

	fmt.Println("Put Profitability: ", ans)
}
