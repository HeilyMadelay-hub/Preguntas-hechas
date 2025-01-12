
def runningSum(nums):
    b=0 # variable to store
    resultant=[] # array to store the resulta

    for a in nums: # loop through each element of the array
        b+=a
        resultant.append(b) #append the result to the resultant array

    return resultant

print(runningSum([8,2,3,4])) 

# En Python, los métodos dentro de una clase deben incluir 'self' como primer parámetro,
# ya que se refiere a la instancia del objeto que llama al método. Esto permite que el método
# acceda y modifique los atributos y otros métodos de la clase. Sin 'self', Python no sabe a qué
# instancia de la clase debe asociar el método, lo que genera un error. Por lo tanto, 'self' es esencial
# para trabajar con métodos de instancia en una clase.
#   class Solution:
#       def runningSum(self, nums): 


