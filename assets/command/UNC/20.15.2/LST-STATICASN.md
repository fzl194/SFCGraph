---
id: UNC@20.15.2@MMLCommand@LST STATICASN
type: MMLCommand
name: LST STATICASN（查询静态ASN）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: STATICASN
command_category: 查询类
applicable_nf:
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- ASN静态配置
status: active
---

# LST STATICASN（查询静态ASN）

## 功能

**适用NF：PGW-C、SGW-C、GGSN**

该命令用来查看本地配置的SGSN、SGW-C信令地址和ASN映射的表项。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVNODEIP | Service Node信令IP地址 | 可选必选说明：可选参数<br>参数含义：该参数用于设置SGSN、SGW-C的信令IP。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [静态ASN（STATICASN）](configobject/UNC/20.15.2/STATICASN.md)

## 使用实例

显示所有ASN配置信息：

```
LST STATICASN:;
RETCODE = 0  操作成功。

ASN配置信息
-----------
Service Node信令IP  =  10.13.13.0
            IP掩码  =  255.255.255.0
               ASN  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询静态ASN（LST-STATICASN）_40108905.md`
