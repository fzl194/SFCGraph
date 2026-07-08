---
id: UNC@20.15.2@MMLCommand@LST TCPSACKSWITCH
type: MMLCommand
name: LST TCPSACKSWITCH（查询TCP SACK开关配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TCPSACKSWITCH
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 对新流生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- 公共参数
- TCP SACK开关
status: active
---

# LST TCPSACKSWITCH（查询TCP SACK开关配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

LST TCPSACKSWITCH命令用来查询Gx，Gy支持SACK选项情况。

## 注意事项

该命令执行后对新数据流生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TCPSACKSWITCH]] · TCP SACK开关配置（TCPSACKSWITCH）

## 使用实例

查询Gx，Gy接口TCP支持SACK情况命令为：

```
LST TCPSACKSWITCH:;
```

```

RETCODE = 0  操作成功

TCP SACK 开关
-------------
Gx接口TCP协议支持SACK选项开关  =  允许
Gy接口TCP协议支持SACK选项开关  =  允许
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-TCPSACKSWITCH.md`
