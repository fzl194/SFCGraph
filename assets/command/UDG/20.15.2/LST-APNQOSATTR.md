---
id: UDG@20.15.2@MMLCommand@LST APNQOSATTR
type: MMLCommand
name: LST APNQOSATTR（查询ApnQosAttr配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNQOSATTR
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 流量管理
- APN的QoS属性配置
status: active
---

# LST APNQOSATTR（查询ApnQosAttr配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询指定APN的带宽控制功能开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@APNQOSATTR]] · ApnQosAttr配置（APNQOSATTR）

## 使用实例

查询APN为apn1.com的带宽控制功能开关：

```
LST APNQOSATTR: APN="apn1.com";
```

```

RETCODE = 0  操作成功。

APN的QoS配置信息
----------------
                  APN  =  apn1.com
           上行Qos开关  =  INHERIT
    上行CAR/SHAPE开关 = NULL
           下行Qos开关  =  INHERIT
    上行CAR/SHAPE开关 = NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNQOSATTR.md`
