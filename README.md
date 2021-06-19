# Object Tracking

My implimentation of object tracking by miminizing the Eucledean distance between centroids of bounding boxes between consicutive frames.

## How It works

These are the steps that occ in this object tracking algorithm.

1. Find Bounding boxes using any algorithm.(Here Ill be using basic face haarcascades)

2. Find the centroids of the bounding boxes every frame.

3. Calculate the distance between the centroids of consicutive frames.

4. For every Centroid find the centroid which is closest, and mark it the same id.

### Prerequisites

What things you need to install the software and how to install them

```bash
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Install the Requirements:

```python
 pip install -r requirements.txt
```

Say what the step will be

```bash
Give the example
```

And repeat

```bash
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Images

![ DESCRIPTION ](https://via.placeholder.com/400)
![ DESCRIPTION ](https://via.placeholder.com/400)

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```bash
Give an example
```

### And coding style tests

Explain what these tests test and why

```bash
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Name](<LINK>) - DESCRIPTION
* [Name](<LINK>) - DESCRIPTION
* [Name](<LINK>) - DESCRIPTION

## Contributing

Please read [CONTRIBUTING.md](https://github.com/) for details on our code of conduct, and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Atharva Gundawar** - *Initial work* - [Github handle](https://github.com/Atharva-Gundawar)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
