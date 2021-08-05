package main

import (
	"fmt"
	"github.com/alyu/configparser"
	"log"
	"os/exec"
	"time"
)

func readOktaConfig() {
	configparser.Delimiter = "="
	config, err := configparser.Read("~/.okta_aws_login_config")
	if err != nil {
		log.Fatal(err)
		return
	}

	s, err := config.AllSections()
	if err != nil {
		log.Fatal(err)
		return
	}

	for _, v := range s {
		time.Sleep(time.Second) // Little Delay is Required to
		go callGimme(v.Name())
	}
}

func callGimme(profile string) {

	gimme := "gimme-aws-creds"
	arg0 := "-p"

	cmd := exec.Command(gimme, arg0, profile)
	stdout, err := cmd.Output()

	if err != nil {
		fmt.Println(err.Error())
		return
	}

	// Print the output
	fmt.Println(string(stdout))
}

func main() {
	fmt.Println("Quick AWS Gimme Setup")

	var input string
	readOktaConfig()
	fmt.Println("Press Enter to quit the Process")
	fmt.Scanln(&input)
}
