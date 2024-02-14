from pricerange import PriceRange

class App(PriceRange):
  def run(self):
    try:
      self.get_input()
    except Exception as e:
      print(e)
      self.run()
