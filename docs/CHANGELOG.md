# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

### Changed

- README correcty specifies that `.env` can be also used for username

### Removed

- The ability to run the program using `make`

## [1.1.0]

### Added

- This present changelog
- Issue title and body can be passed through the command line
- A `.env` file can be used to store locally GitHub username and Personal Access Token
- Test label for test issues

### Changed

- Static printed messages are now stored in `constants.py`

### Fixed

- Not having a `.env` file used to crash the program

## [1.0.0]

### Added

- Code of conduct
- Contributing notice
- Issue/PR templates
- Poetry
- Makefile
- Issue footer
- Ability to add labels to the issue

### Changed

- Moved docs in a specific folder
- Renamed poetry script to `create-issue` (previously: `issue`)
- Side functions are now in a separate file (`utils.py`)

### Removed

- Support of Python 3.7, 3.8 and 3.9
