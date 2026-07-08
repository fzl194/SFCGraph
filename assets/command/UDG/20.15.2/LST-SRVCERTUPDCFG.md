---
id: UDG@20.15.2@MMLCommand@LST SRVCERTUPDCFG
type: MMLCommand
name: LST SRVCERTUPDCFG（查询证书更新拆链配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SRVCERTUPDCFG
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 证书更新拆链配置
status: active
---

# LST SRVCERTUPDCFG（查询证书更新拆链配置）

## 功能

**适用NF：UPF、PGW-U**

该命令用于查询证书更新拆链配置参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SRVCERTUPDCFG]] · 证书更新拆链配置（SRVCERTUPDCFG）

## 使用实例

假如需要查询证书更新拆链配置参数，则命令如下：

```
LST SRVCERTUPDCFG:;
```

```

RETCODE = 0  操作成功
结果如下
------------------------
          证书更新时重建链开关  =  打开
单进程每批次重建链路间隔（秒）  =  4
  单进程每批次重建链路数（条）  =  10
    证书延迟重建链的时间(分钟)  =  5
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SRVCERTUPDCFG.md`
