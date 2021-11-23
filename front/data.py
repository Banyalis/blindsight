# -*- coding: utf-8 -*-

# Модуль с данными для быстрого начала разработки, пока модели и админка еще не созданы.

from django.contrib.staticfiles.storage import staticfiles_storage
from config.settings import STATIC_URL

header = {
    'menu': [
        {
            'title': 'Blindsight',
            'dataId': 'index'
        },
        {
            'title': 'Memories',
            'dataId': 'memories'
        },
        {
            'title': 'About',
            'dataId': 'about'
        }
    ]
}

index = {
    'backgroundVideo': staticfiles_storage.url('videos/home.mp4'),
    'backgroundVideoPoster': staticfiles_storage.url('img/index/videoPoster.jpg'),
    'backgroundImageDesktop': staticfiles_storage.url('img/index/backgroundDesktop.jpg'),
    'backgroundImageMobile': staticfiles_storage.url('img/index/backgroundMobile.jpg')
}

memories = {
    'backgroundVideo': staticfiles_storage.url('videos/about.mp4'),
    'backgroundVideoPoster': staticfiles_storage.url('img/memories/videoPoster.jpg'),
    'backgroundImageDesktop': staticfiles_storage.url('img/memories/backgroundDesktop.jpg'),
    'backgroundImageMobile': staticfiles_storage.url('img/memories/backgroundMobile.jpg'),
    'nav': [
        {
            'slug': '01',
            'title': 'Space Suit',
            'image': staticfiles_storage.url('img/memories/1.jpg'),
            'imageMobile': staticfiles_storage.url('img/memories/1m.jpg'),
            'video': staticfiles_storage.url('videos/memories/1.mp4')
        },
        {
            'slug': '02',
            'title': 'Rorschach',
            'image': staticfiles_storage.url('img/memories/2.jpg'),
            'imageMobile': staticfiles_storage.url('img/memories/2m.jpg'),
            'video': staticfiles_storage.url('videos/memories/2.mp4')
        },
        {
            'slug': '03',
            'title': 'Theseus',
            'image': staticfiles_storage.url('img/memories/3.jpg'),
            'imageMobile': staticfiles_storage.url('img/memories/3m.jpg'),
            'video': staticfiles_storage.url('videos/memories/3.mp4')
        },
        {
            'slug': '04',
            'title': 'Scramblers',
            'image': staticfiles_storage.url('img/memories/4.jpg'),
            'imageMobile': staticfiles_storage.url('img/memories/4m.jpg'),
            'video': staticfiles_storage.url('videos/memories/4.mp4')
        },
        {
            'slug': '05',
            'title': 'Interfaces',
            'image': staticfiles_storage.url('img/memories/5.jpg'),
            'imageMobile': staticfiles_storage.url('img/memories/5m.jpg'),
            'video': staticfiles_storage.url('videos/memories/5.mp4')
        },
        {
            'slug': '06',
            'title': 'Equipment',
            'image': staticfiles_storage.url('img/memories/6.jpg'),
            'imageMobile': staticfiles_storage.url('img/memories/6m.jpg'),
            'video': staticfiles_storage.url('videos/memories/6.mp4')
        },
        {
            'slug': '07',
            'title': 'Characters',
            'image': staticfiles_storage.url('img/memories/7.jpg'),
            'imageMobile': staticfiles_storage.url('img/memories/7m.jpg'),
            'video': staticfiles_storage.url('videos/memories/7.mp4')
        },
        {
            'slug': '08',
            'title': 'Soundtrack',
            'image': staticfiles_storage.url('img/memories/8.jpg'),
            'imageMobile': staticfiles_storage.url('img/memories/8m.jpg'),
            'video': staticfiles_storage.url('videos/memories/8.mp4')
        },
        {
            'slug': '09',
            'title': 'Debrief',
            'image': staticfiles_storage.url('img/memories/9.jpg'),
            'imageMobile': staticfiles_storage.url('img/memories/9m.jpg'),
            'video': staticfiles_storage.url('videos/memories/9.mp4')
        }
    ],
}

about = {
    'backgroundVideo': staticfiles_storage.url('videos/about.mp4'),
    'backgroundVideoPoster': staticfiles_storage.url('img/about/videoPoster.jpg'),
    'backgroundImageDesktop': staticfiles_storage.url('img/about/backgroundDesktop.jpg'),
    'backgroundImageMobile': staticfiles_storage.url('img/about/backgroundMobile.jpg'),
    'creditsList': [
        {
            'position': 'Directed by:',
            'creditsNames': [
                {
                    'url': 'http://www.myshli.com/',
                    'title': 'Danil Krivoruchko'
                }
            ]
        },
        {
            'position': 'Edited by:',
            'creditsNames': [
                {
                    'url': '#',
                    'title': 'Viktoriya Yakubova'
                }
            ]
        },
        {
            'position': 'Score / sound design:',
            'creditsNames': [
                {
                    'url': 'https://echoicaudio.com/',
                    'title': 'Echoic Audio'
                }
            ]
        },
        {
            'position': 'Art:',
            'creditsNames': [
                {
                    'url': 'https://www.behance.net/mrOmvod',
                    'title': 'Artem Otvodenkov'
                },
                {
                    'url': 'https://www.behance.net/hramovsky',
                    'title': 'Dennis Khramov'
                },
                {
                    'url': 'https://www.artstation.com/gr1n',
                    'title': 'Evgeny Kashin'
                },
                {
                    'url': 'https://www.artstation.com/hamen',
                    'title': 'Ivan Khomenko'
                },
                {
                    'url': 'https://jamajurabaev.com/',
                    'title': 'Jama Jurabaev'
                },
                {
                    'url': 'http://www.torysica.com/',
                    'title': 'Tory Sica'
                }
            ]
        },
        {
            'position': 'Modeling:',
            'creditsNames': [
                {
                    'url': 'https://www.artstation.com/splendidfennel',
                    'title': 'Alex Malets'
                },
                {
                    'url': 'https://www.artstation.com/akorovkin',
                    'title': 'Andrei Korovkin'
                },
                {
                    'url': 'https://dimoshadji.com/',
                    'title': 'Dimos Hadjisavvas'
                },
                {
                    'url': 'https://www.artstation.com/makarkoff',
                    'title': 'Ivan Makarkoff'
                },
                {
                    'url': 'https://www.behance.net/simplewolf',
                    'title': 'Kirill Stupin'
                },
                {
                    'url': 'https://alsens.net/',
                    'title': 'Serge Aleynikov'
                },
                {
                    'url': 'https://www.instagram.com/bondjo/',
                    'title': 'Slava Kislyakov'
                },
                {
                    'url': 'https://www.artstation.com/sorokin',
                    'title': 'Valentine Sorokin'
                }
            ]
        },
        {
            'position': '3d:',
            'creditsNames': [
                {
                    'url': 'https://www.behance.net/cheprakov',
                    'title': 'Alexey Cheprakov'
                },
                {
                    'url': 'http://www.myshli.com/',
                    'title': 'Danil Krivoruchko'
                },
                {
                    'url': 'https://www.behance.net/vellocet',
                    'title': 'Dmitry Kulikov'
                },
                {
                    'url': 'https://www.behance.net/maxchell',
                    'title': 'Max Chelyadnikov'
                },
                {
                    'url': 'https://maximgoudin.com',
                    'title': 'Maxim Goudin'
                },
                {
                    'url': 'https://vimeo.com/user1505374',
                    'title': 'Maxim Gureev'
                },
                {
                    'url': 'http://www.sashavinogradova.com/',
                    'title': 'Sasha Vinogradova'
                }
            ]
        },
        {
            'position': 'Web concept & design:',
            'creditsNames': [
                {
                    'url': 'http://repponen.com/',
                    'title': 'Anton Repponen'
                }
            ]
        },
        {
            'position': 'Web development:',
            'creditsNames': [
                {
                    'url': 'http://astroshock.ru/',
                    'title': 'Astroshock'
                }
            ]
        },
        {
            'position': 'Copy Editor',
            'creditsNames': [
                {
                    'url': 'http://anyaformozova.com/',
                    'title': 'Anya Formozova'
                }
            ]

        }
    ]
}

error = {
    'backgroundVideo': staticfiles_storage.url('videos/404.mp4'),
    'backgroundVideoPoster': staticfiles_storage.url('img/404/videoPoster.jpg'),
    'backgroundImageDesktop': staticfiles_storage.url('img/404/backgroundDesktop.jpg'),
    'backgroundImageMobile': staticfiles_storage.url('img/404/backgroundMobile.jpg')
}

