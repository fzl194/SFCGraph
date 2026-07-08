---
id: UNC@20.15.2@MMLCommand@LST LOCCOMMPOLICY
type: MMLCommand
name: LST LOCCOMMPOLICY（查询本地Common Policy配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCCOMMPOLICY
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 用户模板
status: active
---

# LST LOCCOMMPOLICY（查询本地Common Policy配置）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询本地Common Policy配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFILENAME | 用户模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD USERPROFILE命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCCOMMPOLICY]] · 本地Common Policy配置（LOCCOMMPOLICY）

## 使用实例

查询本地Common Policy配置，USERPROFILENAME为testuserprofilename1。

```
LST LOCCOMMPOLICY: USERPROFILENAME= testuserprofilename1;
RETCODE = 0  操作成功

结果如下
--------
用户模板名称  =  testuserprofilename1
优先级  =  3
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LOCCOMMPOLICY.md`
