/*
Tipue Search 4.0
Copyright (c) 2014 Tipue
Tipue Search is released under the MIT License
http://www.tipue.com/search
*/


var tipuesearch_stop_words = ["and", "be", "by", "do", "for", "he", "how", "if", "is", "it", "my", "not", "of", "or", "the", "to", "up", "what", "when"];

var tipuesearch_replace = {
    "words": [
        {
            "word": "tipua",
            "replace_with": "tipue"
        },
        {
            "word": "javscript",
            "replace_with": "javascript"
        }
]
};

var tipuesearch_stem = {
    "words": [
        {
            "word": "e-mail",
            "stem": "email"
        },
        {
            "word": "javascript",
            "stem": "script"
        },
        {
            "word": "javascript",
            "stem": "js"
        }
]
};

var home_dir = "http://localhost/bitsgoacc/";
var tipuesearch_pages = [
                            home_dir + "index.html?sub=computer-centre",
                            home_dir + "index.html?sub=computer-lab",
                            home_dir + "index.html?sub=auditorium",
                            home_dir + "index.html?sub=tele-presence",
                            home_dir + "index.html?sub=server-room",
                            home_dir + "index.html?sub=server-room",
                            home_dir + "index.html?sub=server-room",
                            home_dir + "index.html?sub=server-room"
                        ]