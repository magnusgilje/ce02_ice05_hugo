locals {
  default_tags = tomap({
    "cohort" = var.cohort,
    "pod"    = var.pod,
    "user"   = var.user,
    "env"    = var.env
    }
  )
  target_rg1          = format("rg%s%s%s%straining%03d", var.user, var.env, var.app, var.cohort, var.vers)
  analytics_workspace = format("la%shub", var.cohort)
  analytics_rg        = format("rg-%s-hub", var.cohort)
}

resource "azurerm_resource_group" "deploy" {

  name = local.target_rg1

  location = var.location

  tags = local.default_tags
}

module "iceburg_site" {
  source              = "git::https://kubrick-training@dev.azure.com/kubrick-training/ce02/_git/iceburg_tf_hugo_site?ref=pipeline"
  tags                = local.default_tags
  target_rg           = local.target_rg1
  user                = format("%sice", var.user)
  env                 = var.env
  app                 = var.app
  vers                = var.vers
  user_write_access   = var.env == "dev" ? true : false
  analytics_workspace = local.analytics_workspace
  analytics_rg        = local.analytics_rg

  depends_on = [azurerm_resource_group.deploy]
}