---
id: UNC@20.15.2@MMLCommand@DSP SRVVNFC
type: MMLCommand
name: DSP SRVVNFC（查询服务VNFC）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SRVVNFC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 服务管理
- 服务VNFC
status: active
---

# DSP SRVVNFC（查询服务VNFC）

## 功能

该命令用于查询消费者信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [服务VNFC（SRVVNFC）](configobject/UNC/20.15.2/SRVVNFC.md)

## 使用实例

查询服务VNFC。

DSP SRVVNFC:;

```
%%DSP SRVVNFC:;%%
RETCODE = 0  操作成功。

操作结果如下：
--------------
   服务VNFC ID  =  5
  服务VNFC类型  =  CSLB
  申请服务类型  =  LB服务 & TN服务
服务IP地址规格  =  小规格
    IP业务模式  =  业务模式1
IP接入网络个数  =  1
    TS业务模式  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询服务VNFC（DSP-SRVVNFC）_29627049.md`
