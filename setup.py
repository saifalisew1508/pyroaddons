#  pyroaddons -
#  Copyright (C) 2023-present Abishnoi6 <https://github.com/saifalisew1508>
#
#  This file is part of pyroaddons.
#
#  pyroaddons is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  pyroaddons is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with pyroaddons.  If not, see <http://www.gnu.org/licenses/>.

# ===================================================================

import setuptools

with open("README.md", encoding="utf8") as readme:
    long_description = readme.read()

"""    
with open("requirements.txt", encoding="utf-8") as f:
    requires = f.read().splitlines()
"""


setuptools.setup(
    name="pyroaddons",
    packages=setuptools.find_packages(),
    version="2.3.6",
    description="add-on for Pyrogram || Telegram bot helpers || Easy botting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/saifalisew1508/pyroaddons",
    download_url="https://github.com/saifalisew1508/pyroaddons/releases/latest",
    author="Abishnoi",
    author_email="saifalisew1508@pyroaddons.org",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    keywords="add-on pyrogram bots telegram bot chat messenger mtproto api client library python conversation keyboard userbot patch https",
    project_urls={
        "Tracker": "https://github.com/saifalisew1508/pyroaddons/issues",
        "Community": "https://t.me/pyroaddonspy",
        "Source": "https://github.com/saifalisew1508/pyroaddons",
        "Documentation": "https://github.com/saifalisew1508/pyroaddons/tree/main/doce",
    },
    python_requires="~=3.7",
    zip_safe=False,
    install_requires=["pytz>=2023.3"],
)
