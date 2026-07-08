---
id: UNC@20.15.2@MMLCommand@LST GLOBALNBNS
type: MMLCommand
name: LST GLOBALNBNS（查询系统默认NBNS）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLOBALNBNS
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- DN网络DNS_NBNS选择管理
- NBNS选择管理
- 缺省NBNS
status: active
---

# LST GLOBALNBNS（查询系统默认NBNS）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用来查看系统的NBNS属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLOBALNBNS]] · 系统默认NBNS（GLOBALNBNS）

## 使用实例

查询系统的默认的NBNS属性：

```
%%LST GLOBALNBNS:;%%
RETCODE = 0  操作成功

结果如下
--------
        NBNS功能开关  =  不使能
      主NBNS服务器IP  =  10.1.1.1
      备NBNS服务器IP  =  10.2.2.2
第一优先级服务器属性  =  dhcp
第二优先级服务器属性  =  radius
第三优先级服务器属性  =  local
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询系统默认NBNS（LST-GLOBALNBNS）_22556857.md`
