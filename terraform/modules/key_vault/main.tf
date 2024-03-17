resource "azurerm_key_vault" "keyvault" { 
 name                       = format("vault-%s-%s-%s-001", var.environment, var.project, var.location)
 location                   = var.location
 resource_group_name        = var.resource_group_name
 tenant_id                  = var.tenant_id
 soft_delete_retention_days = var.soft_delete_retention
 purge_protection_enabled   = var.purge_protection_enabled
 tags                       = var.tags

 sku_name = var.sku_name
}

resource "azurerm_key_vault_access_policy" "keyvaultap" {
 key_vault_id = azurerm_key_vault.keyvault.id
 tenant_id    = var.tenant_id
 object_id    = var.sp_id

 key_permissions = ["Get"    , "List", 
		    "Delete" , "Create", 
                    "Import" , "Backup", 
		    "Restore", "Recover"]

 secret_permissions = ["Get"    , "List",
		       "Delete" , "Backup",
		       "Restore", "Recover"]
}
