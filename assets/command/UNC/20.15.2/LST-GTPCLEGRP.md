---
id: UNC@20.15.2@MMLCommand@LST GTPCLEGRP
type: MMLCommand
name: LST GTPCLEGRP（查询GTP-C本地实体组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPCLEGRP
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C本地实体组
status: active
---

# LST GTPCLEGRP（查询GTP-C本地实体组）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于查询GTP-C本地实体组信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [GTP-C本地实体组（GTPCLEGRP）](configobject/UNC/20.15.2/GTPCLEGRP.md)

## 使用实例

查询GTP-C本地实体组信息。

```
%%LST GTPCLEGRP:;%%
RETCODE = 0  操作成功

结果如下
--------
组号  描述信息  

0     s11          
1     s5_s         
2     s5_p         
3     n26 
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GTP-C本地实体组（LST-GTPCLEGRP）_09653069.md`
