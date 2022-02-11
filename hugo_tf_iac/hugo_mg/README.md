## Build Badge

[![Build Status](https://dev.azure.com/kubrick-training/ce02/_apis/build/status/hugo_mg?branchName=azure-pipelines)](https://dev.azure.com/kubrick-training/ce02/_build/latest?definitionId=468&branchName=azure-pipelines)

## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_azurerm"></a> [azurerm](#requirement\_azurerm) | 2.88.1 |
| <a name="requirement_local"></a> [local](#requirement\_local) | 2.1.0 |
| <a name="requirement_random"></a> [random](#requirement\_random) | 3.1.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_azurerm"></a> [azurerm](#provider\_azurerm) | 2.88.1 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_iceburg_site"></a> [iceburg\_site](#module\_iceburg\_site) | git::https://kubrick-training@dev.azure.com/kubrick-training/ce02/_git/iceburg_tf_hugo_site | pipeline |

## Resources

| Name | Type |
|------|------|
| [azurerm_resource_group.deploy](https://registry.terraform.io/providers/hashicorp/azurerm/2.88.1/docs/resources/resource_group) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_app"></a> [app](#input\_app) | application using the storage | `string` | n/a | yes |
| <a name="input_cohort"></a> [cohort](#input\_cohort) | The Cohort id | `string` | n/a | yes |
| <a name="input_env"></a> [env](#input\_env) | The environment name | `string` | n/a | yes |
| <a name="input_location"></a> [location](#input\_location) | the location of the resource group | `string` | n/a | yes |
| <a name="input_pod"></a> [pod](#input\_pod) | The Pod id | `string` | n/a | yes |
| <a name="input_purp"></a> [purp](#input\_purp) | Purpose of the storage | `string` | n/a | yes |
| <a name="input_user"></a> [user](#input\_user) | The user id | `string` | n/a | yes |
| <a name="input_vers"></a> [vers](#input\_vers) | instance or version | `number` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_ice_storage_account_made"></a> [ice\_storage\_account\_made](#output\_ice\_storage\_account\_made) | The generated storage account name |
| <a name="output_ice_url"></a> [ice\_url](#output\_ice\_url) | The generated target URL |
| <a name="output_resource_group"></a> [resource\_group](#output\_resource\_group) | The resource group |