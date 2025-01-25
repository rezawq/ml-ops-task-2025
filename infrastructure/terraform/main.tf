resource "yandex_storage_bucket" "test" {
  bucket = "tf-test-bucket"
  folder_id = var.yc_folder_id
}