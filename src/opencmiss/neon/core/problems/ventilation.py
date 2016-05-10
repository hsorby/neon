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
import sys
import json

from opencmiss.neon.core.problems.base import BaseProblem


def getExecutableForPlatform():
    return 'ventilation-' + sys.platform


class Ventilation(BaseProblem):

    def __init__(self):
        super(Ventilation, self).__init__()
        self.setName('Ventilation')
        # self.setInBuiltExecutable(getExecutableForPlatform())

        self._general_settings = self._defineDefaultGeneralSettings()
        self._script = self._defineDefaultScript()
        self._file_input_outputs = self._defineDefaultFileInputOutputs()
        self._main_parameters = self._defineDefaultMainParameters()
        self._flow_parameters = self._defineDefaultFlowParameters()

    def _defineDefaultGeneralSettings(self):
        d = {}
        d['advanced'] = False
        d['active_geometry'] = 'small_tree'

        return d

    def _defineDefaultScript(self):
        # d = {}
        d = 'from aether.diagnostics import set_diagnostics_on\n' \
            'from aether.indices import ventilation_indices\n' \
            '\n' \
            'set_diagnostics_on(True)\n' \
            '# define an airway tree geometry\n' \
            'ventilation_indices()\n' \
            '\n'

        return d

    def _defineDefaultMainParameters(self):
        d = {}
        d['num_brths'] = 5
        d['num_itns'] = 200
        d['dt'] = 0.05
        d['err_tol'] = 1e-10

        return d

    def _defineDefaultFlowParameters(self):
        d = {}
        d['FRC'] = 3.035
        d['constrict'] = 1.00000E+00
        d['T_interval'] = 4.00000E+00
        d['Gdirn'] = 3
        d['press_in'] = 0.00000E+00
        d['COV'] = 0.00000E+00
        d['RMaxMean'] = 1.0000E+00
        d['RMinMean'] = 1.0000E+00
        d['i_to_e_ratio'] = 1.0000E+00
        d['refvol'] = 0.50000E+00
        d['volume_target'] = 1.00000E+06
        d['pmus_step'] = -196.133
        d['expiration_type'] = 'active'
        d['chest_wall_compliance'] = 2039.4324E+00

        return d

    def _defineDefaultFileInputOutputs(self):
        d = {}
        d['tree_inbuilt'] = True
        d['tree_ipelem'] = ''
        d['tree_ipnode'] = ''
        d['tree_ipfield'] = ''
        d['tree_ipmesh'] = ''

        d['flow_inbuilt'] = True
        d['flow_exelem'] = ''

        d['terminal_exnode'] = ''
        d['tree_exnode'] = ''
        d['tree_exelem'] = ''
        d['ventilation_exelem'] = ''
        d['radius_exelem'] = ''

        return d

    def getGeneralSettings(self):
        return self._general_settings

    def getScript(self):
        return self._script

    def getFileInputOutputs(self):
        return self._file_input_outputs

    def getMainParameters(self):
        return self._main_parameters

    def getFlowParameters(self):
        return self._flow_parameters

    def updateGeneralSettings(self, parameters):
        self._general_settings.update(parameters)

    def updateScript(self, parameters):
        self._script = parameters

    def updateMainParameters(self, parameters):
        self._main_parameters.update(parameters)

    def updateFlowParameters(self, parameters):
        self._flow_parameters.update(parameters)

    def updateFileInputOutputs(self, values):
        self._file_input_outputs.update(values)

    def serialize(self):
        d = {}
        # d['executable_inbuilt'] = self.isInBuiltExecutable()
        d['general'] = self._general_settings
        d['script'] = self._script
        # d['executable'] = self.getExecutable() if not self.isInBuiltExecutable() else ''
        d['file_input_outputs'] = self._file_input_outputs
        d['main_parameters'] = self._main_parameters
        d['flow_parameters'] = self._flow_parameters

        return json.dumps(d)

    def deserialize(self, string):
        d = json.loads(string)
        # executable_inbuilt = d['executable_inbuilt'] if 'executable_inbuilt' in d else True
        # if executable_inbuilt:
        #     self.setInBuiltExecutable(getExecutableForPlatform())
        # else:
        #     self.setExecutable(d['executable'] if 'executable' in d else '')

        self._general_settings = d['general'] if 'general' in d else self._defineDefaultGeneralSettings()
        self._script = d['script'] if 'script' in d else self._defineDefaultScript()
        self._file_input_outputs = d['file_input_outputs'] if 'file_input_outputs' in d else self._defineDefaultFileInputOutputs()
        self._main_parameters = d['main_parameters'] if 'main_parameters' in d else self._defineDefaultMainParameters()
        self._flow_parameters = d['flow_parameters'] if 'flow_parameters' in d else self._defineDefaultFlowParameters()

    def validate(self):
        return True
