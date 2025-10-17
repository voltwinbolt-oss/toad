resource "google_service_account" "default" {
  account_id   = "viks-instances-service-account"
  display_name = "GCP instances service account"
  project = "${PROJECT_ID}"

}

resource "google_compute_instance" "default" {
  project = "${PROJECT_ID}"
  name         = "micro-testbox"
  machine_type = "e2-micro"
  zone         = "europe-north1-a"

  tags = ["micro", "testbox"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-13"
      type  = "pd-standard"
      size  = 10
    }
  }

  network_interface {
    network = "default"
  }

  service_account {
    email  = google_service_account.default.email
    scopes = ["cloud-platform"]
  }
}
