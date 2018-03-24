import unittest 
import calibrator 
import test
import numpy as np 

class TestCalibrator(unittest.TestCase):
	
	def test_keypressQ(self):	
		lower = np.array([50,100,50])
		upper = np.array([200,255,180])
		eye = calibrator.Calibrator.calibrate(self, upper, upper)
		self.assertEqual(None,eye)
		
	def test_keypressSpace(self):	
		lower = np.array([50,100,50])
		upper = np.array([200,255,180])
		eye = calibrator.Calibrator.calibrate(self, upper, upper)
		expectedReturn = np.zeros((300,150,3), np.uint8)
		size = eye.size
		passTest = False
		if size > 0:
			passTest = True 
		self.assertTrue(passTest)
		
	
		
		
if __name__ == '__main__':
    unittest.main()
		