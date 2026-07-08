---
id: UNC@20.15.2@MMLCommand@LST APNQOSBYPASS
type: MMLCommand
name: LST APNQOSBYPASS（查询BYPASS场景QoS描述配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNQOSBYPASS
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 5GC UDM全故障Qos
status: active
---

# LST APNQOSBYPASS（查询BYPASS场景QoS描述配置）

## 功能

**适用NF：SMF**

该命令用于查询APNQOSBYPASS的配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定APN名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNQOSBYPASS]] · BYPASS场景QoS描述配置（APNQOSBYPASS）

## 使用实例

查询APN为"huawei.com"的配置信息：

```
%%LST APNQOSBYPASS:APN="huawei.com";%%
            RETCODE = 0  操作成功

            操作结果如下
            ------------
            APN名称  =  huawei.com
            5G用户QoS索引  = 5

            (结果个数 = 1)

            ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNQOSBYPASS.md`
