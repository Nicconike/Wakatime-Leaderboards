# CHANGELOG


## v1.2.2 (2025-02-02)

### Bug Fixes

- Update Dockerfile to use non-root user and adjust file ownership;
  ([`2b7a134`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/2b7a13459c6582d8c022296e03bb97a89c9992e1))

Addresses the security hotspot in Dockerfile tests: add new tests for error handling functions

### Chores

- Update Pylint Badge
  ([`43e7214`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/43e7214eca61909e7e388467930deca9e8371ef7))

- Update Pylint Badge
  ([`57e7995`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/57e79957c768e38a38f12c995a923f1623a11952))

- Update Wakatime Leaderboards
  ([`2fc6640`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/2fc664099105ecd97b4735c3ed0e92e8cc6a7cf1))

- Update Wakatime Leaderboards
  ([`1353571`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/135357199e559892c1d0133d7b4a85c377cbc324))

- Update Wakatime Leaderboards
  ([`75dcfff`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/75dcfff59c2495afa51575618429d044335e4c2d))

- **deps**: Bump the python-packages group across 1 directory with 3 updates
  ([#33](https://github.com/Nicconike/Wakatime-Leaderboards/pull/33),
  [`24e6591`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/24e659102c03e11bff9dedd873b8de491170407d))

Bumps the python-packages group with 3 updates in the / directory:
  [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release),
  [pylint](https://github.com/pylint-dev/pylint) and
  [pipdeptree](https://github.com/tox-dev/pipdeptree).

Updates `python-semantic-release` from 9.16.1 to 9.17.0 Updates `pylint` from 3.3.3 to 3.3.4 Updates
  `pipdeptree` from 2.24.0 to 2.25.0

### Continuous Integration

- **deps**: Bump python-semantic-release/python-semantic-release
  ([#31](https://github.com/Nicconike/Wakatime-Leaderboards/pull/31),
  [`8866ab1`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/8866ab168a59fb74e8eecc73a146a8122339032a))

Bumps the github-actions group with 1 update:
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).

Updates `python-semantic-release/python-semantic-release` from 9.16.1 to 9.17.0

### Refactoring

- Refactor unit tests and remove dotenv
  ([`ba560e0`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/ba560e00e515292291139675b31f5d4f8ea10c08))


## v1.2.1 (2025-01-14)

### Bug Fixes

- Implement complete error handling while fetching wakatime stats using the API
  ([`5293314`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/5293314616753baeb7526abc4baa3ee65410b2f6))

### Build System

- Fix build-system for toml
  ([`2c1daf4`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/2c1daf44bdd56bf187f6709c7154d0f2ce93de59))

- Fix pyproject.toml & update requirements.txt
  ([`e7bd289`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/e7bd2896c0c97bb768781c031da78cf10885bcd3))

### Chores

- Remove invalid permission
  ([`3c85822`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/3c8582215cfd1e19d492487acf51d703380a64e5))

- Update action.yml
  ([`0eb215c`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/0eb215c126fb81de05e3c403a801089b6002bd9e))

- Update Pylint Badge
  ([`9136b90`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/9136b9027547b27a2efa05e44c40f83f994a6b01))

- Update Wakatime Leaderboards
  ([`88f3791`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/88f3791251a93e49a6fa9ee660e6b755b4ac9ffb))

- Update Wakatime Leaderboards
  ([`569e44d`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/569e44d0b732add5970eca90e663507242583cb3))

- Update Wakatime Leaderboards
  ([`7d708ca`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/7d708ca4a5dc133ab995152251d5e6483b49954a))

- Update Wakatime Leaderboards
  ([`4006f51`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/4006f51d4f560866aded7b2438c338dcd826d561))

- Update Wakatime Leaderboards
  ([`b288206`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/b28820604b367025bedee55ad27513f39a1bcc4c))

- **deps**: Bump pytest-cov in the python-packages group
  ([#22](https://github.com/Nicconike/Wakatime-Leaderboards/pull/22),
  [`caf078a`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/caf078a90df699907bfae0e6171a6515e7cb0b08))

Bumps the python-packages group with 1 update:
  [pytest-cov](https://github.com/pytest-dev/pytest-cov).

Updates `pytest-cov` from 5.0.0 to 6.0.0 -
  [Changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst) -
  [Commits](https://github.com/pytest-dev/pytest-cov/compare/v5.0.0...v6.0.0)

--- updated-dependencies: - dependency-name: pytest-cov dependency-type: direct:production

update-type: version-update:semver-major

dependency-group: python-packages

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump python from 3.12-slim to 3.13-slim in the docker group
  ([#17](https://github.com/Nicconike/Wakatime-Leaderboards/pull/17),
  [`eeaba78`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/eeaba783004e44c82bb86391ad3e276f4ba98c30))

Bumps the docker group with 1 update: python.

Updates `python` from 3.12-slim to 3.13-slim

--- updated-dependencies: - dependency-name: python dependency-type: direct:production

dependency-group: docker

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump python-semantic-release
  ([#19](https://github.com/Nicconike/Wakatime-Leaderboards/pull/19),
  [`73e2520`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/73e2520eb872f4ea338fbaae6fdf0ec101dd8cb4))

Bumps the python-packages group with 1 update in the / directory:
  [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).

Updates `python-semantic-release` from 9.9.0 to 9.11.1 - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.9...v9.11.1)

--- updated-dependencies: - dependency-name: python-semantic-release dependency-type:
  direct:production

update-type: version-update:semver-minor

dependency-group: python-packages

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump python-semantic-release in the python-packages group
  ([#21](https://github.com/Nicconike/Wakatime-Leaderboards/pull/21),
  [`9d2fc49`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/9d2fc498fb39617a8aa10e1f3dec4375df0f9276))

Bumps the python-packages group with 1 update:
  [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).

Updates `python-semantic-release` from 9.11.1 to 9.12.0 - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.11.1...v9.12)

--- updated-dependencies: - dependency-name: python-semantic-release dependency-type:
  direct:production

update-type: version-update:semver-minor

dependency-group: python-packages

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Update setuptools requirement in the python-packages group
  ([#30](https://github.com/Nicconike/Wakatime-Leaderboards/pull/30),
  [`067d43e`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/067d43ea110e75a640160c85abef95b6448fcd93))

Updates the requirements on [setuptools](https://github.com/pypa/setuptools) to permit the latest
  version.

Updates `setuptools` to 75.8.0

### Continuous Integration

- Enable docker publish only when new tag is released
  ([`bc357f9`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/bc357f93836797d077c7c1e10ebd8195ca6409a0))

- Fix docker release
  ([`78f2bcb`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/78f2bcb8b16c2ea889d1b660e5d6a46e3f75050f))

- **deps**: Bump python-semantic-release/python-semantic-release
  ([#16](https://github.com/Nicconike/Wakatime-Leaderboards/pull/16),
  [`8d16e92`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/8d16e92a12a8aaf1d2dcea4914cd9a892b6898ab))

Bumps the github-actions group with 1 update:
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).

Updates `python-semantic-release/python-semantic-release` from 9.9.0 to 9.11.0 - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.9.0...v9.11.0)

--- updated-dependencies: - dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production

update-type: version-update:semver-minor

dependency-group: github-actions

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump python-semantic-release/python-semantic-release
  ([#29](https://github.com/Nicconike/Wakatime-Leaderboards/pull/29),
  [`f8c4f9c`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/f8c4f9ce8d524f21a732ad78c1f7b1237cb191f0))

Bumps the github-actions group with 1 update in the / directory:
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).

Updates `python-semantic-release/python-semantic-release` from 9.15.1 to 9.16.1

- **deps**: Bump the github-actions group across 1 directory with 4 updates
  ([#27](https://github.com/Nicconike/Wakatime-Leaderboards/pull/27),
  [`571ca55`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/571ca553bfde1ff085d875277585484f1ca197de))

Bumps the github-actions group with 4 updates in the / directory:
  [codecov/codecov-action](https://github.com/codecov/codecov-action),
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release),
  [actions/attest-build-provenance](https://github.com/actions/attest-build-provenance) and
  [docker/scout-action](https://github.com/docker/scout-action).

Updates `codecov/codecov-action` from 4 to 5 - [Release
  notes](https://github.com/codecov/codecov-action/releases) -
  [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/codecov/codecov-action/compare/v4...v5)

Updates `python-semantic-release/python-semantic-release` from 9.12.0 to 9.15.1 - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.12.0...v9.15.1)

Updates `actions/attest-build-provenance` from 1 to 2 - [Release
  notes](https://github.com/actions/attest-build-provenance/releases) -
  [Changelog](https://github.com/actions/attest-build-provenance/blob/main/RELEASE.md) -
  [Commits](https://github.com/actions/attest-build-provenance/compare/v1...v2)

Updates `docker/scout-action` from 1.15.0 to 1.16.1 - [Release
  notes](https://github.com/docker/scout-action/releases) -
  [Commits](https://github.com/docker/scout-action/compare/v1.15.0...v1.16.1)

- **deps**: Bump the github-actions group with 2 updates
  ([#20](https://github.com/Nicconike/Wakatime-Leaderboards/pull/20),
  [`dcdce98`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/dcdce98f37b1b0b60b9528c7b1a74e4640664b97))

Bumps the github-actions group with 2 updates:
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
  and [docker/scout-action](https://github.com/docker/scout-action).

Updates `python-semantic-release/python-semantic-release` from 9.11.0 to 9.12.0

Updates `docker/scout-action` from 1.14.0 to 1.15.0

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

### Refactoring

- Check key before initializing repo
  ([`ed1c8f0`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/ed1c8f0dbcd1a1af4c8b5a6196a53a09f0432fdf))


## v1.2.0 (2024-10-12)

### Chores

- Add code time
  ([`eb7c9c7`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/eb7c9c7b772374d93e1cb6d143a2d5b5e52349bf))

- Update dependabot
  ([`c358c79`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/c358c79281ec7bf091c99e40060e0b8317515fd7))

- Update dependabot
  ([`fedd079`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/fedd079b1c92bcaac4ce8af1cc01569c11baa28c))

- Update dependabot labelling
  ([`c031d19`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/c031d1973098a4daacdb6ab6dfa62284735fa62e))

- Update deps
  ([`5d3cde5`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/5d3cde51c0396bf0cce9e98b7444dd196b8e06ec))

- Update Pylint Badge
  ([`9b9cf19`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/9b9cf19c70dc22015641b5a0192eea71f6608758))

- Update Wakatime Leaderboards
  ([`dd8ef25`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/dd8ef25647e0e7bc1899c96a457fd474105556ed))

- Update Wakatime Leaderboards
  ([`e25cadd`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/e25cadd9863f97a35a22fa34332990635c338228))

- Update Wakatime Leaderboards
  ([`273cf90`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/273cf903cc2d491f0902bccf792e59c6c3664167))

- Update Wakatime Leaderboards
  ([`6bcc016`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/6bcc016a12e2a4f107ba184b920d9c3bbc9faa1e))

- Update Wakatime Leaderboards
  ([`1be0281`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/1be02810dc894bfae315fc5d0978fb52ec4f2c32))

- Update Wakatime Leaderboards
  ([`1c96aa7`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/1c96aa76a2810f4a3a5750de61037bbc5e218bff))

- Update Wakatime Leaderboards
  ([`b07baad`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/b07baad4ab4a6c411cbf0bdfb1b7d5fa3451492c))

- Update Wakatime Leaderboards
  ([`05bbf9f`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/05bbf9f133a74522af19006efbaaf66876c596a8))

- Update Wakatime Leaderboards
  ([`8455ff8`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/8455ff87d6ed297d046859d42e1f93756e74e8c0))

- Update Wakatime Leaderboards
  ([`22be7c8`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/22be7c83e6fd0149be8bf42113f6902938fab033))

- Update Wakatime Leaderboards
  ([`86cb9bb`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/86cb9bb95aac19a91fe9c94098d5bd2b41b0945e))

- **deps**: Bump pipdeptree in the python-packages group
  ([#9](https://github.com/Nicconike/Wakatime-Leaderboards/pull/9),
  [`b338911`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/b3389112e83736a26ea7bbac509000d99284063a))

Bumps the python-packages group with 1 update: [pipdeptree](https://github.com/tox-dev/pipdeptree).

Updates `pipdeptree` from 2.23.1 to 2.23.3 - [Release
  notes](https://github.com/tox-dev/pipdeptree/releases) -
  [Commits](https://github.com/tox-dev/pipdeptree/compare/2.23.1...2.23.3)

--- updated-dependencies: - dependency-name: pipdeptree dependency-type: direct:production

update-type: version-update:semver-patch

dependency-group: python-packages

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump python-semantic-release in the python-packages group
  ([#13](https://github.com/Nicconike/Wakatime-Leaderboards/pull/13),
  [`948f4bd`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/948f4bd3ccb552d8fd55c7c53bb9777ad83148ba))

Bumps the python-packages group with 1 update:
  [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).

Updates `python-semantic-release` from 9.8.9 to 9.9.0 - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.8.9...v9.9)

--- updated-dependencies: - dependency-name: python-semantic-release dependency-type:
  direct:production

update-type: version-update:semver-minor

dependency-group: python-packages

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump python-semantic-release in the python-packages group
  ([#4](https://github.com/Nicconike/Wakatime-Leaderboards/pull/4),
  [`b21825b`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/b21825bf14f4fb548f376efec1aa879c0bbb9476))

Bumps the python-packages group with 1 update:
  [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).

Updates `python-semantic-release` from 9.8.6 to 9.8.7 - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.8.6...v9.8.7)

--- updated-dependencies: - dependency-name: python-semantic-release dependency-type:
  direct:production

update-type: version-update:semver-patch

dependency-group: python-packages

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump the python-packages group across 1 directory with 3 updates
  ([#11](https://github.com/Nicconike/Wakatime-Leaderboards/pull/11),
  [`1b44783`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/1b44783418972dcced2335bc7e67adcb4775bbfa))

Bumps the python-packages group with 3 updates in the / directory:
  [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release),
  [pylint](https://github.com/pylint-dev/pylint) and
  [pipdeptree](https://github.com/tox-dev/pipdeptree).

Updates `python-semantic-release` from 9.8.8 to 9.8.9 - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.8.8...v9.8.9)

Updates `pylint` from 3.2.7 to 3.3.1 - [Release
  notes](https://github.com/pylint-dev/pylint/releases) -
  [Commits](https://github.com/pylint-dev/pylint/compare/v3.2.7...v3.3.1)

Updates `pipdeptree` from 2.23.3 to 2.23.4 - [Release
  notes](https://github.com/tox-dev/pipdeptree/releases) -
  [Commits](https://github.com/tox-dev/pipdeptree/compare/2.23.3...2.23.4)

--- updated-dependencies: - dependency-name: python-semantic-release dependency-type:
  direct:production

update-type: version-update:semver-patch

dependency-group: python-packages

- dependency-name: pylint dependency-type: direct:production

update-type: version-update:semver-minor

- dependency-name: pipdeptree dependency-type: direct:production

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump the python-packages group across 1 directory with 3 updates
  ([#6](https://github.com/Nicconike/Wakatime-Leaderboards/pull/6),
  [`b80109f`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/b80109f0e8027145d6521ea157f020f4ca7577da))

Bumps the python-packages group with 3 updates in the / directory:
  [pygithub](https://github.com/pygithub/pygithub),
  [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release) and
  [pylint](https://github.com/pylint-dev/pylint).

Updates `pygithub` from 2.3.0 to 2.4.0 - [Release
  notes](https://github.com/pygithub/pygithub/releases) -
  [Changelog](https://github.com/PyGithub/PyGithub/blob/main/doc/changes.rst) -
  [Commits](https://github.com/pygithub/pygithub/compare/v2.3.0...v2.4.0)

Updates `python-semantic-release` from 9.8.7 to 9.8.8 - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.8.7...v9.8.8)

Updates `pylint` from 3.2.6 to 3.2.7 - [Release
  notes](https://github.com/pylint-dev/pylint/releases) -
  [Commits](https://github.com/pylint-dev/pylint/compare/v3.2.6...v3.2.7)

--- updated-dependencies: - dependency-name: pygithub dependency-type: direct:production

update-type: version-update:semver-minor

dependency-group: python-packages

- dependency-name: python-semantic-release dependency-type: direct:production

update-type: version-update:semver-patch

- dependency-name: pylint dependency-type: direct:production

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

### Continuous Integration

- Add attestations
  ([`ce25d1b`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/ce25d1bb9a323f7084319cd2b70511e293e909a0))

- Add login step for GHCR
  ([`0416cfe`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/0416cfe324114540bf0a14caeb64409b173be6c6))

- Add packages write access
  ([`19286bc`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/19286bc87a8b7b4ae05fd3edb2319892fdf2b41c))

- Bump docker/scout-action in the github-actions group
  ([#2](https://github.com/Nicconike/Wakatime-Leaderboards/pull/2),
  [`8454b06`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/8454b06d6653dc1eb88324c3bbd27c0696116f87))

Bumps the github-actions group with 1 update:
  [docker/scout-action](https://github.com/docker/scout-action).

Updates `docker/scout-action` from 1.12.0 to 1.13.0 - [Release
  notes](https://github.com/docker/scout-action/releases) -
  [Commits](https://github.com/docker/scout-action/compare/v1.12.0...v1.13.0)

--- updated-dependencies: - dependency-name: docker/scout-action dependency-type: direct:production

update-type: version-update:semver-minor

dependency-group: github-actions

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- Bump docker/scout-action in the github-actions group
  ([#8](https://github.com/Nicconike/Wakatime-Leaderboards/pull/8),
  [`8e1979a`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/8e1979af882f16753a6d6d101adc5c7f6cc73b90))

Bumps the github-actions group with 1 update:
  [docker/scout-action](https://github.com/docker/scout-action).

Updates `docker/scout-action` from 1.13.0 to 1.14.0 - [Release
  notes](https://github.com/docker/scout-action/releases) -
  [Commits](https://github.com/docker/scout-action/compare/v1.13.0...v1.14.0)

--- updated-dependencies: - dependency-name: docker/scout-action dependency-type: direct:production

update-type: version-update:semver-minor

dependency-group: github-actions

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- Bump python-semantic-release/python-semantic-release
  ([#3](https://github.com/Nicconike/Wakatime-Leaderboards/pull/3),
  [`5934a85`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/5934a8517924677efea7f50619f8e8c661c3d200))

Bumps the github-actions group with 1 update:
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).

Updates `python-semantic-release/python-semantic-release` from 9.8.6 to 9.8.7 - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.8.6...v9.8.7)

--- updated-dependencies: - dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production

update-type: version-update:semver-patch

dependency-group: github-actions

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- Bump python-semantic-release/python-semantic-release
  ([#7](https://github.com/Nicconike/Wakatime-Leaderboards/pull/7),
  [`805f724`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/805f724b6ddf6f375d5bdf8566726a417a8e72e6))

Bumps the github-actions group with 1 update:
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).

Updates `python-semantic-release/python-semantic-release` from 9.8.7 to 9.8.8 - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.8.7...v9.8.8)

--- updated-dependencies: - dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production

update-type: version-update:semver-patch

dependency-group: github-actions

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- Fix attestation step
  ([`79add4e`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/79add4e0e475bb399c0634c45b765107e6ebe362))

- Fix docker scout step
  ([`ca81546`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/ca8154688a8414a140c900441bacbe8c53d8f16a))

- Fix metadata step
  ([`9add373`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/9add373e77ad3b5ff87bc76b6fe651455a95c95b))

- Fix the tags extraction
  ([`eb32e64`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/eb32e6450b6a9dc11999c73094b716ea8e00345a))

- Fix workflow dep
  ([`8465ec6`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/8465ec6eb2ad68310c141440073ff351165a294f))

- Update all workflows to not be triggered with a bot commit
  ([`f2ece42`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/f2ece42efc89dd719590e5d271e620dc840190e6))

- Update build step
  ([`336139b`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/336139b1b31ceb23a39af2b6134182cb9fe95a44))

- **deps**: Bump python-semantic-release/python-semantic-release
  ([#12](https://github.com/Nicconike/Wakatime-Leaderboards/pull/12),
  [`8bd87d5`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/8bd87d593b505af2d0ee410217990127be35476a))

Bumps the github-actions group with 1 update:
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).

Updates `python-semantic-release/python-semantic-release` from 9.8.8 to 9.8.9 - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.8.8...v9.8.9)

--- updated-dependencies: - dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production

update-type: version-update:semver-patch

dependency-group: github-actions

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump python-semantic-release/python-semantic-release
  ([#14](https://github.com/Nicconike/Wakatime-Leaderboards/pull/14),
  [`8513dcc`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/8513dcc0eb4f5798c028ca09858e7d89a2710885))

Bumps the github-actions group with 1 update:
  [python-semantic-release/python-semantic-release](https://github.com/python-semantic-release/python-semantic-release).

Updates `python-semantic-release/python-semantic-release` from 9.8.9 to 9.9.0 - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.8.9...v9.9.0)

--- updated-dependencies: - dependency-name: python-semantic-release/python-semantic-release
  dependency-type: direct:production

update-type: version-update:semver-minor

dependency-group: github-actions

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- **deps**: Bump sigstore/cosign-installer in the github-actions group
  ([#15](https://github.com/Nicconike/Wakatime-Leaderboards/pull/15),
  [`696aed5`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/696aed5087407952b6ac4a42c4c24267dc4007d2))

Bumps the github-actions group with 1 update:
  [sigstore/cosign-installer](https://github.com/sigstore/cosign-installer).

Updates `sigstore/cosign-installer` from 3.6.0 to 3.7.0 - [Release
  notes](https://github.com/sigstore/cosign-installer/releases) -
  [Commits](https://github.com/sigstore/cosign-installer/compare/v3.6.0...v3.7.0)

--- updated-dependencies: - dependency-name: sigstore/cosign-installer dependency-type:
  direct:production

update-type: version-update:semver-minor

dependency-group: github-actions

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

### Documentation

- Update readme
  ([`8f29920`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/8f299205f5922ee1648013c7ea604b62b856d07e))

- Update readme
  ([`d1d7e2f`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/d1d7e2f45ad0046ce609a92993c0669603e5fba6))

### Features

- Handle edge cases gracefully
  ([`40ecb8e`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/40ecb8e3f7f096b5c6f74147d60c7c740101016a))


## v1.1.0 (2024-08-05)

### Bug Fixes

- Correctly display the country rank
  ([`2409612`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/2409612ab1d73c183a9715bc551e13806123f0da))

### Chores

- Update Pylint Badge
  ([`423eeba`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/423eebaea982ee4f8f7868f7110ed10819ed1f97))

- Update Pylint Badge
  ([`3eebe92`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/3eebe9254d7e8f9f8083044d495d39df7b83feda))

- Update Pylint Badge
  ([`5666ec8`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/5666ec84ca7562e2f3c539b1e5099a0aa26e9612))

- Update Wakatime Leaderboards
  ([`39bc443`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/39bc44381cbb664529f58be644e6da4e8a05a5d6))

- Update Wakatime Leaderboards
  ([`fd9991c`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/fd9991c678f6c145d2bcd94dc64252b20c86cab3))

- Update Wakatime Leaderboards
  ([`4c99501`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/4c9950128560c30166cfd6469f51cdfcee35d71b))

- Update Wakatime Leaderboards
  ([`1f9ea05`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/1f9ea05f22a19cd333a82ba3c1635849c6d338dc))

### Features

- Remove Country Leaderboards
  ([`0ee6c41`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/0ee6c41b49a1a5590acf86926bab3a998df7b6c7))

test: refactor unit tests

### Refactoring

- Update workflow
  ([`800ed81`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/800ed81e84272af5a43d1ad1a760c69548447128))

### Testing

- Fix test_log_execution_time
  ([`b706c46`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/b706c46086b28b589fc07a4199a29b2fc571e162))


## v1.0.0 (2024-08-03)

### Bug Fixes

- Correct the commit msg & table
  ([`6d5b739`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/6d5b739bb5cc826abfd698b8d2479cdcde747875))

### Build System

- Update dockerfile
  ([`73712c3`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/73712c3fe362376f4c0c673dc7ff28ad441ccf0b))

### Chores

- Update Pylint Badge
  ([`ed95bb3`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/ed95bb3e209f6bda331d719b8dff9bc9f33ed126))

- Update Pylint Badge
  ([`899da04`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/899da041dadbdb669987f15a53fad4b7ad38dfce))

- Update Pylint Badge
  ([`b4e5af1`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/b4e5af1e31c4b9e45d6e7256a2f99c43da74bbcc))

- Update Steam Stats
  ([`1d49fda`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/1d49fda2b9c81ef69ff5110ad485c61d861be7d4))

- Update Steam Stats
  ([`bc4ca91`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/bc4ca91e95f8af832de27fe399f90f64ce55ee62))

- Update toml
  ([`8428f5c`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/8428f5cf642ab2f7877267433d51f8dee536cdfb))

- Update Wakatime Leaderboards
  ([`7f92fda`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/7f92fdaac64ea5c8fc6c98911cb0fc1ccace2505))

- Update Wakatime Leaderboards
  ([`72ab52f`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/72ab52f296c698763c516d9bc40ec459bb1cf485))

- Update Wakatime Leaderboards
  ([`a7ab01f`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/a7ab01f5ca7b2c220c6bfe07e95da410b78947f1))

- Wakatime Leaderboards
  ([`ebdba18`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/ebdba18c313bdd4a2cbca294ce908c1a8b2e27fb))

- **release**: Version Release 0.0.0
  ([`1fe82b8`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/1fe82b8a7b49cba64c3fe429204b36ab8d0520da))

- **release**: Version Release 0.0.0
  ([`6875d8e`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/6875d8edb2a120e167ef27c7200a088586a4eb38))

- **release**: Version Release 0.1.0
  ([`c7e11ed`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/c7e11edc0c5569e15640ae25835745e6a3a9f6d8))

### Continuous Integration

- Bump docker/scout-action in the github-actions group
  ([#1](https://github.com/Nicconike/Wakatime-Leaderboards/pull/1),
  [`417d618`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/417d6187243f96280a3037be782b4fb92cf79e21))

Bumps the github-actions group with 1 update:
  [docker/scout-action](https://github.com/docker/scout-action).

Updates `docker/scout-action` from 1.11.0 to 1.12.0 - [Release
  notes](https://github.com/docker/scout-action/releases) -
  [Commits](https://github.com/docker/scout-action/compare/v1.11.0...v1.12.0)

--- updated-dependencies: - dependency-name: docker/scout-action dependency-type: direct:production

update-type: version-update:semver-minor

dependency-group: github-actions

...

Signed-off-by: dependabot[bot] <support@github.com>

Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>

- Check for clean working tree
  ([`9623999`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/9623999489380bf9bbebc742e27e97634b0e29f8))

- Trigger codecov
  ([`b7b5316`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/b7b5316846c6ac466b8919e599b5af5fb01f2795))

- Update workflow
  ([`a6b608d`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/a6b608dd84f5becf27df4815fb59f1f716a6abd1))

BREAKING CHANGE: Release Major Version

### Documentation

- Add security.md
  ([`63a69ae`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/63a69ae33d42cdcaaceee08815aa3f91b377345e))

- Create CODE_OF_CONDUCT.md
  ([`fb169cc`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/fb169cc6337d9b6d2b78a50dff2d0d29388f2ff8))

Signed-off-by: Nicco <38905025+Nicconike@users.noreply.github.com>

### Features

- Update Dockerfile
  ([`dfc0ae0`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/dfc0ae08e2025393375f7dbd3dcd1d9e1eb31d99))

- Update main code to correctly fetch user country
  ([`e89db01`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/e89db01976e10b78f89d855e5f53815bc13d4a97))

### Refactoring

- Update code
  ([`4b4d404`](https://github.com/Nicconike/Wakatime-Leaderboards/commit/4b4d40448437af001f37295597be10c79897cbbf))
