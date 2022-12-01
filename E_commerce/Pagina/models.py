from django.db import models
from uuid import uuid4

class Administrador(models.Model):
    ad = models.AutoField(db_column='AD', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=30)
    usuario = models.CharField(db_column='Usuario', max_length=30)
    contrasenia = models.CharField(db_column='Contrasenia', max_length=30)

    class Meta:
        verbose_name= 'Administrador'
        verbose_name_plural= 'Administradores'
        db_table = 'Administrador'

    def __str__(self):
        return 'Registro del Administrador %s' % (self.nombre)

class Atencion(models.Model):
    at = models.AutoField(db_column='AT', primary_key=True)  # Field name made lowercase.
    dia = models.CharField(db_column='Dia', max_length=20)  # Field name made lowercase.
    apertura = models.TimeField(db_column='Apertura')  # Field name made lowercase.
    clausura = models.TimeField(db_column='Clausura')  # Field name made lowercase.

    class Meta:
        verbose_name= 'Atencion'
        verbose_name_plural = 'Atenciones'
        db_table = 'Atencion'

    def __str__(self):
        return 'Registro de horario n° %s' % (self.at)


class Comentarios(models.Model):
    co = models.AutoField(db_column='CO', primary_key=True)  # Field name made lowercase.
    comentario = models.CharField(db_column='Comentario', max_length=200)  # Field name made lowercase.
    usuario_ci = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_CI')  # Field name made lowercase.

    class Meta:
        verbose_name= 'Comentario'
        verbose_name_plural = 'Comentarios'
        db_table = 'Comentarios'

    def __str__(self):
        return 'Registro de comentario n° %s' % (self.co)


class Empleado(models.Model):
    ci = models.IntegerField(db_column='CI', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    antiguedad = models.IntegerField(db_column='Antiguedad')  # Field name made lowercase.
    rol = models.CharField(db_column='Rol', max_length=30)  # Field name made lowercase.
    gestion_ge = models.ForeignKey('Gestion', models.DO_NOTHING, db_column='Gestion_GE')  # Field name made lowercase.

    class Meta:
        verbose_name= 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleado'

    def __str__(self):
        return 'Registro del Empleado %s con rol de %s' % (self.nombre,self.rol)


class Encuestas(models.Model):
    en = models.AutoField(db_column='EN', primary_key=True)  # Field name made lowercase.
    calidad = models.IntegerField(db_column='Calidad')  # Field name made lowercase.
    empleados = models.IntegerField(db_column='Empleados')  # Field name made lowercase.
    recervacion = models.IntegerField(db_column='Recervacion')  # Field name made lowercase.
    delivery = models.IntegerField(db_column='Delivery')  # Field name made lowercase.
    comida = models.IntegerField(db_column='Comida')  # Field name made lowercase.
    usuario_ci = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_CI')  # Field name made lowercase.
    gestion_ge = models.ForeignKey('Gestion', models.DO_NOTHING, db_column='Gestion_GE')  # Field name made lowercase.

    class Meta:
        verbose_name= 'Encuesta'
        verbose_name_plural = 'Encuestas'
        db_table = 'Encuestas'

    def __str__(self):
        return 'Registro de la encuesta n° %s' % (self.en)


class Georeferencia(models.Model):
    ge = models.AutoField(db_column='GE', primary_key=True)  # Field name made lowercase.
    ubicacion = models.CharField(db_column='Ubicacion', max_length=50)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono')  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=30)  # Field name made lowercase.
    nit = models.IntegerField(db_column='NIT')  # Field name made lowercase.
    sucursal_su = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='Sucursal_SU')  # Field name made lowercase.

    class Meta:
        verbose_name= 'Georeferencia'
        verbose_name_plural = 'Georeferencias'
        db_table = 'Georeferencia'

    def __str__(self):
        return 'Informacion de la georeferencia de %s' % (self.ubicacion)


class Gestion(models.Model):
    ge = models.AutoField(db_column='GE', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    sucursal_su = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='Sucursal_SU')  # Field name made lowercase.

    class Meta:
        verbose_name= 'Gestion'
        verbose_name_plural = 'Gestiones'
        db_table = 'Gestion'

    def __str__(self):
        return 'Registro de la Gestion n° %s' % (self.ge)


