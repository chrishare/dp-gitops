# dp-gitops

GitOps configuration support for Datapower.

# What is this?

I am not really sure yet. What I want it to be in a set of utilities that can represent Datapower configuration (objects, files, cert) in YAML for gitops-style repeatable (headless) deployments, supporting docker and appliance deployment types. In a containerised environment, this would mean using datapower startup.cfg files with that text format, but that is not intuitive to use, which is where YAML + jinja2 comes in.

I don't think we need to go the other way at this time - no cfg format to YAML, since we can use the rest API to retreieve configuration in a much nicer format.

# Design

Basically, we want to feature represent the objects that DataPower uses for configuration. It looks like the rest management API's json are very similar to the SOMA XML format (identical?) - so let's use yaml that corresponds to that rest API's json format.

# Contact

chrishare @ gmail

# License

MIT license.

# Warranty

Absolutely none. I am writing this for personal use and strive to make it safe, secure and correct, but you take the responsiblility of testing and validating that.



