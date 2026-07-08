---
id: UNC@20.15.2@MMLCommand@LST UPCALMVAL
type: MMLCommand
name: LST UPCALMVAL（查询UPC DS粒度N4请求等待超时异常的告警阈值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPCALMVAL
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UPC链路告警
status: active
---

# LST UPCALMVAL（查询UPC DS粒度N4请求等待超时异常的告警阈值）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于查询UPC DS粒度N4请求等待超时异常的告警阈值。

## 注意事项

当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPCALMVAL]] · UPC DS粒度N4请求等待超时异常的告警阈值（UPCALMVAL）

## 使用实例

查询UPC DS粒度N4请求等待超时异常的告警阈值：

```
%%LST UPCALMVAL:;%%
RETCODE = 0  操作成功

结果如下
--------
UPC告警上报阈值(秒)  =  10
(结果个数 = 1)

  -----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPCALMVAL.md`
