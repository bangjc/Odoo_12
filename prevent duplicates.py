# add this code on server action
if record.field:
   existing_field= env['your_model'].search([('id','!=',record.id),('field','=',record.field)])
   if existing_field:
     raise Warning("your message")
