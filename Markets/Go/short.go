/*
* Short Selling Script written in Go
* Returns a dataframe
* Package link: https://github.com/rocketlaunchr/dataframe-go 
*
* install with: 
* go get -u github.com/rocketlaunchr/dataframe-go 
*
* import with: 
* import dataframe "github.com/rocketlaunchr/dataframe-go"
*/

package main

import (
  "fmt"
  dataframe "github.com/rocketlaunchr/dataframe-go"
)

type Stock struct {
  price float64
  shares float64
  mfee float64
  end float64
  steps float64
}

func first_transaction(price float64, shares float64) []float64{
	var principal float64 = shares * price
	var margin_amount float64 = 0.5 * principal
	var total_req float64 = principal + margin_amount
	res := []float64{shares, price, principal, margin_amount, total_req}

	return res
}

func price_increase(end float64, steps float64, mfee float64, shares float64, price float64) {
	var principal float64 = shares *  price
	var margin_amount float64 = 0.5 * principal
	var initial_req float64 = margin_amount + principal
	var margin_call float64 = 0

	sval := dataframe.NewSeriesFloat64("Shares", nil, shares)
	share_price := dataframe.NewSeriesFloat64("Share Price",nil,price)
	short_val := dataframe.NewSeriesFloat64("Short Value",nil,  principal)
	margin_requirement := dataframe.NewSeriesFloat64("Margin Requirement",nil,  margin_amount)
	total_requirement := dataframe.NewSeriesFloat64("Total Requirement",nil,initial_req)
	mcall := dataframe.NewSeriesFloat64("Margin Call", nil, margin_call)

	for i:=price+steps; i < end; i+=steps {
		var short_value float64 = shares * i
		var margin_req float64 = short_value * mfee
		var total_req float64 = short_value + margin_req
		if total_req < initial_req {
		  margin_call = 0
		  sval.Append(shares)
		  share_price.Append(i)
		  short_val.Append(short_value)
		  margin_requirement.Append(margin_req)
		  total_requirement.Append(total_req)
		  mcall.Append(margin_call)
	  } else {
			margin_call = total_req - initial_req
			sval.Append(shares)
			share_price.Append(i)
			short_val.Append(short_value)
			margin_requirement.Append(margin_req)
			total_requirement.Append(total_req)
			mcall.Append(margin_call)
		}
	}
	df := dataframe.NewDataFrame(sval, share_price, short_val, margin_requirement, total_requirement, mcall)
	fmt.Println(df.Table())
}

func price_decrease(end float64, steps float64, mfee float64, shares float64, price float64) {
  var principal float64 = shares * price
  var margin_amount float64 = 0.5 * principal
  var initial_req float64 = margin_amount + principal
  var mrel float64 = 0

  sval := dataframe.NewSeriesFloat64("Shares", nil, shares)
  share_price := dataframe.NewSeriesFloat64("Share Price",nil,price)
  short_val := dataframe.NewSeriesFloat64("Short Sale Value",nil,  principal)
  margin_val := dataframe.NewSeriesFloat64("Additional Value",nil,  margin_amount)
  total_requirement := dataframe.NewSeriesFloat64("Total Requirement",nil,initial_req)
  mreleased := dataframe.NewSeriesFloat64("Margin Released", nil, mrel)

  for i := price - steps; i > end; i-= steps {
	var short_value float64 = shares * i
	var margin_req float64 = 0.5 * short_value
	var total_req float64 = short_value + margin_req
	mrel = initial_req - total_req
	sval.Append(shares)
	share_price.Append(i)
	short_val.Append(short_value)
	margin_val.Append(margin_req)
	total_requirement.Append(total_req)
	mreleased.Append(mrel)
  }

  df := dataframe.NewDataFrame(sval, share_price, short_val, margin_val, total_requirement, mreleased)
  fmt.Println(df.Table())
}

func main() {
	/*
	stock := Stock{50, 1000}

	ans := first_transaction(stock.price, stock.shares)

	fmt.Println("First Transaction: ", ans)
	*/
	//Struct 
	//price, shares, mfee, end, steps

	//Price Increase
	stock := Stock{50.00, 1000.00, 0.3, 80.00, 5.00}

	price_increase(stock.end, stock.steps, stock.mfee, stock.shares, stock.price)

	//Price Decrease 
	stock2 := Stock{50.00, 1000.00, 0.3, 30.00, 5.00}
	price_decrease(stock2.end, stock2.steps, stock2.mfee, stock2.shares, stock2.price)

}
