// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Components/ActorComponent.h"
#include "TImesPlayTest.h"
#include "TestActorComponent.generated.h"

UCLASS( ClassGroup=(Custom), meta=(BlueprintSpawnableComponent) )
class TIMES_API UTestActorComponent : public UActorComponent
{
	GENERATED_BODY()

public:	
	// Sets default values for this component's properties
	UTestActorComponent();

protected:
	// Called when the game starts
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;

	UFUNCTION(BlueprintCallable)
	TArray<int32> GetNumbers(int& product, int size);

	UFUNCTION(BlueprintCallable)
	bool CheckFactors(int factor1, int factor2);

	UFUNCTION(BlueprintCallable)
	bool AllNumbersUsed();

	UPROPERTY(EditAnywhere)
	int32 MinFactor = 1;

	UPROPERTY(EditAnywhere)
	int32 MaxFactor = 10;

	UPROPERTY(EditAnywhere)
	bool RetryWrongAnswers = true;
private:
	TImesPlayTest test;
};
