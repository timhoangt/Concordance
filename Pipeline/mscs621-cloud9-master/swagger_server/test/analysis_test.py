import test_apis
import json

def short_string_test():
    input = "The quick brown fox jumped over the lazy dog"
    expected_output = {
        "input": input,
        "concordance": [
            {
              "count": 1,
              "token": "brown"
            },
            {
              "count": 1,
              "token": "dog"
            },
            {
              "count": 1,
              "token": "fox"
            },
            {
              "count": 1,
              "token": "jumped"
            },
            {
              "count": 1,
              "token": "lazy"
            },
            {
              "count": 1,
              "token": "over"
            },
            {
              "count": 1,
              "token": "quick"
            },
            {
              "count": 2,
              "token": "the"
            }
        ]
    }

    result = test_apis.test_analysis(input, expected_output)
    return result

def medium_string_test():
    input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Vitae ultricies leo integer malesuada nunc vel. Ac turpis egestas sed tempus. Hendrerit gravida rutrum quisque non tellus orci. Pellentesque habitant morbi tristique senectus. Felis eget velit aliquet sagittis id consectetur purus ut. Quam viverra orci sagittis eu volutpat. At quis risus sed vulputate odio ut enim blandit. Tincidunt augue interdum velit euismod in pellentesque massa. Dapibus ultrices in iaculis nunc sed augue lacus. Vitae purus faucibus ornare suspendisse sed. Id porta nibh venenatis cras sed felis eget velit aliquet. Lectus sit amet est placerat in egestas erat imperdiet. Eros donec ac odio tempor orci dapibus ultrices in. In tellus integer feugiat scelerisque varius morbi enim nunc faucibus. Habitasse platea dictumst quisque sagittis. Enim nunc faucibus a pellentesque sit." \
"Eget egestas purus viverra accumsan in nisl nisi scelerisque. Egestas integer eget aliquet nibh praesent tristique. Malesuada nunc vel risus commodo viverra maecenas. Turpis tincidunt id aliquet risus feugiat in ante. Aliquam ut porttitor leo a diam sollicitudin tempor id eu. Nisi vitae suscipit tellus mauris a diam maecenas sed enim. Cras adipiscing enim eu turpis egestas pretium aenean. Morbi tristique senectus et netus. Porta lorem mollis aliquam ut porttitor leo a diam. Metus vulputate eu scelerisque felis imperdiet proin fermentum. Sed sed risus pretium quam vulputate dignissim suspendisse in. Urna et pharetra pharetra massa massa ultricies mi quis. At augue eget arcu dictum varius duis. Sed augue lacus viverra vitae congue eu consequat ac felis. Enim praesent elementum facilisis leo vel fringilla est. Vel fringilla est ullamcorper eget nulla facilisi etiam." \
"Mauris pharetra et ultrices neque ornare aenean euismod elementum. Ultricies integer quis auctor elit. Nulla at volutpat diam ut. Mauris nunc congue nisi vitae suscipit tellus mauris. Quis enim lobortis scelerisque fermentum dui faucibus in ornare. Odio facilisis mauris sit amet massa vitae tortor condimentum. Laoreet suspendisse interdum consectetur libero id. In hac habitasse platea dictumst. Orci nulla pellentesque dignissim enim sit amet venenatis. Sagittis nisl rhoncus mattis rhoncus urna neque viverra. Tellus at urna condimentum mattis pellentesque id nibh tortor. Id neque aliquam vestibulum morbi blandit cursus risus at ultrices. Viverra mauris in aliquam sem. Nulla posuere sollicitudin aliquam ultrices. Ullamcorper eget nulla facilisi etiam dignissim. Ipsum dolor sit amet consectetur adipiscing elit duis tristique. Turpis massa sed elementum tempus. Sociis natoque penatibus et magnis dis parturient montes." \
"Faucibus in ornare quam viverra orci sagittis. Neque aliquam vestibulum morbi blandit. Massa sapien faucibus et molestie ac feugiat. Pulvinar elementum integer enim neque volutpat. Scelerisque viverra mauris in aliquam sem fringilla ut. Porta nibh venenatis cras sed felis eget. In hac habitasse platea dictumst quisque sagittis purus sit amet. Auctor augue mauris augue neque gravida in fermentum et sollicitudin. Et tortor at risus viverra adipiscing at in tellus integer. Tortor at auctor urna nunc id. Cras semper auctor neque vitae tempus quam. Laoreet id donec ultrices tincidunt arcu non sodales neque. Scelerisque eu ultrices vitae auctor." \
"Pellentesque habitant morbi tristique senectus. Velit ut tortor pretium viverra suspendisse potenti nullam ac. Dignissim enim sit amet venenatis. Congue eu consequat ac felis donec et odio. Nunc consequat interdum varius sit amet mattis vulputate. Et pharetra pharetra massa massa ultricies mi quis hendrerit. Nulla pharetra diam sit amet nisl suscipit adipiscing. Pretium viverra suspendisse potenti nullam ac tortor vitae. Accumsan sit amet nulla facilisi morbi tempus. Dignissim suspendisse in est ante in nibh mauris cursus. Curabitur gravida arcu ac tortor dignissim convallis." \
"Felis donec et odio pellentesque diam volutpat commodo. Felis eget velit aliquet sagittis. Habitant morbi tristique senectus et netus et malesuada. Pellentesque dignissim enim sit amet venenatis urna cursus. Enim sed faucibus turpis in eu mi. Ullamcorper malesuada proin libero nunc. Pulvinar pellentesque habitant morbi tristique senectus et. Cras semper auctor neque vitae tempus quam pellentesque nec nam. Vitae ultricies leo integer malesuada nunc vel. Felis eget nunc lobortis mattis. Pretium lectus quam id leo in. Lacus sed viverra tellus in hac. Sit amet consectetur adipiscing elit ut aliquam purus. Eu nisl nunc mi ipsum faucibus vitae aliquet." \
"Amet justo donec enim diam vulputate ut pharetra sit amet. Morbi leo urna molestie at elementum. Posuere sollicitudin aliquam ultrices sagittis orci a scelerisque. Orci eu lobortis elementum nibh tellus molestie. Venenatis tellus in metus vulputate eu scelerisque. Pellentesque elit eget gravida cum sociis natoque penatibus. Morbi enim nunc faucibus a pellentesque sit amet porttitor. Urna id volutpat lacus laoreet non curabitur gravida arcu ac. Rhoncus mattis rhoncus urna neque viverra. Id cursus metus aliquam eleifend mi in nulla posuere. Facilisis volutpat est velit egestas dui id ornare arcu odio. Faucibus scelerisque eleifend donec pretium vulputate sapien nec sagittis. Semper risus in hendrerit gravida rutrum quisque non. Facilisis sed odio morbi quis commodo odio. Faucibus ornare suspendisse sed nisi lacus. Dictumst quisque sagittis purus sit amet." \
"Molestie ac feugiat sed lectus vestibulum. Non nisi est sit amet facilisis magna etiam. Fusce id velit ut tortor pretium. Lectus nulla at volutpat diam ut venenatis tellus in. Mauris rhoncus aenean vel elit scelerisque mauris pellentesque pulvinar pellentesque. Eget magna fermentum iaculis eu non diam phasellus vestibulum. Aenean vel elit scelerisque mauris. In nibh mauris cursus mattis. Vitae et leo duis ut diam quam nulla. Pellentesque elit eget gravida cum sociis natoque penatibus et. Nam aliquam sem et tortor consequat." \
"Purus viverra accumsan in nisl. In egestas erat imperdiet sed euismod nisi porta lorem. Urna et pharetra pharetra massa. Ipsum faucibus vitae aliquet nec ullamcorper. Cursus turpis massa tincidunt dui. Nunc mi ipsum faucibus vitae aliquet nec ullamcorper sit. Neque viverra justo nec ultrices dui. Commodo ullamcorper a lacus vestibulum. Amet porttitor eget dolor morbi non arcu risus quis. Dolor morbi non arcu risus. A cras semper auctor neque vitae tempus quam pellentesque. Eget gravida cum sociis natoque. Diam donec adipiscing tristique risus nec feugiat. Pretium vulputate sapien nec sagittis." \
"Blandit volutpat maecenas volutpat blandit aliquam. Lorem mollis aliquam ut porttitor. Cras fermentum odio eu feugiat. Augue ut lectus arcu bibendum at varius. Urna cursus eget nunc scelerisque. Eu scelerisque felis imperdiet proin fermentum leo vel orci. Eget sit amet tellus cras adipiscing enim eu turpis egestas. Quis eleifend quam adipiscing vitae. Amet consectetur adipiscing elit pellentesque. Mi sit amet mauris commodo quis. Tincidunt praesent semper feugiat nibh sed pulvinar proin gravida."

    expected_output = {
        "input": input,
        "concordance": [
                {
                  "count": 8,
                  "token": "a"
                },
                {
                  "count": 10,
                  "token": "ac"
                },
                {
                  "count": 3,
                  "token": "accumsan"
                },
                {
                  "count": 10,
                  "token": "adipiscing"
                },
                {
                  "count": 4,
                  "token": "aenean"
                },
                {
                  "count": 1,
                  "token": "aliqua"
                },
                {
                  "count": 13,
                  "token": "aliquam"
                },
                {
                  "count": 8,
                  "token": "aliquet"
                },
                {
                  "count": 21,
                  "token": "amet"
                },
                {
                  "count": 2,
                  "token": "ante"
                },
                {
                  "count": 8,
                  "token": "arcu"
                },
                {
                  "count": 11,
                  "token": "at"
                },
                {
                  "count": 7,
                  "token": "auctor"
                },
                {
                  "count": 7,
                  "token": "augue"
                },
                {
                  "count": 1,
                  "token": "bibendum"
                },
                {
                  "count": 5,
                  "token": "blandit"
                },
                {
                  "count": 5,
                  "token": "commodo"
                },
                {
                  "count": 2,
                  "token": "condimentum"
                },
                {
                  "count": 3,
                  "token": "congue"
                },
                {
                  "count": 6,
                  "token": "consectetur"
                },
                {
                  "count": 4,
                  "token": "consequat"
                },
                {
                  "count": 1,
                  "token": "convallis"
                },
                {
                  "count": 8,
                  "token": "cras"
                },
                {
                  "count": 3,
                  "token": "cum"
                },
                {
                  "count": 2,
                  "token": "curabitur"
                },
                {
                  "count": 7,
                  "token": "cursus"
                },
                {
                  "count": 2,
                  "token": "dapibus"
                },
                {
                  "count": 11,
                  "token": "diam"
                },
                {
                  "count": 1,
                  "token": "dictum"
                },
                {
                  "count": 4,
                  "token": "dictumst"
                },
                {
                  "count": 7,
                  "token": "dignissim"
                },
                {
                  "count": 1,
                  "token": "dis"
                },
                {
                  "count": 1,
                  "token": "do"
                },
                {
                  "count": 4,
                  "token": "dolor"
                },
                {
                  "count": 1,
                  "token": "dolore"
                },
                {
                  "count": 7,
                  "token": "donec"
                },
                {
                  "count": 4,
                  "token": "dui"
                },
                {
                  "count": 3,
                  "token": "duis"
                },
                {
                  "count": 8,
                  "token": "egestas"
                },
                {
                  "count": 17,
                  "token": "eget"
                },
                {
                  "count": 1,
                  "token": "eiusmod"
                },
                {
                  "count": 3,
                  "token": "eleifend"
                },
                {
                  "count": 6,
                  "token": "elementum"
                },
                {
                  "count": 9,
                  "token": "elit"
                },
                {
                  "count": 15,
                  "token": "enim"
                },
                {
                  "count": 2,
                  "token": "erat"
                },
                {
                  "count": 1,
                  "token": "eros"
                },
                {
                  "count": 6,
                  "token": "est"
                },
                {
                  "count": 18,
                  "token": "et"
                },
                {
                  "count": 3,
                  "token": "etiam"
                },
                {
                  "count": 15,
                  "token": "eu"
                },
                {
                  "count": 3,
                  "token": "euismod"
                },
                {
                  "count": 3,
                  "token": "facilisi"
                },
                {
                  "count": 5,
                  "token": "facilisis"
                },
                {
                  "count": 13,
                  "token": "faucibus"
                },
                {
                  "count": 10,
                  "token": "felis"
                },
                {
                  "count": 6,
                  "token": "fermentum"
                },
                {
                  "count": 7,
                  "token": "feugiat"
                },
                {
                  "count": 3,
                  "token": "fringilla"
                },
                {
                  "count": 1,
                  "token": "fusce"
                },
                {
                  "count": 9,
                  "token": "gravida"
                },
                {
                  "count": 4,
                  "token": "habitant"
                },
                {
                  "count": 3,
                  "token": "habitasse"
                },
                {
                  "count": 3,
                  "token": "hac"
                },
                {
                  "count": 3,
                  "token": "hendrerit"
                },
                {
                  "count": 2,
                  "token": "iaculis"
                },
                {
                  "count": 14,
                  "token": "id"
                },
                {
                  "count": 4,
                  "token": "imperdiet"
                },
                {
                  "count": 28,
                  "token": "in"
                },
                {
                  "count": 1,
                  "token": "incididunt"
                },
                {
                  "count": 7,
                  "token": "integer"
                },
                {
                  "count": 3,
                  "token": "interdum"
                },
                {
                  "count": 5,
                  "token": "ipsum"
                },
                {
                  "count": 2,
                  "token": "justo"
                },
                {
                  "count": 1,
                  "token": "labore"
                },
                {
                  "count": 6,
                  "token": "lacus"
                },
                {
                  "count": 3,
                  "token": "laoreet"
                },
                {
                  "count": 5,
                  "token": "lectus"
                },
                {
                  "count": 9,
                  "token": "leo"
                },
                {
                  "count": 2,
                  "token": "libero"
                },
                {
                  "count": 3,
                  "token": "lobortis"
                },
                {
                  "count": 4,
                  "token": "lorem"
                },
                {
                  "count": 3,
                  "token": "maecenas"
                },
                {
                  "count": 3,
                  "token": "magna"
                },
                {
                  "count": 1,
                  "token": "magnis"
                },
                {
                  "count": 5,
                  "token": "malesuada"
                },
                {
                  "count": 10,
                  "token": "massa"
                },
                {
                  "count": 6,
                  "token": "mattis"
                },
                {
                  "count": 14,
                  "token": "mauris"
                },
                {
                  "count": 3,
                  "token": "metus"
                },
                {
                  "count": 7,
                  "token": "mi"
                },
                {
                  "count": 4,
                  "token": "molestie"
                },
                {
                  "count": 2,
                  "token": "mollis"
                },
                {
                  "count": 1,
                  "token": "montes"
                },
                {
                  "count": 14,
                  "token": "morbi"
                },
                {
                  "count": 2,
                  "token": "nam"
                },
                {
                  "count": 4,
                  "token": "natoque"
                },
                {
                  "count": 7,
                  "token": "nec"
                },
                {
                  "count": 12,
                  "token": "neque"
                },
                {
                  "count": 2,
                  "token": "netus"
                },
                {
                  "count": 8,
                  "token": "nibh"
                },
                {
                  "count": 6,
                  "token": "nisi"
                },
                {
                  "count": 5,
                  "token": "nisl"
                },
                {
                  "count": 8,
                  "token": "non"
                },
                {
                  "count": 10,
                  "token": "nulla"
                },
                {
                  "count": 2,
                  "token": "nullam"
                },
                {
                  "count": 15,
                  "token": "nunc"
                },
                {
                  "count": 9,
                  "token": "odio"
                },
                {
                  "count": 8,
                  "token": "orci"
                },
                {
                  "count": 6,
                  "token": "ornare"
                },
                {
                  "count": 1,
                  "token": "parturient"
                },
                {
                  "count": 17,
                  "token": "pellentesque"
                },
                {
                  "count": 3,
                  "token": "penatibus"
                },
                {
                  "count": 9,
                  "token": "pharetra"
                },
                {
                  "count": 1,
                  "token": "phasellus"
                },
                {
                  "count": 1,
                  "token": "placerat"
                },
                {
                  "count": 3,
                  "token": "platea"
                },
                {
                  "count": 4,
                  "token": "porta"
                },
                {
                  "count": 5,
                  "token": "porttitor"
                },
                {
                  "count": 3,
                  "token": "posuere"
                },
                {
                  "count": 2,
                  "token": "potenti"
                },
                {
                  "count": 3,
                  "token": "praesent"
                },
                {
                  "count": 8,
                  "token": "pretium"
                },
                {
                  "count": 4,
                  "token": "proin"
                },
                {
                  "count": 4,
                  "token": "pulvinar"
                },
                {
                  "count": 7,
                  "token": "purus"
                },
                {
                  "count": 9,
                  "token": "quam"
                },
                {
                  "count": 9,
                  "token": "quis"
                },
                {
                  "count": 5,
                  "token": "quisque"
                },
                {
                  "count": 5,
                  "token": "rhoncus"
                },
                {
                  "count": 10,
                  "token": "risus"
                },
                {
                  "count": 2,
                  "token": "rutrum"
                },
                {
                  "count": 11,
                  "token": "sagittis"
                },
                {
                  "count": 3,
                  "token": "sapien"
                },
                {
                  "count": 13,
                  "token": "scelerisque"
                },
                {
                  "count": 19,
                  "token": "sed"
                },
                {
                  "count": 3,
                  "token": "sem"
                },
                {
                  "count": 5,
                  "token": "semper"
                },
                {
                  "count": 5,
                  "token": "senectus"
                },
                {
                  "count": 20,
                  "token": "sit"
                },
                {
                  "count": 4,
                  "token": "sociis"
                },
                {
                  "count": 1,
                  "token": "sodales"
                },
                {
                  "count": 4,
                  "token": "sollicitudin"
                },
                {
                  "count": 3,
                  "token": "suscipit"
                },
                {
                  "count": 7,
                  "token": "suspendisse"
                },
                {
                  "count": 11,
                  "token": "tellus"
                },
                {
                  "count": 3,
                  "token": "tempor"
                },
                {
                  "count": 6,
                  "token": "tempus"
                },
                {
                  "count": 5,
                  "token": "tincidunt"
                },
                {
                  "count": 9,
                  "token": "tortor"
                },
                {
                  "count": 8,
                  "token": "tristique"
                },
                {
                  "count": 7,
                  "token": "turpis"
                },
                {
                  "count": 6,
                  "token": "ullamcorper"
                },
                {
                  "count": 9,
                  "token": "ultrices"
                },
                {
                  "count": 5,
                  "token": "ultricies"
                },
                {
                  "count": 10,
                  "token": "urna"
                },
                {
                  "count": 15,
                  "token": "ut"
                },
                {
                  "count": 4,
                  "token": "varius"
                },
                {
                  "count": 8,
                  "token": "vel"
                },
                {
                  "count": 7,
                  "token": "velit"
                },
                {
                  "count": 7,
                  "token": "venenatis"
                },
                {
                  "count": 5,
                  "token": "vestibulum"
                },
                {
                  "count": 17,
                  "token": "vitae"
                },
                {
                  "count": 15,
                  "token": "viverra"
                },
                {
                  "count": 9,
                  "token": "volutpat"
                },
                {
                  "count": 8,
                  "token": "vulputate"
                }
              ]
    }

    result = test_apis.test_analysis(input, expected_output)
    return result

def large_string_test():
    input = open('./swagger_server/test/resources/mobydick.txt', 'r')
    with open('./swagger_server/test/resources/analysis_expected.json', 'r') as data:
        expected_output = json.load(data)

    result = test_apis.test_analysis(input, expected_output)
    return result


def run_tests():
    if (short_string_test()):
        print("\tShort String\t\t\tSuccess")
    else:
        print("\tShort String\t\t\tFailed")

    if (medium_string_test()):
        print("\tMedium String\t\t\tSuccess")
    else:
        print("\tMedium String\t\t\tFailed")

    if (large_string_test()):
        print("\tLarge String\t\t\tSuccess")
    else:
        print("\tLarge String\t\t\tFailed")