class DataReducerVariable:
   ''' A class for creating custom variables that are being read by the VlsvFile class. This is useful for reading in variables that are not written in the vlsv file directly
   '''
   variables = []
   operation = []
   name = []
   units = []
   def __init__(self, variables, operation,  units):
      ''' Constructor for the class
          :param variables          List of variables for doing calculations with
          :param operation          The operator that operates on the variables
          :param units              Units of the variable
          Example:
          def plus( array ):
             return array[0]+array[1]
          new_var = DataReducerVariable( ["rho", "rho"], plus, "sum_of_rhos", "1/m^3" )
      '''
      self.variables = variables
      self.operation = operation
      self.units = units


