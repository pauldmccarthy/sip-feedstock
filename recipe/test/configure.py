import os
import sipconfig

# The name of the SIP build file generated by SIP and used by the build
# system.
build_file = "word.sbf"

# Get the SIP configuration information.
config = sipconfig.Configuration()

# Run SIP to generate the code.  Note that we tell SIP where to find the qt
# module's specification files using the -I flag.
os.system(" ".join([config.sip_bin, "-c", ".", "-b", build_file,
                    "word.sip"]))

# Create the Makefile.
makefile = sipconfig.SIPModuleMakefile(config, build_file)

# Generate the Makefile itself.
makefile.generate()
