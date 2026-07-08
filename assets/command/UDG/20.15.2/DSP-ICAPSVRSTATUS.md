---
id: UDG@20.15.2@MMLCommand@DSP ICAPSVRSTATUS
type: MMLCommand
name: DSP ICAPSVRSTATUS（查询ICAP服务器状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ICAPSVRSTATUS
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- ICAPC管理
- ICAP服务器
status: active
---

# DSP ICAPSVRSTATUS（查询ICAP服务器状态）

## 功能

**适用NF：PGW-U、UPF**

该命令用来显示所有已经配置的ICAP Server或者指定名字的ICAP Server的工作状态信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ICAPSERVERNAME | ICAP服务器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ICAP Server的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ICAPSVRSTATUS]] · ICAP服务器状态（ICAPSVRSTATUS）

## 使用实例

查询所有已经配置的ICAP Server的工作状态信息：

```
DSP ICAPSVRSTATUS:;
```

```

RETCODE = 0  操作成功

ICAP服务器状态
--------------
        Pod 名称  =  icapc-pod-0
        源IP地址  =  192.168.0.1
        源端口号  =  16735
ICAP服务器IP地址  =  192.168.22.64
  ICAP服务器端口  =  1344
  ICAP服务器状态  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-ICAPSVRSTATUS.md`
