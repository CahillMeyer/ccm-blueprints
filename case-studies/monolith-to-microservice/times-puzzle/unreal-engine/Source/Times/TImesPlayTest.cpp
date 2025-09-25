// Fill out your copyright notice in the Description page of Project Settings.


#include "TImesPlayTest.h"
#include <utility>
#include <algorithm>
#include <cassert>
#include <iterator>
#include <random>
#include <time.h>


bool FactorCompareById::operator() (Factors* lhs, Factors* rhs) const
{
	return lhs->id < rhs->id;
}

Factors::Factors(int id, int first, int second)
{
	Factors::id = id;
	First = first <= second ? first : second;
	Second = first >= second ? first : second;
}

bool Factors::operator< (const Factors& rhs) const
{
	return First < rhs.First && Second < rhs.Second || First == rhs.First && Second < rhs.Second;
}

bool Factors::operator== (const Factors& rhs) const
{
	return rhs.First == First && rhs.Second == Second;
}

bool Factors::SameValues(int first, int second)
{
	bool returnVal = false;
	if ((first == First && second == Second) || (first == Second && second == First))
	{
		returnVal = true;
	}
	return returnVal;
}

TImesPlayTest::TImesPlayTest(int maxFactor, int minFactor)
{
	if (minFactor < maxFactor)
	{
		MaxFactor = maxFactor;
		MinFactor = minFactor; 

		SetProductValues();
	}
	else
	{
		throw _invalid_parameter_noinfo;
	}
}

TImesPlayTest::~TImesPlayTest()
{
}

// Makes sure all possible combinations can be used
void TImesPlayTest::SetProductValues()
{
	for (int first = MinFactor; first <= MaxFactor; first++)
	{
		for (int second = MinFactor; second <= MaxFactor; second++)
		{
			int product = first * second;
			if (Values[product].empty() || 
				(Values[product].find({ first,second }) == Values[product].end() && Values[product].find({ second,first }) == Values[product].end()))
			Values[first * second][{first, second}] = 0;
		}
	}
}	

int TImesPlayTest::GetProduct()
{
	int minUsed = ~(-1 << (sizeof(minUsed) * 8 - 1));
	for_each(Values.begin(), Values.end(), [&](const auto& v) 
		{ 
			for_each(v.second.begin(), v.second.end(), [&](const auto& f)
			{
				if (minUsed > (f.second))
				{
					minUsed = f.second;
				}
			});
		});
	
	std::set<int> numbers;
	for_each(Values.begin(), Values.end(), [&](const auto& v) 
		{
			for_each(v.second.begin(), v.second.end(), [&](const auto& f)
			{
				if (minUsed == (f.second))
				{
					numbers.insert(v.first);
				}
			});
		});

	return *select_random(numbers, rand() % numbers.size());
}

std::pair<int, int> TImesPlayTest::RandomMinUsedFactors(void)
{
	int minUsed = ~(-1 << (sizeof(minUsed) * 8 - 1));
	for_each(Values[CurrentProduct].begin(), Values[CurrentProduct].end(), [&](const auto& v)
		{
			if (minUsed > (v.second))
			{
				minUsed = v.second;
			}
		});
	std::set<std::pair<int, int> > factors;

	for_each(Values[CurrentProduct].begin(), Values[CurrentProduct].end(), [&](const auto& v)
		{
			if (minUsed == (v.second))
			{
				factors.insert(v.first);
			}
		});

	return (*select_random(factors, rand() % factors.size()));
}

std::vector<int> TImesPlayTest::GetNumbers(int& product, int size)
{
	std::vector<int> returnValue;
	srand(time(0));
	CurrentProduct = GetProduct(); 
	product = CurrentProduct;

	returnValue = GetNumbersList(size);

	return returnValue;
}

std::vector<int> TImesPlayTest::Randomize(std::vector<int> v)
{
	for(int i = 0; i <= v.size() / 2; i++)
	{
		int fI = rand() % v.size();
		int sI = rand() % v.size();

		int fval = v[fI];
		v[fI] = v[sI];
		v[sI] = fval;
	}
	return v;
}

std::vector<int> TImesPlayTest::GetNumbersList(int size)
{
	std::vector<int> returnValue;
	std::set<int> avoidlist;
	std::map<int, int> timesUsed; // <number, times used>

	for (auto f : Values[CurrentProduct])
	{
		avoidlist.insert(f.first.first);
		avoidlist.insert(f.first.second);
	}
	CurrentFactors = RandomMinUsedFactors();
	returnValue.push_back(CurrentFactors.first);
	returnValue.push_back(CurrentFactors.second);

	int div = MaxFactor - MinFactor + 1 - avoidlist.size();
	int duplicatesAllowed = size / (div == 0 ? 1 : div) + 1;

	while (returnValue.size() < size)
	{
		int i = rand() % MaxFactor + MinFactor; 
		if (avoidlist.find(i) == avoidlist.end())
		{
			if(timesUsed[i] < duplicatesAllowed)
			{
				returnValue.push_back(i);
				timesUsed[i]++;
			}
		}
	}

	return Randomize(returnValue);
}

bool TImesPlayTest::CheckFactors(int factor1, int factor2)
{
	bool returnValue = false;
	// Do calculation even though the CurrentFactors are saved in case there were multiple correct answers 
	if (factor1 * factor2 == CurrentProduct)
	{
		returnValue = true;

		for (auto f : Values[CurrentProduct])
		{
			if ((f.first.first == factor1 && f.first.second == factor2) || (f.first.first == factor2 && f.first.second == factor1))
			{
				Values[CurrentProduct][f.first]++;
				break;
			}
		}
	}
	else if (!RetryWrongAnswers)
	{
		Values[CurrentProduct][CurrentFactors]++;
	}
	return returnValue;
}

bool TImesPlayTest::AllNumbersUsed(void)
{
	int minUsed = ~(-1 << (sizeof(minUsed) * 8 - 1));
	for_each(Values.begin(), Values.end(), [&](const auto& v)
		{
			for_each(v.second.begin(), v.second.end(), [&](const auto& f)
				{
					if (minUsed > (f.second))
					{
						minUsed = f.second;
					}
				});
		});

	return minUsed > 0;
}