class Ingrediente(models.Model):
    in_field = models.AutoField(db_column='IN', primary_key=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.

    class Meta:
        verbose_name= 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
        db_table = 'Ingrediente'
    
    def __str__(self):
        return '%s' % (self.nombre)


class Ofertas(models.Model):
    of = models.AutoField(db_column='OF', primary_key=True)  # Field name made lowercase.
    inicio = models.DateField(db_column='Inicio')  # Field name made lowercase.
    final = models.DateField(db_column='Final')  # Field name made lowercase.
    descuento = models.DecimalField(db_column='Descuento', max_digits=19, decimal_places=4)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.

    class Meta:
        verbose_name= 'Orferta'
        verbose_name_plural = 'Ofertas'
        db_table = 'Ofertas'

    def __str__(self):
        return 'Oferta de %s' % (self.descripcion)


class Orden(models.Model):
    od = models.AutoField(db_column='OD', primary_key=True)  # Field name made lowercase.
    usuario_ci = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_CI')  # Field name made lowercase.
    empleado_ci = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='Empleado_CI')  # Field name made lowercase.

    class Meta:
        verbose_name= 'Orden'
        verbose_name_plural = 'Ordenes'
        db_table = 'Orden'

    def __str__(self):
        return 'Registro de la orden n° %s' % (self.od)


class OrdenPlatillo(models.Model):
    op = models.AutoField(db_column='OP', primary_key=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.
    orden_od = models.ForeignKey(Orden, models.DO_NOTHING, db_column='Orden_OD')  # Field name made lowercase.
    platillo_pl = models.ForeignKey('Platillo', models.DO_NOTHING, db_column='Platillo_PL')  # Field name made lowercase.

    class Meta:
        verbose_name= 'Orden_Platillo'
        verbose_name_plural = 'Orden_Platillos'
        db_table = 'Orden_Platillo'

    def __str__(self):
        return 'Orden PLatillo n° %s' % (self.op)


class Platillo(models.Model):
    pl = models.AutoField(db_column='PL', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=200)  # Field name made lowercase.
    img = models.BinaryField(db_column='Img',null=True)  # Field name made lowercase.
    empleado_ci = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='Empleado_CI')  # Field name made lowercase.

    class Meta:
        verbose_name= 'Platillo'
        verbose_name_plural = 'Platillos'
        db_table = 'Platillo'

    def __str__(self):
        return '%s' % (self.nombre)


class PlatilloIngrediente(models.Model):
    pi = models.AutoField(db_column='PI', primary_key=True)  # Field name made lowercase.
    ingrediente_in = models.ForeignKey(Ingrediente, models.DO_NOTHING, db_column='Ingrediente_IN')  # Field name made lowercase.
    platillo_pl = models.ForeignKey(Platillo, models.DO_NOTHING, db_column='Platillo_PL')  # Field name made lowercase.
    

    class Meta:
        verbose_name= 'Platillo_Ingrediente'
        verbose_name_plural = 'Platillo_Ingredientes'
        db_table = 'Platillo_Ingrediente'

    def __str__(self):
        return 'Registro de los ingredientes por plato n° %s' % (self.pi)


class PlatilloTipoPlatillo(models.Model):
    ptp = models.AutoField(db_column='PTP', primary_key=True)  # Field name made lowercase.
    platillo_pl = models.ForeignKey(Platillo, models.DO_NOTHING, db_column='Platillo_PL')  # Field name made lowercase.
    tipo_platillo_me = models.ForeignKey('TipoPlatillo', models.DO_NOTHING, db_column='Tipo_Platillo_ME')  # Field name made lowercase.
    

    class Meta:
        verbose_name= 'Platillo_Tipo_Platillo'
        verbose_name_plural = 'Platillo_Tipo_Platillos'
        db_table = 'Platillo_Tipo_Platillo'

    def __str__(self):
        return 'Platillo tipo Platillo n° %s' % (self.ptp)


