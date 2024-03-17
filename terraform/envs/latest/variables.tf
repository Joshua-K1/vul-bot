variable "location" {
  type    = string
  default = "uksouth"
}

variable "project" {
  type    = string
  default = "vul-bot"
}

variable "environment" {
  type    = string
  default = "latest"
}

variable "image_tag" {
  type    = string
  default = "main"
}

variable "OPENAI_API_KEY" {
  type        = string
  description = "The Azure OpenAI API key to use for the service"
  sensitive   = true
}

variable "openai_api_url" {
  type        = string
  description = "The Azure OpenAI API URL to use for the service"
  sensitive   = true
}

variable "system_api_key" {
  type        = string
  description = "The Azure System API key to use for the service"
  sensitive   = true
}

variable "azure_vault_id" {
  type        = string
  description = "The Azure Key Vault ID to use for the service"
  sensitive   = true
}

variable "allowed_inbound_ips" {
  type      = list(string)
  default   = [""]
  sensitive = true
}