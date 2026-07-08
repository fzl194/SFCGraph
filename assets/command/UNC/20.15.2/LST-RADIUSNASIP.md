---
id: UNC@20.15.2@MMLCommand@LST RADIUSNASIP
type: MMLCommand
name: LST RADIUSNASIP（查询RADIUS NAS IP）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RADIUSNASIP
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- NAS IP
status: active
---

# LST RADIUSNASIP（查询RADIUS NAS IP）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来查询RADIUSNASIP配置。

## 注意事项

当指定APN参数时，查询结果为指定APN下所有RADIUS NAS IP配置信息。当不指定APN参数时，查询结果为所有的APN实例的RADIUS NAS IP配置信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定APN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RADIUSNASIP]] · RADIUS NAS IP（RADIUSNASIP）

## 使用实例

查询APN实例为huawei.com的RADIUS NAS IP配置：

```
LST RADIUSNASIP:APN="huawei.com";
```

```

RETCODE = 0  操作成功

Radius NAS IP
-------------
     APN名称  =  huawei.com
  NAS IP地址  =  192.168.10.3
NAS IPv6地址  =  NULL
  UP实例标识  =  ..
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RADIUSNASIP.md`