class Recibo(models.Model):
    re = models.AutoField(db_column='RE', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=4)  # Field name made lowercase.
    georeferencia_ge = models.ForeignKey(Georeferencia, models.DO_NOTHING, db_column='Georeferencia_GE')  # Field name made lowercase.
    ofertas_of = models.ForeignKey(Ofertas, models.DO_NOTHING, db_column='Ofertas_OF',null=True)  # Field name made lowercase.
    orden_od = models.ForeignKey(Orden, models.DO_NOTHING, db_column='Orden_OD')  # Field name made lowercase.
    reservacion_rs = models.ForeignKey('Reservacion', models.DO_NOTHING, db_column='Reservacion_RS',null=True)  # Field name made lowercase.
    

    class Meta:
        verbose_name= 'Recibo'
        verbose_name_plural = 'Recibos'
        db_table = 'Recibo'

    def __str__(self):
        return 'Registro de Recibo n° %s' % (self.re)


class Registro(models.Model):
    rg = models.AutoField(db_column='RG', primary_key=True)  # Field name made lowercase.
    clientes = models.IntegerField(db_column='Clientes')  # Field name made lowercase.
    platillos = models.IntegerField(db_column='Platillos')  # Field name made lowercase.
    pedidos = models.IntegerField(db_column='Pedidos')  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    sucursal_su = models.ForeignKey('Sucursal', models.DO_NOTHING, db_column='Sucursal_SU')  # Field name made lowercase.

    class Meta:
        verbose_name= 'Registro'
        verbose_name_plural = 'Registros'
        db_table = 'Registro'

    def __str__(self):
        return 'Registro n° %s' % (self.rg)


class Reservacion(models.Model):
    rs = models.AutoField(db_column='RS', primary_key=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=19, decimal_places=4)  # Field name made lowercase.
    personas = models.IntegerField(db_column='Personas')  # Field name made lowercase.
    mensaje = models.CharField(db_column='Mensaje', max_length=50)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=30, null=True)  # Field name made lowercase.
    usuario_ci = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='Usuario_CI', null=True)  # Field name made lowercase.

    class Meta:
        verbose_name= 'Reservacion'
        verbose_name_plural = 'Reservaciones'
        db_table = 'Reservacion'

    def __str__(self):
        return 'Registro de la reservacion n° %s' % (self.rs)


class Sucursal(models.Model):
    su = models.AutoField(db_column='SU', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    atencion_at = models.ForeignKey(Atencion, models.DO_NOTHING, db_column='Atencion_AT')  # Field name made lowercase.

    class Meta:
        verbose_name= 'Sucursal'
        verbose_name_plural = 'Sucursales'
        db_table = 'Sucursal'

    def __str__(self):
        return 'Registro de la sucursal %s' % (self.nombre)


class TipoPlatillo(models.Model):
    me = models.AutoField(db_column='ME', primary_key=True)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=30)  # Field name made lowercase.

    class Meta:
        verbose_name= 'Tipo_Platillo'
        verbose_name_plural = 'Tipo_Platillos'
        db_table = 'Tipo_Platillo'
    
    def __str__(self):
        return 'Registro de %s' % (self.categoria)


class Usuario(models.Model):
    ci = models.IntegerField(db_column='CI', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    fecha_nacimiento = models.DateField(db_column='Fecha_Nacimiento')  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=30)  # Field name made lowercase.
    nit = models.IntegerField(db_column='NIT')  # Field name made lowercase.

    class Meta:
        verbose_name= 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'Usuario'

    def __str__(self):
        return 'Registro del Usuario %s' % (self.nombre)

# class Total_Encuesta(models.Model):
#     TE = models.AutoField(db_column='TE', primary_key=True)  # Field name made lowercase.
#     calidad = models.IntegerField(db_column='Calidad')  # Field name made lowercase.
#     empleados = models.IntegerField(db_column='Empleados')  # Field name made lowercase.
#     recervacion = models.IntegerField(db_column='Recervacion')  # Field name made lowercase.
#     delivery = models.IntegerField(db_column='Delivery')  # Field name made lowercase.
#     comida = models.IntegerField(db_column='Comida')  # Field name made lowercase.

#     class Meta:
#         verbose_name= 'Total_Encuesta'
#         verbose_name_plural = 'Total_Encuestas'
#         db_table = 'Total_Encuesta' 
