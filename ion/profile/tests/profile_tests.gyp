#
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
{
  'includes': [
    '../../common.gypi',
  ],

  'targets': [
    {
      'target_name': 'ionprofile_test',
      'includes': [ '../../dev/test_target.gypi' ],
      'sources' : [
        'calltracemanager_test.cc',
        'timelinesearch_test.cc',
        'timeline_test.cc',
      ],
      'dependencies' : [
        '<(ion_dir)/profile/profile.gyp:ionprofile',
        '<(ion_dir)/port/port.gyp:ionport',
        '<(ion_dir)/external/gtest.gyp:iongtest_vanilla',
        '<(ion_dir)/gfxprofile/gfxprofile.gyp:iongfxprofile',  # for gpuprofiler
        '<(ion_dir)/gfx/gfx.gyp:iongfx_for_tests',  # for mockgraphics
      ],
    },
  ],
}
