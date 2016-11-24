'''
   Copyright 2015 University of Auckland

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
from opencmiss.neon.ui.simulations.base import BaseSimulationView
from opencmiss.neon.core.simulations.ventilation import Ventilation as VentilationSimulation
from opencmiss.neon.ui.misc.utils import set_wait_cursor

from opencmiss.neon.ui.simulations.ui_ventilationwidget import Ui_VentilationWidget

try:
    from Queue import Empty
except ImportError:
    from queue import Empty  # python 3.x


class Ventilation(BaseSimulationView):

    def __init__(self, shared_gl_widget, parent=None):
        super(Ventilation, self).__init__(parent)
        self._ui = Ui_VentilationWidget()
        self._ui.setupUi(self)

        self._simulation = VentilationSimulation()

    def setup(self):
        parameters = {}
        parameters['name'] = self._problem.getName()
        parameters['general'] = self._problem.getGeneralSettings()
        parameters['script'] = self._problem.getScript()
        parameters['file_input_outputs'] = self._problem.getFileInputOutputs()
        parameters['main_parameters'] = self._problem.getMainParameters()
        parameters['flow_parameters'] = self._problem.getFlowParameters()

        self._simulation.setParameters(parameters)
        self._simulation.setup()
        self._ui.plainTextEdit.clear()

    @set_wait_cursor
    def execute(self):
        self._ui.plainTextEdit.clear()
        p, q = self._simulation.execute()
        while p.is_alive():
            try:
                data = q.get_nowait()
                self._ui.plainTextEdit.appendPlainText(data)
            except Empty:
                pass
# /                print('exception!!!!!')
        # s, r = self._simulation.execute()
        # self._ui.plainTextEdit.setPlainText(s.getvalue())
        # self._ui.plainTextEdit.appendPlainText(r.getvalue())

    def cleanup(self):
        self._ui.plainTextEdit.appendPlainText('')
        filenames = self._simulation.getOutputFilenames()
        for key in filenames:
            if filenames[key]:
                self._ui.plainTextEdit.appendPlainText('Output written to: "{0}"'.format(filenames[key]))
        self._simulation.cleanup()
