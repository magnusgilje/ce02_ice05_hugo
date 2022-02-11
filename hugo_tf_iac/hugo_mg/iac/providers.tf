terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "2.88.1"
    }

    local = {
      source  = "hashicorp/local"
      version = "2.1.0"
    }

    random = {
      source  = "hashicorp/random"
      version = "3.1.0"
    }
  }
}

provider "azurerm" {
  skip_provider_registration = true
  features {
    key_vault {
      purge_soft_delete_on_destroy = true
    }
  }
}

terraform {
  backend "azurerm" {
  }
}