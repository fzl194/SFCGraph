---
id: UDG@20.15.2@MMLCommand@LST APNTRAFDFUNC
type: MMLCommand
name: LST APNTRAFDFUNC（查询APN流量转发配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNTRAFDFUNC
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- 流量转发管理
- APN流量转发功能
status: active
---

# LST APNTRAFDFUNC（查询APN流量转发配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询流量转发功能开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数必须已经通过ADD APN命令配置。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNTRAFDFUNC]] · APN流量转发配置（APNTRAFDFUNC）

## 使用实例

查询apn流量转发功能开关：

```
LST APNTRAFDFUNC:;
```

```

RETCODE = 0 操作成功

流量转发功能开关
---------------------
APN = apn1
流量转发功能开关 = 不使能（关闭）
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNTRAFDFUNC.md`
