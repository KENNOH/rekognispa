terraform {
  required_version = ">= 1.0.0"

  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

provider "digitalocean" {
  token = ""
}

resource "digitalocean_droplet" "rekognispa-server" {
  image     = "ubuntu-18-04-x64"
  name      = "rekognispa-server"
  region    = "nyc1"
  size      = "s-1vcpu-1gb"
  user_data = file("terramino_app.yaml")
  ssh_keys = []
}
