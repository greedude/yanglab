#!/usr/bin/env python
# -*- coding: utf-8 -*-
publications = [
    {
        'title': u'Probablisitic Reasoning by Neurons',
        'authors': 'Yang T and Shadlen MN',
        'year': 2007,
        'vol': 447,
        'pages':'1075-80',
        'journal': "Nature",
    },
    {
        'title': u'The speed and accuracy of a simple perceptual decision: a mathematical primer, in Bayesian Brain: Probabilistic Approaches to Neural Coding',
        'authors': 'Shadlen MN, Hanks TD, Churchland AK, Kiani R, and Yang T',
        'year': 2006,
        'vol': 1,
        'journal': "MIT Press:Cambridge",
    },

    {
        'title': u'The effect of perceptual learning on neuronal responses in monkey visual area V4',
        'authors': 'Yang T and Maunsell JH',
        'year': 2004,
        'vol': 24,
        'pages': "1617-1626",
        'journal': "J. Neurosci",
    },
    {
        'title': u' Physiology correlates of perceptual learning in monkey V1 and V2',
        'authors': 'Ghose G, Yang T, and Maunsell JH ',
        'year': 2002,
        'vol': 87,
        'pages': 6,
        'journal': "J. Neurophysiol.",
    },
]


people = [
    {
        'name': u'Xu Chan',
        'photo': u'xuchan.jpg',
        'position': u'Assistant Investigator',
        'description': u'No',
    },
    {
        'name': u'Shu Mei-ying',
        'photo': u'smy.jpg',
        'position': u'Lab Manager',
        'description': u'No',
    },
    {
        'name': u'Kong Wei',
        'photo': u'kongwei.jpg',
        'position': u'Assistant Experimentalist',
        'description': u'No',
    },
    {
        'name': u'Liu Ying',
        'photo': u'liuying.jpg',
        'position': u'Engineer',
        'description': u'No',
    },
]
for person in people:
    person['last_name'] = person['name'].split()[-1]
