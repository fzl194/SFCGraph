---
id: UNC@20.15.2@MMLCommand@RMV MEASTHRESHOLDRULE
type: MMLCommand
name: RMV MEASTHRESHOLDRULE（删除话统阈值规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MEASTHRESHOLDRULE
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计
status: active
---

# RMV MEASTHRESHOLDRULE（删除话统阈值规则）

## 功能

该命令用于删除话统阈值规则。

## 注意事项

如果该话统阈值规则已经产生相应的“ALM-136802 实时统计紧急阈值超限”、“ALM-136803 实时统计重要阈值超限”、“ALM-136804 实时统计次要阈值超限”或“ALM-136805 实时统计提示阈值超限”告警，在删除该话统阈值规则后，这条告警也会被清除。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：标识网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：无。 |
| TRN | 阈值规则名称 | 可选必选说明：必选参数。<br>参数含义：阈值规则名称。<br>取值范围：字符串类型，长度不超过160个字符。<br>默认值：无。<br>配置原则：仅支持“A-Z”、“a-z”、“0-9”、“-_”、“\u4e00-\u9fa5”中文字符组合。 |

## 操作的配置对象

- [话统阈值规则（MEASTHRESHOLDRULE）](configobject/UNC/20.15.2/MEASTHRESHOLDRULE.md)

## 使用实例

删除话统阈值规则：

```
%%RMV MEASTHRESHOLDRULE: MEID=20, TRN="ttt";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除话统阈值规则(RMV-MEASTHRESHOLDRULE)_29103316.md`
