# dp-gitops

GitOps configuration support for Datapower.

# What is this?

I am not really sure yet. What I want it to be in a set of utilities that can represent Datapower configuration (objects, files, cert) in YAML for gitops-style repeatable (headless) deployments, supporting docker and appliance deployment types. In a containerised environment, this would mean using datapower startup.cfg files with that text format, but that is not intuitive to use, which is where YAML + jinja2 comes in.

I don't think we need to go the other way at this time - no cfg format to YAML, since we can use the rest API to retreieve configuration in a much nicer format.

# Design

Basically, we want to feature represent the objects that DataPower uses for configuration. It looks like the rest management API's json are very similar to the SOMA XML format (identical?) - so let's use yaml that corresponds to that rest API's json format.

# Folder Layout

```
/builds - Sample repositories of *input* configuration; expanded on greatly below - this is what users change
/docs - Documentation
/dp_gitops - All python code
/object-defaults - Defaults value for objects (the values used when custom data is not supplied by the user)
/sample-data - REST Mgmt API examples of objects, can generally be ignored
/soapui - Various SOAPUI tests for SOMA (SOAP Mgmt) interface
/test-data - Test configuration for docker environments
/tests - Tests for the python code
```

# Builds

A build is a datapower deployment, containing:
```
/repository - The input YAMLs the specify the MPGW, cert, WSP, and so on configuration. Generally, one file per datapower object.
/environment/X - The environment-specific values to use when building the datapower objects. For instance, a development server might have a lower rate-limit (SLM) than a production server. X would be development, production and so on - whatever name the user chooses.
/output/X - Where the generated auto-startup.cfg is written, if applicable.
```

How to generate a build?

# TODO

* Write some utilities to call the REST API to pull JSON back and represent in YAML, to save effort doing it by hand.
* Write a flow that takes all YAML objects and produces the full auto-startup.cfg file.
* Write some python to generate REST/SOMA for pushing objects.
* Move defaults to a folder to users can edit them
* Make requirements.txt

# Requirements

* Python 3.6+
* pyyaml
* jinja2

# Contact

chrishare @ gmail dt com

# License

MIT license.

# Warranty

Absolutely none. I am writing this for personal use and strive to make it safe, secure and correct, but you take the responsiblility of testing and validating that.



