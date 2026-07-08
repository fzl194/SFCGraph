---
id: UNC@20.15.2@MMLCommand@LST CONCENPOINT
type: MMLCommand
name: LST CONCENPOINT（查询集中点部署模式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CONCENPOINT
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- 基础参数
- 集中点模式
status: active
---

# LST CONCENPOINT（查询集中点部署模式）

## 功能

**适用NF：PGW-C、SMF**

此命令用于查询集中点的部署模式。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/CONCENPOINT]] · 集中点部署模式（CONCENPOINT）

## 使用实例

查询集中点部署模式：

```
LST CONCENPOINT:;
```

```

RETCODE = 0  操作成功。

集中点信息
----------
 Ga集中点模式  =  单连接
 Gy集中点模式  =  本端IP和Diameter对端主机名
 Gx集中点模式  =  本端IP和Diameter对端主机名
 S6b集中点模式  =  本端IP和Diameter对端主机名
 Ga每进程端口数  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询集中点部署模式（LST-CONCENPOINT）_09896705.md`
