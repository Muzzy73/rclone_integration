// Copyright (c) 2020, 9T9IT and contributors
// For license information, please see license.txt

frappe.ui.form.on("Rclone Integration Settings", {
  refresh: function (frm) {
    _add_sync_backup(frm);
  },
  get_config: async function (frm) {
    const { message: config } = await frappe.call({
      method: "rclone_integration.api.rclone_integration_settings.get_config",
      args: { path: frm.doc.config_path },
    });
    frm.doc.remotes = [];
    config.forEach(function (remote) {
      const remote_child = frm.add_child("remotes");
      remote_child.remote_name = remote;
    });
    frm.refresh_fields("remotes");
  },
});

function _add_sync_backup(frm) {
  if (!frm.doc.remotes) return;
  frm.add_custom_button(__("Sync Backup"), function () {
    frappe.call({
      method: "rclone_integration.api.rclone_integration_settings.sync_backup",
    });
  });
}
