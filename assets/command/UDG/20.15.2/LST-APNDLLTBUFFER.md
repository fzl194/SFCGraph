---
id: UDG@20.15.2@MMLCommand@LST APNDLLTBUFFER
type: MMLCommand
name: LST APNDLLTBUFFER（查询基于APN的下行数据长时间缓存配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNDLLTBUFFER
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- GTP隧道管理
- APN下行数据长时间缓存
status: active
---

# LST APNDLLTBUFFER（查询基于APN的下行数据长时间缓存配置）

## 功能

**适用NF：UPF**

此命令用来查询基于APN的用户下行数据长时间缓存配置。

## 注意事项

如果UPF配置的下行数据缓存个数超过Serving PLMN速率控制的Downlink Rate Limit值，则当缓存的包数超过Downlink Rate Limit时会触发丢包。 所以，设置下行数据缓存个数时需要同时考虑无线侧的能力，下行缓存个数设置过大超过无线的处理能力可能引发丢包。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNDLLTBUFFER]] · 基于APN的下行数据长时间缓存配置（APNDLLTBUFFER）

## 使用实例

查询基于APN的下行报文长时间缓存的配置：

```
LST APNDLLTBUFFER:;
```

```

RETCODE = 0  操作成功

下行数据长时间缓存全局配置
--------------------------
         APN = huawei.com
最大缓存个数 = 1
    存储方式 = 环形存储

(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNDLLTBUFFER.md`
