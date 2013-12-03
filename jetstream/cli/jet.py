"""Command-line interface to the Jetstream framework.

Usage:
  jet list [--config FILE] [--log LEVEL]
  jet run <pipename> [--config FILE] [--log LEVEL]
  jet (-h | --help)
  jet --version

Options:
  -h --help        Show this screen.
  --version        Show version.
  --config FILE    Use a given config file.
  --log LEVEL      Set log level (DEBUG|INFO|WARN|ERROR)

"""

import os, sys, logging
from docopt import docopt
from jetstream.config import from_yaml, MappingConfig
from jetstream.core import Streamer

logging.basicConfig()
logger = logging.getLogger("cli")

def main():

   # handle cmd-line arguments
   args = docopt(__doc__, version='Jetstreamer cli 1.0')

   # parse configuration
   cfgpth = args["--config"] or os.getcwd() + os.sep + "config.yaml"
   cfg = from_yaml(cfgpth)

   # handle commands
   if args["--log"]:
      print("setting log level to %s" % args["--log"])
      logger.setLevel(getattr(logging, args["--log"]))

   if args["list"]:
      names = MappingConfig(cfg).pipes.keys()
      print("Configured pipes: '" + "', '".join(names) + "'")
      sys.exit()

   if args["run"] and args["<pipename>"]:
      s = Streamer(args["<pipename>"], cfg)
      for record in s:
         print(record)

if __name__=="__main__":
   main()

