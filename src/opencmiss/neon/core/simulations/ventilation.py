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
import shutil
import importlib
import os.path
from io import StringIO
# from subprocess import PIPE, Popen
from threading import Thread
from tempfile import NamedTemporaryFile, mkdtemp

from opencmiss.neon.core.simulations.local import LocalSimulation
from opencmiss.neon.core.serializers.identifiervalue import IdentifierValue
from opencmiss.neon.settings.mainsettings import EXTERNAL_DATA_DIR, PYTHON3
from multiprocessing import Process, Queue
from contextlib import contextmanager
# try:
#     from Queue import Queue
# except ImportError:
#     from queue import Queue  # python 3.x

ON_POSIX = 'posix' in sys.builtin_module_names


from StringIO import StringIO


class MyStringIO(StringIO):

    def __init__(self, queue, *args, **kwargs):
        StringIO.__init__(self, *args, **kwargs)
        self.queue = queue

    def write(self, s):





        self.queue.put(s)

    def flush(self):
        self.queue.put(self.getvalue())
        self.truncate(0)


def enqueue_output(out, queue):
    for line in iter(out.readline, b''):
        queue.put(line)
    out.close()


@contextmanager
def std_redirector(stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    tmp_fds = stdin, stdout, stderr
    orig_fds = sys.stdin, sys.stdout, sys.stderr
    sys.stdin, sys.stdout, sys.stderr = tmp_fds
    yield
    sys.stdin, sys.stdout, sys.stderr = orig_fds


class Ventilation(LocalSimulation):

    def __init__(self):
        super(Ventilation, self).__init__()
        self.setName('Ventilation Simulation')
        self.setSerializer(IdentifierValue())
        self._file_locations = {}
        self._dir_locations = {}
        self._output_filenames = {}
        self._initial_wd = None
        self._module = None

    def getOutputFilenames(self):
        return self._output_filenames

    def isSmallTree(self):
        return self._parameters['general']['active_geometry'] == 'small_tree'

    def isLargeTree(self):
        return self._parameters['general']['active_geometry'] == 'large_tree'

    def setup(self):
        general_settings = self._parameters['general']
        file_input_outputs = self._parameters['file_input_outputs']

        output_file_keys = ['terminal_exnode', 'tree_exnode', 'tree_exelem', 'ventilation_exelem', 'radius_exelem']
        output_filenames = {}

        for key in output_file_keys:
            filename = file_input_outputs[key]
            if filename:
                output_filenames[key] = filename
            else:
                out_file_handle = NamedTemporaryFile(prefix='ventilation_{0}_'.format(key), delete=False)
                output_filenames[key] = out_file_handle.name
                out_file_handle.close()

        terminal_file = output_filenames['terminal_exnode']

        self._dir_locations['root'] = mkdtemp(prefix='neon_')
        param_dir = os.path.join(self._dir_locations['root'], 'Parameters')
        self._dir_locations['para'] = param_dir
        os.mkdir(param_dir)

        geometry_flow = {}
        geometry_flow['exnode'] = "'{0}'".format(terminal_file)
        geometry_flow['flowexelem'] = "'{0}'".format(output_filenames['ventilation_exelem'])
        geometry_flow['flowradiusexelem'] = "'{0}'".format(output_filenames['radius_exelem'])
        self._file_locations['geo_main'] = os.path.join(self._dir_locations['para'], 'geometry_evaluate_flow.txt')
        with open(self._file_locations['geo_main'], 'w') as f:
            string = self._serializer.serialize(geometry_flow)
            f.write(string)

        self._output_filenames = output_filenames

        tree_geometry = general_settings['active_geometry']
        inbuilt_tree_ipelem = os.path.join(EXTERNAL_DATA_DIR, self._parameters['name'], 'Geom',
                                           '{0}.ipelem'.format(tree_geometry))
        tree_ipelem = inbuilt_tree_ipelem if file_input_outputs['tree_inbuilt'] or not \
            file_input_outputs['tree_ipelem'] else file_input_outputs['tree_ipelem']
        inbuilt_tree_ipnode = os.path.join(EXTERNAL_DATA_DIR, self._parameters['name'], 'Geom',
                                           '{0}.ipnode'.format(tree_geometry))
        tree_ipnode = inbuilt_tree_ipnode if file_input_outputs['tree_inbuilt'] or not \
            file_input_outputs['tree_ipnode'] else file_input_outputs['tree_ipnode']
        inbuilt_tree_ipfiel = os.path.join(EXTERNAL_DATA_DIR, self._parameters['name'], 'Geom',
                                           '{0}.ipfiel'.format(tree_geometry))
        tree_ipfiel = inbuilt_tree_ipfiel if file_input_outputs['tree_inbuilt'] or not \
            file_input_outputs['tree_ipfield'] else file_input_outputs['tree_ipfield']
        inbuilt_tree_ipmesh = os.path.join(EXTERNAL_DATA_DIR, self._parameters['name'], 'Geom',
                                           '{0}.ipmesh'.format(tree_geometry))
        tree_ipmesh = inbuilt_tree_ipmesh if file_input_outputs['tree_inbuilt'] or not \
            file_input_outputs['tree_ipmesh'] else file_input_outputs['tree_ipmesh']

        geometry_main = {}
        geometry_main['airway_ipelem'] = "'{0}'".format(tree_ipelem)
        geometry_main['airway_ipnode'] = "'{0}'".format(tree_ipnode)
        geometry_main['airway_ipfiel'] = "'{0}'".format(tree_ipfiel)
        geometry_main['airway_ipmesh'] = "'{0}'".format(tree_ipmesh)
        geometry_main['airway_exnode'] = "'{0}'".format(output_filenames['tree_exnode'])
        geometry_main['airway_exelem'] = "'{0}'".format(output_filenames['tree_exelem'])

        self._file_locations['geo_flow'] = os.path.join(self._dir_locations['para'], 'geometry_main.txt')
        with open(self._file_locations['geo_flow'], 'w') as f:
            string = self._serializer.serialize(geometry_main)
            f.write(string)

        self._file_locations['par_main'] = os.path.join(self._dir_locations['para'], 'params_main.txt')
        with open(self._file_locations['par_main'], 'w') as f:
            string = self._serializer.serialize(self._parameters['main_parameters'])
            f.write(string)

        self._file_locations['par_flow'] = os.path.join(self._dir_locations['para'], 'params_evaluate_flow.txt')
        with open(self._file_locations['par_flow'], 'w') as f:
            string = self._serializer.serialize(self._parameters['flow_parameters'])
            f.write(string)

        self._file_locations['script'] = os.path.join(self._dir_locations['root'], 'ventilation_script.py')
        with open(self._file_locations['script'], 'w') as f:
            f.write(self._parameters['script'])

        self._initial_wd = os.getcwd()

    def execute(self):
        script = self._file_locations['script']
        base_script = os.path.basename(script)
        module_name = os.path.splitext(base_script)[0]
        os.chdir(self._dir_locations['root'])
        if self._dir_locations['root'] not in sys.path:
            sys.path.append(self._dir_locations['root'])

        q = Queue()
        p = Process(target=simulate_ventilation, args=(module_name, q))
        p.start()

        # stdout = None
        # stderr = None
        # old = sys.stdout
        # olderr = sys.stderr
        # if stdout is None:
        #     stdout = StringIO()
        # if stderr is None:
        #     stderr = StringIO()
        # sys.stdout = stdout
        # sys.stderr = stderr
        # if hasattr(importlib, 'invalidate_caches'):
        #     importlib.invalidate_caches()
        # if self._module is None:
        #     self._module = importlib.import_module(module_name)
        # else:
        #     if hasattr(importlib, 'reload'):
        #         importlib.reload(self._module)
        #     else:
        #         reload(self._module)
        # sys.stdout = old
        # sys.stderr = olderr
        # s = stdout, stderr
        if self._dir_locations['root'] in sys.path:
            index = sys.path.index(self._dir_locations['root'])
            sys.path.pop(index)

        return p, q

    def cleanup(self):
        os.chdir(self._initial_wd)
        shutil.rmtree(self._dir_locations['root'])

    def validate(self):
        return True


def simulate_ventilation(module_name, q):
    print('something is happening')
    q.put('something in the queue')
    q.put('module name:' + module_name)
    if hasattr(importlib, 'invalidate_caches'):
        importlib.invalidate_caches()

    output = MyStringIO(q)
    with std_redirector(stdout=output, stderr=output):
        print('something is captured?????')
        importlib.import_module(module_name)
