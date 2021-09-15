Downloaded from OTTVerse.com <https://ottverse.com/ffmpeg-builds> 


Configuration Settings 
====================== 
--disable-autodetect 
--enable-amf 
--enable-bzlib 
--enable-cuda 
--enable-cuvid 
--enable-d3d11va 
--enable-dxva2 
--enable-iconv 
--enable-lzma 
--enable-nvenc
--enable-zlib
--enable-sdl2
--enable-ffnvcodec
--enable-nvdec
--enable-cuda-llvm
--enable-libmp3lame
--enable-libopus
--enable-libvorbis
--enable-libvpx
--enable-libx264
--enable-libx265
--enable-libdav1d
--enable-libaom
--disable-debug
--enable-fontconfig
--enable-libass
--enable-libbluray
--enable-libfreetype
--enable-libmfx
--enable-libmysofa
--enable-libopencore-amrnb
--enable-libopencore-amrwb
--enable-libopenjpeg
--enable-libsnappy
--enable-libsoxr
--enable-libspeex
--enable-libtheora
--enable-libtwolame
--enable-libvidstab
--enable-libvo-amrwbenc
--enable-libwavpack
--enable-libwebp
--enable-libxml2
--enable-libzimg
--enable-libshine
--enable-gpl
--enable-avisynth
--enable-libxvid
--enable-libopenmpt
--enable-version3
--enable-libsrt
--enable-libgsm
--enable-libvmaf
--enable-libsvtav1
--enable-librtmp
--enable-mbedtls
--extra-cflags=-DLIBTWOLAME_STATIC
--extra-libs=-lstdc++
--extra-cflags=-DLIBXML_STATIC
--extra-libs=-liconv
--disable-w32threads



Revisions Used
==============
AMF 3ee61d7 Updated to the latest 1.4.21
aom 281cee2a2 Make SF mv_cost_upd_level more aggressive in speed 5
AviSynthPlus 5c050fdc Expr: fix recent; use c_str, not string
cargo-c 247f03c Consolidate the build information in a single struct
dav1d fe903da x86: Rewrite sgr8 SSSE3 asm
ffmpeg 65fdc0e589 lavc/qsvenc: pass the color properties to the SDK
ffnvcodec b641a19 Update headers from Video SDK 11.1
flac b358381a cpu.h: detect AVX/FMA intrinsics availability on clang
fontconfig e291fda Bump version to 2.13.94
freetype2 801cd842e * Version 2.11.0 released. ==========================
fribidi 5464c28 Bumped version to 1.0.10
harfbuzz 9f544e500 [test] Don’t skip subset tests early
libaacs c0d5c14 aacs: error out after gcrypt AES error.
libass 5733e1c ass_face_stream: don't leak first struct if second alloc fails
libavif 5fb03ad Skip YUV/RGB conversion tests except first image
libbdplus bd8c0dd configure.ac: use mingw as the case instead of mingw32
libbluray 311f0928 Bump version (1.3.0)
libmfx 0349e3b API 1.35
libmysofa fc9e9ac CMake: Install import library for shared build
librtmp f1b83c1 Fix race condition in the librtmp install target.
libsoxr 945b592 update NEWS, versions
libwebp c5bc3624 fuzzer/*: normalize src/ includes
libxml2 dea91c97 Fix buffering in xmlOutputBufferWrite
openmpt 44733ab3d [Mod] libopenmpt: Prepare for release.
opus 6b6035ae Remove an unused parameter
rav1e f6c841fe CI: Update to libaom to 3.1.2-dmo1
srt 1a85c02 [core] Annotating CUDT::m_pCryptoControl locking behavior (#2070)
SVT-AV1 44486d23 Static Analysis fixes (#1684)
vidstab 00e0841 Add GCC macros for byte order
vmaf 60b2469e add ci job to validate docker build
vpx f685d508d vp9 rc: Fills VP9_COMP zero at initialization
x264 ae03d92b Add support for Sony XAVC Class 300 and 480
zimg 8d85ae9 colorspace: merge SMPTE 240M and Rec.709 when display-referred







General Notice
===============
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.