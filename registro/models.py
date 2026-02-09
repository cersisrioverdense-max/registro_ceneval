# registro/models.py
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL
class RegistroCeneval(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    seccion_actual = models.PositiveSmallIntegerField(default=1)
    completo = models.BooleanField(default=False)

    def __str__(self):
        return f"Registro {self.usuario.username}"

class DatosPersonales(models.Model):
    registro = models.OneToOneField(RegistroCeneval, on_delete=models.CASCADE)

    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=100)

    fecha_nacimiento = models.DateField()

    SEXO_CHOICES = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    lugar_nacimiento = models.CharField(max_length=100)

    curp = models.CharField(max_length=18)

    ESTADO_CIVIL_CHOICES = [
        ('S', 'Soltero(a)'),
        ('C', 'Casado(a)'),
        ('U', 'Unión libre'),
    ]
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL_CHOICES)

    # Domicilio
    calle = models.CharField(max_length=100)
    numero_exterior = models.CharField(max_length=10)
    numero_interior = models.CharField(max_length=10, blank=True)

    entidad_federativa = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100, blank=True)
    codigo_postal = models.CharField(max_length=5)

    telefono_personal = models.CharField(max_length=15)
    correo_electronico = models.EmailField()

    def __str__(self):
        return f"Datos personales - {self.registro.usuario.username}"

