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
import json
from opencmiss.neon.core.visualisations.base import BaseVisualisation


class Ventilation(BaseVisualisation):

    def __init__(self):
        super(Ventilation, self).__init__()
        self.setName('Ventilation Visualisation')

    def visualise(self, document):
        filenames = self._simulation.getOutputFilenames()
        if self._simulation.isSmallTree():
            visualisation_description = small_default_visualisation
        elif self._simulation.isLargeTree():
            visualisation_description = large_default_visualisation
        else:
            visualisation_description = default_visualisation
        visualisation_description['RootRegion']['Model']['Sources'][0]['FileName'] = filenames['tree_exnode']
        visualisation_description['RootRegion']['Model']['Sources'][1]['FileName'] = filenames['tree_exelem']
        visualisation_description['RootRegion']['Model']['Sources'][2]['FileName'] = filenames['terminal_exnode']
        visualisation_description['RootRegion']['Model']['Sources'][3]['FileName'] = filenames['radius_exelem']
#         visualisation_description['RootRegion']['Model']['Sources'][4]['FileName'] = filenames['ventilation_exelem']
        document.deserialize(json.dumps(visualisation_description))


default_visualisation = large_default_visualisation = {
  "OpenCMISS-Neon Version": [
    0,
    2,
    0
  ],
  "RootRegion": {
    "Fieldmodule": {
      "Fields": [
        {
          "CoordinateSystemType": "RECTANGULAR_CARTESIAN",
          "FieldFiniteElement": {
            "ComponentNames": [
              "1"
            ],
            "NumberOfComponents": 1
          },
          "IsManaged": True,
          "IsTypeCoordinate": False,
          "Name": "compliance"
        },
        {
          "CoordinateSystemType": "RECTANGULAR_CARTESIAN",
          "FieldFiniteElement": {
            "ComponentNames": [
              "x",
              "y",
              "z"
            ],
            "NumberOfComponents": 3
          },
          "IsManaged": True,
          "IsTypeCoordinate": True,
          "Name": "coordinates"
        },
        {
          "CoordinateSystemType": "RECTANGULAR_CARTESIAN",
          "FieldFiniteElement": {
            "ComponentNames": [
              "1"
            ],
            "NumberOfComponents": 1
          },
          "IsManaged": True,
          "IsTypeCoordinate": False,
          "Name": "flow"
        },
        {
          "CoordinateSystemType": "RECTANGULAR_CARTESIAN",
          "FieldFiniteElement": {
            "ComponentNames": [
              "1"
            ],
            "NumberOfComponents": 1
          },
          "IsManaged": True,
          "IsTypeCoordinate": False,
          "Name": "pleural pressure"
        },
        {
          "CoordinateSystemType": "RECTANGULAR_CARTESIAN",
          "FieldFiniteElement": {
            "ComponentNames": [
              "radius"
            ],
            "NumberOfComponents": 1
          },
          "IsManaged": True,
          "IsTypeCoordinate": False,
          "Name": "radius"
        },
        {
          "CoordinateSystemType": "RECTANGULAR_CARTESIAN",
          "FieldFiniteElement": {
            "ComponentNames": [
              "1"
            ],
            "NumberOfComponents": 1
          },
          "IsManaged": True,
          "IsTypeCoordinate": False,
          "Name": "tidal volume"
        }
      ]
    },
    "Model": {
      "Sources": [
        {
          "FileName": "replace-me",
          "Type": "FILE"
        },
        {
          "FileName": "replace-me",
          "Type": "FILE"
        },
        {
          "FileName": "replace-me",
          "Type": "FILE"
        },
        {
          "FileName": "replace-me",
          "Type": "FILE"
        }
      ]
    },
    "Scene": {
      "Graphics": [
        {
          "CoordinateField": "coordinates",
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "MESH1D",
          "LineAttributes": {
            "BaseSize": [
              0,
              0
            ],
            "OrientationScaleField": "radius",
            "ScaleFactors": [
              2,
              2
            ],
            "ShapeType": "CIRCLE_EXTRUSION"
          },
          "Lines": {},
          "Material": "gold",
          "RenderLineWidth": 1,
          "RenderPointSize": 1,
          "RenderPolygonMode": "RENDER_POLYGON_SHADED",
          "Scenecoordinatesystem": "LOCAL",
          "SelectMode": "ON",
          "SelectedMaterial": "default_selected",
          "Tessellation": "default",
          "Type": "LINES",
          "VisibilityFlag": True
        },
        {
          "CoordinateField": "coordinates",
          "DataField": "pleural pressure",
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "NODES",
          "Material": "default",
          "PointAttributes": {
            "BaseSize": [
              4,
              4,
              4
            ],
            "Font": "default",
            "Glyph": "sphere",
            "GlyphOffset": [
              0,
              0,
              0
            ],
            "GlyphRepeatMode": "NONE",
            "GlyphShapeType": "SPHERE",
            "LabelOffset": [
              0,
              0,
              0
            ],
            "LabelText": [
              "",
              "",
              ""
            ],
            "ScaleFactors": [
              1,
              1,
              1
            ]
          },
          "Points": {},
          "RenderLineWidth": 1,
          "RenderPointSize": 1,
          "RenderPolygonMode": "RENDER_POLYGON_SHADED",
          "SamplingAttributes": {
            "ElementPointSamplingMode": "CELL_CENTRES",
            "Location": [
              0,
              0,
              0
            ]
          },
          "Scenecoordinatesystem": "LOCAL",
          "SelectMode": "ON",
          "SelectedMaterial": "default_selected",
          "Spectrum": "default",
          "Tessellation": "default_points",
          "Type": "POINTS",
          "VisibilityFlag": True
        },
        {
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "POINT",
          "Material": "default",
          "PointAttributes": {
            "BaseSize": [
              1,
              1,
              0.01
            ],
            "Font": "default",
            "Glyph": "colour_bar_default",
            "GlyphOffset": [
              0,
              0,
              0
            ],
            "GlyphRepeatMode": "NONE",
            "GlyphShapeType": "",
            "LabelOffset": [
              0,
              0,
              0
            ],
            "LabelText": [
              "",
              "",
              ""
            ],
            "ScaleFactors": [
              1,
              1,
              1
            ]
          },
          "Points": {},
          "RenderLineWidth": 1,
          "RenderPointSize": 1,
          "RenderPolygonMode": "RENDER_POLYGON_SHADED",
          "SamplingAttributes": {
            "ElementPointSamplingMode": "CELL_CENTRES",
            "Location": [
              0,
              0,
              0
            ]
          },
          "Scenecoordinatesystem": "NORMALISED_WINDOW_FIT_LEFT",
          "SelectMode": "ON",
          "SelectedMaterial": "default_selected",
          "Tessellation": "default_points",
          "Type": "POINTS",
          "VisibilityFlag": True
        }
      ],
      "VisibilityFlag": True
    }
  },
  "Sceneviewer": {
    "AntialiasSampling": 0,
    "BackgroundColourRGB": [
      1,
      1,
      1
    ],
    "EyePosition": [
      -320.2511086707393,
      603.2813213721496,
      140.5792138816753
    ],
    "FarClippingPlane": 1602.446914946288,
    "LightingLocalViewer": False,
    "LightingTwoSided": True,
    "LookatPosition": [
      -201.4316695298645,
      -122.7497078428728,
      -146.1533948135313
    ],
    "NearClippingPlane": 39.47957393987889,
    "PerturbLinesFlag": False,
    "ProjectionMode": "PERSPECTIVE",
    "Scene": "/",
    "Scenefilter": "default",
    "TranslationRate": 1,
    "TransparencyMode": "FAST",
    "TumbleRate": 1.5,
    "UpVector": [
      0.06663590038776854,
      -0.3570539488230509,
      0.9317038877290332
    ],
    "ViewAngle": 0.6981317007976333,
    "ZoomRate": 1
  },
  "Spectrums": {
    "DefaultSpectrum": "default",
    "Spectrums": [
      {
        "Components": [
          {
            "Active": True,
            "BandedRatio": 0.2,
            "ColourMappingType": "RAINBOW",
            "ColourMaximum": 1,
            "ColourMinimum": 0,
            "ColourReverse": True,
            "Exaggeration": 1,
            "ExtendAbove": True,
            "ExtendBelow": True,
            "FieldComponent": 1,
            "FixMaximum": False,
            "FixMinimum": False,
            "NumberOfBands": 10,
            "RangeMaximum": 483.9606628417969,
            "RangeMinimum": 478.563232421875,
            "ScaleType": "LINEAR",
            "StepValue": 481.2619476318359
          }
        ],
        "MaterialOverwrite": True,
        "Name": "default"
      }
    ]
  },
  "Tessellations": {
    "DefaultPointsTessellation": "default_points",
    "DefaultTessellation": "default",
    "Tessellations": [
      {
        "CircleDivisions": 12,
        "MinimumDivisions": [
          1
        ],
        "Name": "default",
        "RefinementFactors": [
          4
        ]
      },
      {
        "CircleDivisions": 12,
        "MinimumDivisions": [
          1
        ],
        "Name": "default_points",
        "RefinementFactors": [
          1
        ]
      }
    ]
  }
}


