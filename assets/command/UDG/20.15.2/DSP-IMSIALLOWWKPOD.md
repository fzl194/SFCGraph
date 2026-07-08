---
id: UDG@20.15.2@MMLCommand@DSP IMSIALLOWWKPOD
type: MMLCommand
name: DSP IMSIALLOWWKPOD（查询允许IMSI在特定的Worker Pod上激活信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IMSIALLOWWKPOD
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 允许IMSI在特定的Worker POD上激活
status: active
---

# DSP IMSIALLOWWKPOD（查询允许IMSI在特定的Worker Pod上激活信息）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询当前设置为允许的IMSI和Worker pod。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| WORKERTYPE | Worker类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Worker类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- to：TCP优化。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IMSIALLOWWKPOD]] · 允许IMSI在特定的Worker Pod上激活配置（IMSIALLOWWKPOD）

## 使用实例

当需要查询IMSI 1234567890的允许在哪些Worker Pod上激活配置时，进行如下设置：

```
DSP IMSIALLOWWKPOD: IMSI="1234567890";
```

```

RETCODE = 0  操作成功

允许IMSI在特定的Worker Pod上激活信息
--------------------------------------------------------------------
            IMSI =  1234567890
        Pod 名称 =  to-pod-0
       超时时长  =  1111
      Worker类型 = TCP优化
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询允许IMSI在特定的Worker-Pod上激活信息（DSP-IMSIALLOWWKPOD）_87414915.md`
