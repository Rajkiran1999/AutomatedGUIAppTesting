import myapp
import unittest
import os

class TestMyApp(unittest.TestCase):
    """Each method in this class is a testcase for testing one function"""


    def test_myFirstTest(self):
        app = myapp.Pythagorean()
        print(app)
        self.assertIsNotNone(app) # this tests the existence of the instance of the Pythagorean class in the app variable

    def test_guiExists(self):
        app = myapp.Pythagorean()
        gui = app.build()
        print(gui)
        self.assertIsNotNone(gui) # this tests the existence of the build method in the pythagorean app

    def test_widgetsExists(self):
        app = myapp.Pythagorean()
        gui = app.build()
        widgets = gui.children
        print(gui.children)
        self.assertIsNotNone(widgets)

        self.assertEqual(len(widgets), 5)

        for i in widgets:
            self.assertIsNotNone(i)

    def test_assetsExist(self):
        cwd = os.getcwd()
        print(cwd)
        img1 = os.path.join(cwd, "assets", "diagram.png")
        img2 = os.path.join(cwd, "assets", "logo.png")
        self.assertEqual(os.path.isfile(img1), True)
        self.assertEqual(os.path.isfile(img2), True)

    """Until now we have focused on the existence of these elements. Theor existence doesnt always guarantee correctness. 
       Hence we now focus on the datatype of these elements i.e. theor values."""
    
    def test_dictExists(self):
        app = myapp.Pythagorean()
        gui = app.build()
        output = gui.pythagorean()

        self.assertIsInstance(output, dict)

        for key,val in output.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(val, str)

    """Now after chcecking the existence and the correctness of the datatypes, we now wish to check the values of the inputs and outputs
       that are being sent and received by the program that we are testing."""
    
    def test_inputAB(self):
        app = myapp.Pythagorean()
        gui = app.build()
        widgets = gui.children

        [print(idx,val) for idx,val in enumerate(widgets[1].children)]
        inputA = (widgets[1].children)[4]
        inputB = (widgets[1].children)[2]
        inputA.text = "3"
        inputB.text = "4"

        output = gui.pythagorean()

        self.assertEqual(output, {"c": "5.0"})

    """Above we have tested an ideal scenario where the User only gives the 2 require i/p vars and the comp gives the third val.
       But what if the User had supplied all 3 values by mistake?"""
    
    def test_inputABC(self):
        app = myapp.Pythagorean()
        gui = app.build()
        widgets = gui.children

        [print(idx,val) for idx,val in enumerate(widgets[1].children)]
        inputA = (widgets[1].children)[4]
        inputB = (widgets[1].children)[2]
        inputC = widgets[1].children[0]
        inputA.text = "3"
        inputB.text = "4"
        inputC.text = "5"

        output = gui.pythagorean()
        

        self.assertEqual(output, {"error": "if you already know ALL sides then you don't need me!"})


    """Now we write testcases for corner case values like 5 billion side length or 5 picometer side length. Now we also test for mathematically
       wrong statements like dividing by zero or if the side length is negative"""
    
    def test_inputABwrong(self):
        app = myapp.Pythagorean()
        gui = app.build()
        widgets = gui.children

        [print(idx,val) for idx,val in enumerate(widgets[1].children)]
        inputA = (widgets[1].children)[4]
        inputB = (widgets[1].children)[2]
        inputA.text = "3"
        inputB.text = "-4"

        output = gui.pythagorean()

        self.assertNotEqual(output, {"c": "5.0"})


    """Now that we have handled the wrong inputs in the above testcase, It is time to check for malicious inputs. E.g: SQL Injection: special
       input values that force servers to reveal entire databases without permission"""
    
    def test_inputABwrong2(self):
        app = myapp.Pythagorean()
        gui = app.build()
        widgets = gui.children

        [print(idx,val) for idx,val in enumerate(widgets[1].children)]
        inputA = (widgets[1].children)[4]
        inputB = (widgets[1].children)[2]
        inputA.text = "3"
        inputB.text = "banana"

        output = gui.pythagorean()

        self.assertNotEqual(output, {"c": "5.0"})


if __name__ == '__main__':
    unittest.main()