small_default_visualisation = {
  "OpenCMISS-Neon Version": [
    0,
    2,
    0
  ],
  "RootRegion": {
    "Fieldmodule": {
      "Fields": [
        {
          "CoordinateSystemType": "RECTANGULAR_CARTESIAN",
          "FieldFiniteElement": {
            "ComponentNames": [
              "1"
            ],
            "NumberOfComponents": 1
          },
          "IsManaged": True,
          "IsTypeCoordinate": False,
          "Name": "compliance"
        },
        {
          "CoordinateSystemType": "RECTANGULAR_CARTESIAN",
          "FieldFiniteElement": {
            "ComponentNames": [
              "x",
              "y",
              "z"
            ],
            "NumberOfComponents": 3
          },
          "IsManaged": True,
          "IsTypeCoordinate": True,
          "Name": "coordinates"
        },
        {
          "CoordinateSystemType": "RECTANGULAR_CARTESIAN",
          "FieldFiniteElement": {
            "ComponentNames": [
              "1"
            ],
            "NumberOfComponents": 1
          },
          "IsManaged": True,
          "IsTypeCoordinate": False,
          "Name": "flow"
        },
        {
          "CoordinateSystemType": "RECTANGULAR_CARTESIAN",
          "FieldFiniteElement": {
            "ComponentNames": [
              "1"
            ],
            "NumberOfComponents": 1
          },
          "IsManaged": True,
          "IsTypeCoordinate": False,
          "Name": "pleural pressure"
        },
        {
          "CoordinateSystemType": "RECTANGULAR_CARTESIAN",
          "FieldFiniteElement": {
            "ComponentNames": [
              "radius"
            ],
            "NumberOfComponents": 1
          },
          "IsManaged": True,
          "IsTypeCoordinate": False,
          "Name": "radius"
        },
        {
          "CoordinateSystemType": "RECTANGULAR_CARTESIAN",
          "FieldFiniteElement": {
            "ComponentNames": [
              "1"
            ],
            "NumberOfComponents": 1
          },
          "IsManaged": True,
          "IsTypeCoordinate": False,
          "Name": "tidal volume"
        }
      ]
    },
    "Model": {
      "Sources": [
        {
          "FileName": "replace-me",
          "Type": "FILE"
        },
        {
          "FileName": "replace-me",
          "Type": "FILE"
        },
        {
          "FileName": "replace-me",
          "Type": "FILE"
        },
        {
          "FileName": "replace-me",
          "Type": "FILE"
        }
      ]
    },
    "Scene": {
      "Graphics": [
        {
          "CoordinateField": "coordinates",
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "MESH1D",
          "LineAttributes": {
            "BaseSize": [
              0,
              0
            ],
            "OrientationScaleField": "radius",
            "ScaleFactors": [
              2,
              2
            ],
            "ShapeType": "CIRCLE_EXTRUSION"
          },
          "Lines": {},
          "Material": "gold",
          "RenderLineWidth": 1,
          "RenderPointSize": 1,
          "RenderPolygonMode": "RENDER_POLYGON_SHADED",
          "Scenecoordinatesystem": "LOCAL",
          "SelectMode": "ON",
          "SelectedMaterial": "default_selected",
          "Tessellation": "default",
          "Type": "LINES",
          "VisibilityFlag": True
        },
        {
          "CoordinateField": "coordinates",
          "DataField": "pleural pressure",
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "NODES",
          "Material": "default",
          "PointAttributes": {
            "BaseSize": [
              4,
              4,
              4
            ],
            "Font": "default",
            "Glyph": "sphere",
            "GlyphOffset": [
              0,
              0,
              0
            ],
            "GlyphRepeatMode": "NONE",
            "GlyphShapeType": "SPHERE",
            "LabelOffset": [
              0,
              0,
              0
            ],
            "LabelText": [
              "",
              "",
              ""
            ],
            "ScaleFactors": [
              1,
              1,
              1
            ]
          },
          "Points": {},
          "RenderLineWidth": 1,
          "RenderPointSize": 1,
          "RenderPolygonMode": "RENDER_POLYGON_SHADED",
          "SamplingAttributes": {
            "ElementPointSamplingMode": "CELL_CENTRES",
            "Location": [
              0,
              0,
              0
            ]
          },
          "Scenecoordinatesystem": "LOCAL",
          "SelectMode": "ON",
          "SelectedMaterial": "default_selected",
          "Spectrum": "default",
          "Tessellation": "default_points",
          "Type": "POINTS",
          "VisibilityFlag": True
        },
        {
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "POINT",
          "Material": "default",
          "PointAttributes": {
            "BaseSize": [
              1,
              1,
              0.01
            ],
            "Font": "default",
            "Glyph": "colour_bar_default",
            "GlyphOffset": [
              0,
              0,
              0
            ],
            "GlyphRepeatMode": "NONE",
            "GlyphShapeType": "",
            "LabelOffset": [
              0,
              0,
              0
            ],
            "LabelText": [
              "",
              "",
              ""
            ],
            "ScaleFactors": [
              1,
              1,
              1
            ]
          },
          "Points": {},
          "RenderLineWidth": 1,
          "RenderPointSize": 1,
          "RenderPolygonMode": "RENDER_POLYGON_SHADED",
          "SamplingAttributes": {
            "ElementPointSamplingMode": "CELL_CENTRES",
            "Location": [
              0,
              0,
              0
            ]
          },
          "Scenecoordinatesystem": "NORMALISED_WINDOW_FIT_LEFT",
          "SelectMode": "ON",
          "SelectedMaterial": "default_selected",
          "Tessellation": "default_points",
          "Type": "POINTS",
          "VisibilityFlag": True
        }
      ],
      "VisibilityFlag": True
    }
  },
  "Sceneviewer": {
    "AntialiasSampling": 0,
    "BackgroundColourRGB": [
      1,
      1,
      1
    ],
    "EyePosition": [
      104.8488853572321,
      592.4708896092361,
      -2.011795167724713
    ],
    "FarClippingPlane": 1602.446914946288,
    "LightingLocalViewer": False,
    "LightingTwoSided": True,
    "LookatPosition": [
      -181.7114524841309,
      -139.5188026428223,
      -76.36881637573242
    ],
    "NearClippingPlane": 39.47957393987889,
    "PerturbLinesFlag": False,
    "ProjectionMode": "PERSPECTIVE",
    "Scene": "/",
    "Scenefilter": "default",
    "TranslationRate": 1,
    "TransparencyMode": "FAST",
    "TumbleRate": 1.5,
    "UpVector": [
      -0.09268895456789202,
      -0.06464536129209958,
      0.9935943513147554
    ],
    "ViewAngle": 0.6981317007976272,
    "ZoomRate": 1
  },
  "Spectrums": {
    "DefaultSpectrum": "default",
    "Spectrums": [
      {
        "Components": [
          {
            "Active": True,
            "BandedRatio": 0.2,
            "ColourMappingType": "RAINBOW",
            "ColourMaximum": 1,
            "ColourMinimum": 0,
            "ColourReverse": True,
            "Exaggeration": 1,
            "ExtendAbove": True,
            "ExtendBelow": True,
            "FieldComponent": 1,
            "FixMaximum": False,
            "FixMinimum": False,
            "NumberOfBands": 10,
            "RangeMaximum": 621.7030639648438,
            "RangeMinimum": 408.9003601074219,
            "ScaleType": "LINEAR",
            "StepValue": 515.3017120361328
          }
        ],
        "MaterialOverwrite": True,
        "Name": "default"
      }
    ]
  },
  "Tessellations": {
    "DefaultPointsTessellation": "default_points",
    "DefaultTessellation": "default",
    "Tessellations": [
      {
        "CircleDivisions": 12,
        "MinimumDivisions": [
          1
        ],
        "Name": "default",
        "RefinementFactors": [
          4
        ]
      },
      {
        "CircleDivisions": 12,
        "MinimumDivisions": [
          1
        ],
        "Name": "default_points",
        "RefinementFactors": [
          1
        ]
      }
    ]
  }
}