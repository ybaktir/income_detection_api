terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "3.73.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "ec2" {
  ami = "ami-083602cee93914c0c"
  instance_type = "t2.micro"
  key_name = "clarus"
  security_groups = ["${aws_security_group.allow_http_ssh.name}"]
  tags = {
    "Name" = "created-by-tf"
  }
}

resource "aws_security_group" "allow_http_ssh" {
  name = "allow_http"
  description = "Allow http inbound traffic"

  ingress {
    description = "http"
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]

  }
    ingress {
    description = "ssh"
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]

  }
  tags = {
    Name = "allow_http_ssh"
  }
}
