---
id: UNC@20.15.2@MMLCommand@LST SBIFQDNPORTPLCY
type: MMLCommand
name: LST SBIFQDNPORTPLCY（查询FQDN端口策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SBIFQDNPORTPLCY
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NSSF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- NF通信模式管理
- FQDN端口策略管理
status: active
---

# LST SBIFQDNPORTPLCY（查询FQDN端口策略）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于显示FQDN使用端口号的策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SBIFQDNPORTPLCY]] · FQDN端口策略（SBIFQDNPORTPLCY）

## 使用实例

查询所有FQDN端口号的策略。

```
%%LST SBIFQDNPORTPLCY:;%%
RETCODE = 0  操作成功

结果如下
--------
场景        范围              对端PLMN  端口策略

TARGETADDR  INTERPLMNDEFAULT  NULL      USEPORT
TARGETADDR  BYPLMN            12303     NOTUSEPORT
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SBIFQDNPORTPLCY.md`
