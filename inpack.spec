[project]
name = elastic-search
version = 6.2.4
vendor = elastic.co
homepage = https://www.elastic.co/products/elasticsearch
groups = dev/sys-runtime
description = distributed, RESTful search and analytics engine.

%build
PREFIX="/opt/elastic/search"

cd {{.inpack__pack_dir}}/deps

if [ ! -f "elasticsearch-{{.project__version}}.tar.gz" ]; then
    wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-{{.project__version}}.tar.gz
fi
if [ ! -d "elasticsearch-{{.project__version}}" ]; then
    tar -zxf elasticsearch-{{.project__version}}.tar.gz
fi


cd elasticsearch-{{.project__version}}
cp -rp * {{.buildroot}}/

cd {{.inpack__pack_dir}}/deps
rm -rf elasticsearch-{{.project__version}}

cd {{.inpack__pack_dir}}
mkdir -p {{.buildroot}}/misc/config/
install misc/config/elasticsearch.yml  {{.buildroot}}/misc/config/elasticsearch.yml

%files
