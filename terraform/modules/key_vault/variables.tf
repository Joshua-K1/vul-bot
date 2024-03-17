variable "environment" {
 type        = string 
 description = "The environment context"
}

variable "project" {
 type        = string
 description = "The project name"
}

variable "location" {
 type        = string
 description = "The location of the key vault"
}

variable "resource_group_name" {
 type        = string
 description = "The name of the resource group"
}

variable "tenant_id" {
 type        = string
 description = "Azure tenant id"
}

variable "soft_delete_retention" {
 type = number
 description = "days to retain soft deleted objects"
}

variable "purge_protection_enabled" {
 type        = bool
 description = "Purge protection enabled / disabled"
}

variable "sp_id" {
 type        = string
 description = "Object ID of the Service Principle"
}

variable "sku_name" {
 type        = string
 description = "The Sky of the Key Vault"
}

variable "tags" {
 type        = map(string)
 description = "Tags that should be applied to resources created by this module. Runtime tag values will take precedent over compile time values"
 default     = {}
}
