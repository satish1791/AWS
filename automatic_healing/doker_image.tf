terraform {
  required_providers {
    docker = {
      source = "kreuzwerker/docker"
    }
  }
}

resource "docker_image" "ubuntu" {
  name = "ubuntu:latest"
}

resource "docker_container" "example" {
  name  = "example"
  image = docker_image.ubuntu.image_id
    ports {
    internal = 80
    external = 8080
  }
  env = ["EXAMPLE_VAR=example-value"]
  command = ["/bin/bash", "-c", "while true; do echo hello; sleep 10; done"]
}
