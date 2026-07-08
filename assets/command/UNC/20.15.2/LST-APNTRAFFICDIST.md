---
id: UNC@20.15.2@MMLCommand@LST APNTRAFFICDIST
type: MMLCommand
name: LST APNTRAFFICDIST（查询漫游地动态签约分流控制）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNTRAFFICDIST
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 本地分流管理
- 漫游地动态签约分流控制
status: active
---

# LST APNTRAFFICDIST（查询漫游地动态签约分流控制）

## 功能

**适用NF：SMF**

该命令用于查询漫游地动态签约分流控制。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SELECTEDDNN | Selected DNN | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于漫游地动态签约的分流策略控制特性的AMF带给SMF的Selected DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数必须已经通过命令ADD APN配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNTRAFFICDIST]] · 漫游地动态签约分流控制（APNTRAFFICDIST）

## 使用实例

查询Selected DNN名为“mall1”的漫游地动态签约分流控制属性。

```
%%LST APNTRAFFICDIST: SELECTEDDNN = "mall1";%%
RETCODE = 0 操作成功
结果如下
--------
                     APN名 = mall1
                  赞助商ID = test
     辅锚点UPF上报用量开关 = 使能
在园区内主锚点流量是否计费 = 使能
          用户模板名称 = testuserprofilename
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询漫游地动态签约分流控制（LST-APNTRAFFICDIST）_18982082.md`