class Bloque2Trayectoria(models.Model):

    # ================= CATÁLOGOS =================
    TIPO_INSTITUCION = [
        ('publica', 'Pública'),
        ('privada', 'Privada'),
    ]

    REGIMEN = [
        ('federal', 'Federal'),
        ('estatal', 'Estatal'),
        ('autonoma', 'Autónoma'),
        ('particular', 'Particular'),
    ]

    BACHILLERATO = [
        ('general', 'General'),
        ('tecnologico', 'Tecnológico'),
        ('tecnico', 'Técnico profesional'),
    ]

    TURNO = [
        ('matutino', 'Matutino'),
        ('vespertino', 'Vespertino'),
        ('mixto', 'Mixto'),
    ]

    PROMEDIO = [
        ('6-7', '6 a 7'),
        ('7-8', '7 a 8'),
        ('8-9', '8 a 9'),
        ('9-10', '9 a 10'),
    ]

    NIVEL_ESTUDIOS = [
        ('tecnico', 'Técnico'),
        ('licenciatura', 'Licenciatura'),
        ('maestria', 'Maestría'),
        ('doctorado', 'Doctorado'),
    ]

    IMPORTANCIA = [
        ('muy', 'Muy importante'),
        ('media', 'Importante'),
        ('poca', 'Poco importante'),
    ]

    FRECUENCIA = [
        ('siempre', 'Siempre'),
        ('casi_siempre', 'Casi siempre'),
        ('a_veces', 'Algunas veces'),
        ('nunca', 'Nunca'),
    ]

    SI_NO = [
        (True, 'Sí'),
        (False, 'No'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # ============ CONTEXTO ACADÉMICO ============
    tipo_institucion = models.CharField(max_length=10, choices=TIPO_INSTITUCION)
    regimen = models.CharField(max_length=15, choices=REGIMEN)
    bachillerato = models.CharField(max_length=15, choices=BACHILLERATO)
    area = models.CharField(max_length=100)
    turno = models.CharField(max_length=10, choices=TURNO)
    promedio = models.CharField(max_length=5, choices=PROMEDIO)

    beca = models.BooleanField(
    choices=SI_NO,
    null=True,
    blank=True
)
    motivo_beca = models.CharField(max_length=100, blank=True)

    # ============ MOTIVACIÓN ============
    nivel_estudios = models.CharField(max_length=15, choices=NIVEL_ESTUDIOS)
    importancia_estudiar = models.CharField(max_length=10, choices=IMPORTANCIA)

    motivo_continuar = models.CharField(max_length=150)
    apoyo_familiar = models.BooleanField(
        choices=SI_NO,
        null=True,
        blank=True
    )

    primera_generacion = models.BooleanField(
        choices=SI_NO,
        null=True,
        blank=True
    )

    # ============ HÁBITOS DE ESTUDIO ============
    planeacion = models.CharField(max_length=15, choices=FRECUENCIA)
    organizacion_material = models.CharField(max_length=15, choices=FRECUENCIA)
    estudio_independiente = models.CharField(max_length=15, choices=FRECUENCIA)
    repaso = models.CharField(max_length=15, choices=FRECUENCIA)
    investigacion = models.CharField(max_length=15, choices=FRECUENCIA)

    # ============ TRABAJO EN EQUIPO ============
    colaboracion = models.CharField(max_length=15, choices=FRECUENCIA)
    comparte_info = models.CharField(max_length=15, choices=FRECUENCIA)
    escucha = models.CharField(max_length=15, choices=FRECUENCIA)
    ayuda = models.CharField(max_length=15, choices=FRECUENCIA)
    propone = models.CharField(max_length=15, choices=FRECUENCIA)
    conflictos = models.CharField(max_length=15, choices=FRECUENCIA)

    # ============ RESPONSABILIDAD ============
    cumple = models.CharField(max_length=15, choices=FRECUENCIA)
    entrega_tiempo = models.CharField(max_length=15, choices=FRECUENCIA)
    asiste_clases = models.CharField(max_length=15, choices=FRECUENCIA)
    perseverancia = models.CharField(max_length=15, choices=FRECUENCIA)

    # ============ CONDICIONES ============
    espacio_estudio = models.BooleanField(
    choices=SI_NO,
    null=True,
    blank=True
    )

    acceso_tecnologia = models.BooleanField(
        choices=SI_NO,
        null=True,
        blank=True
    )

    dificultades_economicas = models.BooleanField(
        choices=SI_NO,
        null=True,
        blank=True
    )

    dificultades_academicas = models.BooleanField(
        choices=SI_NO,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Bloque 2 - {self.usuario}"

class Bloque3CaracteristicasEscuela(models.Model):

    ACUERDO = [
        ('totalmente_acuerdo', 'Totalmente de acuerdo'),
        ('de_acuerdo', 'De acuerdo'),
        ('ni', 'Ni de acuerdo ni en desacuerdo'),
        ('en_desacuerdo', 'En desacuerdo'),
        ('totalmente_desacuerdo', 'Totalmente en desacuerdo'),
    ]

    FRECUENCIA = [
        ('siempre', 'Siempre'),
        ('casi_siempre', 'Casi siempre'),
        ('a_veces', 'Algunas veces'),
        ('nunca', 'Nunca'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # ====== CLIMA ESCOLAR ======
    pertenencia = models.CharField(max_length=25, choices=ACUERDO)
    integracion = models.CharField(max_length=25, choices=ACUERDO)
    aceptacion = models.CharField(max_length=25, choices=ACUERDO)
    valores_compartidos = models.CharField(max_length=25, choices=ACUERDO)
    apoyo_escolar = models.CharField(max_length=25, choices=ACUERDO)

    # ====== PRÁCTICAS DOCENTES (CLIMA) ======
    respeto_docente = models.CharField(max_length=15, choices=FRECUENCIA)
    trato_justo = models.CharField(max_length=15, choices=FRECUENCIA)

    # ====== PRÁCTICAS DOCENTES (ENSEÑANZA) ======
    explicacion_clara = models.CharField(max_length=15, choices=FRECUENCIA)
    preparacion_docente = models.CharField(max_length=15, choices=FRECUENCIA)
    dominio_tema = models.CharField(max_length=15, choices=FRECUENCIA)
    resolucion_dudas = models.CharField(max_length=15, choices=FRECUENCIA)

    # ====== APOYO AL APRENDIZAJE ======
    retroalimentacion = models.CharField(max_length=15, choices=FRECUENCIA)
    motivacion_docente = models.CharField(max_length=15, choices=FRECUENCIA)
    seguimiento_academico = models.CharField(max_length=15, choices=FRECUENCIA)

    def __str__(self):
        return f"Bloque 3 - {self.usuario}"
    
    from django.db import models
from django.contrib.auth.models import User

class Bloque4EntornoSocial(models.Model):

    OPCIONES_HORAS = [
        ('0', 'No trabajo'),
        ('1_10', 'De 1 a 10 horas'),
        ('11_20', 'De 11 a 20 horas'),
        ('21_30', 'De 21 a 30 horas'),
        ('31_40', 'De 31 a 40 horas'),
        ('mas_40', 'Más de 40 horas'),
    ]

    NIVEL_ESTUDIOS = [
        ('ninguno', 'Sin estudios'),
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria'),
        ('bachillerato', 'Bachillerato'),
        ('licenciatura', 'Licenciatura'),
        ('posgrado', 'Posgrado'),
    ]

    CANTIDAD = [
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4_mas', '4 o más'),
    ]

    SI_NO = [
        (True, 'Sí'),
        (False, 'No'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    # ====== Trabajo ======
    horas_trabajo = models.CharField(
        max_length=10,
        choices=OPCIONES_HORAS
    )

    # ====== Escolaridad familiar ======
    estudios_jefe_hogar = models.CharField(
        max_length=20,
        choices=NIVEL_ESTUDIOS
    )
    estudios_madre = models.CharField(
        max_length=20,
        choices=NIVEL_ESTUDIOS
    )
    estudios_padre = models.CharField(
        max_length=20,
        choices=NIVEL_ESTUDIOS
    )

    # ====== Hogar ======
    libros_en_casa = models.CharField(
        max_length=10,
        choices=CANTIDAD
    )

    nivel_educativo_esperado = models.CharField(
        max_length=20,
        choices=NIVEL_ESTUDIOS
    )

    personas_trabajando = models.CharField(
        max_length=10,
        choices=CANTIDAD
    )

    # ====== Bienes y servicios ======
    computadora = models.BooleanField(
    choices=SI_NO,
    null=True,
    blank=True
    )

    televisor = models.BooleanField(
        choices=SI_NO,
        null=True,
        blank=True
    )

    automovil = models.BooleanField(
        choices=SI_NO,
        null=True,
        blank=True
    )

    banos_completos = models.CharField(
        max_length=10,
        choices=CANTIDAD,
        null=True,
        blank=True
    )

    celular_inteligente = models.BooleanField(
        choices=SI_NO,
        null=True,
        blank=True
    )

    internet = models.BooleanField(
        choices=SI_NO,
        null=True,
        blank=True
    )

    cuartos_dormir = models.CharField(
        max_length=10,
        choices=CANTIDAD,
        null=True,
        blank=True
    )

