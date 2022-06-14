import unittest

from Interpreter import Interpreter


class Lab3Test(unittest.TestCase):


    # Unit tests for input data validation in aspect-oriented style.
    def test_aspect_oriented_valid(self):

        @Interpreter.typecheck(a=int)
        def inc(a):
            return a + 1
        # Pass in a variable that meets the criteria —— The variable's type is int.
        self.assertEqual(inc(2), 3)
        # A variable that does not qualify is passed in. The variable's type is character, not int.
        self.assertRaises(TypeError, inc, 'b')

        # Test for using Traffic Light example.
    def test_interpreter(self):
        # Test the interpreter for normal function.
        # To configure the state machine.
        intp1 = Interpreter()
        intp1.input_from_file("TrafficLight.txt")
        intp1.input_signal("TURN ON", 0)
        intp1.input_signal("TURN GREEN", 5)
        intp1.input_signal("TURN YELLOW", 8)
        intp1.input_signal("TURN RED", 11)
        intp1.input_signal("TURN OFF", 15)
        intp1.create_action_table()
        intp1.end_state.append("RED")
        intp1.end_input.append("TURN OFF")
        result = intp1.execute()
        intp1.create_graph()
        self.assertEqual(result, True)

        # Test the interpreter's handling of receiving abnormal event list.
        intp2 = Interpreter()
        intp2.input_from_file("TrafficLight.txt")
        intp2.input_signal("TURN RED", 0)
        intp2.input_signal("TURN ON", 5)
        intp2.input_signal("TURN OFF", 8)
        intp2.input_signal("TURN GREEN", 11)
        intp2.input_signal("TURN GREEN", 14)
        intp2.input_signal("TURN OFF", 17)
        intp2.create_action_table()
        intp2.end_state.append("RED")
        intp2.end_input.append("TURN OFF")

        self.assertEqual(intp2.execute(), False)




if __name__ == '__main__':
    unittest.main()
