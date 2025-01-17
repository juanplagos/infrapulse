package scripts

import (
	"context"
	"fmt"
	"log"

	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/ec2"
)

func ListEC2Instances() {
	cfg, err := config.LoadDefaultConfig(context.TODO())
	if err != nil {
		fmt.Println("Error: ", err)
	} else {
		fmt.Println("Success: ", cfg)
	}

	ec2Client := ec2.NewFromConfig(cfg)

	result, err := ec2Client.DescribeInstances(context.TODO(), &ec2.DescribeInstancesInput{})
	if err != nil {
		log.Fatalf("Unable to describe instances, %v", err)
	}

	for _, reservation := range result.Reservations {
		for _, instance := range reservation.Instances {
			fmt.Println("ID: ", *instance.InstanceId)
			fmt.Println("Instance Type: ", instance.InstanceType)
			fmt.Println("State: ", instance.State.Name)
			fmt.Println("Public IP Address: ", instance.PublicIpAddress)
		}
	}
}
