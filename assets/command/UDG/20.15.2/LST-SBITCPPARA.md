---
id: UDG@20.15.2@MMLCommand@LST SBITCPPARA
type: MMLCommand
name: LST SBITCPPARA（查询SBI接口TCP控制参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SBITCPPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- TCP安全管理
status: active
---

# LST SBITCPPARA（查询SBI接口TCP控制参数）

## 功能

该命令用于查询系统的报文流控阈值数以及TCP连接数。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SBITCPPARA]] · SBI接口TCP控制参数（SBITCPPARA）

## 使用实例

查询SYN包流控阈值和连接数执行如下命令：

```
%%LST SBITCPPARA:;%%
RETCODE = 0 操作成功

结果如下
--------
SYN包流控阈值(pps) = 5000
单个对端IP连接限制数 = 0
(结果个数 = 1)

---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SBITCPPARA.md`
