variable "env" {
  type        = string
  description = "The environment name"
}

variable "cohort" {
  type        = string
  description = "The Cohort id"
}

variable "pod" {
  type        = string
  description = "The Pod id"
}

variable "user" {
  type        = string
  description = "The user id"
}

variable "purp" {
  type        = string
  description = "Purpose of the storage"
}

variable "vers" {
  type        = number
  description = "instance or version"
}

variable "app" {
  type        = string
  description = "application using the storage"
}


# variable "retention_days" {
#   type        = number
#   description = "How long logging data will kept"
# }


variable "location" {
  type        = string
  description = "the location of the resource group"
}
