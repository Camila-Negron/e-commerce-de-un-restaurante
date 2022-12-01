# Generated by Django 3.0.6 on 2022-12-01 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('ad', models.AutoField(db_column='AD', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=30)),
                ('usuario', models.CharField(db_column='Usuario', max_length=30)),
                ('contrasenia', models.CharField(db_column='Contrasenia', max_length=30)),
            ],
            options={
                'verbose_name': 'Administrador',
                'verbose_name_plural': 'Administradores',
                'db_table': 'Administrador',
            },
        ),
        migrations.CreateModel(
            name='Atencion',
            fields=[
                ('at', models.AutoField(db_column='AT', primary_key=True, serialize=False)),
                ('dia', models.CharField(db_column='Dia', max_length=20)),
                ('apertura', models.TimeField(db_column='Apertura')),
                ('clausura', models.TimeField(db_column='Clausura')),
            ],
            options={
                'verbose_name': 'Atencion',
                'verbose_name_plural': 'Atenciones',
                'db_table': 'Atencion',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('ci', models.IntegerField(db_column='CI', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=30)),
                ('antiguedad', models.IntegerField(db_column='Antiguedad')),
                ('rol', models.CharField(db_column='Rol', max_length=30)),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'Empleado',
            },
        ),
        migrations.CreateModel(
            name='Georeferencia',
            fields=[
                ('ge', models.AutoField(db_column='GE', primary_key=True, serialize=False)),
                ('ubicacion', models.CharField(db_column='Ubicacion', max_length=50)),
                ('telefono', models.IntegerField(db_column='Telefono')),
                ('correo', models.CharField(db_column='Correo', max_length=30)),
                ('nit', models.IntegerField(db_column='NIT')),
            ],
            options={
                'verbose_name': 'Georeferencia',
                'verbose_name_plural': 'Georeferencias',
                'db_table': 'Georeferencia',
            },
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('in_field', models.AutoField(db_column='IN', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=30)),
            ],
            options={
                'verbose_name': 'Ingrediente',
                'verbose_name_plural': 'Ingredientes',
                'db_table': 'Ingrediente',
            },
        ),
        migrations.CreateModel(
            name='Ofertas',
            fields=[
                ('of', models.AutoField(db_column='OF', primary_key=True, serialize=False)),
                ('inicio', models.DateField(db_column='Inicio')),
                ('final', models.DateField(db_column='Final')),
                ('descuento', models.DecimalField(db_column='Descuento', decimal_places=4, max_digits=19)),
                ('descripcion', models.CharField(db_column='Descripcion', max_length=50)),
            ],
            options={
                'verbose_name': 'Orferta',
                'verbose_name_plural': 'Ofertas',
                'db_table': 'Ofertas',
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('od', models.AutoField(db_column='OD', primary_key=True, serialize=False)),
                ('empleado_ci', models.ForeignKey(db_column='Empleado_CI', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Empleado')),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
                'db_table': 'Orden',
            },
        ),
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('pl', models.AutoField(db_column='PL', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=50)),
                ('descripcion', models.CharField(db_column='Descripcion', max_length=200)),
                ('img', models.BinaryField(db_column='Img', null=True)),
                ('empleado_ci', models.ForeignKey(db_column='Empleado_CI', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Empleado')),
            ],
            options={
                'verbose_name': 'Platillo',
                'verbose_name_plural': 'Platillos',
                'db_table': 'Platillo',
            },
        ),
        migrations.CreateModel(
            name='TipoPlatillo',
            fields=[
                ('me', models.AutoField(db_column='ME', primary_key=True, serialize=False)),
                ('categoria', models.CharField(db_column='Categoria', max_length=30)),
            ],
            options={
                'verbose_name': 'Tipo_Platillo',
                'verbose_name_plural': 'Tipo_Platillos',
                'db_table': 'Tipo_Platillo',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('ci', models.IntegerField(db_column='CI', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=30)),
                ('fecha_nacimiento', models.DateField(db_column='Fecha_Nacimiento')),
                ('correo', models.CharField(db_column='Correo', max_length=30)),
                ('nit', models.IntegerField(db_column='NIT')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuario',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('su', models.AutoField(db_column='SU', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=30)),
                ('atencion_at', models.ForeignKey(db_column='Atencion_AT', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Atencion')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
                'db_table': 'Sucursal',
            },
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('rs', models.AutoField(db_column='RS', primary_key=True, serialize=False)),
                ('fecha', models.DateField(db_column='Fecha')),
                ('costo', models.DecimalField(db_column='Costo', decimal_places=4, max_digits=19)),
                ('personas', models.IntegerField(db_column='Personas')),
                ('mensaje', models.CharField(db_column='Mensaje', max_length=50)),
                ('nombre', models.CharField(db_column='Nombre', max_length=30, null=True)),
                ('correo', models.CharField(db_column='Correo', max_length=30, null=True)),
                ('usuario_ci', models.ForeignKey(db_column='Usuario_CI', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Usuario')),
            ],
            options={
                'verbose_name': 'Reservacion',
                'verbose_name_plural': 'Reservaciones',
                'db_table': 'Reservacion',
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('rg', models.AutoField(db_column='RG', primary_key=True, serialize=False)),
                ('clientes', models.IntegerField(db_column='Clientes')),
                ('platillos', models.IntegerField(db_column='Platillos')),
                ('pedidos', models.IntegerField(db_column='Pedidos')),
                ('fecha', models.DateField(db_column='Fecha')),
                ('sucursal_su', models.ForeignKey(db_column='Sucursal_SU', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Sucursal')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
                'db_table': 'Registro',
            },
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('re', models.AutoField(db_column='RE', primary_key=True, serialize=False)),
                ('fecha', models.DateField(db_column='Fecha')),
                ('total', models.DecimalField(db_column='Total', decimal_places=4, max_digits=19)),
                ('georeferencia_ge', models.ForeignKey(db_column='Georeferencia_GE', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Georeferencia')),
                ('ofertas_of', models.ForeignKey(db_column='Ofertas_OF', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Ofertas')),
                ('orden_od', models.ForeignKey(db_column='Orden_OD', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Orden')),
                ('reservacion_rs', models.ForeignKey(db_column='Reservacion_RS', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Reservacion')),
            ],
            options={
                'verbose_name': 'Recibo',
                'verbose_name_plural': 'Recibos',
                'db_table': 'Recibo',
            },
        ),
        migrations.CreateModel(
            name='PlatilloTipoPlatillo',
            fields=[
                ('ptp', models.AutoField(db_column='PTP', primary_key=True, serialize=False)),
                ('platillo_pl', models.ForeignKey(db_column='Platillo_PL', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Platillo')),
                ('tipo_platillo_me', models.ForeignKey(db_column='Tipo_Platillo_ME', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.TipoPlatillo')),
            ],
            options={
                'verbose_name': 'Platillo_Tipo_Platillo',
                'verbose_name_plural': 'Platillo_Tipo_Platillos',
                'db_table': 'Platillo_Tipo_Platillo',
            },
        ),
        migrations.CreateModel(
            name='PlatilloIngrediente',
            fields=[
                ('pi', models.AutoField(db_column='PI', primary_key=True, serialize=False)),
                ('ingrediente_in', models.ForeignKey(db_column='Ingrediente_IN', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Ingrediente')),
                ('platillo_pl', models.ForeignKey(db_column='Platillo_PL', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Platillo')),
            ],
            options={
                'verbose_name': 'Platillo_Ingrediente',
                'verbose_name_plural': 'Platillo_Ingredientes',
                'db_table': 'Platillo_Ingrediente',
            },
        ),
        migrations.CreateModel(
            name='OrdenPlatillo',
            fields=[
                ('op', models.AutoField(db_column='OP', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(db_column='Cantidad')),
                ('orden_od', models.ForeignKey(db_column='Orden_OD', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Orden')),
                ('platillo_pl', models.ForeignKey(db_column='Platillo_PL', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Platillo')),
            ],
            options={
                'verbose_name': 'Orden_Platillo',
                'verbose_name_plural': 'Orden_Platillos',
                'db_table': 'Orden_Platillo',
            },
        ),
        migrations.AddField(
            model_name='orden',
            name='usuario_ci',
            field=models.ForeignKey(db_column='Usuario_CI', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Usuario'),
        ),
        migrations.CreateModel(
            name='Gestion',
            fields=[
                ('ge', models.AutoField(db_column='GE', primary_key=True, serialize=False)),
                ('fecha', models.DateField(db_column='Fecha')),
                ('sucursal_su', models.ForeignKey(db_column='Sucursal_SU', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Sucursal')),
            ],
            options={
                'verbose_name': 'Gestion',
                'verbose_name_plural': 'Gestiones',
                'db_table': 'Gestion',
            },
        ),
        migrations.AddField(
            model_name='georeferencia',
            name='sucursal_su',
            field=models.ForeignKey(db_column='Sucursal_SU', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Sucursal'),
        ),
        migrations.CreateModel(
            name='Encuestas',
            fields=[
                ('en', models.AutoField(db_column='EN', primary_key=True, serialize=False)),
                ('calidad', models.IntegerField(db_column='Calidad')),
                ('empleados', models.IntegerField(db_column='Empleados')),
                ('recervacion', models.IntegerField(db_column='Recervacion')),
                ('delivery', models.IntegerField(db_column='Delivery')),
                ('comida', models.IntegerField(db_column='Comida')),
                ('gestion_ge', models.ForeignKey(db_column='Gestion_GE', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Gestion')),
                ('usuario_ci', models.ForeignKey(db_column='Usuario_CI', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Usuario')),
            ],
            options={
                'verbose_name': 'Encuesta',
                'verbose_name_plural': 'Encuestas',
                'db_table': 'Encuestas',
            },
        ),
        migrations.AddField(
            model_name='empleado',
            name='gestion_ge',
            field=models.ForeignKey(db_column='Gestion_GE', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Gestion'),
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('co', models.AutoField(db_column='CO', primary_key=True, serialize=False)),
                ('comentario', models.CharField(db_column='Comentario', max_length=200)),
                ('usuario_ci', models.ForeignKey(db_column='Usuario_CI', on_delete=django.db.models.deletion.DO_NOTHING, to='Pagina.Usuario')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'db_table': 'Comentarios',
            },
        ),
    ]