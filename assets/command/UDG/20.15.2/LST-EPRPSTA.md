---
id: UDG@20.15.2@MMLCommand@LST EPRPSTA
type: MMLCommand
name: LST EPRPSTA（查询EPRPSTA对象）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: EPRPSTA
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- EPRPSTA性能统计对象
status: active
---

# LST EPRPSTA（查询EPRPSTA对象）

## 功能

**适用NF：SGW-U、PGW-U**

该命令用于查询EpRpSta对象。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACETYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：接口类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SXA：接口类型为Sxa。<br>- SXB：接口类型为Sxb。<br>- SXBGSN：接口类型为Sxb，且用户角色为GGSN。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@EPRPSTA]] · EPRPSTA对象（EPRPSTA）

## 使用实例

查询接口类型为SXA的EpRpSta对象：

```
LST EPRPSTA: INTERFACETYPE=SXA;
```

```

RETCODE = 0 操作成功。

EpRpSta 配置
---------------------
              对象名称  =  huawei
              接口类型  =  Sxa
        CP NodeID 类型  =  FQDN
 IPv4地址类型的Node Id  =  0.0.0.0
 IPv6地址类型的Node Id  =  ::
     FQDN类型的Node Id  =  new
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-EPRPSTA.md`
