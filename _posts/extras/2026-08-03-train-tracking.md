---
layout: post
categories: extra
title: "Train Video Control"
subtitle: "Model Train-Based Video Playback Control"
title_repeat: 5
comment: "Python, OpenCV, Chrome Extension"
date: 2026-08-03
thumbnail: /assets/img/train-tracking/vertical-view.webp
---

<img src="/assets/img/train-tracking/side-view.webp" class="w-full h-auto mx-auto">

<video autoplay loop muted playsinline preload="metadata" class="w-full sm:w-1/2 h-auto mx-auto">
  <source src="/assets/img/train-tracking/main-video.mp4" type="video/mp4">
</video>

# Motivation
A favourite pasttime of mine, especially when having a meal at home, is to watch 30-60 minute “train front cab view” videos on YouTube. Having once dreamt of driving a train myself, it’s quite entertaining and even calming (same effect as ASMR?) to watch a real driver’s point of view.

<iframe class="w-full aspect-[16/9] mx-auto" src="https://www.youtube.com/embed/HYrfuvxnc_8?si=OT4EpfrLxmYxePt3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

However, videos by nature are rather passively-consumed; not to mention the “action” only happening on-screen. Then, what if we want to emulate a true train driving experience alongside a real-life, physical representation? This project uses a motorised model train set and camera-based visual tracking to control the playback of videos.

# Technical Setup
<img src="/assets/img/train-tracking/apparatus.webp" class="w-full h-auto mx-auto">

The model train and track set are made by KATO, a Japanese model manufacturer. Tracks and locomotives are powered via an approx. 0-15V DC power source, with voltage controlled by a physical controller (blue).

<img src="/assets/img/train-tracking/webcam.webp" class="w-full h-auto mx-auto">

The track is laid out in an oval shape, with the train looping around continuously. A red sticker is attached to one of the train cars, which is monitored by a 1080P webcam from a tripod.

<img src="/assets/img/train-tracking/setup.webp" class="w-full h-auto mx-auto">

<video autoplay loop muted playsinline preload="metadata" class="w-full h-auto mx-auto">
  <source src="/assets/img/train-tracking/tracking-demo.mp4" type="video/mp4">
</video>

The computer runs a simple colour blob tracker in Python and OpenCV, and measures the absolute velocity/speed of the red sticker (train). This scalar speed value is sent via WebSockets to a local Chrome Extension, which controls the playback speed of any on-screen video.

<img src="/assets/img/train-tracking/1euro.webp" class="w-full h-auto mx-auto">

Because raw (X, Y) coordinates are noisy, a [1 Euro Filter](https://gery.casiez.net/1euro/) is applied to the input signal, which applies more smoothing at slower speeds (where the signal-to-noise ratio is lower) and less at higher speeds (where reducing lag is more important). Interactive demo, courtesy of Jonathan Aceituno: https://gery.casiez.net/1euro/InteractiveDemo/

# Acknowledgements
Many thanks to 이랑, 정호, 환준 for organising the workshop, and to all participants who showed off some seriously cool projects :)

<img src="/assets/img/train-tracking/vertical-view.webp" class="w-full sm:w-1/2 -auto mx-auto">