output "ice_url" {
  value       = module.iceburg_site.endpoint
  description = "The generated target URL"
}

output "ice_storage_account_made" {
  value       = module.iceburg_site.name
  description = "The generated storage account name"
}

output "resource_group" {
  value       = azurerm_resource_group.deploy.name
  description = "The resource group"
}
