locals {
  tags = {
    project     = var.project
    environment = var.environment
    datetime    = timestamp()
  }

  apps = {
    service = {
      name              = "vul-bot"
      docker_image_name = "vul-bot/vul-bot:${var.image_tag}"

      app_vars = {
        OPENAI_API_KEY      = var.OPENAI_API_KEY
        OPENAI_API_TYPE     = "azure"
        AZURE_DEPLOYMENT_ID = "default"
        OPENAI_API_HOST     = var.OPENAI_API_KEY
        OPENAI_API_VERSION  = "2023-03-15-preview"
        WEBSITES_PORT       = "8000"
      }
    }
  }
}

resource "azurerm_resource_group" "rg" {
  name     = format("rg-%s-%s-%s", var.project, var.environment, var.location)
  location = var.location
}

module "app_service" {
  source              = "../../modules/app_services"
  environment         = var.environment
  project             = "vul-bot"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku_name            = "B1"
  os_type             = "Linux"
  apps                = local.apps
  registry_name       = "https://ghcr.io"
  allowed_inbound_ips = var.allowed_inbound_ips

  tags = local.tags
}