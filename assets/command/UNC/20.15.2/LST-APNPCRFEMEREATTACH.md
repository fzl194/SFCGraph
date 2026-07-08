---
id: UNC@20.15.2@MMLCommand@LST APNPCRFEMEREATTACH
type: MMLCommand
name: LST APNPCRFEMEREATTACH（查询APN的MBR删除PCC回滚空闲上下文配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNPCRFEMEREATTACH
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- MBR 删除PCC回滚上下文
status: active
---

# LST APNPCRFEMEREATTACH（查询APN的MBR删除PCC回滚空闲上下文配置）

## 功能

**适用NF：SGW-C**

该命令用于查询指定APN的MBR消息删除idle态的PCC回滚上下文的功能。

## 注意事项

当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNPCRFEMEREATTACH]] · APN的MBR删除PCC回滚空闲上下文配置（APNPCRFEMEREATTACH）

## 使用实例

查询“APN名称”为“isp”，删除PCC回滚的idle上下文的功能是否开启。

```
%%LST APNPCRFEMEREATTACH: APN="isp";%%
RETCODE = 0  操作成功

结果如下
------------------------------
              APN名称  =  isp
APN MBR 删除承载配置  =  ENABLE
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNPCRFEMEREATTACH.md`
