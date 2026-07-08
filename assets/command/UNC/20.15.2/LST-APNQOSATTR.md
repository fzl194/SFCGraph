---
id: UNC@20.15.2@MMLCommand@LST APNQOSATTR
type: MMLCommand
name: LST APNQOSATTR（查询指定APN的QoS属性配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNQOSATTR
command_category: 查询类
applicable_nf:
- PGW-C
- SGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- APN的QoS属性
status: active
---

# LST APNQOSATTR（查询指定APN的QoS属性配置信息）

## 功能

**适用NF：PGW-C、SGW-C、SMF、GGSN**

该命令用于查询指定APN的QoS属性配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNQOSATTR]] · 指定APN的QoS属性配置信息（APNQOSATTR）

## 使用实例

查询APN为huawei.com的QoS属性配置信息：

```
%%LST APNQOSATTR: APN="huawei.com";%%
RETCODE = 0  操作成功

APN的QoS配置信息
----------------
             APN名称  =  huawei.com
       有QoS Profile  =  不使能
       QoS Profile名  =  NULL
AAA和PCRF共同协商QoS  =  不使能
        带宽控制开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询指定APN的QoS属性配置信息（LST-APNQOSATTR）_09651477.md`
