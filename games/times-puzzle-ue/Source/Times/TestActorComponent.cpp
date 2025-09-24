// Fill out your copyright notice in the Description page of Project Settings.


#include "TestActorComponent.h"

// Sets default values for this component's properties
UTestActorComponent::UTestActorComponent()
{
	// Set this component to be initialized when the game starts, and to be ticked every frame.  You can turn these features
	// off to improve performance if you don't need them.
	PrimaryComponentTick.bCanEverTick = true;

	test = TImesPlayTest(MaxFactor, MinFactor);
	// ...
}


// Called when the game starts
void UTestActorComponent::BeginPlay()
{
	Super::BeginPlay();
	// ...
	
}


// Called every frame
void UTestActorComponent::TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
{
	Super::TickComponent(DeltaTime, TickType, ThisTickFunction);

	// ...
}

TArray<int32> UTestActorComponent::GetNumbers(int& product, int size)
{
	TArray<int32> returnval;
	for (int n : test.GetNumbers(product, size))
	{
		returnval.Add(n);
	}
	return returnval;
}

bool UTestActorComponent::CheckFactors(int factor1, int factor2)
{
	return test.CheckFactors(factor1, factor2);
}

bool UTestActorComponent::AllNumbersUsed()
{
	return test.AllNumbersUsed();
}


