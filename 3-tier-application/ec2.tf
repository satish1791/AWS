//Create an EC2 instance in each of the subnets, with the appropriate security group and user data.
  
resource "aws_instance" "web_instance" {
  ami = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  subnet_id = aws_subnet.web_subnet.id
  security_groups = [aws_security_group.web_sg.id]
  user_data = <<-EOF
              #!/bin/bash
              echo "Hello, World!" > index.html
              nohup python -m SimpleHTTPServer 80 &
              EOF
}

resource "aws_instance" "app_instance" {
  ami = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  subnet_id = aws_subnet.app_subnet.id
  security_groups = [aws_security_group.app_sg.id]
  user_data = <<-EOF
              #!/bin/bash
              apt-get update
              apt-get install -y apache2
              echo "Hello, World!" > /var/www/html/index
