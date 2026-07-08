---
id: UNC@20.15.2@MMLCommand@ADD SMFAPNGRPMEM
type: MMLCommand
name: ADD SMFAPNGRPMEM（增加APN和DNS关联的APN组的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SMFAPNGRPMEM
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- APN组管理
status: active
---

# ADD SMFAPNGRPMEM（增加APN和DNS关联的APN组的绑定关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于添加APN和DNS关联的APN组的绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入3000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPNAME | APN组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写。<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置到APN组内的APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFAPNGRPMEM]] · APN和DNS关联的APN组的绑定关系（SMFAPNGRPMEM）

## 使用实例

需要根据不同APN业务选择不同DNS服务器时，配置了和DNS关联的APN组之后，再添加APN和APN组的绑定关系，APN组为grp1，APN为huawei.com：

```
ADD SMFAPNGRPMEM: GRPNAME="grp1", APN="huawei.com";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加APN和DNS关联的APN组的绑定关系（ADD-SMFAPNGRPMEM）_88248942.md`
