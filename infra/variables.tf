variable "yc_instance_user" {
  type = string  
}

variable "yc_instance_name" {
  type = string  
}

variable "yc_network_name" {
  type = string
}

variable "yc_subnet_name" {
  type = string
}

variable "yc_service_account_name" {
  type    = string
}

variable "yc_bucket_name" {
  type = string
}

variable "yc_storage_endpoint_url" {
  type = string
  default = "https://storage.yandexcloud.net"
}

variable "public_key_path" {
  type = string
}

variable "private_key_path" {
  type = string
}

variable "admin_password" {
  type = string
  description = "Admin password for the Airflow web interface"
}

variable "yc_config" {
  type = object({
    zone      = string
    folder_id = string
    token     = string
    cloud_id  = string
  })
  description = "Yandex Cloud configuration"
}
