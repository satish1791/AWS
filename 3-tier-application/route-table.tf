// Define a route table for the public subnet and add a route to the internet gateway

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.main_vpc.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main_igw.id
  }
  tags = {
    Name = "public_rt"
  }
}

resource "aws_route_table_association" "web_rta" {
  subnet_id = aws_subnet.web_subnet.id
  route_table_id = aws_route_table.public_rt.id
}

