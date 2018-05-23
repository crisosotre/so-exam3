import psutil

class Stats():

  @classmethod
  def porcentaje_cpu(cls):
    porcentaje = psutil.cpu_percent()
    return porcentaje

  @classmethod
  def ram_disponible(cls):
    ram_disponible = psutil.virtual_memory().available
    return ram_disponible

  @classmethod
  def espacio_disco_disponible(cls):
    espacio_disponible = psutil.disk_usage('/').free
    return espacio_disponible
