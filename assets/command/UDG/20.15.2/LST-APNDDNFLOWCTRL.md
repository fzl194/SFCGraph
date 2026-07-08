---
id: UDG@20.15.2@MMLCommand@LST APNDDNFLOWCTRL
type: MMLCommand
name: LST APNDDNFLOWCTRL（查询APN的下行数据DDN寻呼流控方式）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNDDNFLOWCTRL
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- GTP隧道管理
- 基于APN的下行报文触发寻呼的流控参数
status: active
---

# LST APNDDNFLOWCTRL（查询APN的下行数据DDN寻呼流控方式）

## 功能

**适用NF：UPF**

查询APN的下行数据DDN寻呼流控方式。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数必须已经通过ADD APN命令配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNDDNFLOWCTRL]] · APN的下行数据DDN寻呼流控方式（APNDDNFLOWCTRL）

## 使用实例

查询APN的下行数据DDN寻呼流控方式：

```
LST APNDDNFLOWCTRL: APN="apn1";
```

```

RETCODE = 0  操作成功

APN的下行数据DDN寻呼流控方式信息
--------------------------------------------------------
     APN  =  apn1
流控模式  =  缺省流控模式
报文个数  =  0
时间间隔  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNDDNFLOWCTRL.md`
