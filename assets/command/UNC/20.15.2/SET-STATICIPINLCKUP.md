---
id: UNC@20.15.2@MMLCommand@SET STATICIPINLCKUP
type: MMLCommand
name: SET STATICIPINLCKUP（设置静态地址段在锁定UPF的用户处理）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: STATICIPINLCKUP
command_category: 配置类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF锁定静态IP冲突处理
status: active
---

# SET STATICIPINLCKUP（设置静态地址段在锁定UPF的用户处理）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于设置静态地址段在锁定UPF的用户处理。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ESTLOCKUPF |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ESTLOCKUPF | 静态用户在锁定UPF的激活处理 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的IP所属的地址段被分配到了锁定的UPF时，是否允许静态用户在锁定的UPF激活。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（静态用户不可以在锁定的UPF激活）<br>- ENABLE（静态用户可以在锁定的UPF激活）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST STATICIPINLCKUP查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@STATICIPINLCKUP]] · 静态地址段在锁定UPF的用户处理（STATICIPINLCKUP）

## 使用实例

设置静态用户在锁定UPF的激活处理为ENABLE：

```
SET STATICIPINLCKUP: ESTLOCKUPF=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-STATICIPINLCKUP.md`
