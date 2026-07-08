---
id: UDG@20.15.2@MMLCommand@DSP IMSIBLOCKWKPOD
type: MMLCommand
name: DSP IMSIBLOCKWKPOD（查询阻塞IMSI在特定的Worker Pod上激活信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IMSIBLOCKWKPOD
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 阻塞IMSI在特定的Worker Pod上激活
status: active
---

# DSP IMSIBLOCKWKPOD（查询阻塞IMSI在特定的Worker Pod上激活信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询当前设置为阻塞的IMSI和Work pod。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| WORKERTYPE | Worker类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Worker类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- to：TCP优化。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IMSIBLOCKWKPOD]] · 阻塞IMSI在特定的Worker Pod上激活信息（IMSIBLOCKWKPOD）

## 使用实例

当需要查询IMSI 1234567890的阻塞在哪些Worker Pod上激活配置时，进行如下设置：

```
DSP IMSIBLOCKWKPOD: IMSI="1234567890";
```

```

RETCODE = 0 操作成功

阻塞IMSI在特定的Worker Pod上激活
--------------------------------------------------------------------
            IMSI =  1234567890
        Pod 名称 =  to-pod-0
       超时时长  =  1111
      Worker类型 = TCP优化
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-IMSIBLOCKWKPOD.md`
