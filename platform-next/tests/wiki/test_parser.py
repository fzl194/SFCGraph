from wiki import parser


def test_split_front_matter():
    fm, body = parser.split_front_matter("---\nid: x\n---\n# t\nbody")
    assert fm == "id: x\n"
    assert body == "# t\nbody"


def test_parse_front_matter_fields():
    fm = parser.split_front_matter("---\ntype: MMLCommand\ncategory_path:\n- a\n- b\n---\n# x")[0]
    meta = parser.parse_front_matter(fm)
    assert meta["type"] == "MMLCommand"
    assert meta["category_path"] == ["a", "b"]


def test_relation_type_from_heading():
    assert parser.relation_for_heading("操作的配置对象") == "operates_on"
    assert parser.relation_for_heading("操作本对象的命令") == "operated_by"
    assert parser.relation_for_heading("关联任务") == "has_task"
    assert parser.relation_for_heading("所需 License") == "requires_license"
    assert parser.relation_for_heading("所属目录") == "parent"
    assert parser.relation_for_heading("证据") == "evidenced_by"
    assert parser.relation_for_heading("某个未知小节") == "related"


def test_extract_md_links_resolved():
    body = "## 操作的配置对象\n\n- [URR](configobject/UDG/20.15.2/URR.md)\n"
    links = parser.extract_links(body)
    assert len(links) == 1
    assert links[0].dst == "configobject/UDG/20.15.2/URR.md"
    assert links[0].relation_type == "operates_on"
    assert links[0].resolved is True


def test_extract_placeholder_unresolved():
    body = "关联对象 [[UDG@20.15.2@ConfigObject@URRGROUP]] 待建。"
    links = parser.extract_links(body)
    assert len(links) == 1
    assert links[0].resolved is False
    assert links[0].dst == "UDG@20.15.2@ConfigObject@URRGROUP"
    assert links[0].relation_type == "related"


def test_extract_skips_images_and_external():
    body = "![图](x.png) 和 [外](https://e.com) 和 [文](a.md)"
    links = parser.extract_links(body)
    assert [l.dst for l in links] == ["a.md"]


def test_id_to_object_type():
    assert parser.object_type_of("UDG@20.15.2@Task@0-00001") == "Task"
    assert parser.object_type_of("ConfigurationSolution@charging") == "ConfigurationSolution"
    assert parser.object_type_of("no-at-id") == ""
