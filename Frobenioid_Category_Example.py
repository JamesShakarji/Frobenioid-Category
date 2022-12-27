class Frobenioid:
    def __init__(self, objects, binary_operation, left_action, right_action):
        self.objects = objects
        self.binary_operation = binary_operation
        self.left_action = left_action
        self.right_action = right_action
    
    def tensor_product(self, object_1, object_2):
        """Computes the tensor product of two objects in the Frobenioid."""
        return self.binary_operation(object_1, object_2)
    
    def left_act(self, object, element):
        """Applies the left action of the Frobenioid to an object."""
        return self.left_action(object, element)
    
    def right_act(self, element, object):
        """Applies the right action of the Frobenioid to an object."""
        return self.right_action(element, object)

# Example usage
objects = ['a', 'b', 'c']
binary_operation = lambda x, y: x + y
left_action = lambda x, y: y + x
right_action = lambda x, y: x + y
frobenioid = Frobenioid(objects, binary_operation, left_action, right_action)

tensor_product = frobenioid.tensor_product('a', 'b')
print(f'Tensor product: {tensor_product}')
left_acted = frobenioid.left_act('a', 'x')
print(f'Left action: {left_acted}')
right_acted = frobenioid.right_act('y', 'a')
print(f'Right action: {right_acted}')


#Output should look like this:
#Tensor product: ab
#Left action: xa
#Right action: ya
