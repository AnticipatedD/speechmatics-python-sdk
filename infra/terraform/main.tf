# Copyright Advanced Micro Devices, Inc.
#
# SPDX-License-Identifier: MIT

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.0"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# Secure configuration inputs gating operational variables
variable "sovereign_agent_image" {
  type        = string
  description = "The target deployment container image tag for the sovereign voice agent."
  default     = "speechmatics/sovereign-agent:latest"
}

variable "speechmatics_api_key" {
  type        = string
  description = "Mandatory authentication key utilized to bridge connections with the core speech API."
  sensitive   = true
}

# Sovereign Voice Agent container runtime allocation infrastructure
resource "docker_container" "voice_agent" {
  name  = "speechmatics-sovereign-agent"
  image = var.sovereign_agent_image
  
  # Structural resource governance gates
  memory = 4096
  cpu_shares = 2048

  # Bind local configurations securely from validation domains
  env = [
    "SPEECHMATICS_API_KEY=${var.speechmatics_api_key}",
    "LOG_LEVEL=INFO",
    "ENVIRONMENT=production"
  ]

  ports {
    internal = 8080
    external = 8080
    protocol = "tcp"
  }

  # Security enforcement profile layers
  read_only = false
  privileged = false
  
  security_opts = [
    "no-new-privileges:true"
  ]
}

output "container_id" {
  value       = docker_container.voice_agent.id
  description = "The unique identification hash of the instantiated container infrastructure."
}
