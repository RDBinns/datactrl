datactrl
========

Making the UK register of data controllers more useable


### What's this for?

Ever wanted to know what personal data an organisations has about you and why? The UK Information Commissioner's Office maintains a register of over 350,000 organisations and their personal data practices. This project aims to use this resource to help individuals get an overall picture of what organisations might know about them.

Each organisation (or 'data controller') has an entry which contains;
- Their reasons for collecting the data (e.g. marketing or staff administration)
- Who the data is about (e.g. customers or staff)
- What categories of data are collected (e.g. previous employment or purchase history)
- The kinds of entities who have access to the data (e.g. 'credit reference agencies'
- Any international data transfers


### How data has changed since the ICO's format was updated?

The new format of the register has no differentiation between different _purposes_ of data collection, so it is now impossible to tell which kinds of data / subjects / recipients apply to which purposes. The previous format at least showed which kinds of data collection apply to each stakeholder.

_At present, the website shows both, as not every org registered after the change in how data was captured_

The python script above was designed to parse the old XML version of the register and put it into an SQL database, and should work for copies dated prior to April 2013. There is another project to parse the new version of the register [here](https://github.com/themakshter/privacyMatters) (written in Java).

### Licensing?

Both versions are under an Open Government License.

### Privacy considerations?

The ICO state the following in the README file accompanying the DVD version of the register;

_The register will be provided under the Open Government License and may be reused provided that the reuse of any personal data complies with the requirements of the Data Protection Act and, in particular, that such data are not used in a way that is inconsistent with the purpose for which the register was created, for example not used for direct marketing, or in a way that otherwise adversely affects the privacy of individuals._

For further discussion about this data set and the license see my [data.gov.uk submission](http://data.gov.uk/data-request/ico-public-register-data-controllers) including Owen Boswarva's comment and link to a related request.
