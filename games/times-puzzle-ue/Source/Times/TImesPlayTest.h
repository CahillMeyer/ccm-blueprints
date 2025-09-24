// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include <vector>
#include <map>
#include <set>
#include <array>
#include <utility>

/**
 * 
 */

template<typename S>
auto select_random(const S& s, size_t n) {
	auto it = std::begin(s);
	// 'advance' the iterator n times
	std::advance(it, n);
	return it;
}

struct Factors
{
	int id;
	int First = -1;
	int Second = -1;
	int used = 0;

	Factors(int id, int first, int second);
	bool operator< (const Factors& rhs) const;
	bool operator== (const Factors& rhs) const;
	bool SameValues(int first, int second);
};

struct FactorCompareById
{
	bool operator() (Factors* lhs, Factors* rhs) const;
};

class TImesPlayTest
{
	private:
		std::map</*product*/int, std::map</*factors*/std::pair<int, int>,/*times used*/ int > > Values;
		int MaxFactor = 10;
		int MinFactor = 1;
		bool RetryWrongAnswers = true;

		int CurrentProduct; 
		std::pair<int, int> CurrentFactors;
		
		void SetProductValues();
		
		int GetProduct();
		std::vector<int> GetNumbersList(int size);
		std::pair<int, int> RandomMinUsedFactors(void);
		std::vector<int> Randomize(std::vector<int> v);

	public:
		TImesPlayTest(int maxFactor = 10, int minFactor = 1);
		~TImesPlayTest();

		std::vector<int> GetNumbers(int& product, int size = 9);
		bool CheckFactors(int factor1, int factor2);

		bool AllNumbersUsed(void);
	};
