  try:
    mail_compose_wizard = env['mail.compose.message'].with_context(context=ctx).create(wizard_values)
    mail_compose_wizard.onchange_template_id_wrapper()
    mail_compose_wizard.send_mail()
    partner.write({'send_date': True})
  except Exception as e:
    raise Warning(e)