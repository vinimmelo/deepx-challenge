# DeepX Code Challenge

## Introduction

Code made to solve the challenge of Mars Rover, made by DeepX.

Were created two classes to represent the objects Plateau and Rover, the transformation of the data was made inside the transform file.

After receive the data in the API, the flask application return in json the solution.

In the app_tests file, there is two tests with different data that will test the solution that are asked for.


## Mars Rover Problem

>A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth.

>A rover's position and location is represented by a combination of x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

>In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot. 'M' means move forward one grid point, and maintain the same heading.

>Assume that the square directly North from (x, y) is (x, y+1).

## Prepare the Environment

To run the tests and configure the environment, do the follow steps:

- Install Python3.7
- Git clone the project: `git clone https://github.com/vinimmelo/deepx-challenge.git`
- Cd into the project app: `cd deepx-challenge/App/`
- Run `pip install -r requirements`

Now, there will be two paths to test the application.

####  Run the Tests

- Run the file tests.bat (if you are on a Windows system).
    - `.\tests.bat`
- If you are on Linux or Mac Os run the follow command:
    - `while :; pytest; sleep 5; done`

**P.S:**
- If you want to see the output being generated, run the transform file directly:
    - `python3 transform.py` or `python transform.py`

#### Run the API

- Run `flask run` and connect (by default) to:
    - [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
- Follow the instructions, or send an Post to the API url:
    - [http://127.0.0.1:5000/api](http://127.0.0.1:5000/api)
- Sample of Usage:
    - Run curl: `curl -X POST 127.0.0.1:5000/api -d '{"data": "5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM"}'
`

## Coded With

- **Python**
- Flask
- Flask Restful

## Author

- **Vinicius Melo**

## License

Project based on MIT license terms, see the file [README](https://github.com/vinimmelo/deepx-challenge/blob/master/README.md) for further details.

