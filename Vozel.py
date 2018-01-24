class Vozel:
  ''' Osnovni element verižnega seznama '''
  def __init__(self, kaj=None, kam=None):
     self._podatek = kaj
     self._naslednji  = kam

  def __str__(self):
     return str(self._podatek)
    
  def nastaviPodatek(self, pod):
      '''Vozlu spremeni podatek na pod'''
      self._podatek = pod

  def vrniPodatek(self):
     ''' vrne podatek, ki je v vozlu'''
     return self._podatek

  def nastaviNasled(self, mojNasled) :
     '''Vozlu nastavi novega naslednika'''
     self._naslednji = mojNasled

  def vrniNasled(self):
     ''' Vrne kazalec na naslednji vozel '''
     return self._naslednji

