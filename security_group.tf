terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region to create resources in"
  type        = string
  default     = "us-east-1"
}

resource "aws_security_group" "example" {
  name        = "allow-22027"
  description = "Security group allowing TCP port 22027"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 22027
    to_port     = 22027
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow TCP port 22027"
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    description = "Allow all outbound"
  }

  tags = {
    Name = "allow-22027"
  }
}

variable "vpc_id" {
  description = "The VPC ID where the security group will be created"
  type        = string
}