popups = {
    '01': {
        'shareImage': staticfiles_storage.url('img/share/share-memory01.jpg'),
        'introTitle': 'Space suit',
        'introNumber': '01',
        'introSize': '7.7',
        'introDescription': '3',
        'introText': 'There were the rest of us, though, crammed into the shuttle, embedded in custom spacesuits so padded with shielding we might have been deep-sea divers from a previous century. It was a fine balance; too much shielding would have been worse than none at all, would split primary particles into secondary ones, just as lethal and twice as numerous. Sometimes you had to live with moderate exposure; the only alternative was to embed yourself like a bug in lead.',
        'blocks': [
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'A-01',
                        'date': '12/09/2016',
                        'text': u'Based on the description from the book our space suit should look like a “normal” modern one, but with an extra layer of protection that makes it bulky and heavy.'
                    },
                    {
                        'number': 'A-02',
                        'date': '12/09/2016',
                        'text': u'We wanted to create a design that communicated the space suit’s functionality (within the limits of cinematic convention, of course). A form that could speak to the physical materials and manufacturing methods of the suit. These were our references: divers, sappers (who have the heaviest-duty protection) and traditional space suits. We now needed to find the sweet spot between the three.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Space suit',
                'caption': 'References',
                'file': 'Ref_suit.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'true',
                        'background': '111619',
                        'image': staticfiles_storage.url('img/popups/1/1.png'),
                        'imageZoom': staticfiles_storage.url('img/popups/1/1_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'chat': [
                    {
                        'zoom': 'true',
                        'number': 'A-03',
                        'date': '20/09/2016',
                        'text': 'Question regarding the space suit. Which direction is closer to what you had in mind (before they add all the extra layers of protection).',
                        'image': staticfiles_storage.url('img/popups/1/2.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/1/2_zoom.jpg')
                    },
                    {
                        'theme': 'red',
                        'number': 'Peter Watts',
                        'date': '30/09/2016',
                        'text': u'In all honesty i hadn\'t thought very hard about them. But third from the left is what i\'d point to—before, as you say, they padded themselves up like michelin men to board rorschach.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Direction 1',
                'caption': 'Concept art',
                'file': 'Suit_sketch1.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '7a7b7f',
                        'image': staticfiles_storage.url('img/popups/1/3.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/1/3_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'chat': [
                    {
                        'zoom': 'true',
                        'theme': 'gray',
                        'number': 'A-04',
                        'date': '11/02/2017',
                        'text': 'First concept visualized',
                        'image': staticfiles_storage.url('img/popups/1/4.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/1/4_zoom.jpg')
                    },
                    {
                        'number': 'A-05',
                        'date': '02/03/2017',
                        'text': 'It seemed we were headed in the right direction, but  had gotten too close to creating a clone of the fallout armor.  So, a dead end. Ok, reboot, start over.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Direction 2',
                'caption': 'Concept art',
                'file': 'Suit_sketch2.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '77787c',
                        'image': staticfiles_storage.url('img/popups/1/5.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/1/5_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '77787c',
                        'image': staticfiles_storage.url('img/popups/1/6.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/1/6_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Direction 2',
                'caption': 'Concept art',
                'file': u'Direction_3d‒concept.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': 'cccdd1',
                        'image': staticfiles_storage.url('img/popups/1/7.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/1/7_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'chat': [
                    {
                        'number': 'A-06',
                        'date': '15/10/2017',
                        'text': 'Love it now! Still more work to do, but it would be great to show it to peter and see what he says about this design.'
                    },
                    {
                        'theme': 'red',
                        'number': 'Peter Watts',
                        'date': '24/10/2017',
                        'text': 'Thanks! That\'s the one! That\'s the rorschach incursion suit.'
                    }
                ]
            },
            {
                'type': 'note',
                'question': 'The hardest part is turning a 2d concept into a 3d model.Things end up needing to be added or reimagined. For example, the leg-part exoskeleton was only added at the modeling stage.',
                'answer': 'One of our designers provided the overall direction and worked on the helmet and upper body, while two others worked on the lower body, legs and boots.'
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Final direction',
                'caption': '3d concept',
                'file': 'Suit_wireframe.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/1/8.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/1/8_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'chat': [
                    {
                        'number': 'A-07',
                        'date': '22/08/2019',
                        'text': 'We are 80% done with the suit. The direction is good but some nuance is lacking. We need to bring in one more technical modeler to work out the kinks and finesse the geometry of the suit.'
                    },
                    {
                        'number': 'A-08',
                        'date': '12/09/2019',
                        'text': u'Next—the rig, which will allow us to apply movement to the model in video.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'blackTheme': 'true',
                'showZoom': 'true',
                'title': 'Final',
                'caption': 'Geometry',
                'file': 'Suit_geo.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': 'd7d7d7',
                        'image': staticfiles_storage.url('img/popups/1/9.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/1/9_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'title': 'Final',
                'caption': 'Rig',
                'file': 'Suit_rig.jpg',
                'gallery': [
                    {
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/1/10.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'A-09',
                        'date': '02/10/2019',
                        'text': u'And lastly, the final touches—shading. We tried to emphasize the weightiness dictated by the model’s configuration and add a “military” feel to the design—no extra flourishes, built for durability.<br><br>The result looked to be part-tank, part-astronaut.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Final',
                'caption': 'Final render',
                'file': 'Suite_final.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/1/11.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/1/11_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/1/12.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/1/12_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'chat': [
                    {
                        'number': 'A-10',
                        'date': '05/10/2019',
                        'text': 'This is it! We have to show this to peter and see what he thinks.'
                    },
                    {
                        'theme': 'red',
                        'number': 'Peter Watts',
                        'date': '10/10/2019',
                        'text': u'These are incredible; i kinda wish they were actual movie posters.Still, that\'s the way i envisioned the suits. No one\'s fault but mine if i couldn\'t keep my narratives straight.<br><br>I can always say he just inferred how wide other eyes were from their "topologies", or something…'
                    }
                ]
            },
            {
                'type': 'film',
                'video': staticfiles_storage.url('videos/popups/1/film.mp4'),
                'image': staticfiles_storage.url('img/popups/1/film.jpg'),
                'title': 'Space suit',
                'caption': 'In the film',
                'button': 'true'
            }
        ],
        'wallpaper': 'true',
        'wallpaperImage': staticfiles_storage.url('img/popups/1/wallpaper.jpg'),
        'wallpaperFile': 'A_01.zip / 4 files',
        'wallpaperZip': staticfiles_storage.url('img/popups/1/A_01.zip'),
        'resourcesTitle': '01',
        'resources': [
            {
                'title': 'Number of people involved',
                'value': '6'
            },
            {
                'title': 'Hours Spent',
                'value': '480'
            }
        ],
        'cardImage': staticfiles_storage.url('img/memories/2.jpg'),
        'cardCaption': '02',
        'cardTitle': 'Rorschach',
        'slug': '02'
    },
    '02': {
        'shareImage': staticfiles_storage.url('img/share/share-memory02.jpg'),
        'introTitle': 'Rorschach',
        'introNumber': '02',
        'introSize': '14.9',
        'introDescription': '2',
        'introText': u'Imagine a crown of thorns, twisted, dark and unreflective, grown too thickly tangled to ever rest on any human head. Put it in orbit around a failed star whose own reflected half-light does little more than throw its satellites into silhouette. Occasional bloody highlights glinted like dim embers from its twists and crannies; they only emphasized the darkness everywhere else.<br><br>Imagine an artefact that embodies the very notion of torture, something so wrenched and disfigured that even across uncounted lightyears and unimaginable differences in biology and outlook, you can\'t help but feel that somehow, the structure itself is in pain.<br><br>Now make it the size of a city.',
        'blocks': [
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'B-01',
                        'date': '02/05/2016',
                        'text': u'Rorschach happened to be the very first asset created for this film. A ship-organism, combining the properties of living matter and machine—what algorithmic modeling objective could be more fascinating? We started preliminary testing, but after some calculations it became apparent that the object’s shape was not quite what we had envisioned.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'smallSize': 'true',
                'showZoom': 'true',
                'title': 'Modeling',
                'caption': 'Tests',
                'file': 'Ror_model_0.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '28282c',
                        'image': staticfiles_storage.url('img/popups/2/1.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/2/1_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'largeSize': 'true',
                'chat': [
                    {
                        'number': 'B-02',
                        'date': '16/05/2016',
                        'text': u'Based off the book, we’d imagined rorschach as a very massive torus (with all those spikes and spines on top), but then the math kicked in. We got the torus radius (15000 meters) and volume from these references: "this thing hiding in the shadow of ten jupiters was almost 30 kilometers from side to side." and " rorschach massed 1.8.10^10 kg within a total volume of 2.3.10^8 cubic meters." From the torus volume formula we were able to calculate the radius of the "tube" forming it. We were surprised to discover that the radius was only 28 meters - more like a "very slim, 30 km-diameter ring" rather than a "massive torus-shaped city”.'
                    },
                    {
                        'number': 'B-03',
                        'date': '16/05/2016',
                        'text': u'We realize that it’s not a perfectly-shaped torus, but we were thinking we could probably still use this formula. But judging by the details mentioned in the book, we had been expecting the ring’s inner radius to be around 3-5 km. The question is, was this the way you imagined rorschach? As a very slim ring with a huge diameter, but comparatively tiny inner tube radius?'
                    },
                    {
                        'theme': 'red',
                        'number': 'Peter Watts',
                        'date': '17/05/2016',
                        'text': u'Actually, I never envisioned Rorschach as a single integrated structure—more as a toroidal cloud of objects, loosely connected and held together by magnetic fields:<br><br>...the overall outline was that of a torus, or perhaps a collection of smaller jagged things piled together in a rough ring...<br><br>So most of that volume is empty space.  But looking back,  I guess I didn\'t reinforce that point after they started getting detailed telemetry, so I can see how you\'d think it was a single massive object.'
                    },
                    {
                        'theme': 'red',
                        'number': 'Peter Watts',
                        'date': '17/05/2016',
                        'text': u'I must\'ve based that mass on something—I don\'t think I\'d pull such a number out of my ass without doing a few back-of-the-napkin calculations first— but offhand I doubt I saved them.  I guess I never thought anyone would check. But purely backpedaling, I\'m guessing the difference is that your calculations assume a solid contiguous structure and mine assumed a cloud.<br><br>At least, I hope that\'s it.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Direction 1',
                'caption': 'Blocking',
                'file': 'Ror_dir_01_blocking.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/2/2.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/2/2_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/2/3.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/2/3_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'zoom': 'true',
                        'number': 'B-04',
                        'date': '17/05/2016',
                        'text': 'With your input, i now see that it should look more like this. Did i get it right? And by the way, which version is more accurate, a or b?',
                        'image': staticfiles_storage.url('img/popups/2/4.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/2/4_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'theme': 'red',
                        'heightLimit': 'true',
                        'number': 'Peter Watts',
                        'date': '25/05/2016',
                        'text': 'B, really. The chunks are held together by spines and spires and magnetic fields, so they\'re jumbled pretty closely together. Actually, the art that comes closest to portraying the fragment-density i had in mind was this chinese cover from a few years back; i imagined a thinner torus (bigger hole in the middle), but it captures the overall sense of jostling pieces in close proximity.',
                        'image': staticfiles_storage.url('img/popups/2/5.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/2/5_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Direction 2',
                'caption': 'Test model',
                'file': 'Ror_dir_02_test.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/2/6.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/2/6_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'mediumSize': 'true',
                'showZoom': 'true',
                'title': 'Direction 2',
                'caption': 'Style frames',
                'file': 'Ror_dir_02_frames.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'true',
                        'background': '1b191f',
                        'image': staticfiles_storage.url('img/popups/2/1.png'),
                        'imageZoom': staticfiles_storage.url('img/popups/2/1_zoom.png')
                    }
                ]
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'zoom': 'true',
                        'number': 'B-05',
                        'date': '29/05/2016',
                        'text': u'Here’s a new take on Rorschach. Let us know what you think!',
                        'image': staticfiles_storage.url('img/popups/2/2.png'),
                        'imageZoom': staticfiles_storage.url('img/popups/2/1_zoom.png')
                    },
                    {
                        'theme': 'red',
                        'number': 'Peter Watts',
                        'date': '31/05/2016',
                        'text': u'Dude, that\'s pretty amazing. Even in it\'s current rough state, it\'s by far the most atmospheric rendition of Rorschach I\'ve seen, in terms of conveying the  image that was in my head when I was writing the book…<br><br>…The only complaint I\'d have is the scale of the individual components is too large relative to the scale of the overall megastructure. All those loops and jags and rocky outcrops should be more the size of the individual thorns in the Chinese illustration; Rorschach consists of thousands of those things.<br><br>Other than that, though, it\'s just about perfect.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Direction 3',
                'caption': 'Final model',
                'file': 'Ror_dir_03_model.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/2/7.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/2/7_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/2/8.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/2/8_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/2/9.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/2/9_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'mediumSize': 'true',
                'title': 'Direction 3',
                'caption': 'Modeling tree',
                'file': 'Ror_dir_03_src.jpg',
                'gallery': [
                    {
                        'backgroundGrid': 'false',
                        'background': '313131',
                        'image': staticfiles_storage.url('img/popups/2/10.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'smallSize': 'true',
                'showZoom': 'true',
                'title': 'Direction 3',
                'caption': 'Style frames',
                'file': 'Ror_dir_03_frames.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/2/11.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/2/11_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'B-06',
                        'date': '05/12/2017',
                        'text': u'We are nearly done with the look and feel for Rorschach.<br><br>It’s time to start working on materials, shaders and all the final details for it.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'largeSize': 'true',
                'showZoom': 'true',
                'title': 'Final',
                'caption': 'Render',
                'file': 'Ror_final.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/2/12.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/2/12_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'film',
                'video': staticfiles_storage.url('videos/popups/2/film.mp4'),
                'image': staticfiles_storage.url('img/popups/2/film.jpg'),
                'title': 'Rorschach',
                'caption': 'In the film',
                'button': 'true'
            }
        ],
        'resourcesTitle': '02',
        'resources': [
            {
                'title': 'Number of people involved',
                'value': '1'
            },
            {
                'title': 'Hours Spent',
                'value': '340'
            }
        ],
        'cardImage': staticfiles_storage.url('img/memories/3.jpg'),
        'cardCaption': '03',
        'cardTitle': 'Theseus',
        'slug': '03'
    },
    '03': {
        'shareImage': staticfiles_storage.url('img/share/share-memory03.jpg'),
        'introTitle': 'Theseus',
        'introNumber': '03',
        'introSize': '14.6',
        'introDescription': '2',
        'introText': u'Theseus carried no regular crew—no navigators or engineers, no one to swab the decks, no meat wasted on tasks that machinery orders of mag smaller could perform orders of mag better. Let superfluous deckhands weigh down other ships, if the nonascendent hordes needed to attach some pretense of usefulness to their lives. Let them infest vessels driven only by commercial priorities. The only reason we were here was because nobody had yet optimized software for first contact.',
        'blocks': [
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'C-01',
                        'date': '09/10/2016',
                        'text': u'Theseus was the first 3d asset to require a significant  volume of modeling. From a creative point of view, we had clear directives from peter watts’ website, which featured a drawing of the ship. In addition, the book included detailed descriptions of each of the ship’s parts.'
                    },
                    {
                        'number': 'C-02',
                        'date': '09/10/2018',
                        'text': u'Unsurprisingly, it proved difficult to find a modeler willing to spend hundreds of unpaid hours on a project with an uncertain future. Eventually, we began taking the ship’s construction into our own hands. The plan was to create parts of it and use them to get more modelers interested and willing to participate in the project. To demo the model, we came up with a storyline featuring shots of theseus in construction on earth’s orbit. This story accounted for the fact that only about 20% of the model was built.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Theseus',
                'caption': 'References',
                'file': 'Ref_thesus.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'true',
                        'background': '111619',
                        'image': staticfiles_storage.url('img/popups/3/1.png'),
                        'imageZoom': staticfiles_storage.url('img/popups/3/1_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'mediumSize': 'true',
                'showZoom': 'true',
                'title': 'First test',
                'caption': 'Render',
                'file': 'Thesus_render-a1.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/3/2.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/3/2_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/3/3.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/3/3_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'chat': [
                    {
                        'number': 'C-03',
                        'date': '01/03/2017',
                        'text': 'Hello, peter. Can`t believe my last update on the project was 3 months ago. We`ve put together a presentation with all the frames we have as of now. Theseus is still a work in progress but i think we are almost done with the part below the spine. Take a look.',
                        'image': staticfiles_storage.url('img/popups/3/2.png')
                    },
                    {
                        'theme': 'red',
                        'number': 'Peter Watts',
                        'date': '03/03/2017',
                        'text': 'Jesus, Danil, Honestly, I don\'t know what to say. These are such gorgeous renderings. Can\'t wait to see what comes next.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'mediumSize': 'true',
                'showZoom': 'true',
                'title': 'Iteration no.2',
                'caption': 'Render',
                'file': 'Thesus_render-a2.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/3/4.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/3/4_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/3/5.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/3/5_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'C-04',
                        'date': '08/11/2017',
                        'text': u'Hello, peter. I hope you are doing well. It was the 10 year anniversary of blindsight’s publication about a month ago, did you have a chance to celebrate it?<br><br>I just wanted to share some the progress we`ve made with theseus. Still a work-in-progress, especially the materials. They feel too plastic and cartoony right now, but i still hope you`ll like it.'
                    },
                    {
                        'theme': 'red',
                        'number': 'Peter Watts',
                        'date': '10/11/2017',
                        'text': 'God these are gorgeous. I see what you mean about the plasticy Theseus elements, but you know what? I never really bought in to the whole used-future aesthetic anyway. Movies like Alien and Star Wars feel real and lived-in on a gut level, but seriously: we\'ve got technology that can get us across the galaxy in a week and a half and we still don\'t know how to make paint that doesn\'t peel?  Shiny plastic-looking spaceships may not feel as realistic, but they\'re probably more consistent with the materials tech we\'ll actually have available when such stuff starts getting built.'
                    }
                ]
            },
            {
                'type': 'later',
                'title': '2 Years later',
                'text': 'It proved extremely difficult to find someone to model the spacecraft in a way that would look suitably impressive. In the meantime, we occupied ourselves with other scenes.  Theseus was on hiatus for almost 2 years.'
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Iteration no.3',
                'caption': '3D model',
                'file': 'Thesus_model-a3.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '898a89',
                        'image': staticfiles_storage.url('img/popups/3/6.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/3/6_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '898a89',
                        'image': staticfiles_storage.url('img/popups/3/7.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/3/7_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '898a89',
                        'image': staticfiles_storage.url('img/popups/3/8.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/3/8_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/3/9.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/3/9_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Iteration no.4',
                'caption': 'Test render',
                'file': 'Thesus_render-a4.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/3/10.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/3/10_zoom.jpg')
                    },
                ]
            },
            {
                'type': 'chat',
                'chat': [
                    {
                        'number': 'C-05',
                        'date': '14/01/2019',
                        'text': u'We finished the theseus model! I can`t tell you how excited i was when i hit the render button and saw the complete model for the first time after almost two years of work and delays. We have to spend some more time on the materials though, but this is what we’ve got as of now.'
                    },
                    {
                        'theme': 'red',
                        'number': 'Peter Watts',
                        'date': '16/01/2019',
                        'text': 'This is awesome stuff, as usual. The inevitable question, once again, is: can i post any of this stuff? I\'m guessing no on the teaser as a whole, but what about frame grabs therefrom?'
                    }
                ]
            },
            {
                'type': 'note',
                'question': 'The theseus model ended up consisting of over 62 million polygons and 200+ applied materials and textures.',
                'answer': u'By the end, no workstation could handle the project’s volume, and the only way the ship could be seen in its complete form was after rendering.'
            },
            {
                'type': 'gallery',
                'largeSize': 'true',
                'showZoom': 'true',
                'title': 'Final',
                'caption': 'Render',
                'file': 'Thesus_render-schematic.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '040404',
                        'image': staticfiles_storage.url('img/popups/3/11.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/3/11_zoom.jpg')
                    },
                ]
            },
            {
                'type': 'model',
                'embed': u'<iframe width="100%" height="100%" src="" id="api-frame" allow="autoplay; fullscreen; vr" allowvr allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>'
            },
            {
                'type': 'film',
                'video': staticfiles_storage.url('videos/popups/3/film.mp4'),
                'image': staticfiles_storage.url('img/popups/3/film.jpg'),
                'title': 'Thesus',
                'caption': 'In the film',
                'button': 'true'
            }
        ],
        'wallpaper': 'true',
        'wallpaperImage': staticfiles_storage.url('img/popups/3/wallpaper.jpg'),
        'wallpaperFile': 'C_01.zip / 3 files',
        'wallpaperZip': staticfiles_storage.url('img/popups/3/C_01.zip'),
        'resourcesTitle': '03',
        'resources': [
            {
                'title': 'Number of people involved',
                'value': '4'
            },
            {
                'title': 'Hours Spent',
                'value': '310'
            }
        ],
        'cardImage': staticfiles_storage.url('img/memories/4.jpg'),
        'cardCaption': '04',
        'cardTitle': 'Scramblers',
        'slug': '04'
    },
    '04': {
        'shareImage': staticfiles_storage.url('img/share/share-memory04.jpg'),
        'introTitle': 'Scramblers',
        'introNumber': '04',
        'introSize': '15.1',
        'introDescription': '2',
        'introText': u'Scramblers, everywhere. A seething infestation squirming across the walls, reaching out for the intruder, leaping into the lumen of the passageway to press their counterattack. Not against us. They had attacked one of their own.<br><br>I\'d seen three of its arms ripped off before it had disappeared into a writhing ball in the center of the passageway.',
        'blocks': [
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'D-01',
                        'date': '13/08/2016',
                        'text': u'Animating the Scramblers the normal way wouldn’t work, that much was clear from the start - creating the movement of the tentacles was difficult enough, and in scenes featuring dozens of the creatures it became simply impossible.'
                    },
                    {
                        'number': 'D-02',
                        'date': '13/08/2016',
                        'text': u'For the first test we tried creating tentacles that simply followed the Scramblers’ bodies. We wouldn’t get far with this set up, but at least it solved part of the problem in group scenes.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'videoGallery': 'true',
                'title': 'First test',
                'caption': 'Animation',
                'file': 'Scramb_test_01.mp4',
                'gallery': [
                    {
                        'video': staticfiles_storage.url('videos/popups/4/1.mp4'),
                        'image': staticfiles_storage.url('img/popups/4/v1.jpg'),
                    }
                ]
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'D-03',
                        'date': '08/11/2016',
                        'text': u'Hello, Peter.<br><br>We just wanted to share the progress we’ve made with the illustrations and, for the first time ever—the Scramblers in motion.'
                    },
                    {
                        'theme': 'red',
                        'number': 'Peter Watts',
                        'date': '10/11/2016',
                        'text': u'WOW. The look, the movement of the scramblers is great.  That aesthetic is exactly what I imagined. All I could say is—and this is really minor—all the scramblers you\'ve rendered are juveniles.  As they get older, the central disk thickens and becomes more spheroid; the arms migrate off the equator and end up distributed all over the body.  So the adults don\'t look as much like earthly brittle stars as these guys do.<br><br>But man, I can\'t get over how gorgeous the rendering and the movements are.  If you have any more of this stuff, I\'d love to see it.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Main direction',
                'caption': 'Shader test',
                'file': 'Scramb_render_01.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '18191d',
                        'image': staticfiles_storage.url('img/popups/4/1.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/4/1_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'D-04',
                        'date': '11/11/2018',
                        'text': 'But what about the shots in which the Scramblers interact with their surroundings, rather than just wave their tentacles about? After reviewing articles on Octopus locomotion (our closest reference), and several weeks worth of coding, we were able to create a behavior that seemed convincing enough.',
                        'reference': 'true',
                        'referenceUrl': 'https://www.cell.com/current-biology/fulltext/S0960-9822(15)00266-3',
                        'referenceImage': staticfiles_storage.url('img/popups/4/document.jpg'),
                        'referenceTitle': 'Arm Coordination in Octopus Crawling Involves Unique Motor Control Strategies'
                    },
                    {
                        'number': 'D-05',
                        'date': '20/12/2018',
                        'text': u'The movement of the body was still determined manually. Then, based off this movement and our algorithm each of the tentacles independently searches for the most convenient surface area to attach too, as well as when to detach and search for new footholds.<br><br>The system that controlled the “normal” Scramblers and its upgrade created for Scramblers interacting with their environment.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'mediumSize': 'true',
                'title': 'Animation control',
                'caption': 'Script',
                'file': 'Scramb_script.jpg',
                'gallery': [
                    {
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/4/2.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'D-06',
                        'date': '22/02/2019',
                        'text': u'Time to send off another preview, featuring the “playground” in which we tested the Scramblers movements.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'videoGallery': 'true',
                'title': 'Animation',
                'caption': 'Test',
                'file': 'Scramb_script_animation.mp4',
                'gallery': [
                    {
                        'video': staticfiles_storage.url('videos/popups/4/2.mp4'),
                        'image': staticfiles_storage.url('img/popups/4/v2.jpg'),
                    }
                ]
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'D-07',
                        'date': '26/02/2019',
                        'text': u'Not a big update but I thought you might like this one. Some work in progress on the system that controls the Scramblers leg placement and animation.<br><br>I realized that I have dozens of these guys in one of the shots so animating them manually would take weeks. 85 lines of code and a few pain-in-the-neck hours later each Scrambler can now decide where to place each leg on its own. Not exactly superhuman intelligence but still much better than what I could’ve done by hand.'
                    },
                    {
                        'theme': 'red',
                        'number': 'Peter Watts',
                        'date': '12/02/2019',
                        'text': 'This is really cool (I especially like the little vector/node thingies). But I\'ve already seen a whole wall of those guys squirming and writhing in the trailers, and they looked incredible months ago without any scrambler-level AI. Why is this necessary?'
                    }
                ]
            },
            {
                'type': 'note',
                'question': 'In scenes that showed multiple Scramblers it was possible to cheat a bit and have the tentacles just flow, following their bodies like seaweed.',
                'answer': u'But in the scene where the scrambler swarm attacks Theseus, we needed them to interact with the spaceship’s surface and grip/release with each tentacle in a realistic way. It was a fascinating task to solve. We ended up using Octopus locomotion as a reference.'
            },
            {
                'type': 'gallery',
                'centeredGallery': 'true',
                'videoGallery': 'true',
                'title': 'Shot',
                'caption': 'Previz',
                'file': 'Scramb_shot_previz.mp4',
                'gallery': [
                    {
                        'backgroundGrid': 'true',
                        'background': '15151c',
                        'video': staticfiles_storage.url('videos/popups/4/3.mp4'),
                        'image': staticfiles_storage.url('img/popups/4/v3.jpg'),
                    }
                ]
            },
            {
                'type': 'film',
                'video': staticfiles_storage.url('videos/popups/4/film.mp4'),
                'image': staticfiles_storage.url('img/popups/4/film.jpg'),
                'title': 'Scramblers',
                'caption': 'In the film',
                'button': 'true'
            }
        ],
        'wallpaper': 'true',
        'wallpaperImage': staticfiles_storage.url('img/popups/4/wallpaper.jpg'),
        'wallpaperFile': 'D_01.zip / 1 file',
        'wallpaperZip': staticfiles_storage.url('img/popups/4/D_01.zip'),
        'resourcesTitle': '04',
        'resources': [
            {
                'title': 'Number of people involved',
                'value': '2'
            },
            {
                'title': 'Hours Spent',
                'value': '262'
            }
        ],
        'cardImage': staticfiles_storage.url('img/memories/5.jpg'),
        'cardCaption': '05',
        'cardTitle': 'Interface',
        'slug': '05'
    },
    '05': {
        'shareImage': staticfiles_storage.url('img/share/share-memory05.jpg'),
        'introTitle': 'Interface',
        'introNumber': '05',
        'introSize': '80.2',
        'introDescription': '2',
        'introText': 'By now the probe coasted just a few kilometers off Rorschach\'s leading edge. That close it served up way more than magnetic fields: it presented Rorschach itself in bright, tactical color codes. Invisible curves and spikes iridesced in ConSensus across any number of on-demand pigment schemes: gravity, reflectivity, blackbody emissions. Massive electrical bolts erupting from the tips of thorns rendered in lemon pastels. User-friendly graphics had turned Rorschach into a cartoon.',
        'blocks': [
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'E-01',
                        'date': '05/02/2017',
                        'text': u'The novel has a detailed description of the state of the Solar System around the time of Theseus’ launch. So we started off by trying to recreate the complete chronology of these events in a visualisation—from the discovery of the Burns-Caulfield object to the abrupt change in course <a href="/memories/memory-03/" class="MemoriesPopup-chatItemLink u-Route">Theseus</a> made in order to fly to the Oort cloud region, instead of the planned destination of Kuiper Belt.'
                    },
                    {
                        'number': 'E-02',
                        'date': '07/02/2017',
                        'text': u'It wouldn’t have been hard sci-fi if we had just drawn the orbits and sprinkled a few asteroids throughout at random. So instead we took the actual planets’ trajectories and wound the whole system up to the year 2082.<br><br>We did the same for all the asteroids (found their exact locations and their orbits in the IAU database) and then calculated where that would place them at the time the book’s story starts.'
                    }
                ]
            },
            {
                'type': 'exploration'
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'E-03',
                        'date': '01/03/2017',
                        'text': u'Here’s the whole new vis of events in the Solar System. The funny thing here is that all the asteroids are real ones. I took the orbits data from the International Astronomical Union (IAU) site and spent some time finding their positions in the year 2082. Probably the geekiest project I`ve ever made =)',
                        'reference': 'true',
                        'referenceUrl': 'https://minorplanetcenter.net//iau/lists/MPLists.html',
                        'referenceTitle': 'The Interbational Astronomical Union. Minor Planet Center.'
                    },
                    {
                        'theme': 'red',
                        'number': 'Peter Watts',
                        'date': '03/03/2017',
                        'text': u'Honestly, I don\'t know what to say. These are such gorgeous renderings—and that tactical animation of the various "waves" is the cherry on top. This is the kind of thing you\'d expect to see in a big-budget SF movie.'
                    }
                ]
            },
            {
                'type': 'note',
                'question': u'The first shot didn’t end up making it into the final cut, but it did set the direction for all subsequent data and interface visualization.',
                'answer': u'We were trying to get as much data as possible out of the book and then working off that to create something visually engaging.'
            },
            {
                'type': 'gallery',
                'largeSize': 'true',
                'videoGallery': 'true',
                'title': 'Data vis 1',
                'caption': 'Render',
                'file': 'Ui_belt.mp4',
                'gallery': [
                    {
                        'video': staticfiles_storage.url('videos/popups/5/1.mp4'),
                        'image': staticfiles_storage.url('img/popups/5/v1.jpg'),
                    }
                ]
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'E-04',
                        'date': '01/05/2017',
                        'text': u'This visualization was initially meant to show the <a href="/memories/memory-02/" class="MemoriesPopup-chatItemLink u-Route">Rorschach’s</a> unmasking as a result of the probes sent off <a href="/memories/memory-03/" class="MemoriesPopup-chatItemLink u-Route">Theseus</a>. Instead, it became the basis for a more complicated shot, in which Sarasti is “working his magic” on the telemetric data currents and slowly extrapolating rorschach\'s topology from the statistical anomalies.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'largeSize': 'true',
                'videoGallery': 'true',
                'title': 'Data vis 2',
                'caption': 'Render',
                'file': 'Ui_ben.mp4',
                'gallery': [
                    {
                        'video': staticfiles_storage.url('videos/popups/5/2.mp4'),
                        'image': staticfiles_storage.url('img/popups/5/v2.jpg'),
                    }
                ]
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'E-05',
                        'date': '20/08/2019',
                        'text': u'The book’s characters are all very much post-human - various modifications and implants let them operate with much higher volumes of information than those accessible to a regular person. We considered this when designing the interfaces, making the information density higher than would be comfortable for a typical human. And in <a href="/memories/memory-07/" class="MemoriesPopup-chatItemLink u-Route">Sarasti’s</a> case, the UI could go into hyperdrive - his capabilities of perception and pattern recognition justified any level of complexity. Four-dimensional objects as a system of data visualisation and manipulation - why not?'
                    }
                ]
            },
            {
                'type': 'gallery',
                'mediumSize': 'true',
                'videoGallery': 'true',
                'title': 'Ui elements',
                'caption': 'Prototype',
                'file': 'Ui_elements.mp4',
                'gallery': [
                    {
                        'video': staticfiles_storage.url('videos/popups/5/3.mp4'),
                        'image': staticfiles_storage.url('img/popups/5/v3.jpg'),
                    }
                ]
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'E-06',
                        'date': '14/10/2019',
                        'text': u'The <a href="/memories/memory-01/" class="MemoriesPopup-chatItemLink u-Route">spacesuits’</a> interface was the complete opposite. No human would want to be distracted by complex constellations of data when exploring an alien spaceship full of unknown dangers.<br><br>We modeled them off modern military interfaces, updated for the 2080s. Minimum “frills”, maximum functionality. The dark red color is less distracting and disruptive to night vision. Add to that exact target tracking and a space adaptation map with no “up” or “down”.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'mediumSize': 'true',
                'showZoom': 'true',
                'title': 'Helmet ui',
                'caption': 'Design',
                'file': 'Ui_helmet_design.png',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/5/1.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/5/1_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'mediumSize': 'true',
                'videoGallery': 'true',
                'title': 'Helmet ui',
                'caption': 'Prototype',
                'file': 'Ui_helmet_proto.mp4',
                'gallery': [
                    {
                        'video': staticfiles_storage.url('videos/popups/5/4.mp4'),
                        'image': staticfiles_storage.url('img/popups/5/v4.jpg'),
                    }
                ]
            },
            {
                'type': 'film',
                'video': staticfiles_storage.url('videos/popups/5/film.mp4'),
                'image': staticfiles_storage.url('img/popups/5/film.jpg'),
                'title': 'Interfaces',
                'caption': 'In the film',
                'button': 'true'
            }
        ],
        'wallpaper': 'true',
        'wallpaperImage': staticfiles_storage.url('img/popups/5/wallpaper.jpg'),
        'wallpaperFile': 'E_01.zip / 1 file',
        'wallpaperZip': staticfiles_storage.url('img/popups/5/E_01.zip'),
        'resourcesTitle': '05',
        'resources': [
            {
                'title': 'Number of people involved',
                'value': '3'
            },
            {
                'title': 'Hours Spent',
                'value': '315'
            }
        ],
        'cardImage': staticfiles_storage.url('img/memories/6.jpg'),
        'cardCaption': '06',
        'cardTitle': 'Equipment',
        'slug': '06'
    },
    '06': {
        'shareImage': staticfiles_storage.url('img/share/share-memory06.jpg'),
        'introTitle': 'Equipment',
        'introNumber': '06',
        'introSize': '11.5',
        'introDescription': '2',
        'introText': u'Bates was summoning her troops. We floated before the primary fab port at the base of Theseus\' spine. The plant could just as easily have disgorged the grunts directly into the hold beneath the carapace — that was where they\'d be stored anyway, until called upon — but Bates was giving each a visual inspection before sending it through one of the airlocks a few meters up the passageway. Ritual, perhaps. Military tradition. Certainly there was nothing she could see with her eyes that wouldn\'t be glaringly obvious to the most basic diagnostic.',
        'blocks': [
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'F-01',
                        'date': '02/08/2017',
                        'text': u'The hibernation tech described in the book is more akin to a resurrection from the dead than the standard “freeze” found in other sci-fi novels. The characters refer to the sleeping pods as "coffins", and the hibernation itself is called "being undead." when creating the capsule design, we tried to build off this funereal aesthetic. Starting with the references.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Cryopod',
                'caption': 'References',
                'file': 'Ref_cryopod.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'true',
                        'background': '111619',
                        'image': staticfiles_storage.url('img/popups/6/1.png'),
                        'imageZoom': staticfiles_storage.url('img/popups/6/1_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Cryopod',
                'caption': 'Geometry',
                'file': 'Cryopod_geo_01.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/6/2.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/6/2_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/6/3.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/6/3_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'F-02',
                        'date': '06/09/2017',
                        'text': u'We thought we’d start and end the film with <a href="/memories/memory-07/" class="MemoriesPopup-chatItemLink u-Route">siri</a> lying in the pod/ coffin. We spent quite some time working out the details to make sure the close-ups looked good. We noticed that cryopods in movies/games all tend to have more or less the same design. But you had this really interesting concept of “undead” bodies, instead of just frozen ones.<br><br>We decided to design our pods based on that idea — that\'s where the body being fully covered with a piece of cloth comes from. And the overall contrast of the clean mechanical design of the outer shell with the almost organic inside parts is supposed to support the concept of "dead on the outside/ alive on the inside".'
                    },
                    {
                        'theme': 'red',
                        'number': 'Peter Watts',
                        'date': '07/09/2017',
                        'text': 'Actually, someone sent me those coffin shots a couple of hours before you did. They\'re gorgeous. Not exactly how I\'d envisioned them, but truthfully, your vision is better anyway.'
                    },
                ]
            },
            {
                'type': 'gallery',
                'mediumSize': 'true',
                'showZoom': 'true',
                'title': 'Cryopod',
                'caption': 'Final render',
                'file': 'Pod_highres_01.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/6/4.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/6/4_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/6/5.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/6/5_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/6/6.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/6/6_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'F-03',
                        'date': '04/10/2017',
                        'text': u'<a href="/memories/memory-03/" class="MemoriesPopup-chatItemLink u-Route">Theseus</a> carried two identical shuttles, scylla and charybdis, which the main characters used for sorties on <a href="/memories/memory-02/" class="MemoriesPopup-chatItemLink u-Route">rorschach</a>. The book didn’t really describe the design of these ships, but from individual passages we knew that they could barely fit 4 people in <a href="/memories/memory-01/" class="MemoriesPopup-chatItemLink u-Route">spacesuits</a>. Near the end of the novel, one of the shuttles was converted to accommodate one cryo-pod and the equipment necessary for a multi-year flight. Using this data, we were able to estimate the approximate dimensions of the ships and design them based off that.'
                    },
                    {
                        'number': 'F-04',
                        'date': '19/10/2017',
                        'text': u'Within our team, we ended up calling this asset “frankenshuttle”. The ship model ended up changing hands several times before reaching its final look—too much work was required for just one modeler. One of us would start working on the asset, and then be forced to hand off the work do to other, commercial projects piling up. So the frankenshuttle kept getting passed around between team members.'
                    },
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Shuttle',
                'caption': 'Blocking',
                'file': 'Shuttle_00.jpg',
                'gallery': [
                    {
                        'backgroundGrid': 'false',
                        'background': 'c1c1c1',
                        'image': staticfiles_storage.url('img/popups/6/7.jpg')
                    },
                    {
                        'backgroundGrid': 'false',
                        'background': '7f7f7f',
                        'image': staticfiles_storage.url('img/popups/6/8.jpg')
                    },
                    {
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/6/9.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'F-05',
                        'date': '24/10/2017',
                        'text': u'We’ve just had to push the delivery date to 2018. Sad smile. The truth is our ambitions for this short are growing faster than we can produce the results. The time from october to december is always super busy with commercial work so the other guys had to almost stop their activity on the project. And i’ve been stuck on the cryo-pod’s shuttle interior for almost 4 weeks now, but it still looks too generic to me.'
                    },
                    {
                        'theme': 'red',
                        'number': 'Peter Watts',
                        'date': '24/10/2017',
                        'text': u'Piffle. It looks terrific. I mean, i see what you mean— it could be an outtake from any number of spaceship interiors from alien to the expanse — but dude, the function of the equipment limits the amount of novelty you can inject into design. Sure, you want a distinctive style — but you put too many weird-ass features in a chair and no one will be able to sit in the damn thing.<br><br>Of course, you\'re the expert. But i think it looks beautiful.'
                    },
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Shuttle',
                'caption': 'Shading test',
                'file': 'Shuttle_test_01.jpg',
                'gallery': [
                    {
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/6/10.jpg')
                    },
                    {
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/6/11.jpg')
                    },
                    {
                        'backgroundGrid': 'false',
                        'background': '0a0e11',
                        'image': staticfiles_storage.url('img/popups/6/12.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'F-06',
                        'date': '11/05/2018',
                        'text': u'The drones operated by major bates were featured in many of the novel’s key scenes, so we paid special attention to their design.<br><br>These insect-like machines had to carry heavy protection in order to be able to operate within rorschach’s harsh electromagnetic environment. At the same time, the design needed to preserve their main function — that of combat equipment, semi-autonomous weapons.'
                    },
                    {
                        'zoom': 'true',
                        'number': 'F-07',
                        'date': '30/07/2018',
                        'text': u'We ended up landing on a design borrowed from certain species of beetles — a durable shell that covers the important parts, and can temporarily open up when some action needs to be performed.',
                        'image': staticfiles_storage.url('img/popups/6/13.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/6/13_zoom.jpg')
                    },
                ]
            },
            {
                'type': 'gallery',
                'title': 'Grunt',
                'caption': 'Concept art',
                'file': 'Grunt_art_004.jpg',
                'gallery': [
                    {
                        'backgroundGrid': 'false',
                        'background': 'c6c8ca',
                        'image': staticfiles_storage.url('img/popups/6/14.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'smallSize': 'true',
                'showZoom': 'true',
                'title': 'Grunt',
                'caption': 'Shading test',
                'file': 'Grunt_01.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/6/15.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/6/15_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'videoGallery': 'true',
                'showZoom': 'true',
                'title': 'Grunt',
                'caption': 'Motion test',
                'file': 'Grunt_mt_01.mp4',
                'gallery': [
                    {
                        'video': staticfiles_storage.url('videos/popups/6/1.mp4'),
                        'image': staticfiles_storage.url('img/popups/6/v1.jpg'),
                    },
                    {
                        'video': staticfiles_storage.url('videos/popups/6/2.mp4'),
                        'image': staticfiles_storage.url('img/popups/6/v2.jpg'),
                    }
                ]
            },
            {
                'type': 'note',
                'question': 'While working on the project we created around 30 objects of equipment and examples of technologies mentioned in the book.',
                'answer': 'Not all of them got to play lead parts in the film, but without them it would have been impossible to convey the atmosphere we wanted.'
            },
            {
                'type': 'gallery',
                'mediumSize': 'true',
                'showZoom': 'true',
                'title': 'Interior',
                'caption': 'Geometry',
                'file': 'Int_008.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/6/16.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/6/16_zoom.jpg')
                    },
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/6/17.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/6/17_zoom.jpg')
                    },
                    {
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/6/18.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'smallSize': 'true',
                'title': 'Shuttle chair',
                'caption': 'Geometry',
                'file': 'Chair_01.png',
                'gallery': [
                    {
                        'backgroundGrid': 'false',
                        'background': '4e4e4e',
                        'image': staticfiles_storage.url('img/popups/6/19.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'mediumSize': 'true',
                'showZoom': 'true',
                'title': 'Helmet',
                'caption': 'Shading test',
                'file': 'Shot_010_01_helmet.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/6/20.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/6/20_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'film',
                'video': staticfiles_storage.url('videos/popups/6/film.mp4'),
                'image': staticfiles_storage.url('img/popups/6/film.jpg'),
                'title': 'Equipment',
                'caption': 'In the film',
                'button': 'true'
            }
        ],
        'resourcesTitle': '06',
        'resources': [
            {
                'title': 'Number of people involved',
                'value': '8'
            },
            {
                'title': 'Hours Spent',
                'value': '824'
            }
        ],
        'cardImage': staticfiles_storage.url('img/memories/7.jpg'),
        'cardCaption': '07',
        'cardTitle': 'Characters',
        'slug': '07'
    },
    '07': {
        'shareImage': staticfiles_storage.url('img/share/share-memory07.jpg'),
        'introTitle': 'Characters',
        'introNumber': '07',
        'introSize': '11.1',
        'introDescription': '2',
        'introText': u'It wasn\'t so much the way they looked. The elongate limbs, the pale skin, the canines and the extended mandible—noticeable, yes, even alien, but not disturbing, not frightening. Not even the eyes, really. The eyes of dogs and cats shine in the darkness; we don\'t shiver at the sight.<br><br>Not the way they looked. The way they moved.',
        'blocks': [
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'G-01',
                        'date': '19/03/2017',
                        'text': u'The novel doesn’t have that many characters, which gave Peter Watts ample opportunity to describe each one in depth. We began our work on this part by finding suitable references for each of them. Apart from their appearance, we also needed to figure out their uniforms, find the right mix of recognizable, functional and futuristic.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Characters',
                'caption': 'References',
                'file': 'Char_ref.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'true',
                        'background': '111619',
                        'image': staticfiles_storage.url('img/popups/7/1.png'),
                        'imageZoom': staticfiles_storage.url('img/popups/7/1_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'G-02',
                        'date': '25/03/2017',
                        'text': 'After a few iterations from our concept-artist, we had several character sketches that fit all the qualifications.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Sarasti & bates',
                'caption': 'Concept art',
                'file': 'Char_bates_3.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/7/2.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/7/2_zoom.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'G-03',
                        'date': '01/06/2018',
                        'text': u'We began modeling Sarasti off the concept-art, but then found an AMA of Peter Watts’ on Reddit, in which he mentioned Mads Mikkelsen as the perfect actor for Sarasti’s part. This made our job a lot easier - we took Mads’ appearance as our starting-off point and then tweaked it to fit the vampiric traits described in the book.<br><br>Next we needed to figure out skin and hair shading and create his outfit.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'showZoom': 'true',
                'title': 'Sarasti',
                'caption': 'Shading test',
                'file': 'Sarasti_shading.jpg',
                'gallery': [
                    {
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/7/3.jpg')
                    },
                    {
                        'backgroundGrid': 'false',
                        'background': '313131',
                        'image': staticfiles_storage.url('img/popups/7/4.jpg')
                    },
                    {
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/7/5.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'title': 'Crew outfit',
                'caption': 'Design',
                'file': 'Sarasti_suit.png',
                'gallery': [
                    {
                        'backgroundGrid': 'false',
                        'background': '000000',
                        'image': staticfiles_storage.url('img/popups/7/6.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'largeSize': 'true',
                'showZoom': 'true',
                'title': 'Sarasti',
                'caption': 'Final render',
                'file': 'Sarasti_01_02.jpg',
                'gallery': [
                    {
                        'zoom': 'true',
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/7/7.jpg'),
                        'imageZoom': staticfiles_storage.url('img/popups/7/7_zoom.jpg')
                    },
                    {
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/7/8.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'G-04',
                        'date': '14/07/2018',
                        'text': u'In the case of Siri’s character we were lucky enough to find a suitable actor in a photogrammetry database. So this provided us with a starter model and textures.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'centeredGallery': 'true',
                'title': 'Siri',
                'caption': 'Model & texture',
                'file': 'Siri_geo.png',
                'gallery': [
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '383838',
                        'image': staticfiles_storage.url('img/popups/7/9.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '383838',
                        'image': staticfiles_storage.url('img/popups/7/10.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'G-05',
                        'date': '29/09/2018',
                        'text': 'After some manual clean up of the textures and a bit of retopology the model was ready for animation. The sculptor ended up having to make a few more versions of the model in order to give us all the necessary face and neck positions demanded by the script.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'title': 'Siri',
                'caption': 'Blend shapes',
                'file': 'Siri_blendshapes.png',
                'gallery': [
                    {
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/7/11.jpg')
                    },
                    {
                        'backgroundGrid': 'false',
                        'background': '242328',
                        'image': staticfiles_storage.url('img/popups/7/12.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'G-06',
                        'date': '03/02/2019',
                        'text': u'All that remained was placing the character in the shot’s environment and we were done.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'mediumSize': 'true',
                'title': 'Siri',
                'caption': 'Final render',
                'file': 'Siri_frame.Jpg',
                'gallery': [
                    {
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/7/13.jpg')
                    }
                ]
            },
            {
                'type': 'film',
                'video': staticfiles_storage.url('videos/popups/7/film.mp4'),
                'image': staticfiles_storage.url('img/popups/7/film.jpg'),
                'title': 'Characters',
                'caption': 'In the film',
                'button': 'true'
            }
        ],
        'wallpaper': 'true',
        'wallpaperImage': staticfiles_storage.url('img/popups/7/wallpaper.jpg'),
        'wallpaperFile': 'G_01.zip / 2 files',
        'wallpaperZip': staticfiles_storage.url('img/popups/7/G_01.zip'),
        'resourcesTitle': '07',
        'resources': [
            {
                'title': 'Number of people involved',
                'value': '4'
            },
            {
                'title': 'Hours Spent',
                'value': '382'
            }
        ],
        'cardImage': staticfiles_storage.url('img/memories/8.jpg'),
        'cardCaption': '08',
        'cardTitle': 'Soundtrack',
        'slug': '08'
    },
    '08': {
        'shareImage': staticfiles_storage.url('img/share/share-memory08.jpg'),
        'introTitle': 'Soundtrack',
        'introNumber': '08',
        'introSize': '85.2',
        'introDescription': '2',
        'introText': 'You tell yourself it\'s mostly in your head. You remind yourself it\'s well-documented, an inevitable consequence of meat and magnetism brought too close together. High-energy fields release the ghosts and the grays from your temporal lobe, dredge up paralyzing dread from the midbrain to saturate the conscious mind. They fuck with your motor nerves and make even dormant inlays sing like fine fragile crystal.<br><br>Energy artefacts. That\'s all they are. You repeat that to yourself, you repeat it so often it loses any pretense of rationality and devolves into rote incantation, a spell to ward off evil spirits. They\'re not real, these whispering voices just outside your helmet, those half-seen creatures flickering at the edge of vision.',
        'blocks': [
            {
                'type': 'info',
                'image': staticfiles_storage.url('img/popups/8/1.jpg'),
                'text': u'The soundtrack was created by Bristol based studio <a href="https://echoicaudio.com/" target="_blank" class="MemoriesPopup-infoTextLink">Echoic Audio</a> with George Leggett as Composer. Owen Hemming-Brown as Sound Designer and Tom Gilbert working on the dialogue.'
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'H-01',
                        'date': '08/10/2020',
                        'text': u'The score is dark, brooding and atmospheric. We wanted to avoid Hollywood cliches and make it feel quite tense with lots of bass, movement and rhythm.',
                        'audio': staticfiles_storage.url('audio/1.wav'),
                        'title': 'LowStab.wav'
                    },
                    {
                        'number': 'H-02',
                        'date': '08/10/2020',
                        'text': u'Although there is little conventional thematic material in the score, we felt it was necessary for there to be some kind of repeating motif. George wanted it to sound experimental, synthesised and subtle to create an ominous mood. He synthesised a warped detuned bass sound to act as this repeating motif which can be heard throughout the film.',
                        'audio': staticfiles_storage.url('audio/2.wav'),
                        'title': 'RepeatingMotif.wav'
                    }
                ]
            },
            {
                'type': 'gallery',
                'title': 'Score',
                'caption': 'Wip',
                'file': 'img_3376.jpg',
                'gallery': [
                    {
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/8/2.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'H-03',
                        'date': '08/10/2020',
                        'text': u'One of the main virtual instruments used music was the loop manipulator and granular synthesiser “Cycles”. It allows you to take experimental loops of any kind and manipulate them in so many different ways. It helped us create that feeling of suspense that a drone/loop has without it sounding monotonous or repetitive',
                        'audio': staticfiles_storage.url('audio/3.wav'),
                        'title': 'CyclesDrumloop.wav'
                    },
                    {
                        'number': 'H-04',
                        'date': '08/10/2020',
                        'text': u'As the story unfolds in reverse, we thought it would be interesting to try to use reversed sounds throughout. One way of doing this is to use risers. One way was using an E-bow on an electric guitar, adding plenty of distortion, reverb, and delay and then slowly tuning the strings down.  Then reverse the whole sound so it ending up rising in pitch.  did a similar thing with sustained harmonic notes played on violins and cellos.',
                        'audio': staticfiles_storage.url('audio/4.wav'),
                        'title': 'ReverseGuitar_Distorted_Ebow.wav'
                    }
                ]
            },
            {
                'type': 'gallery',
                'title': 'Score',
                'caption': 'Sound recording',
                'file': 'echoicaudio-10.jpg',
                'gallery': [
                    {
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/8/3.jpg')
                    },
                    {
                        'fill': 'cover',
                        'image': staticfiles_storage.url('img/popups/8/1.png')
                    }
                ]
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'H-05',
                        'date': '08/10/2020',
                        'text': u'The ending of the score uses one short sample of a female voice to create a glitchy, distorted, staccato choir instrument which to me gives it a kind of religiosity and grandeur that non-vocal music can never quite match. It slowly rises and in both volume, intensity and harmonic dissonance as we reach the end of the film.',
                        'audio': staticfiles_storage.url('audio/5.wav'),
                        'title': 'EndingChoir.wav'
                    }
                ]
            },
            {
                'type': 'gallery',
                'centeredGallery': 'true',
                'title': 'Audio design',
                'caption': 'Cycles',
                'file': 'Screen shot 2020-10-06 at 15.35.59.png',
                'gallery': [
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '15151c',
                        'image': staticfiles_storage.url('img/popups/8/4.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'number': 'H-06',
                        'date': '08/10/2020',
                        'text': u'A lot of the production period was done during lockdown so nearly all the dialogue was recorded remotely with actors far and wide. Which was a huge challenge.'
                    },
                    {
                        'number': 'H-07',
                        'date': '08/10/2020',
                        'text': u'We used lots of processing on the dialogue to design characters or create an in helmet feel. a lot of which was done using various impulse responses (such as helmet IR’s) and ‘futz’ effects for radio communications and the television broadcast.',
                        'audio': staticfiles_storage.url('audio/6.wav'),
                        'title': 'SD Clip 1 Dialogue.wav'
                    }
                ]
            },
            {
                'type': 'video',
                'largeSize': 'true',
                'background': '14141b',
                'video': staticfiles_storage.url('videos/popups/8/1.mp4'),
                'videoPoster': staticfiles_storage.url('img/popups/8/poster-1.jpg'),
                'title': 'Sound design',
                'caption': 'Dialogue',
                'file': 'Sd clip 1 dialogue.mov'
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'H-08',
                        'date': '08/10/2020',
                        'text': u'Owen created meticulous and detailed sound design for the film which really brings the film to life like a movie. These were created in groups so robotic movements / spaceships / explosions etc.Cinematic hits, whooshes and impacts. Atmospheres and backgrounds. Foley & Hard FX<br><br>This clip shows how sound was used to create suspense',
                        'audio': staticfiles_storage.url('audio/7.wav'),
                        'title': 'SD Clip 1.wav'
                    }
                ]
            },
            {
                'type': 'video',
                'largeSize': 'true',
                'background': '14141b',
                'video': staticfiles_storage.url('videos/popups/8/2.mp4'),
                'videoPoster': staticfiles_storage.url('img/popups/8/poster-1.jpg'),
                'title': 'Sound design',
                'caption': 'Suspense',
                'file': 'Sd clip 1.mov'
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'number': 'H-09',
                        'date': '08/10/2020',
                        'text': u'This clip shows level of detail used and sounds made from scratch for UI elements',
                        'audio': staticfiles_storage.url('audio/8.wav'),
                        'title': 'SD Clip 2.wav'
                    }
                ]
            },
            {
                'type': 'video',
                'largeSize': 'true',
                'background': '14141b',
                'video': staticfiles_storage.url('videos/popups/8/3.mp4'),
                'videoPoster': staticfiles_storage.url('img/popups/8/poster-2.jpg'),
                'title': 'Sound design',
                'caption': 'Ui elements',
                'file': 'Sd clip 2.mov'
            },
            {
                'type': 'gallery',
                'centeredGallery': 'true',
                'title': 'Soundtrack',
                'caption': 'Final mix',
                'file': 'Pro Tools Session.png',
                'gallery': [
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '15151c',
                        'image': staticfiles_storage.url('img/popups/8/5.jpg')
                    }
                ]
            },
            {
                'type': 'credits',
                'title': 'Credits',
                'credits': [
                    {
                        'character': 'Composer',
                        'voiced': [
                            {
                                'title': 'George Leggett'
                            }
                        ]
                    },
                    {
                        'character': 'Sound Designer',
                        'voiced': [
                            {
                                'title': 'Owen Hemming-Brown'
                            }
                        ]
                    },
                    {
                        'character': 'Dialogue, Production ',
                        'voiced': [
                            {
                                'title': 'Tom Gilbert'
                            }
                        ]
                    }
                ],
                'list': [
                    {
                        'character': 'Siri Keeton',
                        'voiced': [
                            {
                                'title': 'Daniel Shapiro'
                            }
                        ]
                    },
                    {
                        'character': 'The Captain',
                        'voiced': [
                            {
                                'title': 'Norelia Rey'
                            }
                        ]
                    },
                    {
                        'character': 'Susan James/Sascha',
                        'voiced': [
                            {
                                'title': 'Natasia Marquez'
                            }
                        ]
                    },
                    {
                        'character': 'Amanda Bates',
                        'voiced': [
                            {
                                'title': 'Victoria Hogan'
                            }
                        ]
                    },
                    {
                        'character': 'Jukka Sarasti',
                        'voiced': [
                            {
                                'title': 'Ron Marasa'
                            }
                        ]
                    },
                    {
                        'character': 'Rorschach',
                        'voiced': [
                            {
                                'title': 'Emma Maidenberg'
                            }
                        ]
                    },
                    {
                        'character': 'Jim More',
                        'voiced': [
                            {
                                'title': 'Troy Hudson'
                            }
                        ]
                    },
                    {
                        'character': 'News Anchors',
                        'voiced': [
                            {
                                'title': 'Bernie Baggarly'
                            },
                            {
                                'title': 'Alessa Ray'
                            },
                            {
                                'title': 'V Lexx'
                            }
                        ]
                    }
                ]
            },
            {
                'type': 'film',
                'video': staticfiles_storage.url('videos/popups/8/film.mp4'),
                'image': staticfiles_storage.url('img/popups/8/film.jpg'),
                'title': 'Soundtrack',
                'caption': 'In the film',
                'button': 'true'
            }
        ],
        'resourcesTitle': '08',
        'resources': [
            {
                'title': 'Number of people involved',
                'value': '3'
            },
            {
                'title': 'Hours Spent',
                'value': '504'
            }
        ],
        'cardImage': staticfiles_storage.url('img/memories/9.jpg'),
        'cardCaption': '09',
        'cardTitle': 'Debrief',
        'slug': '09'
    },
    '09': {
        'shareImage': staticfiles_storage.url('img/share/share-memory09.jpg'),
        'introTitle': 'Debrief',
        'introNumber': '09',
        'introSize': '45.6',
        'introDescription': '4',
        'introText': 'Sometimes it seems as though my whole life\'s been a struggle to reconnect, to regain whatever got lost when my parents killed their only child. Out in the Oort, I finally won that struggle. Thanks to a vampire and a boatload of freaks and an invading alien horde, I\'m Human again. Maybe the last Human. By the time I get home, I could be the only sentient being in the universe.<br><br>If I\'m even that much. Because I don\'t know if there is such a thing as a reliable narrator. And Cunningham said zombies would be pretty good at faking it.<br><br>So I can\'t really tell you, one way or the other.<br><br>You\'ll just have to imagine you\'re Siri Keeton.',
        'blocks': [
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'theme': 'white',
                        'number': 'Danil K-01',
                        'date': '08/09/2020',
                        'text': 'I read Blindsight for the first time in 2009, when it was translated into Russian. It enjoyed cult status in the 3D-design community at the time, and a friend of mine recommended it to me. I was blown away by the amount of technical, scientific, and psychological details Peter Watts packed into the novel, while still keeping it a tense and fascinating read.'
                    },
                    {
                        'theme': 'white',
                        'number': 'Danil K-02',
                        'date': '08/09/2020',
                        'text': 'It felt like it contained enough excellent, thought-provoking ideas for five books, rather than just one. The text was so vivid that reading it felt, to me, like watching a movie inside my head. However, I had no ambitions to make this movie I imagined, since that was obviously an impossible task, so I patiently waited for someone in Hollywood to pick up the story and make it into a movie.'
                    }
                ]
            },
            {
                'type': 'video',
                'background': '15151c',
                'poster': staticfiles_storage.url('img/popups/9/video-poster-1.jpg'),
                'posterHover': staticfiles_storage.url('img/popups/9/video-poster-hover-1.jpg'),
                'video': staticfiles_storage.url('videos/popups/9/8.mp4'),
                'title': 'Danil Krivoruchko',
                'caption': 'Director',
                'file': 'Interview_01.mp4'
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'theme': 'white',
                        'number': 'Danil K-03',
                        'date': '08/09/2020',
                        'text': u'A few years later I decided to give the book another read, this time in English. To my surprise, I found that the novel was freely available to anyone under Creative Commons. I also discovered a link for donations / notes on the author’s site, which I happily took advantage of. I hadn’t expected Peter to respond, but amazingly, he did. After a brief message exchange with him, I reached out to some of my friends in 3D and animation.<br><br>We ended up deciding that making a few renders based off Peter Watts’ book was a good way to show our love for the best sci-fi novel out there.. And that is how this project got started.'
                    },
                    {
                        'theme': 'white',
                        'number': 'Danil K-04',
                        'date': '08/09/2020',
                        'text': u'Initially, we just wanted to make a bunch of still frames. Creating a full CG animated short felt too time-consuming and ambitious. But as time passed, more and more images were made, which helped attract even more incredibly talented people to the project. As the team grew, we realized that we now had enough resources to pull off animation (or so we thought, ha).<br><br>But everyone involved could only participate in the spare time they had between commercial projects, so the work moved quite slowly.'
                    }
                ]
            },
            {
                'type': 'video',
                'background': '15151c',
                'poster': staticfiles_storage.url('img/popups/9/video-poster-2.jpg'),
                'posterHover': staticfiles_storage.url('img/popups/9/video-poster-hover-2.jpg'),
                'video': staticfiles_storage.url('videos/popups/9/9.mp4'),
                'title': 'Peter Watts',
                'caption': 'Writer',
                'file': 'Interview_02.mp4'
            },
            {
                'type': 'chat',
                'largeSize': 'true',
                'chat': [
                    {
                        'theme': 'white',
                        'number': 'Danil K-05',
                        'date': '08/09/2020',
                        'text': 'I began by simply creating a few style-frames and then gradually moving on to animation tests. At a certain point it began seeming as though there might be enough resources to create something beyond just a series of shots. But at the same time, since there was zero financial backing, it was clear that a short with realistic characters, dialogue and a full script was out of the question.<br><br>That was simply not within the realm of possibility for our team.'
                    },
                    {
                        'theme': 'white',
                        'number': 'Danil K-06',
                        'date': '08/09/2020',
                        'text': u'Eventually I landed on the idea of making a mini-short based on the protagonist Siri’s memories and voice-over narration. The entire novel is Siri’s retelling of the events that took place at first contact with a member of an extraterrestrial civilization, so this seemed like a good framework for our short. We chose around 40 key scenes from the book (omitting dialogue) and then whittled the short-list down to 20.'
                    },
                    {
                        'theme': 'white',
                        'number': 'Danil K-07',
                        'date': '08/09/2020',
                        'text': 'After that the overarching structure of the story became clearer - we were going to begin and end on the hero waking from cryo-sleep. In between these framing scenes, we would focus on his memories, which were going to be shown in reverse order - starting with the final battle between Theseus and Rorschach and ending on the first appearance of the Fireflies in the sky of the Earth, the moment when humanity discovered that we are not alone in this universe.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'title': 'First draft',
                'caption': 'Storyboard',
                'file': 'Boards_bw.zip',
                'gallery': [
                    {
                        'backgroundGrid': 'true',
                        'background': '15151c',
                        'image': staticfiles_storage.url('img/popups/9/1.png')
                    }
                ]
            },
            {
                'type': 'chat',
                'smallSize': 'true',
                'chat': [
                    {
                        'theme': 'white',
                        'number': 'Danil K-08',
                        'date': '08/09/2020',
                        'text': u'I was lucky enough to get to work with an extremely talented storyboard artist in the early stages of the project. Now that we have the final short, it’s curious to see how closely every shot resembles her initial sketches, made 4 years earlier.<br><br>When the content of each shot was clear we moved on to previs, which would make editing the scenes’ layouts, animation and camera movements much easier. This is also where the video editor got involved - I kept updating the previs until everyone was happy with the overall rhythm and montage.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'centeredGallery': 'true',
                'showZoom': 'true',
                'title': 'Final',
                'caption': 'Storyboard',
                'file': 'Boards_tory_final.zip',
                'gallery': [
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/1.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/2.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/3.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/4.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/5.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/6.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/7.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/8.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/9.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/10.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/11.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/12.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/13.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/14.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/15.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/16.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/17.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/18.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/19.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/20.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/21.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/22.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/23.jpg')
                    }
                ]
            },
            {
                'type': 'gallery',
                'centeredGallery': 'true',
                'videoGallery': 'true',
                'title': 'Sample scenes',
                'caption': 'Previzualization',
                'file': 'Previz_015_03_02.zip',
                'gallery': [
                    {
                        'backgroundGrid': 'true',
                        'background': '15151c',
                        'video': staticfiles_storage.url('videos/popups/9/1.mp4'),
                        'image': staticfiles_storage.url('img/popups/9/v1.jpg')
                    },
                    {
                        'backgroundGrid': 'true',
                        'background': '15151c',
                        'video': staticfiles_storage.url('videos/popups/9/2.mp4'),
                        'image': staticfiles_storage.url('img/popups/9/v2.jpg')
                    },
                    {
                        'backgroundGrid': 'true',
                        'background': '15151c',
                        'video': staticfiles_storage.url('videos/popups/9/3.mp4'),
                        'image': staticfiles_storage.url('img/popups/9/v3.jpg')
                    },
                    {
                        'backgroundGrid': 'true',
                        'background': '15151c',
                        'video': staticfiles_storage.url('videos/popups/9/4.mp4'),
                        'image': staticfiles_storage.url('img/popups/9/v4.jpg')
                    },
                    {
                        'backgroundGrid': 'true',
                        'background': '15151c',
                        'video': staticfiles_storage.url('videos/popups/9/5.mp4'),
                        'image': staticfiles_storage.url('img/popups/9/v5.jpg')
                    },
                    {
                        'backgroundGrid': 'true',
                        'background': '15151c',
                        'video': staticfiles_storage.url('videos/popups/9/6.mp4'),
                        'image': staticfiles_storage.url('img/popups/9/v6.jpg')
                    },
                    {
                        'backgroundGrid': 'true',
                        'background': '15151c',
                        'video': staticfiles_storage.url('videos/popups/9/7.mp4'),
                        'image': staticfiles_storage.url('img/popups/9/v7.jpg')
                    }
                ]
            },
            {
                'type': 'chat',
                'mediumSize': 'true',
                'chat': [
                    {
                        'theme': 'white',
                        'number': 'Danil K-09',
                        'date': '08/09/2020',
                        'text': u'Next came the most time-consuming part of the process - each scene required detailed modeling, realistic materials for each of the objects and animation of these objects and the characters. For certain shots this process ended up taking over a year.<br><br>Then all these scenes needed to be rendered. A four-and-a-half minute animation is no joke, when rendering certain frames takes up to 15-20 minutes. Since there was no budget, render-farms were not an option, so almost all the scenes were rendered at home, at night, on my personal computer. The rendering alone took around a month and a half of pure computation, at the very least.'
                    },
                    {
                        'theme': 'white',
                        'number': 'Danil K-10',
                        'date': '08/09/2020',
                        'text': 'When we finished the rendering and shot compositing, the video editor went over the whole thing again, checking and tightening every cut. And finally, each shot went through color-correction, in order to unify all the color schemes and set the tone for the entire film.'
                    }
                ]
            },
            {
                'type': 'gallery',
                'centeredGallery': 'true',
                'showZoom': 'true',
                'title': 'Final frames',
                'caption': 'Color grading',
                'file': 'Bs_cc.zip',
                'gallery': [
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/24.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/25.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/26.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/27.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/28.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/29.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/30.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/31.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/32.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/33.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/34.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/35.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/36.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/37.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/38.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/39.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/40.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/41.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/42.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/43.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/44.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/45.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/46.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/47.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/48.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/49.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/50.jpg')
                    },
                    {
                        'fill': 'cover',
                        'backgroundGrid': 'true',
                        'background': '62656d',
                        'image': staticfiles_storage.url('img/popups/9/51.jpg')
                    }
                ]
            },
            # {
            #     'type': 'video',
            #     'background': '111619',
            #     'video': staticfiles_storage.url('videos/popups/4/film.mp4'),
            #     'title': 'Echoic audio',
            #     'caption': 'Sound design',
            #     'file': 'Interview_03.mp4'
            # },
            {
                'type': 'acknowledgements',
                'acknowledgementsColumns': [
                    {
                        'acknowledgements': [
                            {
                                'name': 'Peter Watts',
                                'link': 'https://www.rifters.com/',
                                'text': u'Thank you for writing the best sci-fi novel I ever read (I mean it!). And for your patience, willingness to answer my endless questions about the most granular details of your book and the positive feedback you provided at each stage. And apologies for my many “it’s too early”’s in response to your requests to publish the drafts we sent you.'
                            },
                            {
                                'name': 'Viktoriya Yakubova',
                                'link': 'https://vimeo.com/umukusum',
                                'text': 'For editing the film, but first and foremost for supporting me throughout these last four years. Without you I would have given up after month one.'
                            },
                            {
                                'name': 'Echoic Audio',
                                'link': 'https://echoicaudio.com/',
                                'text': u'For turning my 30-page, written in broken English brief into one of the most atmospheric scores I’d ever heard. Seeing the film with your sound for the first time ever, I could hardly believe that this was a project I was actually working on. It was incredible!'
                            },
                            {
                                'name': 'The developers of Redshift renderer',
                                'link': 'https://www.redshift3d.com/',
                                'text': 'Without you we could not have physically dealt with these kinds of volumes. Plus you gifted us a year-long license, so thank you squared!'
                            },
                            {
                                'name': 'Artem Otvodenkov',
                                'link': 'https://www.behance.net/mrOmvod',
                                'text': u'For interface animation in the space-suit. The task was way too simple for you, next time we’ll go full throttle :)'
                            }
                        ]
                    },
                    {
                        'acknowledgements': [
                            {
                                'name': 'Dennis Khramov',
                                'link': 'https://www.behance.net/hramovsky',
                                'text': u'for designing the HUD interface in the space-suit. I know you only got to do half of what you could have, since I was constantly asking for things to be simplified.'
                            },
                            {
                                'name': 'Evgeny Kashin',
                                'link': 'https://www.artstation.com/gr1n',
                                'text': 'For the concept art for the space-suit and bots. We were incredibly lucky to have you with us from the start. Thank you for believing in this project, even when we had barely anything to show for it.'
                            },
                            {
                                'name': 'Ivan Khomenko',
                                'link': 'https://www.artstation.com/hamen',
                                'text': 'For the concept of Sarasti and Bates. Creating the appearance of a convincing, genetically-reborn vampire is quite the challenge!'
                            },
                            {
                                'name': 'Jama Jurabaev',
                                'link': 'https://jamajurabaev.com/',
                                'text': u'For giving us the shuttle concept. I remember how surprised you were afterwards at how long it took us to create a production-ready model based off your work - that’s how we roll :)'
                            },
                            {
                                'name': 'Tory Sica',
                                'link': 'http://www.torysica.com/',
                                'text': u'For the insanely cool storyboards. We had to work extremely hard to have our shots look as good as your boards (Which you made in just a few days. Life is so unfair!)'
                            }
                        ]
                    },
                    {
                        'acknowledgements': [
                            {
                                'name': 'Alex Malets',
                                'link': 'https://www.artstation.com/splendidfennel',
                                'text': 'The only one on our team who knew what to do with organic modeling. Without you, Sarasti would have remained a 2D concept and Siri would never have existed at all.'
                            },
                            {
                                'name': 'Andrei Korovkin',
                                'link': 'https://www.artstation.com/akorovkin',
                                'text': u'For help with modeling all of the textile parts of the space suit. Seeing your model made me wish the entire space suit consisted of textiles, too bad that wasn’t possible according to the script :)'
                            },
                            {
                                'name': 'Dimos Hadjisavvas',
                                'link': 'https://dimoshadji.com/',
                                'text': u'For modeling Theseus’ interior spine and for help with the final details of the shuttle. It was such a pleasure seeing how skilfully you handled the problems thrown at you. We were lucky to have someone on our team as experienced as you at working on shorts.'
                            },
                            {
                                'name': 'Ivan Makarkoff',
                                'link': 'https://www.artstation.com/makarkoff',
                                'text': u'As if making most of the Theseus model wasn’t enough (just a piddling 60 million polygons!) you also helped us with elements of the shuttle’s interior, the space suit, and the inside of its helmet. Thank you!'
                            },
                            {
                                'name': 'Kirill Stupin',
                                'link': 'https://www.behance.net/simplewolf',
                                'text': u'For assisting in modeling the bot. I’m super happy with the result, no matter what you say! :)'
                            }
                        ]
                    },
                    {
                        'acknowledgements': [
                            {
                                'name': 'Serge Aleynikov',
                                'link': 'https://alsens.net/',
                                'text': u'For doing most of the modeling work on the space suit. If you hadn’t set us straight, the characters would still be wearing a weird mix of scuba diving gear and the Power armor from Fallout :)'
                            },
                            {
                                'name': 'Slava Kislyakov',
                                'link': 'https://www.instagram.com/bondjo/',
                                'text': u'For modeling the shuttle. You’re responsible for around 60% of the model and those are undoubtedly its best 60%!'
                            },
                            {
                                'name': 'Valentine Sorokin',
                                'link': 'https://www.artstation.com/sorokin',
                                'text': 'For help with parts of the shuttle and for the models you gave us which came in really handy with the bot.'
                            },
                            {
                                'name': 'Alexey Cheprakov',
                                'link': 'https://www.behance.net/cheprakov',
                                'text': u'I don’t know how many billion voxels were in the simulation of Ben’s atmosphere or how long it took to render the entire thing - but I do know that without you this shot would simply have not existed.'
                            },
                            {
                                'name': 'Dmitry Kulikov',
                                'link': 'https://www.behance.net/vellocet',
                                'text': u'Theseus’ appearance in the shots on Earth’s and Ben’s orbits is wholly your doing.. Plus you joined the project at a point where I was ready to give it all up, but your enthusiasm drove me to go on. Thank you!'
                            }
                        ]
                    },
                    {
                        'acknowledgements': [
                            {
                                'name': 'Max Chelyadnikov ',
                                'link': 'https://www.behance.net/maxchell',
                                'text': u'For the excellent compositing of several shots and priceless advice on the compositing of the rest. Without your pages and pages of instructions on Telegram everything would have definitely ended up looking a lot worse.'
                            },
                            {
                                'name': 'Maxim Goudin',
                                'link': 'https://maximgoudin.com',
                                'text': 'For the shot with the Fireflies above the city. I do not know anybody who is capable of making an architectural shot better than you.'
                            },
                            {
                                'name': 'Maxim Gureev',
                                'link': 'https://vimeo.com/user1505374',
                                'text': u'For animating the astronaut in the shot where my animation skills had fallen short even at the previs stage, let alone the final animation.'
                            },
                            {
                                'name': 'Sasha Vinogradova',
                                'link': 'http://www.sashavinogradova.com/',
                                'text': u'For Sarasti’s outfit and animation. I can imagine the pain of animating the outfits for long shots in Marvelous - thank you for agreeing to go through that.'
                            },
                            {
                                'name': u'Аnya Formozova',
                                'link': 'https://www.anyaformozova.com/',
                                'text': u'For turning my faltering speech into what you are reading now.'
                            }
                        ]
                    },
                    {
                        'acknowledgements': [
                            {
                                'name': 'Anton Repponen',
                                'link': 'http://repponen.com/',
                                'text': u'For the site’s design and for attention to detail. Judging by the volume of work required, another person might have taken as long to do this as it took us to make the entire film, but you managed to do it in just a few weeks.'
                            },
                            {
                                'name': 'Astroshock',
                                'link': 'http://astroshock.ru/',
                                'text': u'For developing the site. I remember the moment when you responded to my post saying “if we find a developer, there might be a site” by saying, “Danya, WE’LL do the site!”. From that moment on I knew that when it came to the quality of the website development there was nothing to worry about.'
                            }
                        ]
                    }
                ]
            }
        ],
        'cardImage': staticfiles_storage.url('img/memories/1.jpg'),
        'cardCaption': '01',
        'cardTitle': 'Space suit',
        'slug': '01'
    }
}