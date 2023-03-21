 // create three subnets for each tier: web, app, and db. Define the CIDR block for each subnet and associate them with the VPC
   
   resource "aws_subnet" "web_subnet" {
  cidr_block = "10.0.1.0/24"
  vpc_id = aws_vpc.main_vpc.id
  availability_zone = "us-west-2a"
  tags = {
    Name = "web_subnet"
  }
}

resource "aws_subnet" "app_subnet" {
  cidr_block = "10.0.2.0/24"
  vpc_id = aws_vpc.main_vpc.id
  availability_zone = "us-west-2b"
  tags = {
    Name = "app_subnet"
  }
}

resource "aws_subnet" "db_subnet" {
  cidr_block = "10.0.3.0/24"
  vpc_id = aws_vpc.main_vpc.id
  availability_zone = "us-west-2c"
  tags = {
    Name = "db_subnet"
  }
}
