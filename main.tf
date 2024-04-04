provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "example" {
  bucket = "teste-github-actions-tf"
  acl    = "private"
}