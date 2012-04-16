#
# experiment.py
# Author: David Meisner (davidmax@gmail.com)
#

class Experiment:

  def __init__(self,
               name,
               setup_method,
               experiment_body_method,
               teardown_method):

    # Name the experiment.
    self.name = name

    # The method to setup the experiment.
    self.setup_method = setup_method

    # The actual experiment.
    self.experiment_body_method = experiment_body_method

    # The method to teardown the experiment.
    self.teardown_method = teardown_method

  def Run(self):

    self.setup_method()

    # Record the user who ran the experiment.
    # TODO(davidmax@gmail.com) determine how to do this.
    self.user = ''

    # Mark when we performed the experiment.
    self.start_time_epoch = ''

    start_time = time.time()

    self.experiment_body_method()

    end_time = time.time()
    # Mark the experiment duration.
    self.duration = end_time - start_time

    self.teardown_method()
