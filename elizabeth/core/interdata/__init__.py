# Here you can see data that used in all locales.
# interdata is abbreviation of "International Data".

from .address import *
from .code import *
from .development import *
from .hardware import *
from .internet import *
from .path import *
from .structured import *
from .transport import *

# Dictionary for romanize decorator.
ROMANIZATION_ALPHABETS = {
    'ru': {
        "А": "A", "а": "a",
        "Б": "B", "б": "b",
        "В": "V", "в": "v",
        "Г": "G", "г": "g",
        "Д": "D", "д": "d",
        "Е": "E", "е": "e",
        "Ё": "YO", "ё": "yo",
        "Ж": "ZH", "ж": "zh",
        "З": "Z", "з": "z",
        "И": "I", "и": "i",
        "Й": "YE", "й": "ye",
        "К": "K", "к": "k",
        "Л": "L", "л": "l",
        "М": "M", "м": "m",
        "Н": "N", "н": "n",
        "О": "O", "о": "o",
        "П": "P", "п": "p",
        "Р": "R", "р": "r",
        "С": "S", "с": "s",
        "Т": "T", "т": "t",
        "У": "U", "у": "у",
        "Ф": "F", "ф": "f",
        "Х": "KH", "х": "kh",
        "Ц": "TS", "ц": "ts",
        "Ч": "CH", "ч": "ch",
        "Ш": "SH", "ш": "sh",
        "Щ": "SHCH", "щ": "shch",
        "Ъ": "", "ъ": "",
        "Ы": "Y", "ы": "y",
        "Ь": "", "ь": "",
        "Э": "E", "э": "e",
        "Ю": "YU", "ю": "yu",
        "Я": "JA", "я": "ja",
        'ый': 'y', 'ЫЙ': 'Y',
        'ий': 'y', 'ИЙ': 'Y',
        'ые': 'ye', 'ЫЕ': 'YE',
        ' ': ' '
    }
}

CURRENCY = [
    "AED",
    "AFN",
    "ALL",
    "ARS",
    "ATS",
    "AUD",
    "AUD",
    "BBD",
    "BDT",
    "BEF",
    "BGN",
    "BHD",
    "BMD",
    "BRL",
    "BSD",
    "CAD",
    "CAD",
    "CHF",
    "CHF",
    "CLP",
    "CNY",
    "CNY",
    "COP",
    "CRC",
    "CYP",
    "CZK",
    "DEM",
    "DEM",
    "DKK",
    "DOP",
    "DZD",
    "EEK",
    "EGP",
    "ESP",
    "EUR",
    "FIM",
    "FJD",
    "FRF",
    "GBP",
    "GBP",
    "GRD",
    "HKD",
    "HRK",
    "HUF",
    "IDR",
    "IEP",
    "ILS",
    "INR",
    "INR",
    "IQD",
    "IRR",
    "ISK",
    "ITL",
    "JMD",
    "JOD",
    "JPY",
    "JPY",
    "KES",
    "KRW",
    "KRW",
    "KWD",
    "LBP",
    "LKR",
    "LUF",
    "MAD",
    "MTL",
    "MUR",
    "MXN",
    "MYR",
    "NLG",
    "NLG",
    "NLG",
    "NOK",
    "NZD",
    "NZD",
    "OMR",
    "PEN",
    "PHP",
    "PKR",
    "PLN",
    "PTE",
    "QAR",
    "ROL",
    "RON",
    "RUB",
    "SAR",
    "SDG",
    "SEK",
    "SGD",
    "SIT",
    "SKK",
    "THB",
    "TND",
    "TRY",
    "TTD",
    "TWD",
    "USD",
    "USD",
    "USD",
    "VEB",
    "VEF",
    "VND",
    "XAF",
    "XAF",
    "XAG",
    "XAG",
    "XAU",
    "XAU",
    "XAU",
    "XCD",
    "XCD",
    "XDR",
    "XDR",
    "XDR",
    "XOF",
    "XOF",
    "XPD",
    "XPD",
    "XPF",
    "XPF",
    "XPT",
    "XPT",
    "ZAR",
    "ZAR",
    "ZMK"
]

ROMAN_NUMS = [
    'I',
    'II',
    'III',
    'IV',
    'V',
    'VI',
    'VII',
    'VIII',
    'IX',
    'X',
    'XI',
    'XII',
    'XIII',
    'XIV',
    'XV',
    'XVI',
    'XVII',
    'XVIII',
    'XIX',
    'XX',
    'XXI'
]

