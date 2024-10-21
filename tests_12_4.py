import runner, unittest, logging


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            rn = runner.Runner('name')
            for i in range(-10):
                rn.walk()
            logging.info('test_walk выполнен успешно')
            self.assertEqual(rn.distance, 50)
        except:
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            rnr = runner.Runner('name')
            for i in range(10):
                rnr.run()
            logging.info('test_run выполнен успешно')
            self.assertEqual(rnr.distance, 100)
        except:
            logging.warning('Неверная скорость для Runner')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")
    unittest.main()