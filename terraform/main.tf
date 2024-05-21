# Creating s3 bucket
resource "aws_s3_bucket" "assignment_bucket" {
  bucket = "bucket-assign-unique123"
  
  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}

# Creating aws rds instance
resource "aws_db_instance" "assign_rds" {
  allocated_storage    = 20
  identifier              = "mydb"
  engine               = "mysql"
  engine_version       = "8.0"
  instance_class       = "db.t3.micro"
  username             = "admin"
  password             = "password!123"
  parameter_group_name = "default.mysql8.0"
  publicly_accessible = true
  skip_final_snapshot  = true

   tags = {
    Name = "Myrdsdb"
   }
}


resource "aws_ecr_repository" "assignment_ecr" {
  name                 = "assignment_ecr_repo"
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = true
  } 
  tags = {
    env = "dev"
    name = "assignment_ecr_repo"
  }
}