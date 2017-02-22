'''n
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


class Biomeng321Lab1(BaseVisualisation):

    def __init__(self):
        super(Biomeng321Lab1, self).__init__()
        self.setName('Bioemeng 321 Lab1 Visualisation')

    def visualise(self, document):
        node_filename = self._simulation.getNodeFilename()
        element_filename = self._simulation.getElementFilename()
        visualisation_description = default_visualisation
        visualisation_description['RootRegion']['Model']['Sources'][0]['FileName'] = node_filename
        visualisation_description['RootRegion']['Model']['Sources'][1]['FileName'] = element_filename
        state = json.dumps(visualisation_description)
        document.deserialize(state)

default_visualisation = {
  "OpenCMISS-Neon Version": [
    0,
    2,
    0
  ],
  "Project": "{\"identifier\": \"Biomeng321Lab1\", \"problem\": \"{\\\"boundary_condition\\\": \\\"Model 1 (Uniaxial extension of unit cube)\\\"}\"}",
  "RootRegion": {
    "Model": {
      "Sources": [
        {
          "FileName": "AppData\\Local\\Temp\\biomeng321_lab1_a5cop30h.exnode",
          "Type": "FILE"
        },
        {
          "FileName": "AppData\\Local\\Temp\\biomeng321_lab1_a5cop30h.exelem",
          "Type": "FILE"
        }
      ]
    },
    "Scene": {
      "Graphics": [
        {
          "CoordinateField": "DeformedGeometry",
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "MESH1D",
          "LineAttributes": {
            "BaseSize": [
              0.04,
              0.04
            ],
            "ScaleFactors": [
              1,
              1
            ],
            "ShapeType": "CIRCLE_EXTRUSION"
          },
          "Lines": {},
          "Material": "green",
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
          "CoordinateField": "Geometry",
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "MESH1D",
          "LineAttributes": {
            "BaseSize": [
              0.02,
              0.02
            ],
            "ScaleFactors": [
              1,
              1
            ],
            "ShapeType": "CIRCLE_EXTRUSION"
          },
          "Lines": {},
          "Material": "red",
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
          "CoordinateField": "DeformedGeometry",
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "NODES",
          "Material": "black",
          "PointAttributes": {
            "BaseSize": [
              1,
              1,
              1
            ],
            "Font": "default",
            "Glyph": "point",
            "GlyphOffset": [
              0,
              0,
              0
            ],
            "GlyphRepeatMode": "NONE",
            "GlyphShapeType": "POINT",
            "LabelField": "DeformedGeometry",
            "LabelOffset": [
              0.04,
              0.03,
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
          "Tessellation": "default_points",
          "Type": "POINTS",
          "VisibilityFlag": True
        },
        {
          "CoordinateField": "DeformedGeometry",
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "NODES",
          "Material": "green",
          "PointAttributes": {
            "BaseSize": [
              0.04,
              0.04,
              0.04
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
          "Tessellation": "default_points",
          "Type": "POINTS",
          "VisibilityFlag": True
        },
        {
          "CoordinateField": "Geometry",
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "NODES",
          "Material": "red",
          "PointAttributes": {
            "BaseSize": [
              0.02,
              0.02,
              0.02
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
          "Tessellation": "default_points",
          "Type": "POINTS",
          "VisibilityFlag": True
        },
        {
          "ElementFaceType": "ALL",
          "Exterior": False,
          "FieldDomainType": "POINT",
          "Material": "black",
          "PointAttributes": {
            "BaseSize": [
              1.8,
              1.8,
              1.8
            ],
            "Font": "default",
            "Glyph": "axes_x1x2x3",
            "GlyphOffset": [
              0,
              0,
              0
            ],
            "GlyphRepeatMode": "NONE",
            "GlyphShapeType": "AXES_X1X2X3",
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
      2.13100693234562,
      -3.931815426970709,
      2.377282853637422
    ],
    "FarClippingPlane": 9.97371765089012,
    "LightingLocalViewer": False,
    "LightingTwoSided": True,
    "LookatPosition": [
      0.7499999906867743,
      0.4949999954551458,
      0.7499999906867743
    ],
    "NearClippingPlane": 0.2457230375503514,
    "PerturbLinesFlag": False,
    "ProjectionMode": "PARALLEL",
    "Scene": "/",
    "Scenefilter": "default",
    "TranslationRate": 1,
    "TransparencyMode": "FAST",
    "TumbleRate": 1.5,
    "UpVector": [
      -0.1239893966355493,
      0.3080567702806175,
      0.9432537600276251
    ],
    "ViewAngle": 0.6981317007977098,
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
            "RangeMaximum": 1,
            "RangeMinimum": 0,
            "ScaleType": "LINEAR",
            "StepValue": 0.5
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