EXTENSIONS = {
    "source": [
        ".a",
        ".asm",
        ".asp",
        ".awk",
        ".c",
        ".class",
        ".cpp",
        ".pl",
        ".js",
        ".java",
        ".clj",
        ".py",
        ".rb",
        ".hs",
        ".erl",
        ".rs",
        ".swift",
        ".html",
        ".json",
        ".xml",
        ".css",
        ".php",
        ".jl",
        ".r",
        ".cs",
        "d",
        ".lisp",
        ".cl",
        ".go",
        ".h",
        ".scala",
        ".sc",
        ".ts",
        ".sql"
    ],
    "text": [
        ".doc",
        ".docx",
        ".log",
        ".rtf",
        ".md",
        ".pdf",
        ".odt",
        ".txt"
    ],
    "data": [
        ".csv",
        ".dat",
        ".ged",
        ".pps",
        ".ppt",
        ".pptx"
    ],
    "audio": [
        ".flac",
        ".mp3",
        ".m3u",
        ".m4a",
        ".wav",
        ".wma"
    ],
    "video": [
        ".3gp",
        ".mp4",
        ".abi",
        ".m4v",
        ".mov",
        ".mpg",
        ".wmv"
    ],
    "image": [
        ".bmp",
        ".jpg",
        ".jpeg",
        ".png",
        ".svg"
    ],
    "executable": [
        ".apk",
        ".app",
        ".bat",
        ".jar",
        ".com",
        ".exe"
    ],
    "compressed": [
        ".7z",
        ".war",
        ".zip",
        ".tar.gz",
        ".tar.xz",
        ".rar"
    ]
}

MIME_TYPES = [
    "application/atom+xml",
    "application/ecmascript",
    "application/EDI-X12",
    "application/EDIFACT",
    "application/json",
    "application/javascript",
    "application/ogg",
    "application/pdf",
    "application/postscript",
    "application/rdf+xml",
    "application/rss+xml",
    "application/soap+xml",
    "application/font-woff",
    "application/xhtml+xml",
    "application/xml-dtd",
    "application/xop+xml",
    "application/zip",
    "application/gzip",
    "audio/basic",
    "audio/L24",
    "audio/mp4",
    "audio/mpeg",
    "audio/ogg",
    "audio/vorbis",
    "audio/vnd.rn-realaudio",
    "audio/vnd.wave",
    "audio/webm",
    "image/gif",
    "image/jpeg",
    "image/pjpeg",
    "image/png",
    "image/svg+xml",
    "image/tiff",
    "image/vnd.microsoft.icon",
    "message/http",
    "message/imdn+xml",
    "message/partial",
    "message/rfc822",
    "model/example",
    "model/iges",
    "model/mesh",
    "model/vrml",
    "model/x3d+binary",
    "model/x3d+vrml",
    "model/x3d+xml",
    "multipart/mixed",
    "multipart/alternative",
    "multipart/related",
    "multipart/form-data",
    "multipart/signed",
    "multipart/encrypted",
    "text/cmd",
    "text/css",
    "text/csv",
    "text/html",
    "text/javascript",
    "text/plain",
    "text/vcard",
    "text/xml",
    "video/mpeg",
    "video/mp4",
    "video/ogg",
    "video/quicktime",
    "video/webm",
    "video/x-matroska",
    "video/x-ms-wmv",
    "video/x-flv"
]

MATH_FORMULAS = [
    "A = (ab)/2",
    "A = a2",
    "A = ab",
    "A = (h(a + b))/2",
    "V = (Ah)/3",
    "xn*xm = xn + m",
    "(xn)/(xm) = x^n - m",
    "(x/y)^n = (x^n)/(y^n)",
    "x^n*y^n = (xy)^n",
    "ax2 + bx + c = 0.",
    "(a/b)/(c/d) = (a/b) * (d/c)",
    "π = pi = 3.1415",
    "A = πr^2",
    "P = 4l",
    "V = πr^2*h",
    "V - E + F = 2"
]

BLOOD_GROUPS = (
    'O+', 'A+', 'B+', 'AB+',
    'O−', 'A−', 'B−', 'AB−'
)

FAVORITE_MUSIC_GENRE = (
    "Pop",
    "Rock",
    "Hard Rock",
    "Rhythm & Blues (R&B)",
    "Country",
    "Rock & Roll",
    "Soul",
    "Country Pop",
    "Pop Rock",
    "Heavy Metal",
    "Progressive Rock",
    "Alternative Rock",
    "Jazz",
    "New Wave",
    "Synthpop",
    "Hip Hop",
    "Folk",
    "New Age",
    "Blues Rock",
    "Ambient",
    "Ambient house",
    "Classic",
    "Neoclassic",
    "Drum and bass"
)

GENDER_SYMBOLS = (
    '♂',
    '♀',
    '⚲',
)

SEXUALITY_SYMBOLS = (
    '⚤',
    '⚢',
    '⚣',
    '⚥',
    '⚧',
    '⚪'
)
